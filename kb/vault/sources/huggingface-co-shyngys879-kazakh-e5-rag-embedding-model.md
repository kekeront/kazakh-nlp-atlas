---
kb_id: "hf:shyngys879/kazakh-e5-rag-embedding"
type: "source"
title: "huggingface.co/shyngys879/kazakh-e5-rag-embedding (model card, fetched…"
doi: null
hf_repo: "shyngys879/kazakh-e5-rag-embedding"
year: null
topics: ["embeddings-retrieval"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:shyngys879/kazakh-e5-rag-embedding"]
tags: ["source", "topic/embeddings-retrieval"]
---
# huggingface.co/shyngys879/kazakh-e5-rag-embedding (model card, fetched…

**Topics:** [[embeddings-retrieval]]

## Source URLs
- huggingface.co/shyngys879/kazakh-e5-rag-embedding (model card, fetched 2026-07-03)
- huggingface.co/Nurlykhan/kazembed-v5

## Findings

> [!note] CLAIM — embeddings-retrieval
> Hard-negatives MRR on KazQAD is protocol-defined, not model-defined: the successor card of the same lineage (shyngys879/kazakh-e5-rag-embedding, May 2026) reports mE5-large at MRR 0.4490 under a same-named 'HardTFIDF99' protocol but 0.9189 under its easier 'KazQAD-100 local' candidate variant. Any target formulated as 'beat 0.909' is meaningless without fixing and publishing the candidate-pool construction; evallab implements full-corpus retrieval AND a pinned hard-negative recipe as the canonical protocols.
>
> **Numbers:** mE5-large: 0.4490 (HardTFIDF99) vs 0.9189 (KazQAD-100 local) vs 0.909 (kazembed-v5 card); full-corpus paper baseline MRR 0.382
> **Relevance:** Kills naive '>0.909' target formulation; the lab contract now pins targets to evallab protocols.
> **Source:** huggingface.co/shyngys879/kazakh-e5-rag-embedding (model card, fetched 2026-07-03); huggingface.co/Nurlykhan/kazembed-v5 · **Sweep:** `2026-07-eval-provenance`

## Related
- [[nv-retriever-improving-text-embedding-models-with-effective-hard-negative-mining|NV-Retriever: Improving text embedding models with effective hard-negative mining]] — NV-Retriever formalizes hard-negative mining — the candidate-pool construction that determines shyngys879's swinging MRR
- [[huggingface-co-nurlykhan-kazembed-v5-apache-2-0|huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)]] — refutes: same lineage shows mE5-large collapses 0.919->0.449 by pool, so kazembed-v5 card's 0.909 is a protocol artifact
- [[grep-of-home-altairzhambyl-projects-slms-qymyzlm-evallab|grep of /home/altairzhambyl/projects/SLMs/qymyzlm/evallab (2026-07-04)]] — its protocol-dependence motivates evallab's pinned KazQAD BM25 hard-neg recipe (100 candidates, k1=1.5, b=0.75)

[[Home]]
