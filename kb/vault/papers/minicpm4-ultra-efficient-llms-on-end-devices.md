---
kb_id: "arxiv:2506.07900"
type: "paper"
title: "MiniCPM4: Ultra-Efficient LLMs on End Devices"
arxiv_id: "2506.07900"
doi: null
hf_repo: null
year: 2025
topics: ["hybrid-efficiency-efficient-attention-se"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["MiniCPM4: Ultra-Efficient LLMs on End Devices", "arXiv:2506.07900", "arxiv:2506.07900"]
tags: ["paper", "topic/hybrid-efficiency-efficient-attention-se"]
---
# MiniCPM4: Ultra-Efficient LLMs on End Devices

[arXiv](https://arxiv.org/abs/2506.07900)
**Topics:** [[hybrid-efficiency-efficient-attention-se]]

> [!abstract]
> This paper introduces MiniCPM4, a highly efficient large language model (LLM) designed explicitly for end-side devices. We achieve this efficiency through systematic innovation in four key dimensions: model architecture, training data, training algorithms, and inference systems. Specifically, in terms of model architecture, we propose InfLLM v2, a trainable sparse attention mechanism that accelera …

## Claims

> [!note] CLAIM — hybrid-efficiency-efficient-attention-se
> MiniCPM4-0.5B pairs an edge-tuned transformer with InfLLM-v2 trainable sparse attention (each token attends to <5% of tokens at 128K), reaching up to 7x decode speedup on edge GPUs vs Qwen3-8B with perfect needle retrieval at 128K - a proven sub-600M edge-efficiency reference point.
>
> **Numbers:** <5% tokens attended @128K; up to 7x edge-GPU decode speedup vs Qwen3-8B; 0.5B params
> **Relevance:** Concrete existence proof of a competitive 0.5B edge model, and shows trainable sparse attention as an alternative to sliding-window for extreme long context - though for Kazakh's shorter typical inputs, Gemma-style sliding window is simpler and sufficient.
> **Source:** arXiv:2506.07900 (MiniCPM4); arXiv:2509.24663 (InfLLM-v2) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[native-sparse-attention-hardware-aligned-and-natively-trainable-sparse-attention|Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention]] — MiniCPM4's InfLLM-v2 and Native Sparse Attention are both natively-trainable sparse-attention schemes; shared method family

[[Home]]
