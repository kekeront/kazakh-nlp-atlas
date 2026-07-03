"""Emit an agent-ready grounding digest from the frontier knowledge base.

Turns kb/nodes.jsonl into a compact, token-budgeted context block that a
research/design agent can be seeded with, so each new sweep starts from the
accumulated frontier instead of a cold web search. Presentation only — facts
live in nodes.jsonl (kb_ingest.py owns those).

Usage:
    python scripts/kb_query.py                          # everything, ranked
    python scripts/kb_query.py --topic tokenizer-morphology --topic embed-sota
    python scripts/kb_query.py --grep "MLA|latent" --max-chars 8000
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NODES = ROOT / "kb" / "nodes.jsonl"


def load_nodes() -> list[dict]:
    if not NODES.exists():
        raise SystemExit(f"missing KB: {NODES} (run kb_ingest.py first)")
    return [
        json.loads(line)
        for line in NODES.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def node_ref(n: dict) -> str:
    if n.get("arxiv_id"):
        return f"arXiv:{n['arxiv_id']}"
    if n.get("hf_repo"):
        return f"hf:{n['hf_repo']}"
    if n.get("doi"):
        return f"doi:{n['doi']}"
    return n["id"]


def render(nodes: list[dict], max_chars: int) -> str:
    """Rank nodes by claim count (hubs first) and render until budget runs out."""
    nodes = sorted(nodes, key=lambda n: -len(n["claims"]))
    out: list[str] = [
        "## Frontier KB digest (accumulated verified findings; cite refs as given)",
        "",
    ]
    used = sum(len(s) + 1 for s in out)
    skipped = 0
    for n in nodes:
        year = f", {n['year']}" if n.get("year") else ""
        lines = [f"### {n.get('title') or n['id']} ({node_ref(n)}{year})"]
        for c in n["claims"]:
            mark = " [UNVERIFIED]" if c.get("uncertain") else ""
            nums = f" | {c['numbers']}" if c.get("numbers") else ""
            lines.append(f"- {c['claim']}{nums}{mark}")
        block = "\n".join(lines) + "\n"
        if used + len(block) > max_chars:
            skipped += 1
            continue
        out.append(block)
        used += len(block)
    if skipped:
        out.append(
            f"(+{skipped} lower-ranked papers omitted for budget; query the KB for them)"
        )
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="Query the frontier KB.")
    parser.add_argument(
        "--topic",
        action="append",
        default=[],
        help="filter by sweep area tag (repeatable)",
    )
    parser.add_argument("--grep", default=None, help="regex over title+claims")
    parser.add_argument(
        "--max-chars",
        type=int,
        default=24_000,
        help="digest budget (default 24k chars)",
    )
    args = parser.parse_args()

    nodes = load_nodes()
    if args.topic:
        wanted = set(args.topic)
        nodes = [n for n in nodes if wanted & set(n.get("topics", []))]
    if args.grep:
        rx = re.compile(args.grep, re.I)
        nodes = [
            n
            for n in nodes
            if rx.search(n.get("title") or "")
            or any(rx.search(c["claim"]) for c in n["claims"])
        ]
    if not nodes:
        print("[empty] no KB nodes match the filters", file=sys.stderr)
        return 1
    print(render(nodes, args.max_chars))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
