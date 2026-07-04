---
kb_id: "arxiv:2502.06703"
type: "paper"
title: "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling"
arxiv_id: "2502.06703"
doi: null
hf_repo: null
year: 2025
topics: ["inference-tts"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling", "arXiv:2502.06703", "arxiv:2502.06703"]
tags: ["paper", "topic/inference-tts"]
---
# Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling

[arXiv](https://arxiv.org/abs/2502.06703)
**Topics:** [[inference-tts]]

> [!abstract]
> Test-Time Scaling (TTS) is an important method for improving the performance of Large Language Models (LLMs) by using additional computation during the inference phase. However, current studies do not systematically analyze how policy models, Process Reward Models (PRMs), and problem difficulty influence TTS. This lack of analysis limits the understanding and practical use of TTS methods. In this …

## Claims

> [!note] CLAIM — inference-tts
> Compute-optimal test-time scaling lets sub-1B models beat 405B on MATH-500: Llama-3.2-1B-Instruct 66.2%, 3B 78.2%, Qwen2.5-0.5B 76.4%, Qwen2.5-1.5B 85.6% — all above Llama-3.1-405B CoT baseline 71.4%. Method wins by policy size: beam search for <=7B policies, Best-of-N for >=72B. Compute budgets N in {4,16,64,256} samples/problem.
>
> **Numbers:** 1B=66.2%, 3B=78.2%, 0.5B=76.4%, 1.5B=85.6% vs 405B=71.4% on MATH-500; N up to 256
> **Relevance:** Direct proof-of-concept that a 500M Kazakh model + TTS could close the gap to Sherkala-8B (41.4% KazMMLU); the headline result the paper can build on for Kazakh.
> **Source:** arXiv:2502.06703 'Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling' · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — inference-tts
> PRMs tested were Qwen2.5-Math-PRM-7B and -72B, Skywork-PRM-1.5B/7B, Math-Shepherd-PRM-7B, RLHFlow-PRM-Mistral-8B/Deepseek-8B. Key finding: the compute-optimal TTS strategy is highly dependent on policy model, PRM choice, and problem difficulty; the PRM must match the policy's output distribution or gains collapse, and beam search (not Best-of-N) is optimal for small policies.
>
> **Numbers:** 7 PRMs across 1.5B-72B; N in {4,16,64,256}
> **Relevance:** A Kazakh TTS pipeline needs a verifier trained on the SAME 500M policy's Kazakh outputs; off-the-shelf multilingual PRMs will underperform. Beam-search + PRM is the right small-policy recipe, not naive Best-of-N.
> **Source:** arXiv:2502.06703 · **Sweep:** `slm-architecture-2026-07`

## Related
- [[kinetics-rethinking-test-time-scaling-laws|Kinetics: Rethinking Test-Time Scaling Laws]] — Kinetics refutes Can-1B: compute-optimal TTS overstated once KV memory counted; sub-1B not on Pareto frontier

[[Home]]
