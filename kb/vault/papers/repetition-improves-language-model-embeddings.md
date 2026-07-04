---
kb_id: "arxiv:2402.15449"
type: "paper"
title: "Repetition Improves Language Model Embeddings"
arxiv_id: "2402.15449"
doi: null
hf_repo: null
year: 2024
topics: ["decoder-to-embedder"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Repetition Improves Language Model Embeddings", "arXiv:2402.15449", "arxiv:2402.15449"]
tags: ["paper", "topic/decoder-to-embedder"]
---
# Repetition Improves Language Model Embeddings

[arXiv](https://arxiv.org/abs/2402.15449)
**Topics:** [[decoder-to-embedder]]

> [!abstract]
> Bidirectional models are considered essential for strong text embeddings. Recent approaches to adapt autoregressive language models (LMs) into strong text embedding models have largely had the requirement to modify the LM architecture to be bidirectional. We challenge this premise by introducing "echo embeddings" which converts autoregressive LMs into high quality text embedding models without cha …

## Claims

> [!note] CLAIM — decoder-to-embedder
> Echo embeddings (repeat input twice, mean-pool second occurrence) improve zero-shot decoder embeddings by >5% and nearly match bidirectional-converted models with zero architecture change — but double sequence length/cost. Same paper confirms last-token pooling degrades sharply as input length grows; mean pooling wins by a wide margin for causal LMs.
>
> **Numbers:** +5% zero-shot over classical LM embeddings; 2x inference cost.
> **Relevance:** Useful as a zero-training baseline row in our ablation table and as evidence against naive last-token pooling for an agglutinative language with long words/sentences.
> **Source:** arXiv 2402.15449 (Repetition Improves Language Model Embeddings, ICLR 2025) · **Sweep:** `embeddings-2026-07`

## Related
- [[causal2vec-improving-decoder-only-llms-as-embedding-models-through-a-contextual|Causal2Vec: Improving Decoder-only LLMs as Embedding Models through a Contextual Token]] — Causal2Vec's contextual token cuts sequence 85% / inference 82% vs Echo's input-doubling — direct efficiency refutation of echo-style…

[[Home]]
