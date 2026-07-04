---
kb_id: "arxiv:2506.05333"
type: "paper"
title: "Kinetics: Rethinking Test-Time Scaling Laws"
arxiv_id: "2506.05333"
doi: null
hf_repo: null
year: 2025
topics: ["inference-tts"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["Kinetics: Rethinking Test-Time Scaling Laws", "arXiv:2506.05333", "arxiv:2506.05333"]
tags: ["paper", "topic/inference-tts"]
---
# Kinetics: Rethinking Test-Time Scaling Laws

[arXiv](https://arxiv.org/abs/2506.05333)
**Topics:** [[inference-tts]]

> [!abstract]
> We rethink test-time scaling laws from a practical efficiency perspective, revealing that the effectiveness of smaller models is significantly overestimated. Prior work, grounded in compute-optimality, overlooks critical memory access bottlenecks introduced by inference-time strategies (e.g., Best-of-$N$, long CoTs). Our holistic analysis, spanning models from 0.6B to 32B parameters, reveals a new …

## Claims

> [!note] CLAIM — inference-tts
> CAVEAT — those compute-optimal numbers use oracle per-difficulty method selection and ignore memory cost. Kinetics shows small-model TTS effectiveness is overestimated once KV/memory is counted: Qwen3-0.6B needs 3.5GB KV cache at 32K (model weights only 1.2GB); only 14B+ models benefit from CoT longer than 10K tokens; below that, scaling params beats scaling generation. Block-top-k sparse attention recovers +45 points in the low-cost regime and 8.58x fewer resources.
>
> **Numbers:** Qwen3-0.6B: 3.5GB KV @32K vs 1.2GB weights; CoT>10K tokens only helps >=14B; sparse attn +45pts, 8.58x cheaper
> **Relevance:** Do NOT promise long-CoT gains at 500M; pair TTS with short-CoT + parallel sampling AND efficient/sparse attention, or the KV cache dominates and the 'small model wins' story fails in real latency.
> **Source:** arXiv:2506.05333 'Kinetics: Rethinking Test-Time Scaling Laws' · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — inference-tts
> Latency/token-aware TTS work and Kinetics both conclude that sparse or linear attention is the enabler that returns small models to the compute/latency Pareto frontier under test-time scaling, because parallel sampling and long generation are KV-access-bound rather than FLOP-bound at small scale.
>
> **Numbers:** attention cost L^2*D -> L*B*D with block sparse; TTS is memory-access-bound at small scale
> **Relevance:** To make TTS actually pay off at 500M, combine it with sliding-window/sparse attention so that best-of-N and longer generations don't saturate the 8GB KV budget — otherwise measured speedups evaporate.
> **Source:** arXiv:2506.05333 (Kinetics); arXiv:2509.09864 (Latency and Token-Aware Test-Time Compute) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-time-scaling|Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling]] — Kinetics refutes Can-1B: compute-optimal TTS overstated once KV memory counted; sub-1B not on Pareto frontier
- [[native-sparse-attention-hardware-aligned-and-natively-trainable-sparse-attention|Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention]] — Kinetics names block-top-k sparse attention as TTS enabler; NSA is the hardware-aligned trainable sparse-attention mechanism
- [[kitty-accurate-and-efficient-2-bit-kv-cache-quantization-with-dynamic-channel|Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precis…]] — Both attack the KV-memory wall that caps small-model TTS; Kitty does 2-bit KV quant where Kinetics uses sparse attention

[[Home]]
