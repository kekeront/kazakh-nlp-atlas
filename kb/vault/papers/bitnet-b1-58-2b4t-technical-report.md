---
kb_id: "arxiv:2504.12285"
type: "paper"
title: "BitNet b1.58 2B4T Technical Report"
arxiv_id: "2504.12285"
doi: null
hf_repo: null
year: 2025
topics: ["hybrid-efficiency-efficient-attention-se"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["BitNet b1.58 2B4T Technical Report", "arXiv:2504.12285", "arxiv:2504.12285"]
tags: ["paper", "topic/hybrid-efficiency-efficient-attention-se"]
---
# BitNet b1.58 2B4T Technical Report

[arXiv](https://arxiv.org/abs/2504.12285)
**Topics:** [[hybrid-efficiency-efficient-attention-se]]

> [!abstract]
> We introduce BitNet b1.58 2B4T, the first open-source, native 1-bit Large Language Model (LLM) at the 2-billion parameter scale. Trained on a corpus of 4 trillion tokens, the model has been rigorously evaluated across benchmarks covering language understanding, mathematical reasoning, coding proficiency, and conversational ability. Our results demonstrate that BitNet b1.58 2B4T achieves performanc …

## Claims

> [!note] CLAIM — hybrid-efficiency-efficient-attention-se
> BitNet b1.58 2B4T (native 1.58-bit QAT from scratch, ternary {-1,0,+1} weights + 8-bit activations, W1.58A8, 4T tokens) reaches 0.4GB non-embedding memory (6.5x smaller than Qwen2.5-1.5B's 2.6GB), CPU TPOT 29ms vs 65ms (2.2x faster), 12.4x lower decode energy, and beats INT4 post-training quantization (avg 55.01 vs 51.17) - BUT still trails full-precision on knowledge (MMLU 53.17 vs Qwen2.5-1.5B 60.25).
>
> **Numbers:** 0.4GB non-emb (vs 2.6GB); CPU 29ms vs 65ms TPOT; energy 0.028J vs 0.347J; MMLU 53.17 vs 60.25; beats INT4 PTQ 55.01 vs 51.17
> **Relevance:** Native 1.58-bit is the most aggressive edge option (fits huge headroom on any device, CPU-fast) but the ~7-pt MMLU deficit is exactly the KazMMLU axis you're optimizing - high risk for a knowledge-first Kazakh model. Prefer int4 QAT unless CPU-only deployment is the hard constraint.
> **Source:** arXiv:2504.12285 (BitNet b1.58 2B4T Technical Report), Tables 1-2 · **Sweep:** `slm-architecture-2026-07`

[[Home]]
