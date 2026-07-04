---
kb_id: "arxiv:2404.06395"
type: "paper"
title: "MiniCPM: Unveiling the Potential of Small Language Models with Scalable Training Strategies"
arxiv_id: "2404.06395"
doi: null
hf_repo: null
year: 2024
topics: ["training-recipes"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["MiniCPM: Unveiling the Potential of Small Language Models with Scalable Training Strategies", "arXiv:2404.06395", "arxiv:2404.06395"]
tags: ["paper", "topic/training-recipes"]
---
# MiniCPM: Unveiling the Potential of Small Language Models with Scalable Training Strategies

[arXiv](https://arxiv.org/abs/2404.06395)
**Topics:** [[training-recipes]]

> [!abstract]
> The burgeoning interest in developing Large Language Models (LLMs) with up to trillion parameters has been met with concerns regarding resource efficiency and practical expense, particularly given the immense cost of experimentation. This scenario underscores the importance of exploring the potential of Small Language Models (SLMs) as a resource-efficient alternative. In this context, we introduce …

## Claims

> [!note] CLAIM — training-recipes
> MiniCPM's WSD scheduler yields a compute-optimal data-to-parameter ratio of ~192 tokens/param (vs Chinchilla ~20), and crucially: introducing high-quality + SFT-style data at the START of the decay/annealing phase gives far larger gains than adding the same data in a post-anneal SFT stage. muP-style hyperparameters were transferred from sub-100M 'wind tunnel' proxies to full scale.
>
> **Numbers:** compute-optimal ~192 tok/param; anneal-injection >> post-anneal SFT injection; muP proxy <100M
> **Relevance:** Compute-optimal for 500M is ~96B tokens — far more than ~10B unique Kazakh, confirming the corpus must be padded with transfer/synthetic data. The anneal-injection finding says: front-load curated Kazakh (textbooks/QA/CoT) into decay, don't reserve it for SFT.
> **Source:** arXiv 2404.06395 MiniCPM (arxiv.org/html/2404.06395v1) · **Sweep:** `slm-architecture-2026-07`

[[Home]]
