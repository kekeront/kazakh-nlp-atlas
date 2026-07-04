---
kb_id: "arxiv:2501.01028"
type: "paper"
title: "KaLM-Embedding: Superior Training Data Brings A Stronger Embedding Model"
arxiv_id: "2501.01028"
doi: null
hf_repo: null
year: 2025
topics: ["decoder-to-embedder"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["KaLM-Embedding: Superior Training Data Brings A Stronger Embedding Model", "arXiv:2501.01028", "arxiv:2501.01028"]
tags: ["paper", "topic/decoder-to-embedder"]
---
# KaLM-Embedding: Superior Training Data Brings A Stronger Embedding Model

[arXiv](https://arxiv.org/abs/2501.01028)
**Topics:** [[decoder-to-embedder]]

> [!abstract]
> As retrieval-augmented generation prevails in large language models, embedding models are becoming increasingly crucial. Despite the growing number of general embedding models, prior work often overlooks the critical role of training data quality. In this work, we introduce KaLM-Embedding, a general multilingual embedding model that leverages a large quantity of cleaner, more diverse, and domain-s …

## Claims

> [!note] CLAIM — decoder-to-embedder
> KaLM-Embedding proves a 0.5B decoder (Qwen2-0.5B — our exact size class) can be a top multilingual embedder: causal mask removed, then three stages — weakly-supervised contrastive pretraining (20 data categories), high-quality SFT (100 categories), and contrastive distillation from fine-grained soft teacher signals. V2 outperforms all models under 1B on MTEB and rivals models several times larger.
>
> **Numbers:** Backbone 0.5B; V2 beats bge-multilingual-gemma2 (9B) on Chinese tasks; MIT license.
> **Relevance:** Existence proof for deliverable (2) at 500M — and its contrastive-distillation stage is the single highest-leverage technique to copy.
> **Source:** arXiv 2501.01028 (KaLM-Embedding), arXiv 2506.20923 (KaLM-Embedding-V2) · **Sweep:** `embeddings-2026-07`

**Cited KB notes:** [[kalm-embedding-v2-superior-training-techniques-and-data-inspire-a-versatile]]

## Related
- [[kalm-embedding-v2-superior-training-techniques-and-data-inspire-a-versatile|KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Embedding Mod…]] — KaLM-V2 succeeds KaLM-Embedding v1, adding focal reweighting, online hard-neg mixing, and Qwen3-Emb-8B distillation

[[Home]]
