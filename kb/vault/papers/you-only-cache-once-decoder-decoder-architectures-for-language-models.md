---
kb_id: "arxiv:2405.05254"
type: "paper"
title: "You Only Cache Once: Decoder-Decoder Architectures for Language Models"
arxiv_id: "2405.05254"
doi: null
hf_repo: null
year: 2024
topics: ["hybrid-efficient-attention-architectures", "mla-at-sub-1b-scale"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["You Only Cache Once: Decoder-Decoder Architectures for Language Models", "arXiv:2405.05254", "arxiv:2405.05254"]
tags: ["paper", "topic/hybrid-efficient-attention-architectures", "topic/mla-at-sub-1b-scale"]
---
# You Only Cache Once: Decoder-Decoder Architectures for Language Models

[arXiv](https://arxiv.org/abs/2405.05254)
**Topics:** [[hybrid-efficient-attention-architectures]], [[mla-at-sub-1b-scale]]

> [!abstract]
> We introduce a decoder-decoder architecture, YOCO, for large language models, which only caches key-value pairs once. It consists of two components, i.e., a cross-decoder stacked upon a self-decoder. The self-decoder efficiently encodes global key-value (KV) caches that are reused by the cross-decoder via cross-attention. The overall model behaves like a decoder-only Transformer, although YOCO onl …

## Claims

> [!note] CLAIM — hybrid-efficient-attention-architectures
> YOCO (decoder-decoder) caches only ONE layer of global KV shared by all cross-decoder layers via cross-attention, giving ~L-times less KV memory than a standard L-layer transformer while retaining global attention and near-perfect 1M-context needle retrieval; also enables early-exit prefill.
>
> **Numbers:** ~L x less KV memory (one global KV layer); near-perfect needle retrieval at 1M context
> **Relevance:** An architectural KV-cache alternative to per-layer caching. For a 500M model where weights are tiny and KV dominates at long context, YOCO-style single-cache is a candidate if very long Kazakh documents matter; heavier to implement than sliding-window.
> **Source:** arXiv:2405.05254 (You Only Cache Once, NeurIPS 2024) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — mla-at-sub-1b-scale
> YOCO validated down to 160M: scaling study at 160M/400M/830M/1.4B/2.7B/6.8B/13B shows YOCO (L/2 self-decoder with sliding-window-1024 or gated retention + L/2 cross-decoder reusing ONE global KV) matches Llama-optimized Transformer validation loss across the whole range, incl. the sub-1B points. Global KV memory O((N+L)*D) vs O(L*N*D), ~L-fold cut; 3B model @1M ctx: 12.4GB vs ~116.6GB (9.4x); ~2x total memory at 32K ctx. YOCO-3B trained 1.6T tokens, 8-task avg 0.636 (StableLM-3B-4E1T-competitive).
>
> **Numbers:** sizes 160M-13B comparable loss; 12.4 vs 116.6GB @1M ctx (3B); ~2x @32K; YOCO-3B 1.6T tok, avg 0.636
> **Relevance:** The most aggressive cross-layer sharing (single global KV) holds at 160-830M — an option if the Kazakh model targets long context, though it changes the architecture far more than CLA2.
> **Source:** arXiv 2405.05254 (You Only Cache Once), HTML v2, Figure 3 + memory tables · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[decoder-hybrid-decoder-architecture-for-efficient-reasoning-with-long-generation|Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation]] — Decoder-Hybrid-Decoder (SambaY) directly builds on YOCO's decoder-decoder single-global-KV design for long reasoning
- [[reducing-transformer-key-value-cache-size-with-cross-layer-attention|Reducing Transformer Key-Value Cache Size with Cross-Layer Attention]] — Both reuse KV across depth; YOCO caches once globally for a decoder-decoder split, CLA shares pairwise between adjacent layers
- [[gemma-3-technical-report|Gemma 3 Technical Report]] — Both slash KV cache for long context; SWA local:global interleave vs cache-once decoder-decoder — different mechanism, same 32K goal

[[Home]]
