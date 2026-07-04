---
kb_id: "title:nvidia com en us data center tesla t4 official spec page fetched 2026 07 04 a100 numbers from nvidia a100 datasheet standard published specs local measurement context"
type: "source"
title: "nvidia.com/en-us/data-center/tesla-t4/ (official spec page, fetched 20…"
doi: null
hf_repo: null
year: null
topics: ["hardware-gate"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:nvidia com en us data center tesla t4 official spec page fetched 2026 07 04 a100 numbers from nvidia a100 datasheet standard published specs local measurement context"]
tags: ["source", "topic/hardware-gate"]
---
# nvidia.com/en-us/data-center/tesla-t4/ (official spec page, fetched 20…

**Topics:** [[hardware-gate]]

## Source URLs
- nvidia.com/en-us/data-center/tesla-t4/ (official spec page, fetched 2026-07-04)
- A100 numbers from NVIDIA A100 datasheet (standard published specs)
- local measurement context

## Findings

> [!note] CLAIM — hardware-gate
> Fraction-of-A100 context for all measured numbers: T4 peak is ~21% of one A100 on both axes, and Kaggle gives two of them. NVIDIA official specs: T4 = 65 TFLOPS FP16 mixed-precision, 8.1 TFLOPS FP32, 16 GB GDDR6 at '320+ GB/s', 70 W; A100-40GB = 312 TFLOPS BF16/FP16 tensor, 1555 GB/s. So T4/A100 = 20.8% peak fp16 compute, ~20.6% bandwidth; T4x2 aggregate ~41.7% of one A100 (data-parallel, if both GPUs used). Proxy caveat: our absolute ms were measured on an 80W RTX 2070 laptop (SM75, ~45 fp16 tensor TFLOPS peak, 448 GB/s); actual T4 should be within roughly ±40% on absolute times (faster on compute-bound, slower on bandwidth-bound kernels) with identical PASS/FAIL and dtype behavior.
>
> **Numbers:** T4: 65 FP16 TFLOPS / 8.1 FP32 / 320+ GB/s / 16 GB / 70 W; A100-40GB: 312 TFLOPS BF16/FP16, 1555 GB/s; ratios: 20.8% compute, ~20.6% bandwidth, 2xT4 = 41.7% of A100 compute; measured local matmul ceiling 20.9 fp16 TFLOPS
> **Relevance:** Lets the panel convert any paper's A100-hours into Kaggle-T4x2 wall-clock (multiply by ~4.8x single-T4, ~2.4x dual-T4 ideal) when sizing the 10B-token CPT/from-scratch budget.
> **Source:** nvidia.com/en-us/data-center/tesla-t4/ (official spec page, fetched 2026-07-04); A100 numbers from NVIDIA A100 datasheet (standard published specs); local measurement context · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[lab-measurement-2026-07-04-torch-2-11-0-cu130-transformers|Lab measurement 2026-07-04, torch 2.11.0+cu130, transformers 5.5.2, HF…]] — ~15-20% MFU is derived against T4 spec FLOPs; 2070 measurement is the anchor for the missing T4 0.6B-training number
- [[derived-from-lab-measurement-t4bench2-py-t4bench3-py-kaggle|Derived from lab measurement (t4bench2.py/t4bench3.py) + Kaggle quota…]] — T4=21%-of-A100 ceiling here underpins the 6N-FLOPs T4 compute-budget/token derivation in that node

[[Home]]
