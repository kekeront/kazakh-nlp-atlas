---
kb_id: "arxiv:2502.11089"
type: "paper"
title: "Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention"
arxiv_id: "2502.11089"
doi: null
hf_repo: null
year: 2025
topics: ["deepseek-tech"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention", "arXiv:2502.11089", "arxiv:2502.11089"]
tags: ["paper", "topic/deepseek-tech"]
---
# Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention

[arXiv](https://arxiv.org/abs/2502.11089)
**Topics:** [[deepseek-tech]]

> [!abstract]
> Long-context modeling is crucial for next-generation language models, yet the high computational cost of standard attention mechanisms poses significant computational challenges. Sparse attention offers a promising direction for improving efficiency while maintaining model capabilities. We present NSA, a Natively trainable Sparse Attention mechanism that integrates algorithmic innovations with har …

## Claims

> [!note] CLAIM — deepseek-tech
> NSA (arXiv 2502.11089) hyperparams: compression block l=32, stride 16, selected block l'=64, top-n=16 selected blocks (incl. 1 forced initial + 2 local), sliding window w=512; three branches (compressed / selected / sliding) fused by a learned gate. Validated on a 27B MoE (3B active), pretrained 270B tokens @8k then extended to 32k with YaRN; surpasses full attention on average and is natively trainable. Requires GQA-style head grouping and custom Triton/CUDA kernels for the speedup.
>
> **Numbers:** l=32, stride 16, l'=64, top-n=16, window 512; 27B MoE/3B active; 8k->32k ctx
> **Relevance:** NSA only pays off at long context (>=8k-32k) and needs bespoke kernels; for a 500M Kazakh model with typical 4k context on one A100 it is high-effort, low-return. Deprioritize unless long-context Kazakh (KazQAD long passages) becomes a goal.
> **Source:** arXiv:2502.11089 (Native Sparse Attention) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[kimi-linear-an-expressive-efficient-attention-architecture|Kimi Linear: An Expressive, Efficient Attention Architecture]] — Both natively-trainable efficient-attention architectures validated at scale; NSA's block-sparse vs Kimi Linear's linear attention
- [[kinetics-rethinking-test-time-scaling-laws|Kinetics: Rethinking Test-Time Scaling Laws]] — Kinetics names block-top-k sparse attention as TTS enabler; NSA is the hardware-aligned trainable sparse-attention mechanism
- [[minicpm4-ultra-efficient-llms-on-end-devices|MiniCPM4: Ultra-Efficient LLMs on End Devices]] — MiniCPM4's InfLLM-v2 and Native Sparse Attention are both natively-trainable sparse-attention schemes; shared method family
- [[empirical-this-session-crossover-py-fp16-b-1-d-768|Empirical, this session: crossover.py (fp16, B=1, d=768)]] — NSA claims hardware-aligned attention; node shows fla linear kernels are hardware-MISaligned on SM75 (28-47x SDPA, 64KB fallback)
- [[lab-probe-2026-07-04-torch-nn-attention-sdpa-kernel|Lab probe 2026-07-04 (torch.nn.attention.sdpa_kernel warnings verbatim…]] — NSA's hardware-aligned kernels assume Ampere+; on sm_75 with no FlashAttention such sparse-attention wins do not port to Kaggle T4

[[Home]]
