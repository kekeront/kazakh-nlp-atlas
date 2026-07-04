"""Build the Obsidian research vault from the frontier knowledge base.

Turns kb/nodes.jsonl into a navigable Obsidian vault under kb/vault/ — one note
per node (papers vs source/finding bundles), one Map-of-Content per topic, and a
Home index — usable both in vanilla Obsidian and as raw-markdown Claude Code
session context. Deterministic and idempotent: vault bytes are a pure function of
(nodes.jsonl, vault_links.json). The semantic cross-links + MoC summaries in
vault_links.json come from a separate LLM pass (agents return data; this script
renders and validates it — every [[wikilink]] must resolve or the build fails).

Usage:
    python scripts/build_vault.py                 # full regen (uses vault_links.json if present)
    python scripts/build_vault.py --manifest-only  # write kb/vault_manifest.json for the LLM pass, no vault write
    python scripts/build_vault.py --merge-links a.json b.json ...  # merge agent outputs -> vault_links.json
    python scripts/build_vault.py --check          # regen to a temp tree, diff vs vault, exit 1 on drift
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
NODES = ROOT / "kb" / "nodes.jsonl"
VAULT = ROOT / "kb" / "vault"
MANIFEST = ROOT / "kb" / "vault_manifest.json"
LINKS = ROOT / "kb" / "vault_links.json"

PAPER_STEM_MAX = 80
SOURCE_STEM_MAX = 60
SOURCE_TITLE_MAX = 70
MAX_RELATED_PER_NODE = 5
MAX_EDGES_PER_FROM = 4
MAX_HIGHLIGHTS = 6
RELATED_TOPICS_TOP = 5
ARXIV_RE = re.compile(r"arxiv[:\s/]*(\d{4}\.\d{4,5})", re.IGNORECASE)


# --------------------------------------------------------------------------- #
# stage 0 — load & classify                                                    #
# --------------------------------------------------------------------------- #
def load_nodes() -> list[dict[str, Any]]:
    nodes = [
        json.loads(line) for line in NODES.read_text().splitlines() if line.strip()
    ]
    nodes.sort(key=lambda n: n["id"])  # byte-stable output regardless of file order
    return nodes


def is_paper(node: dict[str, Any]) -> bool:
    return bool(node.get("arxiv_id")) and bool(node.get("abstract"))


def display_title(node: dict[str, Any]) -> str:
    """Human title for a note. Papers use their real title; source bundles use the
    first ';'-separated segment of their URL-soup title, truncated."""
    if is_paper(node):
        return node["title"].strip()
    first = node.get("title", "").split(";", 1)[0].strip()
    if len(first) > SOURCE_TITLE_MAX:
        first = first[:SOURCE_TITLE_MAX].rstrip() + "…"
    return first or node["id"]


def slug(text: str, node_id: str) -> str:
    """NFKC-fold to ASCII kebab-case; empty result falls back to a stable hash."""
    norm = unicodedata.normalize("NFKC", text).lower()
    ascii_only = norm.encode("ascii", "ignore").decode()
    kebab = re.sub(r"[^a-z0-9]+", "-", ascii_only).strip("-")
    if not kebab:
        return "n-" + hashlib.sha1(node_id.encode()).hexdigest()[:8]
    return kebab


def truncate_stem(stem: str, limit: int) -> str:
    if len(stem) <= limit:
        return stem
    cut = stem[:limit]
    boundary = cut.rfind("-")
    if boundary >= limit // 2:
        cut = cut[:boundary]
    return cut.strip("-")


def smart_truncate(text: str, limit: int) -> str:
    """Truncate at a word boundary with an ellipsis — never mid-word (Fable review #3/#4)."""
    text = text.strip()
    if len(text) <= limit:
        return text
    cut = text[:limit]
    space = cut.rfind(" ")
    if space >= limit // 2:
        cut = cut[:space]
    return cut.rstrip(" ,;:.—-") + "…"


def ellipsize_if_cut(text: str) -> str:
    """Append an ellipsis to source text (abstracts) that was pre-truncated mid-sentence."""
    text = text.strip()
    if text and text[-1] not in ".!?…\"')]":
        return text + " …"
    return text


def first_sentence(text: str, limit: int = 90) -> str:
    """A short topic descriptor: the MoC summary's first sentence, word-boundary-capped."""
    text = text.strip()
    match = re.search(r"[.!?](?:\s|$)", text)
    frag = text[: match.start() + 1] if match else text
    return smart_truncate(frag, limit)


def preferred_stem(node: dict[str, Any]) -> str:
    if is_paper(node):
        return truncate_stem(slug(node["title"], node["id"]), PAPER_STEM_MAX)
    return truncate_stem(slug(display_title(node), node["id"]), SOURCE_STEM_MAX)


def compute_filestems(nodes: list[dict[str, Any]], topics: list[str]) -> dict[str, str]:
    """Global, collision-safe id -> filestem map. Any stem claimed by >=2 members
    (including topic MoCs and Home) gets a per-id hash suffix on *every* member, so
    the mapping is stable under input reordering. Fatal if a collision survives."""
    preferred: dict[str, str] = {n["id"]: preferred_stem(n) for n in nodes}
    reserved = {f"topic::{t}": t for t in topics}
    reserved["home::Home"] = "Home"
    all_pref = {**preferred, **reserved}

    counts = Counter(all_pref.values())
    resolved: dict[str, str] = {}
    for key, stem in all_pref.items():
        if counts[stem] > 1 and not key.startswith(("topic::", "home::")):
            stem = f"{stem}-{hashlib.sha1(key.encode()).hexdigest()[:8]}"
        resolved[key] = stem

    final = Counter(resolved.values())
    dupes = {s: c for s, c in final.items() if c > 1}
    if dupes:
        raise SystemExit(f"unresolved filestem collisions: {dupes}")
    return {
        k: v for k, v in resolved.items() if not k.startswith(("topic::", "home::"))
    }


# --------------------------------------------------------------------------- #
# rendering helpers                                                            #
# --------------------------------------------------------------------------- #
def yaml_line(key: str, value: Any) -> str:
    """One frontmatter line; JSON is a valid YAML subset so json.dumps escapes
    colons/quotes/unicode in titles for free."""
    return f"{key}: {json.dumps(value, ensure_ascii=False)}"


def blockquote(text: str) -> list[str]:
    """Callout-body lines: escape [[ so claim text can't spawn phantom links."""
    safe = text.replace("[[", "[\\[")
    return ["> " + line for line in safe.splitlines()] or ["> "]


CALLOUT = {
    "confirmed": ("success", "CONFIRMED"),
    "refuted": ("failure", "REFUTED"),
}


def claim_status(claim: dict[str, Any]) -> tuple[str, str]:
    ver = claim.get("verification")
    if ver and ver.get("verdict"):
        verdict = ver["verdict"]
        head = verdict.split()[0].lower()
        if head in CALLOUT:
            return CALLOUT[head]
        return "question", verdict.split()[0].upper()
    if claim.get("uncertain"):
        return "warning", "UNCERTAIN"
    return "note", "CLAIM"


def render_claim(
    claim: dict[str, Any], arxiv_to_stem: dict[str, str], owner_stem: str
) -> list[str]:
    kind, label = claim_status(claim)
    area = claim.get("area") or "general"
    out = [f"> [!{kind}] {label} — {area}"]
    out += blockquote(claim.get("claim", ""))
    detail: list[tuple[str, str]] = []
    if claim.get("numbers"):
        detail.append(("Numbers", claim["numbers"]))
    if claim.get("relevance"):
        detail.append(("Relevance", claim["relevance"]))
    ver = claim.get("verification")
    if ver:
        if ver.get("verdict"):
            detail.append(("Verdict", ver["verdict"]))
        if ver.get("note"):
            detail.append(("Verification note", ver["note"]))
        if ver.get("settling_experiment"):
            detail.append(("Settling experiment", ver["settling_experiment"]))
    src = claim.get("source") or "—"
    sweep = claim.get("sweep") or "—"
    if detail:
        out.append(">")
        for key, val in detail:
            out.append(f"> **{key}:** {val.replace(chr(10), ' ')}")
    out.append(f"> **Source:** {src.replace(chr(10), ' ')} · **Sweep:** `{sweep}`")

    # in-KB citation mining: link claims that name another KB paper by arXiv id.
    hits: list[str] = []
    haystack = f"{claim.get('claim', '')} {claim.get('source', '')}"
    for match in ARXIV_RE.findall(haystack):
        stem = arxiv_to_stem.get(match)
        if stem and stem != owner_stem and stem not in hits:
            hits.append(stem)
    if hits:
        out.append("")
        out.append("**Cited KB notes:** " + ", ".join(f"[[{s}]]" for s in hits))
    return out


def verdict_tags(node: dict[str, Any]) -> list[str]:
    tags = sorted(
        {
            c["verification"]["verdict"].split()[0].lower()
            for c in node.get("claims", [])
            if c.get("verification") and c["verification"].get("verdict")
        }
    )
    return tags


def related_lines(
    node_id: str,
    edges_by_node: dict[str, list[tuple[str, str]]],
    stems: dict[str, str],
    titles: dict[str, str],
) -> list[str]:
    edges = edges_by_node.get(node_id, [])
    if not edges:
        return []
    out = ["", "## Related"]
    for other_id, why in edges:
        title = titles[other_id]
        disp = title if len(title) <= 90 else title[:90].rstrip() + "…"
        out.append(f"- [[{stems[other_id]}|{disp}]] — {why}")
    return out


# --------------------------------------------------------------------------- #
# note templates                                                               #
# --------------------------------------------------------------------------- #
def render_paper(
    node: dict[str, Any],
    ctx: dict[str, Any],
) -> str:
    title = display_title(node)
    claims = node.get("claims", [])
    aliases = [title, f"arXiv:{node['arxiv_id']}", node["id"]]
    fm = [
        "---",
        yaml_line("kb_id", node["id"]),
        yaml_line("type", "paper"),
        yaml_line("title", title),
        yaml_line("arxiv_id", node.get("arxiv_id")),
        yaml_line("doi", node.get("doi")),
        yaml_line("hf_repo", node.get("hf_repo")),
        yaml_line("year", node.get("year")),
        yaml_line("topics", node.get("topics", [])),
        yaml_line("claims", len(claims)),
        yaml_line("uncertain_claims", sum(1 for c in claims if c.get("uncertain"))),
        yaml_line("verdicts", verdict_tags(node)),
        yaml_line("aliases", aliases),
        yaml_line("tags", ["paper", *[f"topic/{t}" for t in node.get("topics", [])]]),
        "---",
    ]
    body = [f"# {title}", ""]
    body.append(f"[arXiv](https://arxiv.org/abs/{node['arxiv_id']})")
    if node.get("topics"):
        body.append("**Topics:** " + ", ".join(f"[[{t}]]" for t in node["topics"]))
    body += ["", "> [!abstract]", *blockquote(ellipsize_if_cut(node["abstract"])), ""]
    body.append("## Claims")
    for claim in claims:
        body.append("")
        body += render_claim(claim, ctx["arxiv_to_stem"], ctx["stems"][node["id"]])
    body += related_lines(node["id"], ctx["edges_by_node"], ctx["stems"], ctx["titles"])
    body += ["", "[[Home]]"]
    return "\n".join(fm + body) + "\n"


def render_source(node: dict[str, Any], ctx: dict[str, Any]) -> str:
    title = display_title(node)
    claims = node.get("claims", [])
    fm = [
        "---",
        yaml_line("kb_id", node["id"]),
        yaml_line("type", "source"),
        yaml_line("title", title),
        yaml_line("doi", node.get("doi")),
        yaml_line("hf_repo", node.get("hf_repo")),
        yaml_line("year", node.get("year")),
        yaml_line("topics", node.get("topics", [])),
        yaml_line("claims", len(claims)),
        yaml_line("uncertain_claims", sum(1 for c in claims if c.get("uncertain"))),
        yaml_line("verdicts", verdict_tags(node)),
        yaml_line("aliases", [node["id"]]),
        yaml_line("tags", ["source", *[f"topic/{t}" for t in node.get("topics", [])]]),
        "---",
    ]
    body = [f"# {title}", ""]
    if node.get("topics"):
        body.append("**Topics:** " + ", ".join(f"[[{t}]]" for t in node["topics"]))
    segments = [s.strip() for s in node.get("title", "").split(";") if s.strip()]
    if segments:
        body += ["", "## Source URLs"]
        body += [f"- {seg}" for seg in segments]
    body += ["", "## Findings"]
    for claim in claims:
        body.append("")
        body += render_claim(claim, ctx["arxiv_to_stem"], ctx["stems"][node["id"]])
    body += related_lines(node["id"], ctx["edges_by_node"], ctx["stems"], ctx["titles"])
    body += ["", "[[Home]]"]
    return "\n".join(fm + body) + "\n"


def render_moc(topic: str, ctx: dict[str, Any]) -> str:
    members = ctx["topic_nodes"][topic]
    papers = [n for n in members if is_paper(n)]
    sources = [n for n in members if not is_paper(n)]
    uncertain = sum(
        1 for n in members for c in n.get("claims", []) if c.get("uncertain")
    )
    moc = ctx["mocs"].get(topic, {})

    fm = [
        "---",
        yaml_line("type", "moc"),
        yaml_line("topic", topic),
        yaml_line("nodes", len(members)),
        yaml_line("papers", len(papers)),
        yaml_line("sources", len(sources)),
        yaml_line("uncertain_claims", uncertain),
        yaml_line("tags", ["moc"]),
        "---",
    ]
    body = [f"# Topic: {topic}", ""]
    summary = moc.get("summary")
    body.append(
        summary or "_No synthesized summary yet — regenerate with the semantic pass._"
    )

    highlights = moc.get("highlights", [])
    if highlights:
        body += ["", "## Frontier highlights"]
        for hl in highlights:
            nid = hl["node_id"]
            if nid in ctx["stems"]:
                title = ctx["titles"][nid]
                disp = title if len(title) <= 80 else title[:80].rstrip() + "…"
                body.append(f"- [[{ctx['stems'][nid]}|{disp}]] — {hl['phrase']}")

    def sort_key(n: dict[str, Any]) -> tuple[int, str]:
        return (-(n.get("year") or 0), n["id"])

    if papers:
        body += ["", f"## Papers ({len(papers)})"]
        for n in sorted(papers, key=sort_key):
            title = ctx["titles"][n["id"]]
            disp = title if len(title) <= 100 else title[:100].rstrip() + "…"
            year = n.get("year") or "n.d."
            area = (n.get("claims") or [{}])[0].get("area", "")
            tail = f" — {area}" if area else ""
            body.append(f"- [[{ctx['stems'][n['id']]}|{disp}]] ({year}){tail}")

    if sources:
        body += ["", f"## Sources & findings ({len(sources)})"]
        for n in sorted(sources, key=lambda n: n["id"]):
            title = ctx["titles"][n["id"]]
            first_claim = (n.get("claims") or [{}])[0].get("claim", "")
            snip = first_claim[:120].rstrip() + ("…" if len(first_claim) > 120 else "")
            tail = f" — {snip}" if snip else ""
            body.append(f"- [[{ctx['stems'][n['id']]}|{title}]]{tail}")

    related = ctx["related_topics"].get(topic, [])
    if related:
        body += ["", "## Related topics"]
        for other, shared in related:
            body.append(f"- [[{other}]] — {shared} shared nodes")

    body += ["", "[[Home]]"]
    return "\n".join(fm + body) + "\n"


def render_home(nodes: list[dict[str, Any]], ctx: dict[str, Any]) -> str:
    papers = [n for n in nodes if is_paper(n)]
    topic_counts = ctx["topic_nodes"]
    total_claims = sum(len(n.get("claims", [])) for n in nodes)
    verified = sum(
        1
        for n in nodes
        for c in n.get("claims", [])
        if (c.get("verification") or {}).get("verdict")
    )
    pct = round(100 * verified / total_claims, 1) if total_claims else 0.0

    def topic_uncertain(t: str) -> int:
        return sum(
            1
            for n in topic_counts[t]
            for c in n.get("claims", [])
            if c.get("uncertain")
        )

    def topic_papers(t: str) -> int:
        return sum(1 for n in topic_counts[t] if is_paper(n))

    fm = [
        "---",
        yaml_line("type", "home"),
        yaml_line("tags", ["moc"]),
        yaml_line("nodes", len(nodes)),
        yaml_line("papers", len(papers)),
        yaml_line("sources", len(nodes) - len(papers)),
        yaml_line("topics", len(topic_counts)),
        yaml_line("claims", total_claims),
        "---",
    ]
    body = [
        "# Kazakh NLP Atlas — Research Vault",
        "",
        "Knowledge base of the Kazakh Frontier Lab. Two pillars: **QymyzLM** (Kazakh SLM,",
        "≤600M active params) and the **best Kazakh text-embedding model**. Every note is",
        "generated from `kb/nodes.jsonl` — do not edit generated notes by hand (use `notes/`);",
        "regenerate with `python scripts/build_vault.py`.",
        "",
        "## How to use this vault (Claude Code)",
        "1. Start at the topic map below; open the MoC nearest your design question.",
        '2. MoC "Frontier highlights" = the current best-supported picture per topic.',
        "3. Claim callouts encode evidence status: `[!success] CONFIRMED` / `[!failure] REFUTED`",
        "   / `[!warning] UNCERTAIN` / `[!note] CLAIM` (asserted, unverified). Treat UNCERTAIN",
        "   and REFUTED as not load-bearing for design decisions.",
        "4. `kb_id` in frontmatter is the canonical citation key used by /design-panel and /research-sweep.",
        "",
        f"> [!warning] Verification coverage ~{pct}%",
        f"> Only {verified}/{total_claims} claims carry a CONFIRMED/REFUTED/PLAUSIBLE verdict from adversarial"
        " review. The rest render as `[!note] CLAIM` — asserted by a single sweep agent and NOT yet audited."
        " Treat unaudited numbers as provisional, not vetted.",
        "",
        "## Pillars",
    ]

    pillars = ctx["home"].get("pillars")
    assigned: set[str] = set()
    if pillars:
        groups = []
        for pillar in pillars:
            topics = [t for t in pillar.get("topics", []) if t in topic_counts]
            groups.append((pillar["name"], topics))
            assigned.update(topics)
        leftover = sorted(set(topic_counts) - assigned)
        if leftover:
            groups.append(("Cross-cutting / meta", leftover))
    else:
        groups = [("All topics", sorted(topic_counts))]

    for name, topics in groups:
        if not topics:
            continue
        body += [
            "",
            f"### {name}",
            "",
            "| Topic | Nodes | Uncertain |",
            "| --- | --- | --- |",
        ]
        for t in sorted(topics, key=lambda t: (-len(topic_counts[t]), t)):
            body.append(f"| [[{t}]] | {len(topic_counts[t])} | {topic_uncertain(t)} |")

    body += [
        "",
        "## All topics A–Z",
        "",
        "| Topic | Focus | Nodes | Papers | Uncertain |",
        "| --- | --- | --- | --- | --- |",
    ]
    for t in sorted(topic_counts):
        summary = (ctx["mocs"].get(t) or {}).get("summary") or ""
        focus = first_sentence(summary).replace("|", "\\|") if summary else "—"
        body.append(
            f"| [[{t}]] | {focus} | {len(topic_counts[t])} | {topic_papers(t)} | {topic_uncertain(t)} |"
        )
    return "\n".join(fm + body) + "\n"


# --------------------------------------------------------------------------- #
# context assembly                                                             #
# --------------------------------------------------------------------------- #
def build_context(nodes: list[dict[str, Any]], links: dict[str, Any]) -> dict[str, Any]:
    topic_nodes: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for n in nodes:
        for t in n.get("topics", []):
            topic_nodes[t].append(n)
    topics = sorted(topic_nodes)

    stems = compute_filestems(nodes, topics)
    titles = {n["id"]: display_title(n) for n in nodes}
    arxiv_to_stem = {n["arxiv_id"]: stems[n["id"]] for n in nodes if n.get("arxiv_id")}

    # related topics by node co-occurrence (>=2 shared), top-N by shared count.
    co: dict[str, Counter] = defaultdict(Counter)
    node_topics = {n["id"]: n.get("topics", []) for n in nodes}
    for ts in node_topics.values():
        for i, a in enumerate(ts):
            for b in ts[i + 1 :]:
                co[a][b] += 1
                co[b][a] += 1
    related_topics: dict[str, list[tuple[str, int]]] = {}
    for t in topics:
        pairs = [(o, c) for o, c in co[t].items() if c >= 2]
        pairs.sort(key=lambda x: (-x[1], x[0]))
        related_topics[t] = pairs[:RELATED_TOPICS_TOP]

    # semantic edges -> per-node rendered Related (already capped/deduped at merge).
    valid = set(stems)
    edges_by_node: dict[str, list[tuple[str, str]]] = defaultdict(list)
    seen_pairs: set[tuple[str, str]] = set()
    for edge in links.get("edges", []):
        a, b, why = edge.get("from"), edge.get("to"), edge.get("why", "")
        if a not in valid or b not in valid or a == b:
            continue
        key = tuple(sorted((a, b)))
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        edges_by_node[a].append((b, why))
        edges_by_node[b].append((a, why))
    for nid in list(edges_by_node):
        edges_by_node[nid] = edges_by_node[nid][:MAX_RELATED_PER_NODE]

    return {
        "stems": stems,
        "titles": titles,
        "arxiv_to_stem": arxiv_to_stem,
        "topic_nodes": topic_nodes,
        "topics": topics,
        "related_topics": related_topics,
        "edges_by_node": edges_by_node,
        "mocs": links.get("mocs", {}),
        "home": links.get("home", {}),
    }


# --------------------------------------------------------------------------- #
# manifest (the LLM-pass contract)                                             #
# --------------------------------------------------------------------------- #
def write_manifest(nodes: list[dict[str, Any]], ctx: dict[str, Any]) -> None:
    manifest = {
        "version": 1,
        "nodes": [
            {
                "kb_id": n["id"],
                "type": "paper" if is_paper(n) else "source",
                "filestem": ctx["stems"][n["id"]],
                "title": ctx["titles"][n["id"]],
                "year": n.get("year"),
                "topics": n.get("topics", []),
                "claims": [
                    {
                        "area": c.get("area"),
                        "claim": c.get("claim"),
                        "numbers": c.get("numbers"),
                        "uncertain": bool(c.get("uncertain")),
                        "verdict": (c.get("verification") or {}).get("verdict"),
                    }
                    for c in n.get("claims", [])
                ],
            }
            for n in nodes
        ],
        "topics": {
            t: {
                "node_ids": [n["id"] for n in ctx["topic_nodes"][t]],
                "count": len(ctx["topic_nodes"][t]),
            }
            for t in ctx["topics"]
        },
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(
        f"wrote {MANIFEST.relative_to(ROOT)} ({len(nodes)} nodes, {len(ctx['topics'])} topics)"
    )


# --------------------------------------------------------------------------- #
# merge agent outputs -> vault_links.json                                      #
# --------------------------------------------------------------------------- #
def merge_links(
    paths: list[str], nodes: list[dict[str, Any]], ctx: dict[str, Any]
) -> None:
    valid = set(ctx["stems"])
    edges: list[dict[str, str]] = []
    mocs: dict[str, Any] = {}
    home: dict[str, Any] = {}
    dropped = 0

    for path in paths:
        payload = json.loads(Path(path).read_text())
        blocks = payload if isinstance(payload, list) else [payload]
        for block in blocks:
            if "home" in block:
                home = block["home"]
            topic = block.get("topic")
            if topic:
                summary = block.get("summary")
                highlights = [
                    h
                    for h in block.get("highlights", [])[:MAX_HIGHLIGHTS]
                    if h.get("node_id") in valid
                ]
                mocs[topic] = {"summary": summary, "highlights": highlights}
            per_from: Counter = Counter()
            for edge in block.get("edges", []):
                a, b, why = (
                    edge.get("from"),
                    edge.get("to"),
                    (edge.get("why") or "").strip(),
                )
                if a not in valid or b not in valid or a == b or not why:
                    dropped += 1
                    continue
                if per_from[a] >= MAX_EDGES_PER_FROM:
                    dropped += 1
                    continue
                per_from[a] += 1
                edges.append(
                    {
                        "from": a,
                        "to": b,
                        "why": smart_truncate(why, 140),
                        "agent": f"topic:{topic}",
                    }
                )

    # dedupe symmetric edges, keep lexicographically-first (from,to)'s why.
    best: dict[tuple[str, str], dict[str, str]] = {}
    node_topics = {n["id"]: set(n.get("topics", [])) for n in nodes}
    for e in edges:
        key = tuple(sorted((e["from"], e["to"])))
        if key not in best or (e["from"], e["to"]) < (
            best[key]["from"],
            best[key]["to"],
        ):
            best[key] = e

    def cross_topic(e: dict[str, str]) -> int:
        return (
            0
            if node_topics.get(e["from"], set()) & node_topics.get(e["to"], set())
            else 1
        )

    # global cap: <=MAX_RELATED_PER_NODE rendered per node (rank cross-topic, short why, lexicographic).
    ranked = sorted(
        best.values(),
        key=lambda e: (-cross_topic(e), len(e["why"]), e["from"], e["to"]),
    )
    per_node: Counter = Counter()
    kept: list[dict[str, str]] = []
    for e in ranked:
        if (
            per_node[e["from"]] >= MAX_RELATED_PER_NODE
            or per_node[e["to"]] >= MAX_RELATED_PER_NODE
        ):
            dropped += 1
            continue
        per_node[e["from"]] += 1
        per_node[e["to"]] += 1
        kept.append(e)
    kept.sort(key=lambda e: (e["from"], e["to"]))

    out = {
        "version": 1,
        "edges": kept,
        "mocs": {k: mocs[k] for k in sorted(mocs)},
        "home": home,
    }
    LINKS.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(
        f"wrote {LINKS.relative_to(ROOT)}: {len(kept)} edges, {len(mocs)} MoCs, {dropped} dropped"
    )


# --------------------------------------------------------------------------- #
# stage 1/3/4 — scaffold + apply + validate                                    #
# --------------------------------------------------------------------------- #
def render_all(nodes: list[dict[str, Any]], ctx: dict[str, Any]) -> dict[Path, str]:
    files: dict[Path, str] = {}
    for n in nodes:
        stem = ctx["stems"][n["id"]]
        if is_paper(n):
            files[VAULT / "papers" / f"{stem}.md"] = render_paper(n, ctx)
        else:
            files[VAULT / "sources" / f"{stem}.md"] = render_source(n, ctx)
    for t in ctx["topics"]:
        files[VAULT / "maps" / f"{t}.md"] = render_moc(t, ctx)
    files[VAULT / "Home.md"] = render_home(nodes, ctx)
    return files


def validate(files: dict[Path, str], ctx: dict[str, Any]) -> None:
    valid_targets = set(ctx["stems"].values()) | set(ctx["topics"]) | {"Home"}
    link_re = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
    problems: list[str] = []
    for path, text in files.items():
        for target in link_re.findall(text):
            if target not in valid_targets:
                problems.append(f"{path.name}: dangling [[{target}]]")
    stems = [p.stem for p in files if p.parent.name in ("papers", "sources")]
    if len(stems) != len(set(stems)):
        problems.append("duplicate filestems across papers/sources")
    for t in ctx["topics"]:
        if VAULT / "maps" / f"{t}.md" not in files:
            problems.append(f"topic {t} has no MoC")
    if problems:
        raise SystemExit("VALIDATION FAILED:\n  " + "\n  ".join(problems[:40]))


def write_vault(files: dict[Path, str]) -> None:
    for sub in ("papers", "sources", "maps", "notes"):
        (VAULT / sub).mkdir(parents=True, exist_ok=True)
    (VAULT / "notes" / ".gitkeep").touch()
    for sub in ("papers", "sources", "maps"):
        for stale in (VAULT / sub).glob("*.md"):
            stale.unlink()
    (VAULT / "Home.md").unlink(missing_ok=True)
    for path, text in files.items():
        path.write_text(text)


def check_drift(files: dict[Path, str]) -> int:
    drift = []
    for path, text in files.items():
        if not path.exists() or path.read_text() != text:
            drift.append(path.relative_to(ROOT))
    on_disk = {
        p for sub in ("papers", "sources", "maps") for p in (VAULT / sub).glob("*.md")
    }
    extra = on_disk - set(files)
    if drift or extra:
        for p in drift:
            print(f"DRIFT: {p}")
        for p in extra:
            print(f"EXTRA: {p.relative_to(ROOT)}")
        return 1
    print(f"vault in sync ({len(files)} notes)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--manifest-only",
        action="store_true",
        help="write vault_manifest.json, no vault",
    )
    group.add_argument(
        "--merge-links",
        nargs="+",
        metavar="JSON",
        help="merge agent outputs into vault_links.json",
    )
    group.add_argument(
        "--check",
        action="store_true",
        help="exit 1 if the on-disk vault differs from a fresh build",
    )
    args = parser.parse_args(argv)

    nodes = load_nodes()
    links = json.loads(LINKS.read_text()) if LINKS.exists() else {}
    ctx = build_context(nodes, links)

    if args.manifest_only:
        write_manifest(nodes, ctx)
        return 0
    if args.merge_links:
        merge_links(args.merge_links, nodes, ctx)
        return 0

    files = render_all(nodes, ctx)
    validate(files, ctx)
    if args.check:
        return check_drift(files)

    write_vault(files)
    edges = sum(len(v) for v in ctx["edges_by_node"].values()) // 2
    print(
        f"vault built: {len(files)} notes, {len(ctx['topics'])} MoCs, {edges} semantic edges applied"
    )
    print("point Claude Code sessions at kb/vault/Home.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
