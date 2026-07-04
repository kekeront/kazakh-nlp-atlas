---
kb_id: "title:lab measurement t4bench2 py t4bench3 py qwen3 0 6b base config json max position embeddings 32768"
type: "source"
title: "Lab measurement t4bench2.py/t4bench3.py"
doi: null
hf_repo: null
year: null
topics: ["kaggle-t4x2-compute-vram-budget-for-the"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:lab measurement t4bench2 py t4bench3 py qwen3 0 6b base config json max position embeddings 32768"]
tags: ["source", "topic/kaggle-t4x2-compute-vram-budget-for-the"]
---
# Lab measurement t4bench2.py/t4bench3.py

**Topics:** [[kaggle-t4x2-compute-vram-budget-for-the]]

## Source URLs
- Lab measurement t4bench2.py/t4bench3.py
- Qwen3-0.6B-Base config.json (max_position_embeddings=32768)

## Findings

> [!note] CLAIM — kaggle-t4x2-compute-vram-budget-for-the
> [measured; recipe lever] Context length 4096 costs ~23% throughput vs 2048 at this scale (1,584 vs 1,948-2,049 tok/s measured, attention recompute share grows with s), while Qwen3-0.6B natively supports 32,768 positions — CPT at 2048 ctx with a small late 4K-annealing phase would raise the weekly token budget to ~0.38-0.65B tokens and is standard practice for data-limited CPT. No Kazakh-specific long-context evidence exists either way.
>
> **Numbers:** 1,584 tok/s @4096 vs 1,948 @2048 (bs1) and 2,049 (bs4): +23-29%; weekly budget 0.31-0.53B -> 0.38-0.65B tok
> **Relevance:** A free ~25% compute recovery for the quota-starved plan; KazMMLU 3-shot prompts fit well under 2048 tokens, so the eval target does not require 4K training context.
> **Source:** Lab measurement t4bench2.py/t4bench3.py; Qwen3-0.6B-Base config.json (max_position_embeddings=32768) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[base-of-rope-bounds-context-length|Base of RoPE Bounds Context Length]] — proposed 2048-ctx CPT with late 4K annealing interacts with RoPE base, which bounds usable context length

[[Home]]
