---
kb_id: "doi:10.1145/3746252.3761077)"
type: "source"
title: "huggingface.co/blog/embedding-quantization"
doi: "10.1145/3746252.3761077)"
hf_repo: "blog/embedding-quantization"
year: null
topics: ["decoder-to-embedder"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["doi:10.1145/3746252.3761077)"]
tags: ["source", "topic/decoder-to-embedder"]
---
# huggingface.co/blog/embedding-quantization

**Topics:** [[decoder-to-embedder]]

## Source URLs
- huggingface.co/blog/embedding-quantization
- ACM CIKM 2025 QAMA (dl.acm.org/doi/10.1145/3746252.3761077)
- huggingface.co/blog/matryoshka

## Findings

> [!note] CLAIM — decoder-to-embedder
> Matryoshka + quantization is a near-free market feature: int8 scalar quantization loses almost nothing (recall -1.46%, MRR -2.72% at 384d); pure binary is a cliff (-17% recall) but binary + float rescoring retains 95-96%; 2-bit/hybrid schemes recover 95-98% at >90% memory reduction. Qwen3-Embedding already ships MRL 32-1024, so parity requires it.
>
> **Numbers:** int8: -1.46% recall; binary: -17%; binary+rescore: 95-96% retention; 2-bit: 95-98% at >90% memory saved.
> **Relevance:** Train with MRL loss from the start and publish int8/binary retention numbers on kkMTEB — cheap differentiation for the 'best embedder on the market' claim.
> **Source:** huggingface.co/blog/embedding-quantization; ACM CIKM 2025 QAMA (dl.acm.org/doi/10.1145/3746252.3761077); huggingface.co/blog/matryoshka · **Sweep:** `embeddings-2026-07`

[[Home]]
