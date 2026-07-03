"""Merge structured research-sweep findings into the frontier knowledge base.

The KB is the layer that keeps agent-driven literature sweeps cumulative: every
sweep's findings land here as claim-bearing paper nodes, deduplicated by the
same canonical id used across the atlas, so the next sweep starts from what the
last one learned instead of from a cold web search.

Separation of concerns (mirrors the atlas):
  * kb/sweeps/*.json   -> raw sweep outputs, immutable FACTS as collected
  * kb/nodes.jsonl     -> merged, deduplicated paper nodes with claims
  * kb_query.py        -> agent-ready grounding digests (presentation)

Input format — the workflow sweep output:
    {"research": [{"area": str,
                   "findings": [{"claim", "source", "numbers"?,
                                 "relevance"?, "uncertain"?}],
                   "recommendations": [str], "open_questions": [str]}],
     ...}
Any top-level list of such area-objects (e.g. "gapFills") is ingested too.

Usage:
    python scripts/kb_ingest.py kb/sweeps/slm-2026-07.json --sweep slm-2026-07
    python scripts/kb_ingest.py kb/sweeps/*.json --enrich
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

try:
    # arXiv responses are external input: defusedxml blocks XXE/billion-laughs
    from defusedxml import ElementTree as ET
except ImportError:  # --enrich is optional; fail only when it is actually used
    ET = None

ROOT = Path(__file__).resolve().parent.parent
NODES = ROOT / "kb" / "nodes.jsonl"

ARXIV_RE = re.compile(r"(?:arxiv[:./\s]+(?:abs/)?|^)(\d{4}\.\d{4,5})(?:v\d+)?", re.I)
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s,;\"']+)", re.I)
HF_RE = re.compile(r"huggingface\.co/([\w.-]+/[\w.-]+)", re.I)


def canonical_id(arxiv_id: str | None, doi: str | None, title: str) -> str:
    """Stable node id; MUST match scrape_citations.py / build_map.py."""
    if arxiv_id:
        return f"arxiv:{arxiv_id}"
    if doi:
        return f"doi:{doi.lower()}"
    return "title:" + re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def parse_source(source: str) -> dict:
    """Extract identifiers from a free-form source string a researcher wrote."""
    arxiv = ARXIV_RE.search(source)
    doi = DOI_RE.search(source)
    hf = HF_RE.search(source)
    # Title guess: strip ids/urls, keep the longest remaining text run.
    text = re.sub(r"https?://\S+", " ", source)
    text = re.sub(r"arxiv[:./\s]*(abs/)?\d{4}\.\d{4,5}(v\d+)?", " ", text, flags=re.I)
    title = max(
        (t.strip(" -—·|,;") for t in text.split("—")), key=len, default=""
    ).strip()
    return {
        "arxiv_id": arxiv.group(1) if arxiv else None,
        "doi": doi.group(1) if doi else None,
        "hf_repo": hf.group(1) if hf else None,
        "title": title or source[:120],
    }


def load_nodes() -> dict[str, dict]:
    if not NODES.exists():
        return {}
    nodes = {}
    for line in NODES.read_text(encoding="utf-8").splitlines():
        if line.strip():
            n = json.loads(line)
            nodes[n["id"]] = n
    return nodes


def save_nodes(nodes: dict[str, dict]) -> None:
    NODES.parent.mkdir(parents=True, exist_ok=True)
    with NODES.open("w", encoding="utf-8") as fh:
        for n in sorted(nodes.values(), key=lambda n: n["id"]):
            fh.write(json.dumps(n, ensure_ascii=False) + "\n")


def iter_area_objects(payload: object):
    """Yield every {area, findings, ...} object anywhere in the sweep output."""
    if isinstance(payload, dict):
        if "findings" in payload and "area" in payload:
            yield payload
        else:
            for v in payload.values():
                yield from iter_area_objects(v)
    elif isinstance(payload, list):
        for v in payload:
            yield from iter_area_objects(v)


def ingest(path: Path, sweep: str, nodes: dict[str, dict]) -> tuple[int, int]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    new_nodes = new_claims = 0
    for area_obj in iter_area_objects(payload):
        area = area_obj.get("area", "unknown")
        for f in area_obj.get("findings", []):
            src = parse_source(f.get("source", ""))
            nid = canonical_id(src["arxiv_id"], src["doi"], src["title"])
            node = nodes.get(nid)
            if node is None:
                node = {
                    "id": nid,
                    "title": src["title"],
                    "arxiv_id": src["arxiv_id"],
                    "doi": src["doi"],
                    "hf_repo": src["hf_repo"],
                    "year": None,
                    "topics": [],
                    "claims": [],
                }
                nodes[nid] = node
                new_nodes += 1
            if area not in node["topics"]:
                node["topics"].append(area)
            claim = {
                "claim": f.get("claim", ""),
                "numbers": f.get("numbers"),
                "relevance": f.get("relevance"),
                "uncertain": bool(f.get("uncertain")),
                "sweep": sweep,
                "area": area,
            }
            if not any(c["claim"] == claim["claim"] for c in node["claims"]):
                node["claims"].append(claim)
                new_claims += 1
    return new_nodes, new_claims


def enrich(nodes: dict[str, dict], sleep: float = 3.1) -> int:
    """Fill title/year/abstract for arXiv nodes via the arXiv API (batched)."""
    if ET is None:
        print(
            "[warn] --enrich needs defusedxml (uv pip install defusedxml); skipped",
            file=sys.stderr,
        )
        return 0
    todo = [n for n in nodes.values() if n.get("arxiv_id") and not n.get("year")]
    done = 0
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for i in range(0, len(todo), 20):
        batch = todo[i : i + 20]
        ids = ",".join(n["arxiv_id"] for n in batch)
        url = f"http://export.arxiv.org/api/query?id_list={ids}&max_results=20"
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                tree = ET.fromstring(resp.read())
        except (OSError, ET.ParseError) as exc:
            print(
                f"[warn] arXiv batch failed ({exc}); keeping sparse nodes",
                file=sys.stderr,
            )
            continue
        by_id = {}
        for entry in tree.findall("a:entry", ns):
            eid = entry.findtext("a:id", "", ns) or ""
            m = ARXIV_RE.search(eid)
            if m:
                by_id[m.group(1)] = entry
        for n in batch:
            entry = by_id.get(n["arxiv_id"])
            if entry is None:
                continue
            n["title"] = " ".join((entry.findtext("a:title", "", ns) or "").split())
            n["year"] = (
                int((entry.findtext("a:published", "", ns) or "0000")[:4]) or None
            )
            abstract = " ".join((entry.findtext("a:summary", "", ns) or "").split())
            n["abstract"] = abstract[:400]
            done += 1
        if i + 20 < len(todo):
            time.sleep(sleep)  # arXiv API rate courtesy
    return done


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest sweep findings into the KB.")
    parser.add_argument("inputs", nargs="+", type=Path, help="sweep output JSON files")
    parser.add_argument(
        "--sweep", default=None, help="sweep label (default: file stem)"
    )
    parser.add_argument(
        "--enrich", action="store_true", help="fetch metadata from arXiv API"
    )
    args = parser.parse_args()

    nodes = load_nodes()
    for path in args.inputs:
        added_n, added_c = ingest(path, args.sweep or path.stem, nodes)
        print(f"[ingest] {path.name}: +{added_n} nodes, +{added_c} claims")
    if args.enrich:
        print(f"[enrich] {enrich(nodes)} nodes enriched from arXiv")
    save_nodes(nodes)
    total_claims = sum(len(n["claims"]) for n in nodes.values())
    print(f"[done] KB: {len(nodes)} nodes, {total_claims} claims -> {NODES}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
