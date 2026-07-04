---
kb_id: "title:mteb pypi package mteb get tasks languages kaz verified locally 2026 07 03"
type: "source"
title: "mteb PyPI package, mteb.get_tasks(languages=['kaz']), verified locally…"
doi: null
hf_repo: null
year: null
topics: ["embed-sota"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:mteb pypi package mteb get tasks languages kaz verified locally 2026 07 03"]
tags: ["source", "topic/embed-sota"]
---
# mteb PyPI package, mteb.get_tasks(languages=['kaz']), verified locally…

**Topics:** [[embed-sota]]

## Source URLs
- mteb PyPI package, mteb.get_tasks(languages=['kaz']), verified locally 2026-07-03

## Findings

> [!note] CLAIM — embed-sota
> VERIFIED by running the mteb library locally (July 2026): MTEB contains exactly 16 Kazakh tasks, of which only 11 are text-embedding-relevant: 5 bitext mining (Flores, NTREX, Tatoeba, WebFAQ QAs/Questions), 3 classification (SIB200Classification.v2, CyrillicTurkicLangClassification, TurkicClassification), 1 clustering (SIB200ClusteringS2S), 2 retrieval (BelebeleRetrieval, WebFAQRetrieval). There is ZERO Kazakh STS, zero pair classification, zero reranking, and zero native QA retrieval — KazQAD is NOT integrated into MTEB.
>
> **Numbers:** 16 tasks total (incl. 5 audio/any2any); 2 text retrieval tasks, 0 STS, 0 reranking.
> **Relevance:** This is the concrete missing-benchmark bottleneck: 'best Kazakh embedder' cannot currently be demonstrated on MTEB — building kk-MTEB tasks is a mandatory roadmap milestone, not optional.
> **Source:** mteb PyPI package, mteb.get_tasks(languages=['kaz']), verified locally 2026-07-03 · **Sweep:** `embeddings-2026-07`

## Related
- [[huggingface-co-datasets-mteb-webfaqretrieval|huggingface.co/datasets/mteb/WebFAQRetrieval]] — the tiny kaz WebFAQ split is one of the few tasks mteb.get_tasks(languages=['kaz']) actually returns

[[Home]]
