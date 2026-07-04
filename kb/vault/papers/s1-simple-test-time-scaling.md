---
kb_id: "arxiv:2501.19393"
type: "paper"
title: "s1: Simple test-time scaling"
arxiv_id: "2501.19393"
doi: null
hf_repo: null
year: 2025
topics: ["inference-tts"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["s1: Simple test-time scaling", "arXiv:2501.19393", "arxiv:2501.19393"]
tags: ["paper", "topic/inference-tts"]
---
# s1: Simple test-time scaling

[arXiv](https://arxiv.org/abs/2501.19393)
**Topics:** [[inference-tts]]

> [!abstract]
> Test-time scaling is a promising new approach to language modeling that uses extra test-time compute to improve performance. Recently, OpenAI's o1 model showed this capability but did not publicly share its methodology, leading to many replication efforts. We seek the simplest approach to achieve test-time scaling and strong reasoning performance. First, we curate a small dataset s1K of 1,000 ques …

## Claims

> [!note] CLAIM — inference-tts
> Budget forcing (s1: append 'Wait' to extend thinking) gave s1-32B up to +27% on MATH/AIME24, but it FAILS at small scale: with R1-Distill-Qwen-1.5B, forcing thinking from ~17K to ~25K tokens makes accuracy steadily DECLINE, and distilled small models hallucinate/repeat (content loops, over-reflection, no final answer) during long thinking.
>
> **Numbers:** s1-32B +27% AIME/MATH; R1-distill-1.5B accuracy drops as tokens 17K->25K
> **Relevance:** Budget forcing is a large-model trick; a 500M Kazakh model should not rely on forced long CoT. Prefer short-CoT + best-of-N/self-consistency.
> **Source:** arXiv:2501.19393 (s1); arXiv:2507.14419 'It's Not That Simple'; arXiv:2506.11274 · **Sweep:** `slm-architecture-2026-07`

## Related
- [[mobilellm-r1-exploring-the-limits-of-sub-billion-language-model-reasoners-with|MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Train…]] — s1 budget forcing collapses on 1.5B distills; MobileLLM-R1 probes whether sub-billion reasoning is trainable at all

[[Home]]
