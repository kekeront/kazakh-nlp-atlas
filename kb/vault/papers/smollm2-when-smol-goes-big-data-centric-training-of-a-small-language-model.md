---
kb_id: "arxiv:2502.02737"
type: "paper"
title: "SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model"
arxiv_id: "2502.02737"
doi: null
hf_repo: "blog/smollm3"
year: 2025
topics: ["sota-slm", "training-recipes", "small-lm-training-recipes-qymyzlm-design"]
claims: 3
uncertain_claims: 0
verdicts: []
aliases: ["SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model", "arXiv:2502.02737", "arxiv:2502.02737"]
tags: ["paper", "topic/sota-slm", "topic/training-recipes", "topic/small-lm-training-recipes-qymyzlm-design"]
---
# SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model

[arXiv](https://arxiv.org/abs/2502.02737)
**Topics:** [[sota-slm]], [[training-recipes]], [[small-lm-training-recipes-qymyzlm-design]]

> [!abstract]
> While large language models have facilitated breakthroughs in many applications of artificial intelligence, their inherent largeness makes them computationally expensive and challenging to deploy in resource-constrained settings. In this paper, we document the development of SmolLM2, a state-of-the-art "small" (1.7 billion parameter) language model (LM). To attain strong performance, we overtrain …

## Claims

> [!note] CLAIM — sota-slm
> SmolLM2-360M is a deep-thin GQA transformer: 32 layers, d_model 960, FFN 2560, 15 query heads / 5 KV heads (GQA 3:1), vocab 49,152, 8K context, TIED input/output embeddings, trained on 4T tokens single-stage. SmolLM2-135M is 30 layers, d_model 576, 9Q/3KV heads, 2T tokens. Explicitly follows MobileLLM's 'depth over width' recipe.
>
> **Numbers:** 360M: 32L, d960, 15Q/5KV, FFN2560, vocab49152, 8K ctx, 4T tok, tied emb
> **Relevance:** This is the closest analogue to the target 500-600M from-scratch design; its 49K vocab + tied embeddings + 32-layer deep-thin shape is a proven sub-1B blueprint the Kazakh model should match or exceed in depth.
> **Source:** arXiv 2502.02737 (SmolLM2) + HF config; ritvik19 Papers Explained 176 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — training-recipes
> SmolLM2's smaller models were NOT multi-stage: 360M (4T tokens, ~11 tok/param) and 135M (2T, ~15 tok/param) used a single-stage high-quality-data recipe, while only the 1.7B used 4-stage mixing over 11T. WSD schedule, peak LR 3.0e-3 for 360M (5.0e-4 for 1.7B), 10-20% linear decay tail, global batch ~2M tokens, AdamW beta=(0.9,0.95), vocab 49,152. The decay/anneal stage up-weights the best data (FineMath4+, Stack-Edu, Cosmopedia v2, InfiWebMath).
>
> **Numbers:** 360M=4T tok (~11/param); 135M=2T (~15/param); 1.7B=11T (~6.5/param); LR 3e-3(360M)/5e-4(1.7B); batch ~2M tok; vocab 49,152; decay=last 10-20%
> **Relevance:** A 500M model is in the 'single-stage high-quality' regime, not multi-stage. Directly sets LR (~3e-3), batch (~2M tok), vocab (~50K matches user's Unigram-50K), and the anneal-on-best-data pattern for the Kazakh from-scratch run.
> **Source:** arXiv 2502.02737 SmolLM2: When Smol Goes Big (arxiv.org/html/2502.02737v1) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] SmolLM3-3B (HF, 2025) recipe deltas vs SmolLM2 relevant downscale evidence: AdamW (0.9,0.95), WD 0.1, grad clip 1.0, WSD schedule with 2000 warmup steps and linear decay to 0 over final 10%, global batch 2.36M tokens @ seq 4096, 11.2T tokens, LR 2e-4 (3B-scale — NOT transferable to 500M, where SmolLM2 used 3e-3). Confirms the pattern: peak LR falls ~10-15x from 360M to 3B; warmup ~2000 steps is scale-invariant across DCLM/MobileLLM-R1/SmolLM3.
>
> **Numbers:** 2e-4 @ 3B vs 3e-3 @ 360M; warmup 2000 steps in 4/4 modern recipes; batch 2.36M tok
> **Relevance:** Locks warmup=2000 steps and the LR-vs-scale curve for the design spec; warns against copying any 1B+ LR downward.
> **Source:** https://huggingface.co/blog/smollm3 (search-verified); SmolLM2 arXiv:2502.02737 (KB) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Trans…]] — MHA2MLA converts SmolLM-135M/360M/1B7 — these SmolLM2 GQA models are the from-scratch base it upcycles

[[Home]]
