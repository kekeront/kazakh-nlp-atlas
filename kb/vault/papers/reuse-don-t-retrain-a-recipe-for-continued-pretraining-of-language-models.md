---
kb_id: "arxiv:2407.07263"
type: "paper"
title: "Reuse, Don't Retrain: A Recipe for Continued Pretraining of Language Models"
arxiv_id: "2407.07263"
doi: null
hf_repo: null
year: 2024
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Reuse, Don't Retrain: A Recipe for Continued Pretraining of Language Models", "arXiv:2407.07263", "arxiv:2407.07263"]
tags: ["paper", "topic/continual-pt-lowres-qlora-vs-full-cpt-re"]
---
# Reuse, Don't Retrain: A Recipe for Continued Pretraining of Language Models

[arXiv](https://arxiv.org/abs/2407.07263)
**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]]

> [!abstract]
> As language models have scaled both their number of parameters and pretraining dataset sizes, the computational cost for pretraining has become intractable except for the most well-resourced teams. This increasing cost makes it ever more important to be able to reuse a model after it has completed pretraining; allowing for a model's abilities to further improve without needing to train from scratc …

## Claims

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested] LR-schedule evidence CONFLICTS across the three strongest CPT recipes — do not average: (a) Ibrahim 2403.08763: re-warm to high LR then re-decay (+replay) matches union re-training at 405M; (b) NVIDIA 'Reuse, Don't Retrain' (15B, 8T-token base): start at η_min of pretraining (4.5e-5), cosine to η_min/100, NO warmup, switch general→QA blend at η_max/5, giving +9% relative avg accuracy at 300B CPT tokens (48.9%→55.4% cumulative +13%); (c) Sailor 0.5B: constant 1e-4 (recovery-friendly); (d) EstLLM: trapezoidal WSD. NVIDIA explicitly warns re-warming a heavily-trained base can hurt; Ibrahim shows not re-warming slows adaptation.
>
> **Numbers:** NVIDIA: η_min 4.5e-5 → 4.5e-7, no warmup, +9%@300B; Ibrahim: rewarm+redecay+5–25% replay; Sailor: 1e-4 constant
> **Relevance:** Qwen3-0.6B is a heavily-overtrained base (KB: transfer benefit decays log with base tokens) — the panel must pick a schedule; WSD/constant-with-final-decay is the only family compatible with interruptible Kaggle sessions AND both papers' cautions.
> **Source:** arXiv:2407.07263 (Reuse Don't Retrain) HTML v1; arXiv:2403.08763 PDF; arXiv:2404.03608; arXiv:2603.02041 · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[simple-and-scalable-strategies-to-continually-pre-train-large-language-models]], [[sailor-open-language-models-for-south-east-asia]], [[estllm-enhancing-estonian-capabilities-in-multilingual-llms-via-continued]]

## Related
- [[reusing-overtrained-language-models-saturates-scaling|Reusing Overtrained Language Models Saturates Scaling]] — Bounds 'Reuse Don't Retrain': the reuse/transfer benefit saturates as base pretraining tokens grow, decaying the advantage

[[Home]]
