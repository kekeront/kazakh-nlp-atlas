---
kb_id: "arxiv:2405.09673"
type: "paper"
title: "LoRA Learns Less and Forgets Less"
arxiv_id: "2405.09673"
doi: null
hf_repo: null
year: 2024
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re", "small-lm-training-recipes-qymyzlm-design"]
claims: 2
uncertain_claims: 1
verdicts: []
aliases: ["LoRA Learns Less and Forgets Less", "arXiv:2405.09673", "arxiv:2405.09673"]
tags: ["paper", "topic/continual-pt-lowres-qlora-vs-full-cpt-re", "topic/small-lm-training-recipes-qymyzlm-design"]
---
# LoRA Learns Less and Forgets Less

[arXiv](https://arxiv.org/abs/2405.09673)
**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]], [[small-lm-training-recipes-qymyzlm-design]]

> [!abstract]
> Low-Rank Adaptation (LoRA) is a widely-used parameter-efficient finetuning method for large language models. LoRA saves memory by training only low rank perturbations to selected weight matrices. In this work, we compare the performance of LoRA and full finetuning on two target domains, programming and mathematics. We consider both the instruction finetuning (approximately 100K prompt-response pai …

## Claims

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested] In the CPT regime LoRA substantially underperforms full fine-tuning: on Llama-2-7B code CPT (StarCoder-Python), best LoRA (r=256) at 20B tokens reaches HumanEval 0.224 ≈ full fine-tuning with only 4B tokens (0.218); full FT at 20B = 0.263. Math CPT (OpenWebMath): LoRA r=256 GSM8K 0.203 vs full FT 0.293. Forgetting (source-domain avg, higher=better): LoRA r=256 0.617 vs full FT 0.545 at 20B code tokens — LoRA forgets less but learns ~5x less data-efficiently.
>
> **Numbers:** HumanEval: LoRA-r256@20B 0.224 vs full@20B 0.263 vs full@4B 0.218; GSM8K: 0.203 vs 0.293; forgetting 0.617 vs 0.545
> **Relevance:** Quantifies the QLoRA-CPT quality tax: with ~10B Kazakh tokens, LoRA-CPT would deliver roughly what full CPT gets from ~2B tokens. If QLoRA is kept for T4 memory reasons, rank must be ≥256 on all linear layers.
> **Source:** arXiv:2405.09673 (LoRA Learns Less and Forgets Less, TMLR 2024), Tables S1–S4 via arxiv HTML v2 · **Sweep:** `slm-arch-for-kazakh`

> [!warning] UNCERTAIN — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] LoRA vs full fine-tuning for continued pretraining (Biderman et al.): in the CPT regime (20B unstructured tokens, code+math domains), standard low-rank LoRA substantially underperforms full finetuning; full FT learns weight perturbations of rank 10-100x typical LoRA configs. LoRA's advantage is forgetting mitigation (better retention of base-model capabilities than full FT even with regularization). Language acquisition (Kazakh) is a larger distribution shift than code/math — the underperformance risk is at least as bad.
>
> **Numbers:** CPT setting = 20B tokens; full-FT perturbation rank 10-100x LoRA rank; exact score gaps not extracted
> **Relevance:** Direct challenge to the lab's QLoRA-CPT plan: for Kazakh CPT on Qwen3-0.6B, QLoRA will likely leave points on the table vs full FT. Counter-consideration: LoRA's forgetting resistance protects ru/en ability needed for kk/ru code-switching. Never tested on Kazakh — this is a cheap, high-value lab experiment (0.6B full-FT is feasible on T4x2, see recommendations).
> **Source:** arXiv:2405.09673 (LoRA Learns Less and Forgets Less), abstract-level verification this sweep · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[small-languages-big-models-a-study-of-continual-training-on-languages-of-norway|Small Languages, Big Models: A Study of Continual Training on Languages of Norway]] — Both study continual pretraining for a new language; direct LoRA-vs-full evidence for the Kazakh CPT path
- [[sparse-memory-finetuning-as-a-low-forgetting-alternative-to-lora-and-full|Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetuning]] — Both frame the learn-vs-forget tradeoff; SMF positions itself as low-forgetting alternative to LoRA AND full-FT
- [[continual-learning-via-sparse-memory-finetuning|Continual Learning via Sparse Memory Finetuning]] — both frame method choice around forgetting; A's sparse-mem NQ F1 -11% directly beats B's 'LoRA forgets less' claim (-71%)
- [[hydra-unifying-document-retrieval-and-generation-in-a-single-vision-language|Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model]] — Hydra's frozen-base + r=32 LoRA retrieval mode banks on exactly the 'LoRA forgets less' property this paper quantifies
- [[lab-measurement-peak-vram-standard-adam-state-arithmetic-2|Lab measurement (peak VRAM) + standard Adam state arithmetic (2+2+4+4+…]] — VRAM says QLoRA has no rationale at 0.6B so full-FT dominates; LoRA-Learns-Less confirms LoRA underperforms full-FT

[[Home]]
