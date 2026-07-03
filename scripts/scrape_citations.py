"""Enrich the corpus with a real citation graph.

Reads paper/survey/papers.json and asks Semantic Scholar -- via the *batch*
endpoint, one POST per 100 papers instead of one request per paper -- for each
paper's reference list. We keep only edges whose target is also in our corpus
(intra-corpus "who cites whom inside Kazakh NLP"), plus best-effort edges to a
small set of global breakthrough papers so the graph shows how Kazakh work
hangs off the global canon.

If Semantic Scholar rate-limits us into the ground, fall back to a TF-IDF
cosine-similarity graph over abstracts (pure numpy) so the feature still ships,
clearly labelled `method="tfidf-fallback"`.

Output: paper/survey/citations.json

Usage:
    python code/scrape_citations.py
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

S2_BATCH = "https://api.semanticscholar.org/graph/v1/paper/batch"
S2_FIELDS = "title,citationCount,references.externalIds"
USER_AGENT = "kazakh-nlp-survey/1.0 (research map; mailto:hey@evgenyastapov.com)"

# Global breakthrough papers, keyed by arXiv id, so a Kazakh paper's reference
# to (say) the Transformer is captured as an edge to a labelled global hub.
GLOBAL_ARXIV: dict[str, dict] = {
    "1301.3781": {"label": "word2vec", "year": 2013},
    "1409.3215": {"label": "seq2seq", "year": 2014},
    "1409.0473": {"label": "Attention (Bahdanau)", "year": 2014},
    "1508.07909": {"label": "BPE for NMT (Sennrich)", "year": 2016},
    "1706.03762": {"label": "Transformer", "year": 2017},
    "1810.04805": {"label": "BERT", "year": 2018},
    "1907.11692": {"label": "RoBERTa", "year": 2019},
    "1910.10683": {"label": "T5", "year": 2019},
    "1911.02116": {"label": "XLM-R", "year": 2019},
    "2005.14165": {"label": "GPT-3", "year": 2020},
    "2010.11934": {"label": "mT5", "year": 2020},
    "2012.15613": {"label": "How Good is Your Tokenizer", "year": 2021},
    "2203.15556": {"label": "Chinchilla", "year": 2022},
    "2302.13971": {"label": "LLaMA", "year": 2023},
    "2305.15425": {"label": "Tokenizer Unfairness (Petrov)", "year": 2023},
    "2411.14198": {"label": "MorphScore", "year": 2024},
}


def canonical_id(arxiv_id: str | None, doi: str | None, title: str) -> str:
    """Stable node id; MUST match the same function in build_map.py."""
    if arxiv_id:
        return f"arxiv:{arxiv_id}"
    if doi:
        return f"doi:{doi.lower()}"
    return "title:" + re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def _post_json(url: str, payload: dict, *, retries: int = 4, timeout: int = 40) -> object | None:
    body = json.dumps(payload).encode("utf-8")
    backoff = 4.0
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(
            url, data=body, method="POST",
            headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503, 504) and attempt < retries:
                wait = backoff * attempt
                print(f"  [retry {attempt}/{retries}] HTTP {exc.code}; sleeping {wait:.0f}s", file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"  [http error] {exc.code}", file=sys.stderr)
            return None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            if attempt < retries:
                time.sleep(backoff * attempt)
                continue
            print(f"  [network error] {exc}", file=sys.stderr)
            return None
    return None


def _ref_to_keys(ext: dict | None) -> list[str]:
    """Candidate canonical ids a reference could match in our lookups."""
    if not ext:
        return []
    keys: list[str] = []
    ax = ext.get("ArXiv")
    if ax:
        keys.append(f"arxiv:{ax}")
    doi = ext.get("DOI")
    if doi:
        keys.append(f"doi:{doi.lower()}")
    return keys


def fetch_citations(papers: list[dict]) -> dict | None:
    """Return citation graph via S2 batch, or None on terminal failure."""
    # corpus lookup: any canonical id -> our node id
    corpus_ids: dict[str, str] = {}
    s2_query_ids: list[str] = []          # ARXIV:/DOI: strings to send
    s2_to_node: dict[str, str] = {}       # query id -> node id
    for p in papers:
        nid = canonical_id(p.get("arxiv_id"), p.get("doi"), p.get("title", ""))
        corpus_ids[nid] = nid
        if p.get("arxiv_id"):
            qid = f"ARXIV:{p['arxiv_id']}"
        elif p.get("doi"):
            qid = f"DOI:{p['doi']}"
        else:
            qid = None
        if qid and qid not in s2_to_node:
            s2_query_ids.append(qid)
            s2_to_node[qid] = nid

    # global hubs join the target lookup
    global_lookup = {f"arxiv:{ax}": f"global:{ax}" for ax in GLOBAL_ARXIV}

    edges: list[list[str]] = []
    node_citations: dict[str, int] = {}
    referenced_globals: set[str] = set()
    resolved = 0
    with_refs = 0

    print(f"[s2-batch] resolving {len(s2_query_ids)} papers in chunks of 100", file=sys.stderr)
    for start in range(0, len(s2_query_ids), 100):
        chunk = s2_query_ids[start:start + 100]
        url = f"{S2_BATCH}?fields={S2_FIELDS}"
        data = _post_json(url, {"ids": chunk})
        if data is None:
            print(f"  chunk {start}: no response", file=sys.stderr)
            time.sleep(3)
            continue
        if not isinstance(data, list):
            print(f"  chunk {start}: unexpected payload", file=sys.stderr)
            continue
        for qid, obj in zip(chunk, data):
            if not obj:
                continue
            resolved += 1
            src = s2_to_node[qid]
            cc = obj.get("citationCount")
            if isinstance(cc, int):
                node_citations[src] = cc
            refs = obj.get("references") or []
            if refs:
                with_refs += 1
            for ref in refs:
                for key in _ref_to_keys(ref.get("externalIds")):
                    if key in corpus_ids and corpus_ids[key] != src:
                        edges.append([src, corpus_ids[key]])
                    elif key in global_lookup:
                        gid = global_lookup[key]
                        edges.append([src, gid])
                        referenced_globals.add(key.split(":", 1)[1])
        print(f"  chunk {start}: resolved so far {resolved}, edges {len(edges)}", file=sys.stderr)
        time.sleep(2)

    if resolved == 0:
        return None  # let caller fall back

    # de-dup edges
    uniq = sorted({tuple(e) for e in edges})
    edges = [list(e) for e in uniq]

    return {
        "method": "s2-batch",
        "stats": {
            "resolved": resolved,
            "with_refs": with_refs,
            "edges": len(edges),
            "global_hubs_hit": len(referenced_globals),
        },
        "edges": edges,
        "node_citations": node_citations,
        "global_nodes": {
            f"global:{ax}": {**meta, "arxiv": ax}
            for ax, meta in GLOBAL_ARXIV.items()
            if ax in referenced_globals
        },
    }


# --------------------------------------------------------------------------- #
# TF-IDF fallback (pure numpy) -- topical-similarity edges, not citations
# --------------------------------------------------------------------------- #


def tfidf_fallback(papers: list[dict], *, top_per_node: int = 3, min_sim: float = 0.12) -> dict:
    import numpy as np

    docs = [f"{p.get('title','')} {p.get('abstract','')}".lower() for p in papers]
    node_ids = [canonical_id(p.get("arxiv_id"), p.get("doi"), p.get("title", "")) for p in papers]

    tok = re.compile(r"[a-zà-ÿЀ-ӿ]{3,}")
    vocab: dict[str, int] = {}
    rows: list[dict[int, int]] = []
    for d in docs:
        counts: dict[int, int] = {}
        for w in tok.findall(d):
            idx = vocab.setdefault(w, len(vocab))
            counts[idx] = counts.get(idx, 0) + 1
        rows.append(counts)

    n_docs, n_vocab = len(docs), len(vocab)
    tf = np.zeros((n_docs, n_vocab), dtype=np.float32)
    for i, counts in enumerate(rows):
        for j, c in counts.items():
            tf[i, j] = c
    df = (tf > 0).sum(axis=0)
    idf = np.log((1 + n_docs) / (1 + df)) + 1.0
    mat = tf * idf
    norms = np.linalg.norm(mat, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    mat = mat / norms
    sim = mat @ mat.T

    edges: list[list[str]] = []
    for i in range(n_docs):
        order = np.argsort(-sim[i])
        added = 0
        for j in order:
            if j == i or sim[i, j] < min_sim:
                continue
            edges.append([node_ids[i], node_ids[int(j)]])
            added += 1
            if added >= top_per_node:
                break
    uniq = sorted({tuple(sorted(e)) for e in edges})
    return {
        "method": "tfidf-fallback",
        "stats": {"edges": len(uniq), "note": "topical similarity, NOT citations"},
        "edges": [list(e) for e in uniq],
        "node_citations": {
            canonical_id(p.get("arxiv_id"), p.get("doi"), p.get("title", "")): p.get("citation_count")
            for p in papers if p.get("citation_count") is not None
        },
        "global_nodes": {},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the citation graph for the atlas.")
    parser.add_argument("--data", type=Path, default=Path("paper/survey/papers.json"))
    parser.add_argument("--out", type=Path, default=Path("paper/survey/citations.json"))
    parser.add_argument("--force-fallback", action="store_true", help="skip S2, use TF-IDF")
    args = parser.parse_args()

    papers = json.loads(args.data.read_text(encoding="utf-8")).get("papers", [])
    print(f"[load] {len(papers)} papers", file=sys.stderr)

    result = None if args.force_fallback else fetch_citations(papers)
    if result is None:
        print("[fallback] S2 unavailable -> TF-IDF similarity graph", file=sys.stderr)
        result = tfidf_fallback(papers)

    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[done] method={result['method']} stats={result['stats']} -> {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
