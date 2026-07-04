---
kb_id: "arxiv:2505.01618"
type: "paper"
title: "Don't be lazy: CompleteP enables compute-efficient deep transformers"
arxiv_id: "2505.01618"
doi: null
hf_repo: null
year: 2025
topics: ["residual-stream-stability-qymyzlm-design", "small-lm-training-recipes-qymyzlm-design"]
claims: 2
uncertain_claims: 1
verdicts: []
aliases: ["Don't be lazy: CompleteP enables compute-efficient deep transformers", "arXiv:2505.01618", "arxiv:2505.01618"]
tags: ["paper", "topic/residual-stream-stability-qymyzlm-design", "topic/small-lm-training-recipes-qymyzlm-design"]
---
# Don't be lazy: CompleteP enables compute-efficient deep transformers

[arXiv](https://arxiv.org/abs/2505.01618)
**Topics:** [[residual-stream-stability-qymyzlm-design]], [[small-lm-training-recipes-qymyzlm-design]]

> [!abstract]
> We study compute efficiency of LLM training when using different parameterizations, i.e., rules for adjusting model and optimizer hyperparameters (HPs) as model size changes. Some parameterizations fail to transfer optimal base HPs (such as learning rate) across changes in model depth, requiring practitioners to either re-tune these HPs as they scale up (expensive), or accept sub-optimal training …

## Claims

> [!note] CLAIM — residual-stream-stability-qymyzlm-design
> [transferable-untested] CompleteP (depth-muP with alpha=1) achieves depth-wise hyperparameter transfer AND non-lazy learning in all layers, giving 12-34% compute-efficiency improvement over prior parameterizations and widening the range of compute-efficient width/depth ratios. Relevant only if the from-scratch run tunes HPs on a <100M proxy and/or considers a deep-narrow shape.
>
> **Numbers:** 12-34% compute-efficiency vs prior SOTA parameterizations; alpha=1 depth scaling; experiments on Cerebras CS-3 (scales not in abstract)
> **Relevance:** For a SINGLE 500M target the KB position stands (skip explicit muP sweeps; weight decay dominates LR transfer, 2510.19093). CompleteP matters only if the panel picks a deep-narrow shape (e.g. 32L x 1024d to cut KV cache) where depth-transfer from the wind tunnel becomes load-bearing. Verdict: scale/shape-conditional, not default.
> **Source:** arXiv:2505.01618 (CompleteP, Cerebras+Princeton/Harvard/ETH, abstract fetched 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

> [!warning] UNCERTAIN — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] muP status 2025-2026: (a) CompleteP (arXiv:2505.01618, Cerebras, COLM/NeurIPS 2025) extends transfer to DEPTH and claims compute-efficiency gains for deep transformers over standard muP; (b) arXiv:2510.19093 argues weight decay, not muP, is the primary mechanism stabilizing update dynamics through most of training — muP's assumptions 'hold only briefly at the start' and its benefit is replaceable by modified warmup; (c) arXiv:2512.22382 (Dec 2025) unifies transfer across modules/width/depth/batch/duration. Net practice signal: for a SINGLE-SCALE 500M run, muP machinery buys little; tuned literature HPs (DCLM/SmolLM2/MobileLLM-R1 all in the 3e-3..4e-3 band with WD 0.033-0.1) + proper warmup are the 2025-2026 small-lab default.
>
> **Numbers:** LR consensus band at 350-500M: 3e-3 (DCLM 412M, SmolLM2-360M) to 4e-3 (MobileLLM-R1); WD 0.033 (DCLM) vs 0.1 (SmolLM2/MobileLLM-R1/Moonlight)
> **Relevance:** Kills a whole tempting workstream: no muP sweep on free compute; adopt the converged HP band and spend the compute on data ablations instead.
> **Source:** arXiv:2505.01618; arXiv:2510.19093; arXiv:2512.22382 (abstracts/HTML verified to exist and claims read; CompleteP efficiency percentages not pinned) · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[weight-decay-may-matter-more-than-mup-for-learning-rate-transfer-in-practice]]

## Related
- [[u-p-the-unit-scaled-maximal-update-parametrization|u-$μ$P: The Unit-Scaled Maximal Update Parametrization]] — Competing muP variant (unit-scaled max-update) vs CompleteP's depth-muP for single-scale HP transfer
- [[predictable-scale-part-i-step-law-optimal-hyperparameter-scaling-law-in-large|Predictable Scale: Part I, Step Law -- Optimal Hyperparameter Scaling Law in Large Languag…]] — both are HP-transfer/scaling recipes for picking LR on a small proxy before the full run
- [[weight-decay-may-matter-more-than-mup-for-learning-rate-transfer-in-practice|Weight Decay may matter more than muP for Learning Rate Transfer in Practice]] — CompleteP extends muP transfer to depth; 2510.19093 says muP benefit is replaceable by modified warmup — direct disagreement

[[Home]]
