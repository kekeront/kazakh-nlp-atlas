---
kb_id: "arxiv:2402.03216"
type: "paper"
title: "M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation"
arxiv_id: "2402.03216"
doi: null
hf_repo: "BAAI/bge-m3"
year: 2024
topics: ["embed-sota"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation", "arXiv:2402.03216", "arxiv:2402.03216"]
tags: ["paper", "topic/embed-sota"]
---
# M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation

[arXiv](https://arxiv.org/abs/2402.03216)
**Topics:** [[embed-sota]]

> [!abstract]
> In this paper, we introduce a new embedding model called M3-Embedding, which is distinguished for its versatility in \textit{Multi-Linguality}, \textit{Multi-Functionality}, and \textit{Multi-Granularity}. It provides a uniform support for the semantic retrieval of more than 100 working languages. It can simultaneously accomplish the three common retrieval functionalities: dense retrieval, multi-v …

## Claims

> [!note] CLAIM — embed-sota
> BGE-M3 (568M, XLM-R-large): unified tri-head model — dense (1024d CLS), learned sparse lexical weights, and ColBERT-style multi-vector — trained with self-knowledge distillation where the sum of the three heads' scores forms the teacher distribution; 8192-token context (query 512/passage 8192 in pretraining); SOTA-at-release on MIRACL multilingual retrieval; ~1.2B weakly-supervised pairs then fine-tuning.
>
> **Numbers:** 568M params, 1024d dense, 100+ languages, 8192 ctx; MMTEB mean 59.56.
> **Relevance:** The hybrid dense+sparse+multi-vector design is especially attractive for agglutinative Kazakh, where learned sparse lexical matching can compensate for morphological variation that hurts dense-only retrieval.
> **Source:** https://arxiv.org/abs/2402.03216; https://huggingface.co/BAAI/bge-m3 · **Sweep:** `embeddings-2026-07`

## Related
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models]] — BGE-M3 encoder beats decoder-embedder Qwen3-Emb-0.6B on Kazakh Belebele (0.9017 vs 0.7545) — encoder > decoder-to-embedder on kk
- [[per-model-belebeleretrieval-json-files-extracted-2026-07-03|per-model BelebeleRetrieval.json files (extracted 2026-07-03)]] — BGE-M3 (M3-Embedding, 568M) is the concrete ≤600M bar at 0.9017 on BelebeleRetrieval kaz that QymyzLM's embedder must clear

[[Home]]
