"""Local MCP server exposing the Kazakh NLP frontier KB (kb/nodes.jsonl) as query tools.

Read-only. Serves the lab's research knowledge graph over stdio so any MCP client
(Claude Code, etc.) can search papers, pull claims-with-sources, list the topic
taxonomy, and get a prompt-ready digest — replacing the ``kb_query.py`` shell hop
with native, structured tools.

Data provenance (matters for any distribution beyond personal use):
- Paper metadata + abstracts: arXiv (metadata dedicated CC0) via export.arxiv.org.
- Paper search + citation counts: Semantic Scholar / S2AG (ODC-BY 1.0) — attribution required.
- Claims, verdicts, topics, synthesis: original work of the Kazakh Frontier Lab.

Run (no install needed):
    env -u PYTHONPATH uv run --with "mcp[cli]" python scripts/kb_mcp.py
Override the KB path with the KB_PATH env var.
"""

from __future__ import annotations

import json
import os
import re
from collections import Counter
from pathlib import Path

# Resilient import: the official SDK's server class is `FastMCP`; newer builds
# rename it to `MCPServer`. Both expose the same .tool()/.resource()/.run() API.
try:
    from mcp.server.fastmcp import FastMCP as _Server  # type: ignore
except ImportError:  # pragma: no cover - depends on installed SDK version
    from mcp.server.mcpserver import MCPServer as _Server  # type: ignore

KB_PATH = Path(
    os.environ.get(
        "KB_PATH",
        Path(__file__).resolve().parent.parent / "kb" / "nodes.jsonl",
    )
)

mcp = _Server("kazakh-nlp-kb")


# --------------------------------------------------------------------------- #
# Pure data layer — no MCP dependency, unit-testable in isolation.
# --------------------------------------------------------------------------- #
def load_nodes() -> list[dict]:
    """Load all KB nodes from the JSONL file (one JSON object per line)."""
    nodes: list[dict] = []
    with KB_PATH.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                nodes.append(json.loads(line))
    return nodes


def _is_paper(n: dict) -> bool:
    """A paper node carries a real abstract (vs. a claim-only source node)."""
    return bool(n.get("abstract"))


def _haystack(n: dict) -> str:
    """Lowercased searchable text for a node: title + abstract + topics + claims."""
    return " ".join(
        [
            str(n.get("title") or ""),
            str(n.get("abstract") or ""),
            " ".join(n.get("topics", []) or []),
            " ".join(str(c.get("claim") or "") for c in (n.get("claims") or [])),
        ]
    ).lower()


def _summary(n: dict, snippet: str = "") -> dict:
    out = {
        "id": n.get("id"),
        "title": n.get("title"),
        "year": n.get("year"),
        "arxiv_id": n.get("arxiv_id") or None,
        "topics": n.get("topics", []) or [],
        "is_paper": _is_paper(n),
        "n_claims": len(n.get("claims", []) or []),
    }
    if snippet:
        out["snippet"] = snippet
    return out


def _snippet(n: dict) -> str:
    abstract = str(n.get("abstract") or "").strip()
    if abstract:
        return abstract[:240] + ("…" if len(abstract) > 240 else "")
    claims = n.get("claims") or []
    if claims:
        first = str(claims[0].get("claim") or "").strip()
        return first[:240] + ("…" if len(first) > 240 else "")
    return ""


def search_nodes(query: str, limit: int) -> list[dict]:
    q = query.lower().strip()
    terms = [t for t in re.split(r"\s+", q) if t]
    scored: list[tuple[int, dict]] = []
    for n in load_nodes():
        hay = _haystack(n)
        score = sum(hay.count(t) for t in terms) if terms else int(q in hay)
        if score:
            scored.append((score, n))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [_summary(n, _snippet(n)) for _, n in scored[: max(1, limit)]]


def find_node(node_id: str) -> dict | None:
    node_id = node_id.strip()
    candidates = {node_id, f"arxiv:{node_id}"}
    for n in load_nodes():
        if n.get("id") in candidates or (
            n.get("arxiv_id") and n.get("arxiv_id") == node_id
        ):
            return n
    return None


def get_claims(
    topic: str | None,
    area: str | None,
    verified_only: bool,
    uncertain_only: bool,
    limit: int,
) -> list[dict]:
    out: list[dict] = []
    tl = (topic or "").lower().strip()
    al = (area or "").lower().strip()
    for n in load_nodes():
        if tl and not any(tl in t.lower() for t in (n.get("topics") or [])):
            continue
        for c in n.get("claims") or []:
            if al and al not in str(c.get("area") or "").lower():
                continue
            if verified_only and not c.get("verification"):
                continue
            if uncertain_only and not c.get("uncertain"):
                continue
            out.append(
                {
                    "claim": c.get("claim"),
                    "numbers": c.get("numbers"),
                    "area": c.get("area"),
                    "source": c.get("source"),
                    "uncertain": bool(c.get("uncertain")),
                    "verification": c.get("verification"),
                    "node_id": n.get("id"),
                    "node_title": n.get("title"),
                }
            )
            if len(out) >= max(1, limit):
                return out
    return out


def list_topics() -> list[dict]:
    counter: Counter[str] = Counter()
    for n in load_nodes():
        for t in n.get("topics") or []:
            counter[t] += 1
    return [{"topic": t, "n_nodes": c} for t, c in counter.most_common()]


def kb_stats() -> dict:
    nodes = load_nodes()
    papers = [n for n in nodes if _is_paper(n)]
    claims = [c for n in nodes for c in (n.get("claims") or [])]
    verified = [c for c in claims if c.get("verification")]
    uncertain = [c for c in claims if c.get("uncertain")]
    topics = {t for n in nodes for t in (n.get("topics") or [])}
    return {
        "n_nodes": len(nodes),
        "n_papers": len(papers),
        "n_sources": len(nodes) - len(papers),
        "n_topics": len(topics),
        "n_claims": len(claims),
        "n_verified_claims": len(verified),
        "n_uncertain_claims": len(uncertain),
        "kb_path": str(KB_PATH),
    }


def render_digest(topic: str | None, grep: str | None, max_chars: int) -> str:
    tl = (topic or "").lower().strip()
    pat = re.compile(grep, re.IGNORECASE) if grep else None
    lines: list[str] = []
    for n in load_nodes():
        if tl and not any(tl in t.lower() for t in (n.get("topics") or [])):
            continue
        if pat and not pat.search(_haystack(n)):
            continue
        ref = n.get("id") or n.get("arxiv_id") or "?"
        head = f"### [{ref}] {n.get('title')} ({n.get('year')})"
        body = []
        for c in n.get("claims") or []:
            mark = (
                "✓" if c.get("verification") else ("?" if c.get("uncertain") else "•")
            )
            nums = f" [{c['numbers']}]" if c.get("numbers") else ""
            src = f" (src: {c['source']})" if c.get("source") else ""
            body.append(f"  {mark} {c.get('claim')}{nums}{src}")
        block = head + ("\n" + "\n".join(body) if body else "")
        lines.append(block)
    text = "\n".join(lines)
    if len(text) > max_chars:
        text = text[:max_chars].rsplit("\n", 1)[0] + "\n…[truncated]"
    return text or "(no matching nodes)"


# --------------------------------------------------------------------------- #
# MCP tool surface — thin wrappers; docstrings become tool descriptions.
# --------------------------------------------------------------------------- #
@mcp.tool()
def kb_search(query: str, limit: int = 8) -> list[dict]:
    """Keyword-search the Kazakh NLP KB over titles, abstracts, topics and claim
    text. Returns the best-matching nodes (id, title, year, topics, snippet,
    n_claims), most relevant first. Use this to discover which papers/notes cover
    a subject before pulling full detail with kb_get_node."""
    return search_nodes(query, limit)


@mcp.tool()
def kb_get_node(node_id: str) -> dict:
    """Fetch one KB node in full by id (e.g. "arxiv:1808.06226" or the bare
    arXiv number). Returns title, year, arxiv_id, doi, hf_repo, topics, abstract,
    and the complete list of claims (each with numbers, source, verdict)."""
    n = find_node(node_id)
    if n is None:
        return {"error": f"node not found: {node_id}"}
    return {
        "id": n.get("id"),
        "title": n.get("title"),
        "year": n.get("year"),
        "arxiv_id": n.get("arxiv_id") or None,
        "doi": n.get("doi") or None,
        "hf_repo": n.get("hf_repo") or None,
        "topics": n.get("topics", []) or [],
        "abstract": n.get("abstract") or None,
        "claims": n.get("claims", []) or [],
    }


@mcp.tool()
def kb_claims(
    topic: str | None = None,
    area: str | None = None,
    verified_only: bool = False,
    uncertain_only: bool = False,
    limit: int = 30,
) -> list[dict]:
    """Pull evidence claims across the KB, each with its source and (if any)
    verification verdict, plus the owning node's id/title. Filter by topic
    (substring match on a node's topics), area (substring on the claim's area),
    verified_only (only claims with an adversarial verdict), or uncertain_only.
    This is the primary tool for grounding a number in a citable source."""
    return get_claims(topic, area, verified_only, uncertain_only, limit)


@mcp.tool()
def kb_topics() -> list[dict]:
    """List the KB topic taxonomy as [{topic, n_nodes}], most-populated first.
    Use it to see how the research graph is organised before filtering."""
    return list_topics()


@mcp.tool()
def kb_summary() -> dict:
    """Return KB size/coverage stats: node/paper/source counts, distinct topics,
    total claims, and how many are adversarially verified vs. flagged uncertain."""
    return kb_stats()


@mcp.tool()
def kb_digest(
    topic: str | None = None, grep: str | None = None, max_chars: int = 8000
) -> str:
    """Render a compact, prompt-ready Markdown digest of matching nodes and their
    claims (✓=verified, ?=uncertain, •=unverified), capped at max_chars. Filter by
    topic (substring on node topics) and/or grep (regex over title+abstract+claims).
    Mirrors scripts/kb_query.py — inject this into a research/design agent's prompt."""
    return render_digest(topic, grep, max_chars)


@mcp.resource("kb://about")
def about() -> str:
    """Provenance + licensing of this knowledge base (read before redistribution)."""
    s = kb_stats()
    return (
        "Kazakh NLP frontier knowledge base — Kazakh Frontier Lab.\n"
        f"{s['n_nodes']} nodes ({s['n_papers']} papers, {s['n_sources']} sources), "
        f"{s['n_topics']} topics, {s['n_claims']} claims "
        f"({s['n_verified_claims']} adversarially verified).\n\n"
        "Provenance / licensing:\n"
        "- Paper metadata + abstracts: arXiv (metadata dedicated CC0), export.arxiv.org.\n"
        "- Paper search + citation counts: Semantic Scholar / S2AG (ODC-BY 1.0) — "
        "attribution required.\n"
        "- Claims, verdicts, topics, synthesis: original work of the Kazakh Frontier Lab.\n"
    )


if __name__ == "__main__":
    mcp.run()  # stdio transport by default
