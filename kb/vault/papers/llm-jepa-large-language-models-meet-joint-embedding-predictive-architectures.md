---
kb_id: "arxiv:2509.14252"
type: "paper"
title: "LLM-JEPA: Large Language Models Meet Joint Embedding Predictive Architectures"
arxiv_id: "2509.14252"
doi: null
hf_repo: null
year: 2025
topics: ["decoder-to-embedder"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["LLM-JEPA: Large Language Models Meet Joint Embedding Predictive Architectures", "arXiv:2509.14252", "arxiv:2509.14252"]
tags: ["paper", "topic/decoder-to-embedder"]
---
# LLM-JEPA: Large Language Models Meet Joint Embedding Predictive Architectures

[arXiv](https://arxiv.org/abs/2509.14252)
**Topics:** [[decoder-to-embedder]]

> [!abstract]
> Large Language Model (LLM) pretraining, finetuning, and evaluation rely on input-space reconstruction and generative capabilities. Yet, it has been observed in vision that embedding-space training objectives, e.g., with Joint Embedding Predictive Architectures (JEPAs), are far superior to their input-space counterpart. That mismatch in how training is achieved between language and vision opens up …

## Claims

> [!note] CLAIM — decoder-to-embedder
> There is NO established recipe that integrates a contrastive objective INTO LM pretraining at scale — GRIT, KaLM, Qwen3-Embedding all do contrastive work as a post-pretraining stage; the closest research is LLM-JEPA (joint-embedding predictive auxiliary objectives on LLMs, 2025), still exploratory. Meanwhile direct Kazakh SLM competitors exist as of 2026 — SozKZ (50M-600M Llama-style, 50K BPE, 9B kk tokens from scratch; 600M scores 30.3% on Kazakh cultural QA) and KazByte (byte-level adapter on Qwen) — but NEITHER touches embeddings.
>
> **Numbers:** SozKZ-600M: 30.3% Kazakh cultural QA (vs Llama-3.2-1B 32.0%); 9B training tokens.
> **Relevance:** Two implications: (a) a contrastive auxiliary loss during pretraining would be a novel but risky headline — frame it as an ablation, not the core bet; (b) the embedding deliverable is our clean differentiation from SozKZ/KazByte, who must now be cited and beaten on the generative side too.
> **Source:** arXiv 2509.14252 (LLM-JEPA); arXiv 2603.20854 (SozKZ); arXiv 2603.27859 (KazByte) · **Sweep:** `embeddings-2026-07`

**Cited KB notes:** [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch]], [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter]]

## Related
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] — Cites KazByte byte-adapter as the other Kazakh SLM competitor; neither touches embeddings, validating embedding-first

[[Home]]
