---
kb_id: "arxiv:2404.05961"
type: "paper"
title: "LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders"
arxiv_id: "2404.05961"
doi: null
hf_repo: null
year: 2024
topics: ["decoder-to-embedder"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders", "arXiv:2404.05961", "arxiv:2404.05961"]
tags: ["paper", "topic/decoder-to-embedder"]
---
# LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders

[arXiv](https://arxiv.org/abs/2404.05961)
**Topics:** [[decoder-to-embedder]]

> [!abstract]
> Large decoder-only language models (LLMs) are the state-of-the-art models on most of today's NLP tasks and benchmarks. Yet, the community is only slowly adopting these models for text embedding tasks, which require rich contextualized representations. In this work, we introduce LLM2Vec, a simple unsupervised approach that can transform any decoder-only LLM into a strong text encoder. LLM2Vec consi …

## Claims

> [!note] CLAIM — decoder-to-embedder
> LLM2Vec is the cheapest post-hoc conversion and has numbers AT SMALL SCALE: S-LLaMA-1.3B reaches MTEB 49.42 unsupervised (bidir + MNTP + SimCSE) and 61.96 supervised. MNTP costs only 1000 steps on one A100; SimCSE ~2.5h (7B). Crucially, enabling bidirectional attention WITHOUT training hurts most models (except Mistral), and mean pooling beat EOS/last-token pooling across all their models.
>
> **Numbers:** S-LLaMA-1.3B: 49.42 unsup / 61.96 sup MTEB; Mistral-7B: 56.80 unsup. MNTP: 1000 steps, batch 32, 1xA100-80GB.
> **Relevance:** Sets the realistic ceiling for pure post-hoc conversion at ~1B: 61.96 supervised — below Qwen3-Embedding-0.6B's 64.33. Post-hoc conversion alone will not win; it needs the Qwen3/KaLM-style data pipeline on top.
> **Source:** arXiv 2404.05961 (LLM2Vec) · **Sweep:** `embeddings-2026-07`

## Related
- [[kalm-embedding-v2-superior-training-techniques-and-data-inspire-a-versatile|KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Embedding Mod…]] — Both strip the causal mask (bidirectional) + mean pooling to convert a decoder; iso-scale 0.5B evidence bidir+mean beats causal+EOS
- [[huggingface-co-kz-transformers-kaz-roberta-conversational|huggingface.co/kz-transformers/kaz-roberta-conversational]] — kaz-roberta is the strongest monolingual kk encoder but never got sentence-embedding training; LLM2Vec-style conversion is the missing step

[[Home]]
