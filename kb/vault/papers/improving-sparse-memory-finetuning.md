---
kb_id: "arxiv:2604.05248"
type: "paper"
title: "Improving Sparse Memory Finetuning"
arxiv_id: "2604.05248"
doi: null
hf_repo: null
year: 2026
topics: ["post-hoc-attachment-of-engram-style-cond"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Improving Sparse Memory Finetuning", "arXiv:2604.05248", "arxiv:2604.05248"]
tags: ["paper", "topic/post-hoc-attachment-of-engram-style-cond"]
---
# Improving Sparse Memory Finetuning

[arXiv](https://arxiv.org/abs/2604.05248)
**Topics:** [[post-hoc-attachment-of-engram-style-cond]]

> [!abstract]
> Large Language Models (LLMs) are typically static after training, yet real-world applications require continual adaptation to new knowledge without degrading existing capabilities. Standard approaches to updating models, like full finetuning or parameter-efficient methods (e.g., LoRA), face a fundamental trade-off: catastrophic forgetting. They modify shared dense representations, causing interfer …

## Claims

> [!note] CLAIM — post-hoc-attachment-of-engram-style-cond
> [transferable-untested] The attachment loss-spike is real and documented, and memory-only 'healing' fixes it cheaply: the companion retrofit-pipeline paper states verbatim that after replacing FFN layers {8,12,16} of Qwen2.5-0.5B-Instruct with random-init memory, 'Immediately after replacement, model behavior degrades because the forward computation has changed... This drastic change initially degrades model perplexity, necessitating a recovery phase.' Recovery = finetune ONLY new memory params on ~20,000 OpenAssistant (oasst1) samples; validation loss recovers ~2.3 -> ~2.1 and plateaus within ~1,000 steps (batch not >16). After healing, sparse memory finetuning learns TriviaQA rapidly (strong F1 within a few hundred steps) while full finetuning barely moves on-target and monotonically degrades GSM8K loss.
>
> **Numbers:** Healing: 20k oasst1 samples (Sec 3.3; Sec 4.1 says 10k — internal inconsistency), val loss ~2.3 -> ~2.1 in ~1,000 steps, memory-only training; Stage-3 TriviaQA 1k samples; forgetting probes GSM8K loss + NaturalQuestions F1
> **Relevance:** Predicts and bounds the failure mode for QymyzLM's Engram attach on Kaggle T4: expect an immediate perplexity spike, and budget a short memory-only healing phase (thousands of samples, not billions of tokens) before joint QLoRA-CPT. Note this paper used the destructive replacement mode; additive alpha=0.01 (finding 2) largely avoids the spike.
> **Source:** arXiv:2604.05248v1 (Improving Sparse Memory Finetuning, UMich, Apr 6 2026), Sec. 3.3 + Fig. 2/4/5; PDF saved at [fetched PDF] · **Sweep:** `slm-arch-for-kazakh`

[[Home]]
