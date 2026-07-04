---
type: "moc"
topic: "training-recipes"
nodes: 16
papers: 15
sources: 1
uncertain_claims: 5
tags: ["moc"]
---
# Topic: training-recipes

The frontier is anchored by one proven Kazakh recipe: Sherkala-8B reached KazMMLU 41.4% (chat) / 51.6% (base) by continual-pretraining Llama-3.1-8B on a 45.3B-token 3:1:3 Kazakh:(Ru+Tr):English mix with a +25% WECHSEL-initialized vocab extension — and the field-wide prior is unambiguous: every published Kazakh SOTA is an adaptation, none from-scratch. For QymyzLM's CPT backbone, Qwen3-0.6B is extreme deployment overtraining (~60k tok/param, QK-Norm for fp16 stability), which is a double-edged foundation given that reused overtrained models are argued to saturate. Established levers: WSD scheduling with anneal-phase high-quality-data injection (MiniCPM ~192 tok/param; SmolLM2 single-stage LR 3e-3 @360M), directly-fitted LR/batch formulas from Step Law that make an explicit muP sweep largely avoidable, the data-constrained ≤4-epoch repetition law (binding on Kazakh's 9-10B corpus → ≤40B useful tokens), and knowledge distillation where MobileLLM-R1 matches Qwen3-0.6B on reasoning with 11.7% of the tokens and finds SFT>RL at sub-1B. The contested/uncertain edge: whether a strong teacher even helps (Strong Teacher Not Needed reports non-monotone, sometimes-reversing gains; uncertain), translationese risk in Sherkala's 24%-synthetic-MT Kazakh, and forgetting mitigation without replay (LayRA layer-selective LoRA). Open question: given a from-scratch Chinchilla run is a multi-month Kaggle-T4 commitment (~256-650 wall-hours), is QLoRA/full CPT on Qwen3-0.6B the only feasible path, and does overtraining-saturation undercut it?

## Frontier highlights
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resour…]] — The proven Kazakh recipe: continual-PT Llama-3.1-8B, 45.3B 3:1:3 mix, +25% vocab → 41.4/51.6 KazMMLU ceiling
- [[qwen3-technical-report|Qwen3 Technical Report]] — QymyzLM's CPT backbone: Qwen3-0.6B, 36T tok (~60k/param), QK-Norm carries the fp16 stability safeguard
- [[mobilellm-r1-exploring-the-limits-of-sub-billion-language-model-reasoners-with|MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with…]] — MobileLLM-R1 matches Qwen3-0.6B reasoning on 11.7% of tokens; SFT>RL sub-1B, KD from Llama-3.1-8B
- [[scaling-data-constrained-language-models|Scaling Data-Constrained Language Models]] — Data-constrained law: ≤4 epochs ≈ fresh data; binds Kazakh's ~10B corpus to ≤40B useful tokens
- [[predictable-scale-part-i-step-law-optimal-hyperparameter-scaling-law-in-large|Predictable Scale: Part I, Step Law -- Optimal Hyperparameter Scaling Law in Lar…]] — Step Law's fitted eta/batch formulas give ready HPs (~2e-3, ~0.4M tok @350M/20B), skipping a muP sweep
- [[strong-teacher-not-needed-on-distillation-in-llm-pretraining|Strong Teacher Not Needed? On Distillation in LLM Pretraining]] — Contests distillation dogma: stronger teachers can saturate/reverse gains; weak same-size teachers still help [uncertain]

## Papers (15)
- [[strong-teacher-not-needed-on-distillation-in-llm-pretraining|Strong Teacher Not Needed? On Distillation in LLM Pretraining]] (2026) — training-recipes
- [[smollm2-when-smol-goes-big-data-centric-training-of-a-small-language-model|SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model]] (2025) — sota-slm
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting]] (2025) — tokenizer-morphology
- [[predictable-scale-part-i-step-law-optimal-hyperparameter-scaling-law-in-large|Predictable Scale: Part I, Step Law -- Optimal Hyperparameter Scaling Law in Large Language Model Pr…]] (2025) — training-recipes
- [[gemma-3-technical-report|Gemma 3 Technical Report]] (2025) — sota-slm
- [[qwen3-technical-report|Qwen3 Technical Report]] (2025) — sota-slm
- [[continually-adding-new-languages-to-multilingual-language-models|Continually Adding New Languages to Multilingual Language Models]] (2025) — training-recipes
- [[mobilellm-r1-exploring-the-limits-of-sub-billion-language-model-reasoners-with|MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipe…]] (2025) — training-recipes
- [[weight-decay-may-matter-more-than-mup-for-learning-rate-transfer-in-practice|Weight Decay may matter more than muP for Learning Rate Transfer in Practice]] (2025) — training-recipes
- [[minicpm-unveiling-the-potential-of-small-language-models-with-scalable-training|MiniCPM: Unveiling the Potential of Small Language Models with Scalable Training Strategies]] (2024) — training-recipes
- [[aya-expanse-combining-research-breakthroughs-for-a-new-multilingual-frontier|Aya Expanse: Combining Research Breakthroughs for a New Multilingual Frontier]] (2024) — training-recipes
- [[yulan-mini-an-open-data-efficient-language-model|YuLan-Mini: An Open Data-efficient Language Model]] (2024) — training-recipes
- [[scaling-data-constrained-language-models|Scaling Data-Constrained Language Models]] (2023) — training-recipes
- [[textbooks-are-all-you-need|Textbooks Are All You Need]] (2023) — training-recipes
- [[fp8-lm-training-fp8-large-language-models|FP8-LM: Training FP8 Large Language Models]] (2023) — training-recipes

## Sources & findings (1)
- [[general-cross-lingual-transfer-literature|General cross-lingual-transfer literature]] — Curriculum/order: starting from high-resource competence then adapting to the low-resource language exploits cross-lingu…

## Related topics
- [[small-lm-training-recipes-qymyzlm-design]] — 5 shared nodes
- [[sota-slm]] — 3 shared nodes
- [[attention-kv-architecture-sub-1b]] — 2 shared nodes

[[Home]]
