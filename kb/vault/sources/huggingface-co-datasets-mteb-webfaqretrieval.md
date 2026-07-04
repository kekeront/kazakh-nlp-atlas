---
kb_id: "hf:mteb/webfaqretrieval"
type: "source"
title: "huggingface.co/datasets/mteb/WebFAQRetrieval"
doi: null
hf_repo: "mteb/WebFAQRetrieval"
year: null
topics: ["embeddings-retrieval"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:mteb/webfaqretrieval"]
tags: ["source", "topic/embeddings-retrieval"]
---
# huggingface.co/datasets/mteb/WebFAQRetrieval

**Topics:** [[embeddings-retrieval]]

## Source URLs
- huggingface.co/datasets/mteb/WebFAQRetrieval
- huggingface.co/datasets/PaDaS-Lab/webfaq (2026-07-03)

## Findings

> [!note] CLAIM — embeddings-retrieval
> MTEB's existing WebFAQRetrieval kaz split is tiny (300 queries, 2,995 docs, 1 qrel/query) — usable only as a secondary eval, not a headline; PaDaS-Lab/webfaq kaz (12,510 pairs) is usable as natural training pairs but MUST be deduplicated against the WebFAQRetrieval kaz test queries (eval subset is sampled from the same crawl).
>
> **Numbers:** kaz eval: 300 queries / 2,995 docs / 1 qrel per query; kaz training pairs: 12,510
> **Relevance:** Train/test contamination trap for the embedding track.
> **Source:** huggingface.co/datasets/mteb/WebFAQRetrieval; huggingface.co/datasets/PaDaS-Lab/webfaq (2026-07-03) · **Sweep:** `2026-07-eval-provenance`

## Related
- [[webfaq-a-multilingual-collection-of-natural-q-a-datasets-for-dense-retrieval|WebFAQ: A Multilingual Collection of Natural Q&A Datasets for Dense Retrieval]] — WebFAQ supplies the WebFAQRetrieval-kaz MTEB task (~12.5k kk natural pairs; e5-large nDCG@10 0.7269)
- [[mmteb-massive-multilingual-text-embedding-benchmark|MMTEB: Massive Multilingual Text Embedding Benchmark]] — WebFAQRetrieval is an MMTEB task; MMTEB is the benchmark whose kaz coverage is too thin for a headline eval
- [[mteb-pypi-package-mteb-get-tasks-languages-kaz-verified|mteb PyPI package, mteb.get_tasks(languages=['kaz']), verified locally…]] — the tiny kaz WebFAQ split is one of the few tasks mteb.get_tasks(languages=['kaz']) actually returns

[[Home]]
