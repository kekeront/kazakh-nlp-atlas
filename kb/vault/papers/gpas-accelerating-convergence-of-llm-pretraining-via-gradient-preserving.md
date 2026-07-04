---
kb_id: "arxiv:2506.22049"
type: "paper"
title: "GPAS: Accelerating Convergence of LLM Pretraining via Gradient-Preserving Activation Scaling"
arxiv_id: "2506.22049"
doi: null
hf_repo: null
year: 2025
topics: ["residual-stream-stability-qymyzlm-design"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["GPAS: Accelerating Convergence of LLM Pretraining via Gradient-Preserving Activation Scaling", "arXiv:2506.22049", "arxiv:2506.22049"]
tags: ["paper", "topic/residual-stream-stability-qymyzlm-design"]
---
# GPAS: Accelerating Convergence of LLM Pretraining via Gradient-Preserving Activation Scaling

[arXiv](https://arxiv.org/abs/2506.22049)
**Topics:** [[residual-stream-stability-qymyzlm-design]]

> [!abstract]
> Modern Large Language Models, such as the LLaMA, Qwen and DeepSeek series, predominantly adopt the Pre-LayerNorm (Pre-LN) Transformer architecture. While being stable during pretraining and scalable to large model sizes, Pre-LN suffers from an exponential growth in activation variance across layers, causing the shortcut to dominate over sub-layer outputs in the residual connection and limiting the …

## Claims

> [!warning] UNCERTAIN — residual-stream-stability-qymyzlm-design
> [transferable-untested] GPAS (Gradient-Preserving Activation Scaling) scales down intermediate activations while keeping gradients unchanged (learnable gate + stop-gradient), reporting consistent gains at 71M-1B over Pre-LN and improving Sandwich-LN/DeepNorm variants — a 2025 competitor to LayerNorm Scaling in the same variance-control niche. Exact perplexity deltas not extracted from primary source.
>
> **Numbers:** scales 71M-1B; 'consistent performance gains'; exact deltas not verified
> **Relevance:** Only matters as the third option in the variance-control bake-off (Peri-LN vs LNS vs GPAS) at the 50M proxy; activation down-scaling is additionally fp16-friendly (reduces overflow headroom pressure). Low priority: verify numbers only if the proxy bake-off actually happens.
> **Source:** arXiv:2506.22049 (GPAS, abstract fetched 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

[[Home]]
