---
kb_id: "arxiv:2407.15831"
type: "paper"
title: "NV-Retriever: Improving text embedding models with effective hard-negative mining"
arxiv_id: "2407.15831"
doi: null
hf_repo: null
year: 2024
topics: ["embeddings-training"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["NV-Retriever: Improving text embedding models with effective hard-negative mining", "arXiv:2407.15831", "arxiv:2407.15831"]
tags: ["paper", "topic/embeddings-training"]
---
# NV-Retriever: Improving text embedding models with effective hard-negative mining

[arXiv](https://arxiv.org/abs/2407.15831)
**Topics:** [[embeddings-training]]

> [!abstract]
> Text embedding models have been popular for information retrieval applications such as semantic search and Question-Answering systems based on Retrieval-Augmented Generation (RAG). Those models are typically Transformer models that are fine-tuned with contrastive learning objectives. One of the challenging aspects of fine-tuning embedding models is the selection of high quality hard-negative passa …

## Claims

> [!note] CLAIM — embeddings-training
> NV-Retriever's positive-aware hard-negative mining (TopK-PercPos) is the concrete recipe for evallab's pinned hard-negative protocol: mine top-k negatives with a teacher retriever, then DISCARD any candidate whose relevance score exceeds 95% of the positive's score (removes false negatives). This was the optimal setting and topped MTEB-Retrieval on release.
>
> **Numbers:** threshold = 95% of positive score (TopK-PercPos); NV-Retriever-v1 MTEB-Retrieval/BEIR 60.9, +0.65 over prior, #1 on 2024-07-07
> **Relevance:** TRANSFERABLE-UNTESTED on Kazakh. Fixes the exact protocol ambiguity the KB flags (mE5-large scores 0.449 vs 0.919 on KazQAD depending on candidate pool). Pin KazQAD hard-negatives via TopK-PercPos@95% with an mE5-large teacher over the 815k-passage corpus for a defensible, reproducible number.
> **Source:** arXiv:2407.15831 (NV-Retriever, Moreira et al. 2024) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[nv-embed-improved-techniques-for-training-llms-as-generalist-embedding-models|NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models]] — Same NVIDIA embedding lineage; NV-Retriever's positive-aware hard-negative mining complements NV-Embed's latent-attention two-stage tuning
- [[grep-of-evallab-2026-07-04|grep of evallab (2026-07-04)]] — NV-Retriever's TopK-PercPos is the concrete recipe behind evallab's pinned hard-negative protocol (100 BM25 candidates)
- [[webfaq-a-multilingual-collection-of-natural-q-a-datasets-for-dense-retrieval|WebFAQ: A Multilingual Collection of Natural Q&A Datasets for Dense Retrieval]] — Both on hard-negative mining; WebFAQ 2.0 finds random negatives beat mined hard-negs under MNR (false negatives), tension with…
- [[huggingface-co-shyngys879-kazakh-e5-rag-embedding-model|huggingface.co/shyngys879/kazakh-e5-rag-embedding (model card, fetched…]] — NV-Retriever formalizes hard-negative mining — the candidate-pool construction that determines shyngys879's swinging MRR

[[Home]]
