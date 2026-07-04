---
kb_id: "arxiv:2511.23404"
type: "paper"
title: "LFM2 Technical Report"
arxiv_id: "2511.23404"
doi: null
hf_repo: null
year: 2025
topics: ["sota-slm", "hybrid-efficient-attention-architectures"]
claims: 3
uncertain_claims: 0
verdicts: []
aliases: ["LFM2 Technical Report", "arXiv:2511.23404", "arxiv:2511.23404"]
tags: ["paper", "topic/sota-slm", "topic/hybrid-efficient-attention-architectures"]
---
# LFM2 Technical Report

[arXiv](https://arxiv.org/abs/2511.23404)
**Topics:** [[sota-slm]], [[hybrid-efficient-attention-architectures]]

> [!abstract]
> We present LFM2, a family of Liquid Foundation Models designed for efficient on-device deployment and strong task capabilities. Using hardware-in-the-loop architecture search under edge latency and memory constraints, we obtain a compact hybrid backbone that combines gated short convolutions with a small number of grouped query attention blocks, delivering up to 2x faster prefill and decode on CPU …

## Claims

> [!note] CLAIM — sota-slm
> LFM2-350M is a hybrid: 16 layers = 10 double-gated short-convolution blocks (depthwise conv, kernel 3) + 6 GQA attention blocks, hidden 1024, FFN 4608, 16Q/8KV heads, vocab 65,536 (byte-level BPE), 32K context, ~11T tokens. Scores MMLU 43.43, IFEval 65.12, GSM8K 30.10. LFM2-700M (d1536, 24Q/8KV) and LFM2-1.2B (d2048, MMLU 55.23) share the same 16-layer, 6-attention layout.
>
> **Numbers:** 350M: 16L (10 conv+6 GQA), d1024, FFN4608, vocab65536, 11T tok, MMLU43.4
> **Relevance:** Shows the winning hybrid recipe at this scale: keep only ~6 attention layers, offload most token-mixing to cheap gated convolutions for 2x CPU throughput and low KV memory. Directly compatible with the user's Engram/mHC additions if they replace some attention layers with conv.
> **Source:** arXiv 2511.23404 (LFM2 Technical Report), Table 1 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — hybrid-efficient-attention-architectures
> LFM2 (on-device) uses a minimal conv-attention hybrid: 16 blocks = 10 gated short convolutions (kernel k=3, double-gated 'LIV' conv) + 6 GQA attention blocks, identical layout for 350M/700M/1.2B (2.6B = 30 blocks: 22 conv + 8 GQA). Their hardware-in-the-loop search concluded 'most of the benefits of recent hybrid SSM/linear-attention blocks can be captured by their short convolutional submodules plus a small number of global attention layers.'
>
> **Numbers:** 10 conv + 6 GQA of 16 (=37.5% attention); vocab 65,536; 32K context; 10T training tokens
> **Relevance:** Direct template for a <=600M multilingual hybrid: short convs are far cheaper/simpler than Mamba-2 on CPU yet capture most SSM benefit, while keeping ~37% attention preserves knowledge/recall for KazMMLU. Stronger match to the edge target than a full SSM stack.
> **Source:** arXiv:2511.23404 (LFM2 Technical Report), Table 1; HF LiquidAI/LFM2-350M · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — hybrid-efficient-attention-architectures
> LFM2-350M beats Qwen3-0.6B on multilingual MMLU despite fewer params, and is within ~1.5 pts on English MMLU; on-device it is ~2x faster than Qwen3 on CPU. This is direct evidence a conv-attention hybrid competes with the best ~500M transformer on multilingual knowledge.
>
> **Numbers:** MMMLU: LFM2-350M 37.99 vs Qwen3-0.6B 30.84; MMLU 43.43 vs 44.93; Snapdragon 8 Elite LFM2-700M vs Qwen3-0.6B: prefill 522 vs 318 tok/s (+64%), 4K decode 80.2 vs 41.8 tok/s (+92%)
> **Relevance:** Qwen3-0.6B is the strongest measured Kazakh baseline (KazMMLU 32.8%). A hybrid that already outscores it on multilingual MMLU while decoding ~2x faster on CPU is the target-shaped competitor to beat.
> **Source:** arXiv:2511.23404; HF LiquidAI/LFM2-350M model card · **Sweep:** `slm-architecture-2026-07`

## Related
- [[hymba-a-hybrid-head-architecture-for-small-language-models|Hymba: A Hybrid-head Architecture for Small Language Models]] — Rival small-LM hybrids: LFM2 conv+few-GQA vs Hymba parallel hybrid-head attention+SSM

[[Home]]
