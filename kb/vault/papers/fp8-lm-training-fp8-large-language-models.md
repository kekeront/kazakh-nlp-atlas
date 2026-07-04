---
kb_id: "arxiv:2310.18313"
type: "paper"
title: "FP8-LM: Training FP8 Large Language Models"
arxiv_id: "2310.18313"
doi: null
hf_repo: null
year: 2023
topics: ["training-recipes"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["FP8-LM: Training FP8 Large Language Models", "arXiv:2310.18313", "arxiv:2310.18313"]
tags: ["paper", "topic/training-recipes"]
---
# FP8-LM: Training FP8 Large Language Models

[arXiv](https://arxiv.org/abs/2310.18313)
**Topics:** [[training-recipes]]

> [!abstract]
> In this paper, we explore FP8 low-bit data formats for efficient training of large language models (LLMs). Our key insight is that most variables, such as gradients and optimizer states, in LLM training can employ low-precision data formats without compromising model accuracy and requiring no changes to hyper-parameters. Specifically, we propose a new FP8 automatic mixed-precision framework for tr …

## Claims

> [!note] CLAIM — training-recipes
> FP8 pretraining yields ~34-37% throughput gain and ~42% memory reduction and can match bf16 accuracy, BUT native FP8 tensor cores exist only on Hopper (H100) and Blackwell (B200); naive FP8 is unstable and needs per-tensor scaling / selective bf16 layers. The user's A100 40GB (Ampere) has NO FP8 support.
>
> **Numbers:** FP8: +34-37% throughput, -42% memory (H100); A100=Ampere, no FP8 tensor cores
> **Relevance:** Hard constraint: on the specified 1xA100 budget, bf16 is the correct and only sensible precision. FP8 is irrelevant unless the run moves to H100/B200. Don't spec FP8.
> **Source:** arXiv 2310.18313 FP8-LM; arXiv 2405.18710 To FP8 and Back Again; NVIDIA FP8 blog · **Sweep:** `slm-architecture-2026-07`

## Related
- [[deepseek-v3-technical-report|DeepSeek-V3 Technical Report]] — V3's fine-grained tile/block FP8 recipe builds on FP8-LM; both hit the Hopper-only tensor-core hardware constraint

[[Home]]
