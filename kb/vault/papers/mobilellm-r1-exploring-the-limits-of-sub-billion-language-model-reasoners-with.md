---
kb_id: "arxiv:2509.24945"
type: "paper"
title: "MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes"
arxiv_id: "2509.24945"
doi: null
hf_repo: null
year: 2025
topics: ["training-recipes", "small-lm-training-recipes-qymyzlm-design"]
claims: 4
uncertain_claims: 0
verdicts: []
aliases: ["MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes", "arXiv:2509.24945", "arxiv:2509.24945"]
tags: ["paper", "topic/training-recipes", "topic/small-lm-training-recipes-qymyzlm-design"]
---
# MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes

[arXiv](https://arxiv.org/abs/2509.24945)
**Topics:** [[training-recipes]], [[small-lm-training-recipes-qymyzlm-design]]

> [!abstract]
> The paradigm shift in large language models (LLMs) from instinctive responses to chain-of-thought (CoT) reasoning has fueled two prevailing assumptions: (1) reasoning capabilities only emerge in sufficiently large models, and (2) such capabilities require training on massive datasets. While the first assumption has already been challenged by recent sub-billion-parameter reasoning models such as Qw …

## Claims

> [!note] CLAIM — training-recipes
> MobileLLM-R1-950M (22 layers, 1536 dim, 24 heads / 6 KV = GQA 4:1, 128K vocab, embedding tying) was pretrained on only 4.2T tokens (~4,400 tok/param, resampled from ~2T curated) in 2 WSD phases (peak LR 4.0e-3, 2K warmup, linear decay to 10% over 500K steps), with phase-1 logit KD from Llama-3.1-8B-Instruct. It matches/beats Qwen3-0.6B on math/code (MATH500 74.0 vs 73.0, AIME24 15.5 vs 11.3, LiveCodeBench 19.9 vs 14.9) using 11.7% of Qwen3's tokens; reasoning SFT gave large gains and SFT beat RL for the tiny model.
>
> **Numbers:** 950M, GQA 4:1, 128K vocab; 4.2T tok (~4.4k/param); LR 4e-3; MATH500 74.0 vs Qwen3-0.6B 73.0; AIME24 15.5 vs 11.3; SFT>RL
> **Relevance:** Proof that a sub-1B from-scratch model with careful data + light KD + reasoning SFT can beat Qwen3-0.6B — the user's exact goal. Validates GQA 4:1 (user has 2:1), LR ~4e-3, logit-KD from an 8B teacher, and a reasoning-SFT stage. 360M/140M variants exist too.
> **Source:** arXiv 2509.24945 MobileLLM-R1 (arxiv.org/html/2509.24945) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — training-recipes
> Reasoning/CoT capability can emerge in sub-billion models via careful data curation + reasoning SFT, and SFT outperforms RL at that scale (MobileLLM-R1); Qwen3-0.6B likewise obtains its thinking mode through distillation, not scale. But this requires reasoning-SFT data in the target language, which barely exists for Kazakh.
>
> **Numbers:** reasoning emerges <1B; SFT>RL for tiny models; MobileLLM-R1 uses Tulu-3-SFT + OpenMath/Code/Science-Reasoning-2
> **Relevance:** A light Kazakh CoT-SFT stage is worth including and can differentiate the paper, but the CoT data must be synthesized/translated (via a Kazakh-fluent teacher) since native Kazakh reasoning corpora are absent — a real risk and a novel contribution angle.
> **Source:** arXiv 2509.24945 MobileLLM-R1; arXiv 2505.09388 Qwen3 · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[qwen3-technical-report]]

> [!note] CLAIM — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] MobileLLM-R1 (Meta, 2025) full open recipe at 140M/360M/950M: Adam beta=(0.9,0.95) eps 1e-8, WD 0.1 (pretraining only), peak LR 4.0e-3 with 2k-step warmup then linear decay to 0.1x peak; two pretraining phases of 2T tokens each at seq 2048 (global batch ~4M tok/step derived from 2T/500k steps; table lists per-device batch 16); mid-training 2x100B tokens at LR 3.6e-4 with knowledge distillation from Llama-3.1-8B-Instruct as teacher. All sizes use QK-norm and tied input/output embeddings, 128k vocab. Arch is NOT deep-narrow: 360M = 15 layers, d=1024, 16Q/4KV, FFN 4096 — the same Meta lineage that founded deep-narrow (MobileLLM 2024, 30-42L at 125M) shipped a shallow-wide 360M in 2025.
>
> **Numbers:** LR 4e-3 pretrain / 3.6e-4 mid-train; 4.2T total tokens; 360M: 15L/d1024/16Q/4KV/FFN4096; KD teacher Llama-3.1-8B-Instruct in mid-training
> **Relevance:** Second independent LR anchor (3e-3..4e-3 at 360-500M with ~1-4M token batches); QK-norm+tied-embeddings consensus; weakens a blind deep-narrow default for QymyzLM — depth/width should be argued per-target, not by MobileLLM-2024 authority.
> **Source:** arXiv:2509.24945 (MobileLLM-R1), Table 1 + training-details section (HTML) · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] MobileLLM-R1-950M matches/surpasses Qwen3-0.6B on reasoning with 11.7% of its tokens (4.2T vs 36T) but still loses on knowledge: base-model MMLU 47.4% (5-shot) vs Qwen3-0.6B 52.4%; MobileLLM-R1-360M-base: GSM8K 39.4% (8-shot), MATH500 13.4% (4-shot), MMLU 26.8% (5-shot) vs Qwen3-0.6B 60.9/29.8/52.4. Token-efficient recipes close reasoning gaps far faster than knowledge gaps.
>
> **Numbers:** 950M: MMLU 47.4 vs Qwen3-0.6B 52.4; 360M: MMLU 26.8, GSM8K 39.4; 4.2T = 11.7% of 36T
> **Relevance:** KazMMLU is a knowledge benchmark — a 500M model on ~10-40B effective Kazakh tokens cannot out-knowledge a 36T-token base by recipe alone; consistent with Engram-KB evidence that memory/lookup capacity, not recipe, is the knowledge lever. Beat-Qwen3 plan should lean on Kazakh-specific data + memory, not generic recipe gains.
> **Source:** arXiv:2509.24945, Table 6 (base models) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement|DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]] — Both push reasoning below R1's 1.5B distill floor; MobileLLM-R1 tests sub-billion reasoning the R1 distills never reached
- [[s1-simple-test-time-scaling|s1: Simple test-time scaling]] — s1 budget forcing collapses on 1.5B distills; MobileLLM-R1 probes whether sub-billion reasoning is trainable at all
- [[mobilellm-optimizing-sub-billion-parameter-language-models-for-on-device-use|MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases]] — Same Meta lineage that founded deep-narrow MobileLLM shipped a shallow-wide 360M in R1 — reversed shape choice
- [[marktechpost-2025-09-14|MarkTechPost 2025-09-14]] — This blog summarizes the MobileLLM-R1 primary paper's sub-1B reasoning results

[[Home]]
