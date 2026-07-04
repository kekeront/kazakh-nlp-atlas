---
kb_id: "arxiv:2406.11477"
type: "paper"
title: "How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Target Language Text?"
arxiv_id: "2406.11477"
doi: null
hf_repo: null
year: 2024
topics: ["qymyzlm-architecture-fork"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Target Language Text?", "arXiv:2406.11477", "arxiv:2406.11477"]
tags: ["paper", "topic/qymyzlm-architecture-fork"]
---
# How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Target Language Text?

[arXiv](https://arxiv.org/abs/2406.11477)
**Topics:** [[qymyzlm-architecture-fork]]

> [!abstract]
> Large language models (LLMs) have shown remarkable capabilities in many languages beyond English. Yet, LLMs require more inference steps when generating non-English text due to their reliance on English-centric tokenizers and vocabulary, resulting in higher usage costs to non-English speakers. Vocabulary expansion with target language tokens is a widely used cross-lingual vocabulary adaptation app …

## Claims

> [!note] CLAIM — qymyzlm-architecture-fork
> [transferable-untested (10 languages, no Turkic)] Plain (non-staged) vocabulary EXPANSION on TIED embeddings is published and works: Yamaguchi et al. expand Gemma2-9B (tie_word_embeddings=true, 256K vocab) explicitly preserving the source weight-tying config (their footnote 3: 'We follow the original configuration of the source model regarding weight tying'), with heuristic init (Mean/Align) + LAPT, and get competitive generation performance and up to 1.57x speedup. So it is NOT expansion that requires untying — only EEVE-style STAGED freezing does. Same paper: at extreme low data (30K sentences, <=5M tokens) full vocabulary REPLACEMENT (32K target vocab, Gemma2) catastrophically fails: best replacement init (Mean) 34 pts on Telugu MC vs Source 74 and expansion-Align 60; Random/FOCUS near-zero MT. Expansion also costs source-language knowledge: English MC/MMLU drops avg 5.3 pts (Gemma2) to 18.7 pts (Llama3) vs <=2 pts for CPT-only.
>
> **Numbers:** Gemma2-9B tied expansion: speedups 1.07-1.57x, competitive MT/SUM; replacement @<=5M tokens: Telugu MC 34 (repl-Mean) vs 74 (Source) vs 60 (expansion-Align); forgetting: −5.3 (Gemma2) / −10 (Llama2) / −18.7 (Llama3) pts English vs <=2 for CPT-only; |V_new|=100-5K, 30K sentences
> **Relevance:** Answers sub-question 2: staged expansion is unnecessary, joint tied expansion is precedented — but on Qwen3-0.6B expansion of +30K tokens makes the tied table 181,936x1024 = 186.3M, total ~627M, BREAKING the 600M cap, and untying adds +155.6M (total ~752M). So expansion is cap-infeasible regardless of tying mechanics; and full swap must NOT be attempted at <1B-token pilot scale (replacement failure regime).
> **Source:** Yamaguchi, Villavicencio, Aletras, arXiv:2406.11477v3 (Computational Linguistics 2025), Sec 3 fn.3, Tables 6, 9, 11 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[efficient-and-effective-vocabulary-expansion-towards-multilingual-large|Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models]] — Both parameter-efficient vocab-expansion recipes for new languages; EEVE staged-freeze vs 0.01GB-target expansion
- [[universal-cross-tokenizer-distillation-via-approximate-likelihood-matching|Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching]] — Yamaguchi finds low-data full replacement catastrophically fails; ALM cross-tokenizer distillation offers a training-signal route to…

[[Home]]
