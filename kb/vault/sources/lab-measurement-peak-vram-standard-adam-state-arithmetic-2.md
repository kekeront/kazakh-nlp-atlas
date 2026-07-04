---
kb_id: "title:lab measurement peak vram standard adam state arithmetic 2 2 4 4 4 bytes param mixed precision bitsandbytes 8 bit adam"
type: "source"
title: "Lab measurement (peak VRAM) + standard Adam state arithmetic (2+2+4+4+…"
doi: null
hf_repo: null
year: null
topics: ["kaggle-t4x2-compute-vram-budget-for-the"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:lab measurement peak vram standard adam state arithmetic 2 2 4 4 4 bytes param mixed precision bitsandbytes 8 bit adam"]
tags: ["source", "topic/kaggle-t4x2-compute-vram-budget-for-the"]
---
# Lab measurement (peak VRAM) + standard Adam state arithmetic (2+2+4+4+…

**Topics:** [[kaggle-t4x2-compute-vram-budget-for-the]]

## Source URLs
- Lab measurement (peak VRAM) + standard Adam state arithmetic (2+2+4+4+4 bytes/param mixed-precision)
- bitsandbytes 8-bit Adam

## Findings

> [!note] CLAIM — kaggle-t4x2-compute-vram-budget-for-the
> [measured + derived] VRAM is NOT the binding constraint and the asserted ZeRO-2/FSDP requirement is unnecessary: full-FT of 0.6B fits a SINGLE 16GB T4. Measured fwd+bwd peak at bs1x4096 is 2.73 GiB; adding fp16 params 1.19GB + fp16 grads 1.19GB (in peak) + fp32 AdamW m,v 4.77GB + fp32 master 2.38GB ≈ 11.5-12.5GB total < ~15GB usable. With bitsandbytes 8-bit Adam, optimizer states drop to ~1.2GB => ~7GB total. Corollary 1: use plain DDP on T4x2 (avoids ZeRO sharding traffic over PCIe — Kaggle T4x2 has no NVLink). Corollary 2: QLoRA has NO memory rationale at 0.6B (fp16 weights are only 1.19GB; NF4 saves <0.9GB while adding dequant overhead and blocking full-param CPT gains) — full-FT strictly dominates on this hardware.
>
> **Numbers:** peak fwd+bwd 2.73 GiB @ 4K ctx; full-FT total ~12.3GB (fp32 Adam) or ~7GB (8-bit Adam) vs 16GB T4; QLoRA weight saving <0.9GB
> **Relevance:** Simplifies the CPT recipe: full-FT + plain DDP + 8-bit Adam on T4x2; removes QLoRA and FSDP/ZeRO from the recommended path, freeing VRAM headroom for larger micro-batches.
> **Source:** Lab measurement (peak VRAM) + standard Adam state arithmetic (2+2+4+4+4 bytes/param mixed-precision); bitsandbytes 8-bit Adam · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[empirical-muon-ns-py-code-read-of-raw-githubusercontent-com|Empirical: muon_ns.py + code read of raw.githubusercontent.com/KellerJ…]] — Muon's single momentum buffer confirms the ~50% optimizer-VRAM saving vs the AdamW 2+2+4+4+4 arithmetic in that node
- [[lora-learns-less-and-forgets-less|LoRA Learns Less and Forgets Less]] — VRAM says QLoRA has no rationale at 0.6B so full-FT dominates; LoRA-Learns-Less confirms LoRA underperforms full-FT
- [[continual-learning-via-sparse-memory-finetuning|Continual Learning via Sparse Memory Finetuning]] — VRAM rules out QLoRA as the PEFT; sparse-memory finetuning is the competing low-forgetting alternative to full-FT

[[Home]]
