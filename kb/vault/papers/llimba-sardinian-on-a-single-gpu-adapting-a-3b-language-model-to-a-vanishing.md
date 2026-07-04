---
kb_id: "arxiv:2605.09015"
type: "paper"
title: "LLiMba: Sardinian on a Single GPU -- Adapting a 3B Language Model to a Vanishing Romance Language"
arxiv_id: "2605.09015"
doi: null
hf_repo: null
year: 2026
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["LLiMba: Sardinian on a Single GPU -- Adapting a 3B Language Model to a Vanishing Romance Language", "arXiv:2605.09015", "arxiv:2605.09015"]
tags: ["paper", "topic/continual-pt-lowres-qlora-vs-full-cpt-re"]
---
# LLiMba: Sardinian on a Single GPU -- Adapting a 3B Language Model to a Vanishing Romance Language

[arXiv](https://arxiv.org/abs/2605.09015)
**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]]

> [!abstract]
> Sardinian, a Romance language with roughly one million speakers, has minimal presence in modern NLP. Commercial services do not support it, and current language models do not produce it reliably. We present LLiMba, a 3B parameter Sardinian-ready model adapted from Qwen2.5-3B-Instruct through continued pretraining (CPT) and supervised fine-tuning (SFT) on a single 24 GB consumer GPU. The corpus con …

## Claims

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested, single-GPU regime] LLiMba (2026): Qwen2.5-3B-Instruct adapted to Sardinian on ONE 24GB consumer GPU with only 11.5M target-language tokens + 2.4M related-Romance tokens (CPT → ppl 6.76), then SFT comparison: rsLoRA r=256 reached 28.5 BLEU (En→Sardinian) vs full fine-tuning 21.0 and CPT-only 17.3; conclusion 'adapter capacity matters more than the choice among LoRA variants'. Note this is the extreme-low-data regime where full FT overfits — opposite conclusion to the 20B-token CPT regime of arXiv:2405.09673.
>
> **Numbers:** 11.5M+2.4M tokens; 24GB GPU; rsLoRA-r256 28.5 BLEU vs full-FT 21.0 vs CPT 17.3; CPT ppl 6.76
> **Relevance:** Maps the LoRA-vs-full crossover: with ≥1B tokens (lab's case) full CPT wins; below ~100M tokens high-rank LoRA wins. Also proof that meaningful adaptation runs fit consumer/Kaggle GPUs.
> **Source:** arXiv:2605.09015 (LLiMba) · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[lora-learns-less-and-forgets-less]]

[[Home]]
