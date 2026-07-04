---
kb_id: "title:grep of home altairzhambyl projects slms qymyzlm evallab 2026 07 04 hardneg py constants protocol kazqad hardneg bm25 v1 n candidates 100 bm25 k1 1 5 bm25 b 0 75"
type: "source"
title: "grep of /home/altairzhambyl/projects/SLMs/qymyzlm/evallab (2026-07-04)"
doi: null
hf_repo: null
year: null
topics: ["joint-generative-embedding-head-on-one-6"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:grep of home altairzhambyl projects slms qymyzlm evallab 2026 07 04 hardneg py constants protocol kazqad hardneg bm25 v1 n candidates 100 bm25 k1 1 5 bm25 b 0 75"]
tags: ["source", "topic/joint-generative-embedding-head-on-one-6"]
---
# grep of /home/altairzhambyl/projects/SLMs/qymyzlm/evallab (2026-07-04)

**Topics:** [[joint-generative-embedding-head-on-one-6]]

## Source URLs
- grep of /home/altairzhambyl/projects/SLMs/qymyzlm/evallab (2026-07-04)
- hardneg.py constants PROTOCOL='kazqad-hardneg-bm25-v1', N_CANDIDATES=100, BM25_K1=1.5, BM25_B=0.75

## Findings

> [!note] CLAIM — joint-generative-embedding-head-on-one-6
> PROTOCOL-NAME CONFLICT with the mission brief: the phrase 'TopK-PercPos protocol' appears NOWHERE in the evallab repo (grep over src/, README, CLAUDE.md returns zero hits). The actual pinned protocol names are 'KazQADRetrieval' (full-corpus) and 'kazqad-hardneg-bm25-v1' (KazQAD-HardNeg, MRR@10, N_CANDIDATES=100, DEFAULT_SEED=13). Design-panel documents must use the code-pinned names or the published numbers will be un-linkable to runner records.
>
> **Numbers:** 0 grep hits for 'TopK' or 'PercPos' in evallab
> **Relevance:** Prevents the design panel from anchoring the embedding contract to a protocol name that does not exist in the single source of truth.
> **Source:** grep of /home/altairzhambyl/projects/SLMs/qymyzlm/evallab (2026-07-04); hardneg.py constants PROTOCOL='kazqad-hardneg-bm25-v1', N_CANDIDATES=100, BM25_K1=1.5, BM25_B=0.75 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[nv-retriever-improving-text-embedding-models-with-effective-hard-negative-mining|NV-Retriever: Improving text embedding models with effective hard-negative mining]] — NV-Retriever's TopK-PercPos is the concrete recipe behind evallab's pinned hard-negative protocol (100 BM25 candidates)
- [[huggingface-co-shyngys879-kazakh-e5-rag-embedding-model|huggingface.co/shyngys879/kazakh-e5-rag-embedding (model card, fetched…]] — its protocol-dependence motivates evallab's pinned KazQAD BM25 hard-neg recipe (100 candidates, k1=1.5, b=0.75)
- [[huggingface-co-api-datasets-issai-kazqad-retrieval-issai|huggingface.co/api/datasets/issai/kazqad-retrieval, .../issai/kazparc…]] — The pinned protocol reads issai/kazqad-retrieval @ a3999685; this dataset-API source is the provenance for the 825k-passage full corpus

[[Home]]
