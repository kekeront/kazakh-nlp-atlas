"""Scrape and structure the Kazakh-NLP research corpus.

Pulls papers from two complementary sources and merges them into a single,
de-duplicated, auto-tagged dataset:

  * arXiv API  (http://export.arxiv.org/api/query) -- preprints, reliable, free.
  * Semantic Scholar Graph API -- adds non-arXiv venues (ACL, MDPI, Frontiers)
    and citation counts. Best-effort: rate-limited without a key, so failures
    degrade gracefully instead of aborting the run.

Scope: Kazakh-only. A paper is kept only if it is about NLP/ML *and* mentions
Kazakh (or the alt spelling "qazaq"). The relevance filter is intentionally
explicit and conservative -- better to drop a borderline paper than to pollute
the corpus with Kazakhstan-the-country physics papers.

Output: paper/survey/papers.json  -- pure scraped facts, reproducible.
The editorial layer (flagship-model comparison, gap analysis) lives in
build_map.py, not here, so this file stays a faithful record of what exists.

Usage:
    python code/scrape_papers.py [--out paper/survey/papers.json] [--no-s2]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET  # Element type + ParseError only
from dataclasses import asdict, dataclass, field
from pathlib import Path

# Parse XML through defusedxml to neutralise XXE / billion-laughs attacks
# (arXiv's API is served over http://, so the response is not fully trusted).
# Fall back to stdlib only if defusedxml is unavailable.
try:
    from defusedxml.ElementTree import fromstring as _safe_fromstring
except ImportError:  # pragma: no cover
    _safe_fromstring = ET.fromstring

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

ARXIV_ENDPOINT = "http://export.arxiv.org/api/query"
S2_ENDPOINT = "https://api.semanticscholar.org/graph/v1/paper/search"
USER_AGENT = "kazakh-nlp-survey/1.0 (research map; mailto:hey@evgenyastapov.com)"

# arXiv: broad recall queries. `all:` searches every field, so these two cover
# the field; relevance/category filtering happens client-side below.
ARXIV_QUERIES: list[str] = [
    "all:kazakh",
    "all:qazaq",
]

# Semantic Scholar: targeted topical queries to surface non-arXiv venues.
S2_QUERIES: list[str] = [
    "kazakh language model",
    "kazakh large language model",
    "kazakh tokenization",
    "kazakh morphology nlp",
    "kazakh BERT",
    "kazakh machine translation",
    "kazakh speech recognition",
    "kazakh named entity recognition",
    "kazakh text dataset corpus",
    "kazakh natural language processing",
]

# Only keep papers in these arXiv categories (drop physics/astro/etc.).
RELEVANT_ARXIV_CATS = {
    "cs.CL", "cs.AI", "cs.LG", "cs.IR", "cs.NE", "cs.SD", "eess.AS", "stat.ML",
}

# A kept paper must contain at least one of these (NLP/ML relevance) ...
RELEVANCE_TERMS = (
    "language model", "llm", "nlp", "natural language", "token", "morpholog",
    "transformer", "bert", "gpt", "llama", "qwen", "embedding", "corpus",
    "dataset", "translation", "speech", "asr", "tts", "named entity", "ner",
    "sentiment", "text classification", "question answering", "benchmark",
    "fine-tun", "pretrain", "summariz", "treebank", "subword", "vocabulary",
)

# ... and must mention Kazakh (scope guard).
KAZAKH_TERMS = ("kazakh", "qazaq", "kazax")

# Multi-label category tagging. Order matters only for readability.
CATEGORY_KEYWORDS: dict[str, tuple[str, ...]] = {
    "tokenization": ("token", "subword", "bpe", "sentencepiece", "wordpiece", "vocabulary", "fertility"),
    "morphology": ("morpholog", "segmentation", "agglutinat", "treebank", "lemmat", "affix", "morpheme"),
    "language-model": ("language model", "llm", "gpt", "llama", "qwen", "pretrain", "causal", "foundation model"),
    "machine-translation": ("translation", "mt ", "nmt", "parallel corpus", "multilingual translation"),
    "speech": ("speech", "asr", "tts", "acoustic", "voice", "audio", "phonem"),
    "ner-ie": ("named entity", "ner", "information extraction", "relation extraction"),
    "dataset-corpus": ("dataset", "corpus", "benchmark", "annotated", "treebank", "resource"),
    "evaluation": ("evaluation", "benchmark", "metric", "leaderboard", "probing"),
    "classification": ("classification", "sentiment", "toxic", "detection"),
    "embeddings": ("embedding", "word2vec", "representation", "semantic similarity"),
}


# --------------------------------------------------------------------------- #
# Data model
# --------------------------------------------------------------------------- #


@dataclass
class Paper:
    """One research artifact, source-agnostic."""

    title: str
    abstract: str
    year: int | None
    date: str | None  # ISO yyyy-mm-dd when known
    authors: list[str]
    url: str
    arxiv_id: str | None = None
    doi: str | None = None
    venue: str | None = None
    citation_count: int | None = None
    categories: list[str] = field(default_factory=list)  # our tags
    arxiv_cats: list[str] = field(default_factory=list)  # raw arXiv subject classes
    sources: list[str] = field(default_factory=list)  # {"arxiv","semantic_scholar"}

    def dedup_key(self) -> str:
        """Stable identity for merging across sources."""
        if self.arxiv_id:
            return f"arxiv:{self.arxiv_id}"
        if self.doi:
            return f"doi:{self.doi.lower()}"
        return f"title:{_norm_title(self.title)}"


def _norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


# --------------------------------------------------------------------------- #
# HTTP helper
# --------------------------------------------------------------------------- #


def _http_get(url: str, *, timeout: int = 30, retries: int = 3) -> bytes | None:
    """GET with a courteous UA and exponential backoff on 429/5xx.

    Returns None on terminal failure so callers can degrade gracefully.
    """
    backoff = 3.0
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503, 504) and attempt < retries:
                wait = backoff * attempt
                print(f"  [retry {attempt}/{retries}] HTTP {exc.code}; sleeping {wait:.0f}s", file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  [http error] {exc.code} for {url}", file=sys.stderr)
            return None
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt < retries:
                time.sleep(backoff * attempt)
                continue
            print(f"  [network error] {exc} for {url}", file=sys.stderr)
            return None
    return None


# --------------------------------------------------------------------------- #
# arXiv
# --------------------------------------------------------------------------- #

_ATOM = "{http://www.w3.org/2005/Atom}"
_ARXIV_NS = "{http://arxiv.org/schemas/atom}"


def _parse_arxiv_entry(entry: ET.Element) -> Paper | None:
    raw_id = (entry.findtext(f"{_ATOM}id") or "").strip()
    # e.g. http://arxiv.org/abs/2503.01493v2  ->  2503.01493
    m = re.search(r"arxiv\.org/abs/([^v\s]+)", raw_id)
    arxiv_id = m.group(1) if m else None

    title = re.sub(r"\s+", " ", (entry.findtext(f"{_ATOM}title") or "").strip())
    abstract = re.sub(r"\s+", " ", (entry.findtext(f"{_ATOM}summary") or "").strip())
    published = (entry.findtext(f"{_ATOM}published") or "").strip()
    date = published[:10] if len(published) >= 10 else None
    year = int(date[:4]) if date else None

    authors = [
        (a.findtext(f"{_ATOM}name") or "").strip()
        for a in entry.findall(f"{_ATOM}author")
    ]
    authors = [a for a in authors if a]

    cats = [
        c.get("term", "")
        for c in entry.findall(f"{_ATOM}category")
    ]
    cats = [c for c in cats if c]

    doi = entry.findtext(f"{_ARXIV_NS}doi")
    url = raw_id or (f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else "")

    if not title or not arxiv_id:
        return None

    return Paper(
        title=title,
        abstract=abstract,
        year=year,
        date=date,
        authors=authors,
        url=url,
        arxiv_id=arxiv_id,
        doi=doi.strip() if doi else None,
        venue="arXiv",
        arxiv_cats=cats,
        sources=["arxiv"],
    )


def fetch_arxiv(*, page_size: int = 100, max_per_query: int = 300) -> list[Paper]:
    out: list[Paper] = []
    for query in ARXIV_QUERIES:
        print(f"[arxiv] query={query!r}", file=sys.stderr)
        for start in range(0, max_per_query, page_size):
            params = urllib.parse.urlencode(
                {
                    "search_query": query,
                    "start": start,
                    "max_results": page_size,
                    "sortBy": "submittedDate",
                    "sortOrder": "descending",
                }
            )
            body = _http_get(f"{ARXIV_ENDPOINT}?{params}")
            if body is None:
                break
            try:
                root = ET.fromstring(body)
            except ET.ParseError as exc:
                print(f"  [xml parse error] {exc}", file=sys.stderr)
                break
            entries = root.findall(f"{_ATOM}entry")
            if not entries:
                break
            for e in entries:
                p = _parse_arxiv_entry(e)
                if p is not None:
                    out.append(p)
            print(f"  start={start} -> {len(entries)} entries", file=sys.stderr)
            if len(entries) < page_size:
                break
            time.sleep(3)  # arXiv asks for ~3s between requests
    return out


# --------------------------------------------------------------------------- #
# Semantic Scholar
# --------------------------------------------------------------------------- #

_S2_FIELDS = "title,abstract,year,authors,venue,citationCount,externalIds,url,publicationDate"


def _parse_s2_paper(obj: dict) -> Paper | None:
    title = (obj.get("title") or "").strip()
    if not title:
        return None
    abstract = (obj.get("abstract") or "").strip()
    ext = obj.get("externalIds") or {}
    arxiv_id = ext.get("ArXiv")
    doi = ext.get("DOI")
    date = obj.get("publicationDate")  # yyyy-mm-dd or None
    year = obj.get("year")
    authors = [a.get("name", "").strip() for a in (obj.get("authors") or [])]
    authors = [a for a in authors if a]
    url = obj.get("url") or (f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else "")
    cc = obj.get("citationCount")

    return Paper(
        title=re.sub(r"\s+", " ", title),
        abstract=re.sub(r"\s+", " ", abstract),
        year=int(year) if isinstance(year, int) else None,
        date=date if (date and len(date) >= 10) else None,
        authors=authors,
        url=url,
        arxiv_id=arxiv_id.strip() if arxiv_id else None,
        doi=doi.strip() if doi else None,
        venue=(obj.get("venue") or None),
        citation_count=int(cc) if isinstance(cc, int) else None,
        sources=["semantic_scholar"],
    )


def fetch_semantic_scholar(*, limit: int = 100) -> list[Paper]:
    out: list[Paper] = []
    for query in S2_QUERIES:
        params = urllib.parse.urlencode(
            {"query": query, "fields": _S2_FIELDS, "limit": limit}
        )
        print(f"[s2] query={query!r}", file=sys.stderr)
        body = _http_get(f"{S2_ENDPOINT}?{params}")
        if body is None:
            print("  [s2] skipped (no response)", file=sys.stderr)
            time.sleep(2)
            continue
        try:
            payload = json.loads(body)
        except json.JSONDecodeError as exc:
            print(f"  [s2 json error] {exc}", file=sys.stderr)
            continue
        for obj in payload.get("data") or []:
            p = _parse_s2_paper(obj)
            if p is not None:
                out.append(p)
        print(f"  -> {len(payload.get('data') or [])} hits", file=sys.stderr)
        time.sleep(2)  # be polite to the shared rate-limit pool
    return out


# --------------------------------------------------------------------------- #
# Relevance, tagging, merge
# --------------------------------------------------------------------------- #


def is_relevant(p: Paper) -> bool:
    """Kazakh-only NLP/ML scope guard."""
    blob = f"{p.title} {p.abstract}".lower()
    if not any(k in blob for k in KAZAKH_TERMS):
        return False
    # arXiv papers: require a relevant subject class when we have one.
    if p.arxiv_cats and not (set(p.arxiv_cats) & RELEVANT_ARXIV_CATS):
        # allow through only if the text is strongly NLP-relevant anyway
        if not any(t in blob for t in RELEVANCE_TERMS):
            return False
    return any(t in blob for t in RELEVANCE_TERMS)


def tag_categories(p: Paper) -> list[str]:
    blob = f"{p.title} {p.abstract}".lower()
    tags = [
        cat
        for cat, kws in CATEGORY_KEYWORDS.items()
        if any(kw in blob for kw in kws)
    ]
    return tags or ["other"]


def merge(papers: list[Paper]) -> list[Paper]:
    """De-duplicate across sources, preferring richer fields."""
    by_key: dict[str, Paper] = {}
    for p in papers:
        key = p.dedup_key()
        if key not in by_key:
            by_key[key] = p
            continue
        cur = by_key[key]
        # union sources
        for s in p.sources:
            if s not in cur.sources:
                cur.sources.append(s)
        # prefer the longer abstract
        if len(p.abstract) > len(cur.abstract):
            cur.abstract = p.abstract
        # fill citation count from S2
        if cur.citation_count is None and p.citation_count is not None:
            cur.citation_count = p.citation_count
        # fill missing scalars
        cur.doi = cur.doi or p.doi
        cur.arxiv_id = cur.arxiv_id or p.arxiv_id
        cur.venue = cur.venue or p.venue
        cur.date = cur.date or p.date
        cur.year = cur.year or p.year
        if len(p.authors) > len(cur.authors):
            cur.authors = p.authors
        if not cur.arxiv_cats and p.arxiv_cats:
            cur.arxiv_cats = p.arxiv_cats
    return list(by_key.values())


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def main() -> int:
    parser = argparse.ArgumentParser(description="Scrape the Kazakh-NLP research corpus.")
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("paper/survey/papers.json"),
        help="output JSON path",
    )
    parser.add_argument("--no-s2", action="store_true", help="skip Semantic Scholar")
    parser.add_argument("--no-arxiv", action="store_true", help="skip arXiv")
    args = parser.parse_args()

    raw: list[Paper] = []
    if not args.no_arxiv:
        raw += fetch_arxiv()
    if not args.no_s2:
        raw += fetch_semantic_scholar()

    print(f"[merge] {len(raw)} raw records", file=sys.stderr)
    merged = merge(raw)
    print(f"[merge] {len(merged)} after dedup", file=sys.stderr)

    kept = [p for p in merged if is_relevant(p)]
    for p in kept:
        p.categories = tag_categories(p)
    print(f"[filter] {len(kept)} Kazakh-NLP relevant", file=sys.stderr)

    # newest first; undated papers sink to the bottom
    kept.sort(key=lambda p: (p.date or "0000-00-00"), reverse=True)

    source_counts = {"arxiv": 0, "semantic_scholar": 0, "both": 0}
    for p in kept:
        if len(p.sources) > 1:
            source_counts["both"] += 1
        elif p.sources:
            source_counts[p.sources[0]] = source_counts.get(p.sources[0], 0) + 1

    cat_counts: dict[str, int] = {}
    for p in kept:
        for c in p.categories:
            cat_counts[c] = cat_counts.get(c, 0) + 1

    payload = {
        "meta": {
            "scope": "kazakh-only",
            "sources": ["arxiv", "semantic_scholar"],
            "arxiv_queries": ARXIV_QUERIES,
            "s2_queries": S2_QUERIES,
            "count": len(kept),
            "source_breakdown": source_counts,
            "category_breakdown": dict(sorted(cat_counts.items(), key=lambda kv: -kv[1])),
            "note": "Scraped facts only. Editorial layer (flagship models, gaps) lives in build_map.py.",
        },
        "papers": [asdict(p) for p in kept],
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[done] wrote {len(kept)} papers -> {args.out}", file=sys.stderr)
    print(f"[done] categories: {payload['meta']['category_breakdown']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
