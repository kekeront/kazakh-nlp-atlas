---
kb_id: "arxiv:2407.17465"
type: "paper"
title: "u-$μ$P: The Unit-Scaled Maximal Update Parametrization"
arxiv_id: "2407.17465"
doi: null
hf_repo: null
year: 2024
topics: ["residual-stream-stability-qymyzlm-design"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["u-$μ$P: The Unit-Scaled Maximal Update Parametrization", "arXiv:2407.17465", "arxiv:2407.17465"]
tags: ["paper", "topic/residual-stream-stability-qymyzlm-design"]
---
# u-$μ$P: The Unit-Scaled Maximal Update Parametrization

[arXiv](https://arxiv.org/abs/2407.17465)
**Topics:** [[residual-stream-stability-qymyzlm-design]]

> [!abstract]
> The Maximal Update Parametrization ($μ$P) aims to make the optimal hyperparameters (HPs) of a model independent of its size, allowing them to be swept using a cheap proxy model rather than the full-size target model. We present a new scheme, u-$μ$P, which improves upon $μ$P by combining it with Unit Scaling, a method for designing models that makes them easy to train in low-precision. The two tech …

## Claims

> [!note] CLAIM — residual-stream-stability-qymyzlm-design
> [transferable-untested] u-muP: standard muP DIVERGES in FP16 due to gradient underflow; u-muP (muP + Unit Scaling) trains in FP16 without loss scaling, reaches lower loss than plain muP, and works out-of-the-box in FP8; public 1B and 7B checkpoints exist (Aleph-Alpha/umup-research-1b-bf16, -7b-bf16). Directly extends KB entry on muP-vs-weight-decay (2510.19093): if any muP wind-tunnel is used for the from-scratch run, plain muP on a T4 fp16 is a documented divergence risk.
>
> **Numbers:** muP diverges in FP16 (gradient underflow); u-muP: FP16 without loss scaling, FP8 out-of-box; validated with 1B/7B public checkpoints
> **Relevance:** The lab's proxy-sweep plan (MiniCPM-style <100M wind tunnel, in KB) meets fp16-only T4 hardware. Verdict: either use u-muP for the wind tunnel, or skip muP entirely (per KB 2510.19093) and fix LR/batch via fitted laws + dynamic GradScaler. Do NOT run plain muP in fp16.
> **Source:** arXiv:2407.17465 (u-muP, abstract + search verification 2026-07-04); HF Aleph-Alpha/umup-research-1b-bf16 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[weight-decay-may-matter-more-than-mup-for-learning-rate-transfer-in-practice|Weight Decay may matter more than muP for Learning Rate Transfer in Practice]] — u-muP claims muP fixes fp16 divergence; 2510.19093 argues weight decay not muP drives LR transfer — disputes muP's value
- [[predictable-scale-part-i-step-law-optimal-hyperparameter-scaling-law-in-large|Predictable Scale: Part I, Step Law -- Optimal Hyperparameter Scaling Law in Large Languag…]] — Competing routes to hyperparameter transfer: Step Law's directly-fitted LR/batch formulas vs u-muP's unit-scaled parametrization
- [[don-t-be-lazy-completep-enables-compute-efficient-deep-transformers|Don't be lazy: CompleteP enables compute-efficient deep transformers]] — Competing muP variant (unit-scaled max-update) vs CompleteP's depth-muP for single-scale HP transfer

[[Home]]
