---
kb_id: "arxiv:2509.11414"
type: "paper"
title: "Continually Adding New Languages to Multilingual Language Models"
arxiv_id: "2509.11414"
doi: null
hf_repo: null
year: 2025
topics: ["training-recipes"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Continually Adding New Languages to Multilingual Language Models", "arXiv:2509.11414", "arxiv:2509.11414"]
tags: ["paper", "topic/training-recipes"]
---
# Continually Adding New Languages to Multilingual Language Models

[arXiv](https://arxiv.org/abs/2509.11414)
**Topics:** [[training-recipes]]

> [!abstract]
> Multilingual language models are trained on a fixed set of languages, and to support new languages, the models need to be retrained from scratch. This is an expensive endeavor and is often infeasible, as model developers tend not to release their pre-training data. Naive approaches, such as continued pretraining, suffer from catastrophic forgetting; however, mitigation strategies like experience r …

## Claims

> [!note] CLAIM — training-recipes
> Continual language addition without original-data replay: LayRA (LoRA applied only to the first ~10 and last ~2 transformer layers, rank 8, alpha 16, LR 3e-4 linear) gives the best forgetting-vs-learning tradeoff among full-CPT, LoRA-CPT, and layer-selective CPT on Llama-3.1-8B / Qwen-2.5-7B adding Galician/Swahili/Urdu (~1.2B tokens each). Standard replay (re-mixing original-language data) remains the most common forgetting mitigation when original data IS available.
>
> **Numbers:** LoRA rank 8 alpha 16, LR 3e-4; first-10 + last-2 layers; ~1.2B tokens/new-language; 8B/7B bases
> **Relevance:** If the path becomes continual-pretraining a strong small base (Qwen3-0.6B is already 32.8%) rather than from-scratch, LayRA gives a cheap, forgetting-safe recipe. Since the user HAS Kazakh+Russian+English data, explicit replay mixing (Sherkala-style) is preferable to replay-free.
> **Source:** arXiv 2509.11414 Continually Adding New Languages to Multilingual LMs (arxiv.org/html/2509.11414v1) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[simple-and-scalable-strategies-to-continually-pre-train-large-language-models|Simple and Scalable Strategies to Continually Pre-train Large Language Models]] — LayRA is the no-replay alternative to the replay + LR-rewarming standard continual-PT baseline this establishes
- [[sparse-memory-finetuning-as-a-low-forgetting-alternative-to-lora-and-full|Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetuning]] — Both target low-forgetting language addition; LayRA = layer-selective LoRA vs sparse-memory finetuning — competing forgetting-mitigation…

[[Home]]
