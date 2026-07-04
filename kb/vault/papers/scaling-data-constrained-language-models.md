---
kb_id: "arxiv:2305.16264"
type: "paper"
title: "Scaling Data-Constrained Language Models"
arxiv_id: "2305.16264"
doi: null
hf_repo: null
year: 2023
topics: ["training-recipes", "small-lm-training-recipes-qymyzlm-design"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["Scaling Data-Constrained Language Models", "arXiv:2305.16264", "arxiv:2305.16264"]
tags: ["paper", "topic/training-recipes", "topic/small-lm-training-recipes-qymyzlm-design"]
---
# Scaling Data-Constrained Language Models

[arXiv](https://arxiv.org/abs/2305.16264)
**Topics:** [[training-recipes]], [[small-lm-training-recipes-qymyzlm-design]]

> [!abstract]
> The current trend of scaling language models involves increasing both parameter count and training dataset size. Extrapolating this trend suggests that training dataset size may soon be limited by the amount of text data available on the internet. Motivated by this limit, we investigate scaling language models in data-constrained regimes. Specifically, we run a large set of experiments varying the …

## Claims

> [!note] CLAIM — training-recipes
> Data-constrained scaling: training up to ~4 epochs of repeated data incurs negligible loss penalty vs equivalent fresh tokens; returns decay sharply after, with ~16 epochs marking strong diminishing returns. Validated up to 900B tokens and 9B params.
>
> **Numbers:** <=4 epochs ~= fresh data; ~16 epochs = diminishing; experiments <=900B tok, <=9B params
> **Relevance:** With ~10B unique Kazakh tokens, repeating up to 4 epochs (~40B Kazakh 'visits') is provably near-free. Cap Kazakh at <=4 epochs and fill the remaining budget with Russian (code-switch), Turkic, English and synthetic data rather than over-repeating Kazakh.
> **Source:** arXiv 2305.16264 Scaling Data-Constrained Language Models (Muennighoff et al., NeurIPS 2023) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] Compute feasibility re-derivation for from-scratch on Kaggle T4x2: 6*N*D = 6 * 5e8 * 1e10 = 3e19 FLOPs. T4 fp16 peak 65 TFLOPS; at an optimistic 25% MFU, 2 GPUs deliver ~3.25e13 FLOP/s -> ~9.2e5 s ~ 256 wall-clock hours ~ 8.5+ weeks of Kaggle's ~30 GPU-h/week quota for ONE epoch-equivalent pass — before checkpoint/restart overhead of 12h session caps, and T4 realistic MFU for small models is usually 10-20%, i.e. 400-650 hours. Combined with the KB's data-constrained law (<=4 epochs useful: 9-10B corpus -> <=40B useful tokens), a full Chinchilla-style from-scratch run is a multi-month commitment; QLoRA/full CPT on Qwen3-0.6B at 1-3B Kazakh tokens is 1-2 orders of magnitude cheaper.
>
> **Numbers:** 3e19 FLOPs; 256-650 T4x2 wall-hours depending on MFU 10-25%; Kaggle ~30 h/week
> **Relevance:** Hard constraint for the design panel: 'from-scratch later' requires either token-budget cuts (5B tokens halves it), Muon's ~2x FLOP efficiency, or paid/pooled compute; CPT-now is the only schedule-feasible path.
> **Source:** Re-derived from 6ND formula + NVIDIA T4 spec (65 TFLOPS fp16) + Kaggle quota (30 GPU-h/week, 12h sessions); KB arXiv:2305.16264 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[reusing-overtrained-language-models-saturates-scaling|Reusing Overtrained Language Models Saturates Scaling]] — Overtrained-base saturation complicates the ≤4-epoch reuse law: reusing an overtrained model saturates continued scaling
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — Data-constrained + T4 feasibility argues against from-scratch; SozKZ is the executed Kazakh-from-scratch counterpoint
- [[repetition-over-diversity-high-signal-data-filtering-for-sample-efficient|Repetition over Diversity: High-Signal Data Filtering for Sample-Efficient German Language…]] — Both argue repeated high-signal data rivals fresh tokens; Repetition-over-Diversity extends the ≤4-epoch result
- [[why-do-language-models-perform-worse-for-morphologically-complex-languages|Why do language models perform worse for morphologically complex languages?]] — Concludes gap is data-quantity driven after byte scaling; grounds it in data-constrained scaling laws
- [[derived-from-lab-measurement-t4bench2-py-t4bench3-py-kaggle|Derived from lab measurement (t4bench2.py/t4bench3.py) + Kaggle quota…]] — feasible ~3.8-6.4B-token envelope must be spent under data-constrained scaling (repeat-epoch value bounds)

[[Home]]
