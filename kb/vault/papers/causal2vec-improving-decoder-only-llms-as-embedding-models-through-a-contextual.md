---
kb_id: "arxiv:2507.23386"
type: "paper"
title: "Causal2Vec: Improving Decoder-only LLMs as Embedding Models through a Contextual Token"
arxiv_id: "2507.23386"
doi: null
hf_repo: null
year: 2025
topics: ["decoder-to-embedder"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Causal2Vec: Improving Decoder-only LLMs as Embedding Models through a Contextual Token", "arXiv:2507.23386", "arxiv:2507.23386"]
tags: ["paper", "topic/decoder-to-embedder"]
---
# Causal2Vec: Improving Decoder-only LLMs as Embedding Models through a Contextual Token

[arXiv](https://arxiv.org/abs/2507.23386)
**Topics:** [[decoder-to-embedder]]

> [!abstract]
> Decoder-only large language models (LLMs) have been increasingly adopted to build embedding models for diverse tasks. To overcome the inherent limitations of causal attention in representation learning, many existing methods modify the attention mechanism to be bidirectional, potentially undermining LLMs' ability to extract semantic information acquired during pre-training. Meanwhile, leading unid …

## Claims

> [!note] CLAIM — decoder-to-embedder
> Causal2Vec keeps the causal mask untouched (no surgery on the generative backbone): a tiny BERT-style pre-encoder compresses the input into one Contextual token prepended to the decoder; the embedding is concat(last hidden of Contextual token, EOS token). SOTA among models trained only on public retrieval data, while cutting sequence length up to 85% and inference time up to 82% vs echo-style methods.
>
> **Numbers:** MTEB 66.10 vs 65.87 for best bidirectional method under identical training data.
> **Relevance:** The most backbone-friendly conversion for a shared generative+embedding model: no attention-mask change means the generative weights and the Engram/mHC architecture stay intact.
> **Source:** arXiv 2507.23386 (Causal2Vec) · **Sweep:** `embeddings-2026-07`

## Related
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models]] — Causal2Vec fixes decoder causal-mask limitation via a prepended bidirectional contextual token vs Qwen3's plain EOS pooling
- [[repetition-improves-language-model-embeddings|Repetition Improves Language Model Embeddings]] — Causal2Vec's contextual token cuts sequence 85% / inference 82% vs Echo's input-doubling — direct efficiency refutation of echo-style…

[[Home]]
