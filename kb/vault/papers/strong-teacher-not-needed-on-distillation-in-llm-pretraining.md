---
kb_id: "arxiv:2605.23857"
type: "paper"
title: "Strong Teacher Not Needed? On Distillation in LLM Pretraining"
arxiv_id: "2605.23857"
doi: null
hf_repo: null
year: 2026
topics: ["training-recipes", "small-lm-training-recipes-qymyzlm-design"]
claims: 2
uncertain_claims: 1
verdicts: []
aliases: ["Strong Teacher Not Needed? On Distillation in LLM Pretraining", "arXiv:2605.23857", "arxiv:2605.23857"]
tags: ["paper", "topic/training-recipes", "topic/small-lm-training-recipes-qymyzlm-design"]
---
# Strong Teacher Not Needed? On Distillation in LLM Pretraining

[arXiv](https://arxiv.org/abs/2605.23857)
**Topics:** [[training-recipes]], [[small-lm-training-recipes-qymyzlm-design]]

> [!abstract]
> Knowledge distillation generally assumes a strong-to-weak relationship where stronger teachers yield better students. In this work, we examine this assumption about distillation in large language model pretraining. By varying architecture sizes and training token budgets, we create strong-to-weak, same-level, and weak-to-strong teacher-student relationships, and study distillation's effectiveness …

## Claims

> [!warning] UNCERTAIN — training-recipes
> 'Strong Teacher Not Needed' finds a stronger teacher is NOT always better in pretraining distillation: pushing the teacher to more params or more training tokens can saturate or even reverse the distillation gain, while even small/undertrained teachers improve larger students when the LM loss and KD loss are properly mixed. Distillation improves OOD/downstream generalization more readily than in-domain fitting.
>
> **Numbers:** non-monotonic teacher-quality effect; small/undertrained teachers still help; KD helps OOD>in-domain (exact optimal size-ratio not verifiable from available text)
> **Relevance:** De-risks teacher choice for Kazakh: a modestly-sized Kazakh-fluent teacher (e.g. Sherkala-8B) can beat a giant non-Kazakh one. Don't over-invest in the largest teacher; prioritize the teacher's Kazakh competence and mix KD with the LM loss.
> **Source:** arXiv 2605.23857 Strong Teacher Not Needed? On Distillation in LLM Pretraining (Lu & Liu) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] Distillation-vs-pure-next-token at pretraining, systematic study (Princeton, 2026): with LM/KD loss mixing coefficient alpha searched over {0.2,0.4,0.5,0.6,0.8,1.0}, even WEAK and SAME-SIZE teachers improve students — a 0.7B teacher trained on only 30B tokens still gives +1.3% downstream accuracy to a 1.7B student trained on 50B tokens. Stronger teachers saturate or REVERSE gains (8.0B teacher optimal alpha across 10/30/50/80/100/300B teacher tokens: 0.4,0.6,0.8,1.0,1.0,0.8 — non-monotone). Weaker teachers demand lower alpha (more ground-truth loss); pure KD (alpha=1.0) underperforms mixed loss for weak teachers. Findings replicate across student sizes 0.7B-8.0B (Table 3); gains show up in OOD/downstream more than in-domain ppl. Setup: Llama3-family, GQA 4:1, vocab 128,256, teachers 0.7B/1.7B/3.8B/8.0B x {10..300B} tokens.
>
> **Numbers:** alpha grid {0.2..1.0}; 0.7B@30B-tok teacher -> +1.3% downstream on 1.7B@50B student; 24 teacher configs; students 0.7B-8.0B
> **Relevance:** Kazakh has NO strong teacher — this is the license to distill anyway: e.g., an early CPT checkpoint or same-size Kazakh model as teacher with low alpha (0.2-0.5) during from-scratch pretraining. Directly actionable and never tested on any low-resource language.
> **Source:** arXiv:2605.23857 (Strong Teacher Not Needed? On Distillation in LLM Pretraining), read from PDF · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compressio…]] — X-EcoMLA finds bigger same-tokenizer teacher unlocks deeper lossless compression; 'Strong Teacher Not Needed' contests teacher-strength…
- [[deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement|DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]] — DeepSeek-R1 distillation assumes a very strong teacher; this node shows stronger teachers can saturate or reverse gains
- [[universal-cross-tokenizer-distillation-via-approximate-likelihood-matching|Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching]] — Both on KD; cross-tokenizer distillation enables teacher/student across vocabularies, complementing the weak-teacher-suffices finding

[[Home]]
