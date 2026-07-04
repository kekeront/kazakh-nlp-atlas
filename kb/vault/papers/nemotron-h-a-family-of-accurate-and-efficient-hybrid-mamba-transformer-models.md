---
kb_id: "arxiv:2504.03624"
type: "paper"
title: "Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models"
arxiv_id: "2504.03624"
doi: null
hf_repo: null
year: 2025
topics: ["hybrid-efficiency-efficient-attention-se"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models", "arXiv:2504.03624", "arxiv:2504.03624"]
tags: ["paper", "topic/hybrid-efficiency-efficient-attention-se"]
---
# Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models

[arXiv](https://arxiv.org/abs/2504.03624)
**Topics:** [[hybrid-efficiency-efficient-attention-se]]

> [!abstract]
> As inference-time scaling becomes critical for enhanced reasoning capabilities, it is increasingly becoming important to build models that are efficient to infer. We introduce Nemotron-H, a family of 8B and 56B/47B hybrid Mamba-Transformer models designed to reduce inference cost for a given accuracy level. To achieve this goal, we replace the majority of self-attention layers in the common Transf …

## Claims

> [!note] CLAIM — hybrid-efficiency-efficient-attention-se
> Sequential Mamba-heavy hybrids trade knowledge headroom for throughput. IBM Granite 4.0 uses ~9:1 Mamba-2:transformer (>70% long-context memory reduction). NVIDIA Nemotron-H/Nano-2 set attention to ~8% of layers (e.g. 4 self-attn of 52 for the 8B; rest Mamba-2+FFN), yielding up to 6-6.3x throughput vs Qwen3-8B at 8K-in/16K-out and 1.8-3x at 65K context.
>
> **Numbers:** Granite 4.0: 9:1 Mamba:transformer, >70% mem cut; Nemotron-H-8B: 4 attn / 24 Mamba-2 / 24 MLP = 52 layers (~8% attn); Nano-2: up to 6.3x throughput vs Qwen3-8B
> **Relevance:** These ratios are optimized for long-context throughput at 8B+, not for knowledge at 500M. For Kazakh, the ~8% attention floor is risky on KazMMLU; use them as the throughput ceiling, not the default ratio.
> **Source:** IBM Granite 4.0 announcement (Oct 2025); arXiv:2504.03624 (Nemotron-H); arXiv:2508.14444 (Nemotron Nano 2) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[gated-delta-networks-improving-mamba2-with-delta-rule|Gated Delta Networks: Improving Mamba2 with Delta Rule]] — Both Mamba-transformer hybrids; Nemotron-H sets KB's ~7-8% attention floor, above which GDN's 3:1-2:1 ratios sit
- [[falcon-h1-a-family-of-hybrid-head-language-models-redefining-efficiency-and|Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance]] — Falcon-H1 runs attention+Mamba-2 parallel per layer; Nemotron-H interleaves them sequentially
- [[empirical-this-session-tmp-claude-1000-home-altairzhambyl-8a3008cc|Empirical, this session: /tmp/claude-1000/-home-altairzhambyl-projects…]] — Node gates hybrid design: Mamba2 costs 28-47x SDPA on SM75, so a Nemotron-H-style Mamba2-Transformer hybrid is T4-infeasible

[[Home]]
