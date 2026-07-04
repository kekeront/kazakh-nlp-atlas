---
kb_id: "title:github com dao ailab flash attention issues 2372 github com dao ailab grouped latent attention readme kernels deferred to fa3 hopper hopper gpus cuda 12 3 github com songtaoliu0823 mlra"
type: "source"
title: "github.com/Dao-AILab/flash-attention/issues/2372"
doi: null
hf_repo: null
year: null
topics: ["gla-2-gta-arxiv-2505-21487-zadouri-strau"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:github com dao ailab flash attention issues 2372 github com dao ailab grouped latent attention readme kernels deferred to fa3 hopper hopper gpus cuda 12 3 github com songtaoliu0823 mlra"]
tags: ["source", "topic/gla-2-gta-arxiv-2505-21487-zadouri-strau"]
---
# github.com/Dao-AILab/flash-attention/issues/2372

**Topics:** [[gla-2-gta-arxiv-2505-21487-zadouri-strau]]

## Source URLs
- github.com/Dao-AILab/flash-attention/issues/2372
- github.com/Dao-AILab/grouped-latent-attention README (kernels deferred to FA3 /hopper, Hopper GPUs, CUDA 12.3+)
- github.com/SongtaoLiu0823/MLRA

## Findings

> [!note] CLAIM — gla-2-gta-arxiv-2505-21487-zadouri-strau
> The only GLA kernels live in FlashAttention-3 hopper (same lab, not independent), require H100 + CUDA 12.3+, and the toolchain is fragile: the MLRA authors — the only confirmed external group training GLA-2 (with added gating) through FA3 — hit a v3.0.0 regression in the gated code path (GLA-2 val loss 3.6086 vs 3.5550 at step 1000 vs v3.0.0b1; matches SDPA only with gating off), reported 2026-03-19 in issue #2372, still open.
>
> **Numbers:** GLA-2+gating val loss @1000 steps: 3.5550 (v3.0.0b1) vs 3.6086 (v3.0.0), +0.054 regression; 1 known external training user; kernels H100-only
> **Relevance:** Even at training time (not just serving), GLA support is one-vendor, one-GPU-generation, and currently has an open correctness regression — high integration risk for a modest-compute lab.
> **Source:** github.com/Dao-AILab/flash-attention/issues/2372; github.com/Dao-AILab/grouped-latent-attention README (kernels deferred to FA3 /hopper, Hopper GPUs, CUDA 12.3+); github.com/SongtaoLiu0823/MLRA · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[derived-from-lab-measurement-t4bench2-py-t4bench3-py-kaggle|Derived from lab measurement (t4bench2.py/t4bench3.py) + Kaggle quota…]] — GLA kernels need H100+CUDA12.3; lab's canonical compute is Kaggle T4 (sm75) — GLA/GTA unrunnable there

[[Home]]
