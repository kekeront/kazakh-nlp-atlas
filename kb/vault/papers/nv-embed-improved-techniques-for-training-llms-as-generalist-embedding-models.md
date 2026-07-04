---
kb_id: "arxiv:2405.17428"
type: "paper"
title: "NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models"
arxiv_id: "2405.17428"
doi: null
hf_repo: null
year: 2024
topics: ["decoder-to-embedder"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models", "arXiv:2405.17428", "arxiv:2405.17428"]
tags: ["paper", "topic/decoder-to-embedder"]
---
# NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models

[arXiv](https://arxiv.org/abs/2405.17428)
**Topics:** [[decoder-to-embedder]]

> [!abstract]
> Decoder-only LLM-based embedding models are beginning to outperform BERT or T5-based embedding models in general-purpose text embedding tasks, including dense vector-based retrieval. In this work, we introduce NV-Embed, incorporating architectural designs, training procedures, and curated datasets to significantly enhance the performance of LLM as a versatile embedding model, while maintaining its …

## Claims

> [!note] CLAIM — decoder-to-embedder
> NV-Embed's latent-attention pooling (512 latents, 8 heads) beats both mean and last-token pooling, and its two-stage instruction tuning (stage 1: retrieval with in-batch negatives; stage 2: blend non-retrieval tasks, disable in-batch negatives) was the recipe that set the MTEB record at 69.32 (v1, Mistral-7B base).
>
> **Numbers:** MTEB 69.32 (NV-Embed-v1); pooling: 512 latents / 8 heads.
> **Relevance:** Latent-attention pooling is a cheap add-on head (~few M params) worth ablating against mean pooling on the 500M backbone; the two-stage negatives schedule is directly copyable.
> **Source:** arXiv 2405.17428 (NV-Embed) · **Sweep:** `embeddings-2026-07`

## Related
- [[nv-retriever-improving-text-embedding-models-with-effective-hard-negative-mining|NV-Retriever: Improving text embedding models with effective hard-negative mining]] — Same NVIDIA embedding lineage; NV-Retriever's positive-aware hard-negative mining complements NV-Embed's latent-attention two-stage tuning
- [[onegen-efficient-one-pass-unified-generation-and-retrieval-for-llms|OneGen: Efficient One-Pass Unified Generation and Retrieval for LLMs]] — Both turn a decoder LLM into a retriever; NV-Embed drops the causal mask for pure embedding, OneGen keeps it for joint gen+retrieval via…

[[Home]]
