---
kb_id: "arxiv:2505.10772"
type: "paper"
title: "Ranked Voting based Self-Consistency of Large Language Models"
arxiv_id: "2505.10772"
doi: null
hf_repo: null
year: 2025
topics: ["inference-tts"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Ranked Voting based Self-Consistency of Large Language Models", "arXiv:2505.10772", "arxiv:2505.10772"]
tags: ["paper", "topic/inference-tts"]
---
# Ranked Voting based Self-Consistency of Large Language Models

[arXiv](https://arxiv.org/abs/2505.10772)
**Topics:** [[inference-tts]]

> [!abstract]
> Majority voting is considered an effective method to enhance chain-of-thought reasoning, as it selects the answer with the highest "self-consistency" among different reasoning paths (Wang et al., 2023). However, previous chain-of-thought reasoning methods typically generate only a single answer in each trial, thereby ignoring the possibility of other potential answers. As a result, these alternati …

## Claims

> [!note] CLAIM — inference-tts
> Self-consistency / majority voting needs zero verifier and zero training and historically lifts GSM8K by +17.9 points; ranked-voting variants beat plain majority voting; marginal gains shrink as pass@1 rises.
>
> **Numbers:** +17.9 GSM8K (Wang et al.); ranked voting > majority
> **Relevance:** The cheapest TTS for Kazakh — requires no Kazakh PRM/ORM. On MCQ benchmarks (KazMMLU, TUMLU) with verifiable answers it is immediately deployable; make it the default TTS baseline.
> **Source:** Wang et al. self-consistency (via arXiv:2505.10772 'Ranked Voting based Self-Consistency'); survey arXiv:2503.24235 · **Sweep:** `slm-architecture-2026-07`

[[Home]]
