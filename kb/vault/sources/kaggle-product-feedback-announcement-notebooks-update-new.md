---
kb_id: "title:kaggle product feedback announcement notebooks update new gpu t4s options"
type: "source"
title: "Kaggle product-feedback announcement   ([Notebooks update] New GPU (T4…"
doi: null
hf_repo: null
year: null
topics: ["kaggle-t4x2-compute-vram-budget-for-the"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:kaggle product feedback announcement notebooks update new gpu t4s options"]
tags: ["source", "topic/kaggle-t4x2-compute-vram-budget-for-the"]
---
# Kaggle product-feedback announcement   ([Notebooks update] New GPU (T4…

**Topics:** [[kaggle-t4x2-compute-vram-budget-for-the]]

## Source URLs
- Kaggle product-feedback announcement   ([Notebooks update] New GPU (T4s) options)

## Findings

> [!note] CLAIM — kaggle-t4x2-compute-vram-budget-for-the
> [transferable-untested; hardware fact] Kaggle free-tier quota confirmed: ~30 GPU-hours/week, 12h max session, and the T4x2 option (2x Tesla T4, 16GB each, sm_75, fp16-only tensor cores, no NVLink) consumes quota at 1x rate — 1 wall-clock hour of T4x2 = 1 quota hour, so the effective budget is ~60 GPU-hours/week in 12h chunks (>=3 session restarts per full week).
>
> **Numbers:** 30 h/week; 12 h/session; T4x2 = 1x quota; 2x16GB VRAM
> **Relevance:** Sets the hard weekly token budget for QymyzLM CPT; the 1x-quota T4x2 rate means DDP across both GPUs is effectively free throughput.
> **Source:** Kaggle product-feedback announcement https://www.kaggle.com/product-feedback/361104 ([Notebooks update] New GPU (T4s) options); https://www.kaggle.com/docs/efficient-gpu-usage; https://www.kaggle.com/general/108481 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[empirical-smoke-one-py-smoke2-py-timings-this-session|Empirical: smoke_one.py / smoke2.py timings this session]] — The 7-9 min per-session Triton compile tax compounds the Kaggle session/quota limits described in that announcement

[[Home]]
