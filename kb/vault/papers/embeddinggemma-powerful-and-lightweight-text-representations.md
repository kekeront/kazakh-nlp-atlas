---
kb_id: "arxiv:2509.20354"
type: "paper"
title: "EmbeddingGemma: Powerful and Lightweight Text Representations"
arxiv_id: "2509.20354"
doi: null
hf_repo: "blog/embeddinggemma"
year: 2025
topics: ["embed-sota"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["EmbeddingGemma: Powerful and Lightweight Text Representations", "arXiv:2509.20354", "arxiv:2509.20354"]
tags: ["paper", "topic/embed-sota"]
---
# EmbeddingGemma: Powerful and Lightweight Text Representations

[arXiv](https://arxiv.org/abs/2509.20354)
**Topics:** [[embed-sota]]

> [!abstract]
> We introduce EmbeddingGemma, a new lightweight, open text embedding model based on the Gemma 3 language model family. Our innovative training recipe strategically captures knowledge from larger models via encoder-decoder initialization and geometric embedding distillation. We improve model robustness and expressiveness with a spread-out regularizer, and ensure generalizability by merging checkpoin …

## Claims

> [!note] CLAIM — embed-sota
> EmbeddingGemma (308M = ~100M transformer + ~200M embedding params) is the best open model under 500M on MTEB Multilingual v2. Recipe: encoder initialized from T5Gemma (encoder-decoder trained from Gemma 3, giving bidirectional context), mean pooling, 768d with MRL truncation to 512/256/128, geometric embedding distillation from Gemini Embedding (teacher), spread-out regularizer, model souping over domain-specialized checkpoints, and QAT for sub-200MB RAM inference.
>
> **Numbers:** 61.15 MTEB Multilingual v2 mean, 250+ languages, 768d->128d MRL, <200MB RAM after QAT.
> **Relevance:** Proof that a ~300M model with distillation from a large teacher reaches near-1B quality; T5Gemma-style encoder init from your own decoder SLM is the architecture bridge between the two deliverables.
> **Source:** https://arxiv.org/abs/2509.20354; https://developers.googleblog.com/en/introducing-embeddinggemma/; https://huggingface.co/blog/embeddinggemma · **Sweep:** `embeddings-2026-07`

## Related
- [[mgte-generalized-long-context-text-representation-and-reranking-models-for|mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual T…]] — mGTE (305M) and EmbeddingGemma (308M) are competing lightweight multilingual v0 base options with MRL and instruction prefixes
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models]] — Both sub-1B decoder→embedders; Qwen3-Emb-0.6B (64.33) beats EmbeddingGemma-308M (61.15) on MMTEB but loses params/QAT
- [[afrimteb-and-afrie5-benchmarking-and-adapting-text-embedding-models-for-african|AfriMTEB and AfriE5: Benchmarking and Adapting Text Embedding Models for African Languages]] — AfriMTEB finds EmbeddingGemma underperforms the E5 family on African LRLs — external evidence its lightweight-decoder gains don't transfer…
- [[per-model-belebeleretrieval-json-files-extracted-2026-07-03|per-model BelebeleRetrieval.json files (extracted 2026-07-03)]] — EmbeddingGemma-300m measured at 0.6839 — the sub-600M laggard showing size alone doesn't buy kk retrieval quality

[[Home]]
