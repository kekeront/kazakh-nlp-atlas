---
kb_id: "arxiv:2511.18643"
type: "paper"
title: "Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost"
arxiv_id: "2511.18643"
doi: null
hf_repo: null
year: 2025
topics: ["hybrid-efficient-attention-architectures"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost", "arXiv:2511.18643", "arxiv:2511.18643"]
tags: ["paper", "topic/hybrid-efficient-attention-architectures"]
---
# Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost

[arXiv](https://arxiv.org/abs/2511.18643)
**Topics:** [[hybrid-efficient-attention-architectures]]

> [!abstract]
> The KV cache is a dominant memory bottleneck for LLM inference. While 4-bit KV quantization preserves accuracy, 2-bit often degrades it, especially on long-context reasoning. We close this gap via an algorithm-system co-design for mixed-precision KV caching: Kitty. On the algorithm side, extensive experiments show that Dynamic Channel-wise Precision Boost -- which ranks Key-cache channels by sensi …

## Claims

> [!note] CLAIM — hybrid-efficient-attention-architectures
> KV-cache quantization: 4-bit KV is essentially lossless (KIVI: per-channel key + per-token value, tuning-free) giving ~2.6x peak memory cut and 2.35-3.47x throughput; but 2-bit KV degrades sharply (average drops of -10 to -15 points) unless a small fraction of sensitive key channels are kept at higher precision.
>
> **Numbers:** 4-bit KV ~lossless, 2.6x mem, 2.35-3.47x throughput; 2-bit KV: -10.15 to -15.23 avg accuracy; KIVI = 2-bit per-channel K / per-token V
> **Relevance:** For the edge Kazakh model, ship 4-bit KV cache quantization (safe, near-free) but do NOT go 2-bit. Combined with sliding-window 5:1 this makes long-context inference on 8GB feasible.
> **Source:** KIVI (ICML 2024, github jy-yuan/KIVI); arXiv:2511.18643 (Kitty 2-bit KV) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[a-systematic-study-of-cross-layer-kv-sharing-for-efficient-llm-inference|A Systematic Study of Cross-Layer KV Sharing for Efficient LLM Inference]] — Orthogonal, composable KV-cut axis: layer-sharing vs 2-bit KV quantization
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Trans…]] — MHA2MLA's headline 92.19% cut stacks MLA with Int4 HQQ; Kitty is an orthogonal 2-bit KV-quant axis
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] — Competing KV-cache reduction axes: MLA latent compression vs Kitty 2-bit KV quantization
- [[kinetics-rethinking-test-time-scaling-laws|Kinetics: Rethinking Test-Time Scaling Laws]] — Both attack the KV-memory wall that caps small-model TTS; Kitty does 2-bit KV quant where Kinetics uses sparse attention

[[Home]]
