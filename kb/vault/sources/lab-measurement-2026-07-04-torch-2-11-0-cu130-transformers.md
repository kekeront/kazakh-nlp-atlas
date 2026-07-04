---
kb_id: "title:lab measurement 2026 07 04 torch 2 11 0 cu130 transformers 5 5 2 hf qwen qwen3 0 6b base config json"
type: "source"
title: "Lab measurement 2026-07-04, torch 2.11.0+cu130, transformers 5.5.2, HF…"
doi: null
hf_repo: null
year: null
topics: ["kaggle-t4x2-compute-vram-budget-for-the"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:lab measurement 2026 07 04 torch 2 11 0 cu130 transformers 5 5 2 hf qwen qwen3 0 6b base config json"]
tags: ["source", "topic/kaggle-t4x2-compute-vram-budget-for-the"]
---
# Lab measurement 2026-07-04, torch 2.11.0+cu130, transformers 5.5.2, HF…

**Topics:** [[kaggle-t4x2-compute-vram-budget-for-the]]

## Source URLs
- Lab measurement 2026-07-04, torch 2.11.0+cu130, transformers 5.5.2, HF Qwen/Qwen3-0.6B-Base config.json

## Findings

> [!note] CLAIM — kaggle-t4x2-compute-vram-budget-for-the
> [measured-in-lab on the target checkpoint; language-agnostic] Direct fp16 training microbenchmark of Qwen/Qwen3-0.6B-Base (measured 596.0M params, config: 28L, d=1024, GQA 16/8 heads, head_dim 128, vocab 151,936, tied embeddings, bf16-native) on RTX 2070 Max-Q (Turing sm_75, same fp16-only architecture class as T4): with gradient checkpointing, mem-efficient SDPA, chunked cross-entropy, and a full optimizer step — 1,584 tok/s at bs1x4096 (2.59 s/step, peak 2.73 GiB), 1,948 tok/s at bs2x2048, 2,049 tok/s at bs4x2048 (peak 4.25 GiB). Batch scaling is nearly flat => compute-bound at ~6.0-7.3 TFLOPs on a 6N basis (~8-9.8 TFLOPs incl. checkpoint recompute, i.e. ~15-20% MFU). No published T4 tokens/s number for 0.6B-class training exists; this is the closest hardware anchor. Benchmark scripts: t4bench2.py and t4bench3.py.
>
> **Numbers:** 1,584 tok/s @ 4096 ctx; 2,049 tok/s @ bs4x2048; peak 2.73-4.25 GiB fwd+bwd; 596.0M params; ~15-20% MFU
> **Relevance:** Replaces the asserted-but-unmeasured throughput assumption with a same-architecture fp16 measurement; T4 (65 TFLOPS peak, 70W-capped) should land in the same 1.5-2.5k tok/s/GPU band at 4K ctx.
> **Source:** Lab measurement 2026-07-04, torch 2.11.0+cu130, transformers 5.5.2, HF Qwen/Qwen3-0.6B-Base config.json · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[nvidia-com-en-us-data-center-tesla-t4-official-spec-page|nvidia.com/en-us/data-center/tesla-t4/ (official spec page, fetched 20…]] — ~15-20% MFU is derived against T4 spec FLOPs; 2070 measurement is the anchor for the missing T4 0.6B-training number

[[Home]]
