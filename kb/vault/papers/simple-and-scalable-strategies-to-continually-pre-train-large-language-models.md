---
kb_id: "arxiv:2403.08763"
type: "paper"
title: "Simple and Scalable Strategies to Continually Pre-train Large Language Models"
arxiv_id: "2403.08763"
doi: null
hf_repo: null
year: 2024
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Simple and Scalable Strategies to Continually Pre-train Large Language Models", "arXiv:2403.08763", "arxiv:2403.08763"]
tags: ["paper", "topic/continual-pt-lowres-qlora-vs-full-cpt-re"]
---
# Simple and Scalable Strategies to Continually Pre-train Large Language Models

[arXiv](https://arxiv.org/abs/2403.08763)
**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]]

> [!abstract]
> Large language models (LLMs) are routinely pre-trained on billions of tokens, only to start the process over again once new data becomes available. A much more efficient solution is to continually pre-train these models, saving significant compute compared to re-training. However, the distribution shift induced by new data typically results in degraded performance on previous data or poor adaptati …

## Claims

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested] Canonical replay/LR recipe (405M + 10B models, TMLR 2024): LR re-warming + re-decaying + replay matches full re-training on the union of datasets. Replay dose: 5% for weak shift (Pile→SlimPajama), 25% for strong shift (English→German ≈ the Kazakh case). Adopted at scale: Zamba used 60% replay in a 50B-token decay phase; DeepSeek-V2 used 30% replay + a non-decayed checkpoint for 6T-token CPT. Paper also proposes 'infinite' (constant-plus-final-decay) schedules to avoid committing to a token budget and to skip re-warming between phases.
>
> **Numbers:** 5% weak / 25% strong shift; adopters 30% (DeepSeek-V2, 6T) and 60% (Zamba, 50B decay); models 405M & 10B
> **Relevance:** Sets the en/ru replay floor for the ~10B-token Kazakh CPT plan: Kazakh→ru/en is a strong shift, so ≥25% replay; the infinite-schedule option fits interruptible Kaggle sessions.
> **Source:** arXiv:2403.08763 (Ibrahim et al., Simple and Scalable Strategies to Continually Pre-train LLMs) — exact percentages verified in PDF text (lines re: '5% replay for SlimPajama and 25% replay for German') · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model|DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model]] — DeepSeek-V2 scales Ibrahim's replay recipe: 30% replay + non-decayed checkpoint for 6T-token CPT
- [[the-zamba2-suite-technical-report|The Zamba2 Suite: Technical Report]] — Zamba2 adopts 60% replay in a 50B-token decay phase — high-dose instance of Ibrahim's replay finding
- [[small-languages-big-models-a-study-of-continual-training-on-languages-of-norway|Small Languages, Big Models: A Study of Continual Training on Languages of Norway]] — NorMistral's 3-stage tokenizer-swap + realign + full CPT instantiates the general continual-pretraining recipe this formalizes
- [[continually-adding-new-languages-to-multilingual-language-models|Continually Adding New Languages to Multilingual Language Models]] — LayRA is the no-replay alternative to the replay + LR-rewarming standard continual-PT baseline this establishes
- [[derived-from-lab-measurement-t4bench2-py-t4bench3-py-kaggle|Derived from lab measurement (t4bench2.py/t4bench3.py) + Kaggle quota…]] — budget bounds the CPT recipe this paper recommends; 20-25B tok-seen exceeds the Kaggle quota by ~40-80x

[[Home]]
