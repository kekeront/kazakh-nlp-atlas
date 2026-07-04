---
kb_id: "arxiv:2407.05841"
type: "paper"
title: "An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language Models"
arxiv_id: "2407.05841"
doi: null
hf_repo: null
year: 2024
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language Models", "arXiv:2407.05841", "arxiv:2407.05841"]
tags: ["paper", "topic/continual-pt-lowres-qlora-vs-full-cpt-re"]
---
# An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language Models

[arXiv](https://arxiv.org/abs/2407.05841)
**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]]

> [!abstract]
> Language Models (LMs) excel in natural language processing tasks for English but show reduced performance in most other languages. This problem is commonly tackled by continually pre-training and fine-tuning these models for said languages. A significant issue in this process is the limited vocabulary coverage in the original model's tokenizer, leading to inadequate representation of new languages …

## Claims

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested] Embedding-init choice for new vocab largely washes out after brief CPT: with 500M tokens/language of continued pretraining, sophisticated inits (CW2V, OFA) and simple ones (multivariate Gaussian, mean) converge — 'CW2V quickly converges with OFA within less than 4 checkpoints'. Init only matters at zero/low CPT budget (LLaMA-2-7B before CPT: CW2V 17.0/27.3 CHRF En→X/X→En vs OFA 11.2/16.2). FOCUS/WECHSEL not directly compared. Corroborated by arXiv:2406.14670: 'the simplest embedding initialization works well across various experimental settings'.
>
> **Numbers:** CPT budget 2.5B tokens (500M/lang + 500M en); pre-CPT gap CW2V 17.0 vs OFA 11.2 CHRF; convergence <4 checkpoints
> **Relevance:** The lab can use plain subword-mean init (Hewitt-style) instead of replicating Sherkala's OpenAI-embedding WECHSEL pipeline — zero API cost, same post-CPT quality, given ≥0.5B Kazakh tokens will follow.
> **Source:** arXiv:2407.05841 (Empirical Comparison of Vocabulary Expansion and Initialization Approaches), HTML; arXiv:2406.14670 abstract · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[efficient-and-effective-vocabulary-expansion-towards-multilingual-large|Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models]] — Both study vocab-expansion init; EEVE's staged freezing needs untied embeddings (breaks 0.6B cap) where the empirical study just compares…
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Settin…]] — Sherkala's WECHSEL top-5 embedding init is one vocab-expansion initialization method empirically compared in this study
- [[training-free-tokenizer-transplantation-via-orthogonal-matching-pursuit|Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit]] — OMP benchmarks against the WECHSEL/FOCUS init this paper surveys — OMP 99.1% vs FOCUS 73.4% vs WECHSEL 63.0% MMLU

[[Home]]
