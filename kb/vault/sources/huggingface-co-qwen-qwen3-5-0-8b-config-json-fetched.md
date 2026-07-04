---
kb_id: "hf:qwen/qwen3.5-0.8b"
type: "source"
title: "huggingface.co/Qwen/Qwen3.5-0.8B config.json (fetched directly)"
doi: null
hf_repo: "Qwen/Qwen3.5-0.8B"
year: null
topics: ["mla-sub1b"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:qwen/qwen3.5-0.8b"]
tags: ["source", "topic/mla-sub1b"]
---
# huggingface.co/Qwen/Qwen3.5-0.8B config.json (fetched directly)

**Topics:** [[mla-sub1b]]

## Source URLs
- huggingface.co/Qwen/Qwen3.5-0.8B config.json (fetched directly)

## Findings

> [!note] CLAIM — mla-sub1b
> Resolves KB [UNVERIFIED] on Qwen3.5 sub-1B: Qwen/Qwen3.5-0.8B config.json shows NO MLA — it is a hybrid: 24 layers, hidden_size=1024, layer pattern 3 linear-attention (Gated DeltaNet: 16 lin K/V heads, dim 128, conv kernel 4, output gate) : 1 full attention (8 Q heads / 2 KV heads GQA), vocab 248,320, ctx 262,144, partial_rotary_factor 0.25, no MoE in the 0.8B. So the newest frontier sub-1B (Mar 2026) chose hybrid-linear + GQA-2 over MLA for long context.
>
> **Numbers:** 759M-class, 24L, d=1024, GDN:full = 3:1, full-attn GQA 8Q:2KV, vocab 248,320, ctx 262,144
> **Relevance:** Adoption signal: at 262K context even a 0.8B flagship avoids per-layer softmax KV entirely rather than compressing it with MLA — the lab's 32K target makes MLA/CLA2 sufficient, but this is the competitor architecture to name in the paper.
> **Source:** huggingface.co/Qwen/Qwen3.5-0.8B config.json (fetched directly) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[gated-delta-networks-improving-mamba2-with-delta-rule|Gated Delta Networks: Improving Mamba2 with Delta Rule]] — Qwen3.5-0.8B's 3:1 linear layers ARE Gated DeltaNet — it chose hybrid-linear + GQA-2 over MLA for 256K context

[[Home]]
