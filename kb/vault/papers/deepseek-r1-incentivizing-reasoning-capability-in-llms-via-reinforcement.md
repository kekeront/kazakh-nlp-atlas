---
kb_id: "arxiv:2501.12948"
type: "paper"
title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
arxiv_id: "2501.12948"
doi: null
hf_repo: null
year: 2025
topics: ["deepseek-tech", "inference-tts"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning", "arXiv:2501.12948", "arxiv:2501.12948"]
tags: ["paper", "topic/deepseek-tech", "topic/inference-tts"]
---
# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

[arXiv](https://arxiv.org/abs/2501.12948)
**Topics:** [[deepseek-tech]], [[inference-tts]]

> [!abstract]
> General reasoning represents a long-standing and formidable challenge in artificial intelligence. Recent breakthroughs, exemplified by large language models (LLMs) and chain-of-thought prompting, have achieved considerable success on foundational reasoning tasks. However, this success is heavily contingent upon extensive human-annotated demonstrations, and models' capabilities are still insufficie …

## Claims

> [!note] CLAIM — deepseek-tech
> R1-style reasoning distillation: DeepSeek-R1-Distill-Qwen-1.5B was SFT-distilled from R1 on 800K samples (600K reasoning CoT + 200K general), initialized from Qwen2.5-Math-1.5B, reaching AIME 28.9% and MATH 83.9% - beating GPT-4o/Claude-3.5 on math. The smallest official distill is 1.5B; no 500M distill was released, and gains depend on a strong same-family base and abundant CoT data.
>
> **Numbers:** 800K samples (600K reason+200K gen); 1.5B: AIME 28.9%, MATH 83.9%; smallest distill=1.5B
> **Relevance:** Reasoning distillation is a real lever but (a) validated at 1.5B not 500M and (b) needs Kazakh CoT data that barely exists. Treat as a stretch post-training step (translate/synthesize Kazakh CoT), not a core architecture bet for KazMMLU.
> **Source:** arXiv:2501.12948 (DeepSeek-R1) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — inference-tts
> Reasoning distillation to 1.5B works when the base is domain-matched: DeepSeek-R1-Distill-Qwen-1.5B (built on Qwen2.5-Math-1.5B) hits 83.9% MATH-500 and 28.9% AIME24 from 800K R1-generated CoT traces — beating GPT-4o/Claude-3.5 on math, at ~1.1GB.
>
> **Numbers:** 1.5B distill: 83.9% MATH-500, 28.9% AIME24; 800K traces; ~1.1GB
> **Relevance:** If reasoning is a target, distill R1-style CoT (translated to Kazakh) onto a knowledge/math-specialized Kazakh base rather than expecting reasoning to emerge from 9-10B pretraining tokens alone.
> **Source:** arXiv:2501.12948 (DeepSeek-R1); HF deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B · **Sweep:** `slm-architecture-2026-07`

## Related
- [[mobilellm-r1-exploring-the-limits-of-sub-billion-language-model-reasoners-with|MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Train…]] — Both push reasoning below R1's 1.5B distill floor; MobileLLM-R1 tests sub-billion reasoning the R1 distills never reached
- [[strong-teacher-not-needed-on-distillation-in-llm-pretraining|Strong Teacher Not Needed? On Distillation in LLM Pretraining]] — DeepSeek-R1 distillation assumes a very strong teacher; this node shows stronger teachers can saturate or reverse gains

[[Home]]
