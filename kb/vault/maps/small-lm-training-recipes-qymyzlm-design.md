---
type: "moc"
topic: "small-lm-training-recipes-qymyzlm-design"
nodes: 11
papers: 11
sources: 0
uncertain_claims: 6
tags: ["moc"]
---
# Topic: small-lm-training-recipes-qymyzlm-design

The recipe frontier for a ≤600M Kazakh SLM is now sharply forked into two costed paths. CONFIRMED convergence exists for from-scratch HPs at 350-500M: warmup ~2000 steps (4/4 modern recipes), peak LR in the 3e-3 (DCLM-412M, SmolLM2-360M) to 4e-3 (MobileLLM-R1) band, WD 0.033-0.1, single-stage high-quality data, and a 4-way-convergent fp16 stability stack (QK-norm + z-loss 1e-4 + RMSNorm/reordered-norm, per OLMo2/DCLM/Qwen3/MobileLLM-R1). DCLM 400M-1x (412M/8.2B tok) is the closest fully-specified analog. The decisive constraint is compute: re-derived at 3e19 FLOPs, a from-scratch pass needs 256-650 T4x2 wall-hours (~8+ weeks of Kaggle's 30 GPU-h/week) versus QLoRA/CPT of Qwen3-0.6B being 1-2 orders cheaper — but LoRA-in-CPT underperforms full FT ~5x on data-efficiency (Biderman: HumanEval LoRA-r256@20B 0.224 vs full 0.263), and Kazakh is a larger distribution shift than code/math. Contested: muP's value at single scale (2510.19093 argues weight decay, not muP, drives LR transfer), whether Muon's ~52%-of-AdamW-FLOPs win survives fp16 Newton-Schulz on T4 (unvalidated anywhere), and teacher strength for distillation (Strong-Teacher-Not-Needed: same-size/weak teachers help, stronger ones can reverse gains). Open question: can a QLoRA/CPT path on Qwen3-0.6B (already 32.8% KazMMLU) clear the ≥36% design bar without paying the from-scratch compute, given LoRA's learning deficit.

## Frontier highlights
- [[datacomp-lm-in-search-of-the-next-generation-of-training-sets-for-language|DataComp-LM: In search of the next generation of training sets for language mode…]] — DCLM 400M-1x (412M/8.2B tok) — the closest fully-specified published analog to a 500M/10B Kazakh run
- [[scaling-data-constrained-language-models|Scaling Data-Constrained Language Models]] — Data-constrained law (≤4 epochs≈fresh) + re-derived T4 feasibility: from-scratch = 256-650 wall-hours vs CPT 1-2 orders cheaper
- [[qwen3-technical-report|Qwen3 Technical Report]] — Qwen3-0.6B — the frozen CPT backbone at 32.8% KazMMLU, already carries QK-Norm fp16 safeguard
- [[lora-learns-less-and-forgets-less|LoRA Learns Less and Forgets Less]] — LoRA in CPT underperforms full FT ~5x on data-efficiency; risk worse for a big Kazakh distribution shift
- [[2-olmo-2-furious|2 OLMo 2 Furious]] — OLMo2 fp16-only stability stack (QK-norm+z-loss 1e-4+reordered RMSNorm) — the T4 no-bf16 recipe
- [[mobilellm-r1-exploring-the-limits-of-sub-billion-language-model-reasoners-with|MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with…]] — MobileLLM-R1: full open recipe, LR 4e-3, matches Qwen3-0.6B reasoning on 11.7% of tokens but loses on knowledge

## Papers (11)
- [[strong-teacher-not-needed-on-distillation-in-llm-pretraining|Strong Teacher Not Needed? On Distillation in LLM Pretraining]] (2026) — training-recipes
- [[smollm2-when-smol-goes-big-data-centric-training-of-a-small-language-model|SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model]] (2025) — sota-slm
- [[muon-is-scalable-for-llm-training|Muon is Scalable for LLM Training]] (2025) — small-lm-training-recipes-qymyzlm-design
- [[don-t-be-lazy-completep-enables-compute-efficient-deep-transformers|Don't be lazy: CompleteP enables compute-efficient deep transformers]] (2025) — residual-stream-stability-qymyzlm-design
- [[qwen3-technical-report|Qwen3 Technical Report]] (2025) — sota-slm
- [[mobilellm-r1-exploring-the-limits-of-sub-billion-language-model-reasoners-with|MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipe…]] (2025) — training-recipes
- [[lora-learns-less-and-forgets-less|LoRA Learns Less and Forgets Less]] (2024) — continual-pt-lowres-qlora-vs-full-cpt-re
- [[datacomp-lm-in-search-of-the-next-generation-of-training-sets-for-language|DataComp-LM: In search of the next generation of training sets for language models]] (2024) — small-lm-training-recipes-qymyzlm-design
- [[2-olmo-2-furious|2 OLMo 2 Furious]] (2024) — residual-stream-stability-qymyzlm-design
- [[scaling-data-constrained-language-models|Scaling Data-Constrained Language Models]] (2023) — training-recipes
- [[small-scale-proxies-for-large-scale-transformer-training-instabilities|Small-scale proxies for large-scale Transformer training instabilities]] (2023) — attention-kv-architecture-sub-1b

## Related topics
- [[training-recipes]] — 5 shared nodes
- [[residual-stream-stability-qymyzlm-design]] — 3 shared nodes
- [[attention-kv-architecture-sub-1b]] — 2 shared nodes
- [[sota-slm]] — 2 shared nodes

[[Home]]
