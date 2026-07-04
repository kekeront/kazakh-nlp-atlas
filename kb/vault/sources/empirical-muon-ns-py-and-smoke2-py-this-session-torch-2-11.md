---
kb_id: "title:empirical muon ns py and smoke2 py this session torch 2 11 0 cu130 sm75"
type: "source"
title: "Empirical: muon_ns.py and smoke2.py this session (torch 2.11.0+cu130,…"
doi: null
hf_repo: null
year: null
topics: ["hardware-gate"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:empirical muon ns py and smoke2 py this session torch 2 11 0 cu130 sm75"]
tags: ["source", "topic/hardware-gate"]
---
# Empirical: muon_ns.py and smoke2.py this session (torch 2.11.0+cu130,…

**Topics:** [[hardware-gate]]

## Source URLs
- Empirical: muon_ns.py and smoke2.py this session (torch 2.11.0+cu130, SM75)

## Findings

> [!note] CLAIM — hardware-gate
> bf16 on SM75 is a silent trap across the stack: torch.cuda.is_bf16_supported() returns True on SM75 (torch 2.11), and bf16 Triton kernels compile and run — but without tensor cores. Measured bf16 GEMM is 7.3x slower than fp16 and even 1.7x slower than fp32. All fla kernels pass in bf16 but at 1.2-1.6x their fp16 time. Every training config for Kaggle T4 must pin fp16 + GradScaler and must not trust the bf16 capability flag. Flag: transferable-untested.
>
> **Numbers:** 4096^3 matmul: fp16 20.93 TFLOPS (tensor cores), bf16 2.88 TFLOPS, fp32 4.83 TFLOPS; KDA bf16 22.8 ms vs fp16 14.2 ms (1.6x); GDN bf16 175.0 vs 144.3 ms (1.2x); Mamba2 bf16 253.8 vs 245.6 ms
> **Relevance:** Design-panel configs copied from 2025-26 papers (all bf16-native) will run but silently lose most tensor-core throughput on T4; loss-scaling (GradScaler) requirements of fp16 must be part of the training recipe, including for Engram gating and QLoRA-CPT.
> **Source:** Empirical: muon_ns.py and smoke2.py this session (torch 2.11.0+cu130, SM75) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[defeating-the-training-inference-mismatch-via-fp16|Defeating the Training-Inference Mismatch via FP16]] — Converging fp16>bf16 prescription: node's reason is SM75 tensor-core absence, this paper's is defeating train-inference mismatch

[[Home]]
