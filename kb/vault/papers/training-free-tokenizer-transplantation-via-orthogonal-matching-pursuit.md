---
kb_id: "arxiv:2506.06607"
type: "paper"
title: "Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit"
arxiv_id: "2506.06607"
doi: null
hf_repo: null
year: 2025
topics: ["architecture-fork"]
claims: 3
uncertain_claims: 1
verdicts: []
aliases: ["Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit", "arXiv:2506.06607", "arxiv:2506.06607"]
tags: ["paper", "topic/architecture-fork"]
---
# Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit

[arXiv](https://arxiv.org/abs/2506.06607)
**Topics:** [[architecture-fork]]

> [!abstract]
> We present a training-free method to transplant tokenizers in pretrained large language models (LLMs) by reconstructing unseen token embeddings via Orthogonal Matching Pursuit (OMP). Specifically, we approximate each out-of-vocabulary token as a sparse linear combination of shared tokens, in two phases: first, compute each new token's representation in the donor embedding space with a small dictio …

## Claims

> [!note] CLAIM — architecture-fork
> The from-scratch camp's core justification (a Kazakh-native tokenizer) is largely capturable by adaptation: a good training-free transplant grafts an efficient tokenizer onto a strong base near-losslessly. OMP retains 99.1% of MMLU on Qwen->Llama-1B zero-shot and recovers to 101.4% after only 2B CPT tokens; FOCUS retains just 73.4% and WECHSEL 63.0% for the same swap.
>
> **Numbers:** Qwen->Llama 1B MMLU: OMP-K64 36.4 vs 36.73 base (99.1%); after 2B-token CPT 101.4%. FOCUS 73.4%, WECHSEL 63.0%, ZeroEmbed 99.1%. (Llama->Mistral-12B: OMP 96.4%, FOCUS 35.6%.)
> **Relevance:** You can transplant a low-fertility Kazakh tokenizer onto Qwen3-0.6B-Base and keep ~all of its 32.8% starting knowledge, then CPT on 9-10B Kazakh tokens — getting BOTH the fertility win and a knowledge head-start from-scratch cannot match. Prefer OMP-style init over FOCUS/ZeTT for retention.
> **Source:** arXiv 2506.06607 (Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit), results tables · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — architecture-fork
> Critical caveat that specifically threatens KazMMLU (STEM-heavy): cross-scheme tokenizer transplants catastrophically break numeric reasoning unless digit tokenization is preserved. GSM8K collapses -78.7% (Qwen->Llama) and -73.8% (Llama->Mistral) after transplant; a same-numeric-scheme transfer (NeMo->Qwen) drops only -5.6%.
>
> **Numbers:** GSM8K: Qwen->Llama 0.0675->0.0144 (-78.7%); Llama->Mistral 0.5588->0.1463 (-73.8%); NeMo->Qwen 82.6->78.0 (-5.6%).
> **Relevance:** KazMMLU includes STEM subjects with numbers; a naive Kazakh-tokenizer swap that re-tokenizes digits could wipe out STEM accuracy. Strong argument to (a) preserve Qwen's digit/number tokenization in any transplant, or (b) run a no-swap CPT arm as the safe control.
> **Source:** arXiv 2506.06607 (OMP transplant), math/GSM8K analysis · **Sweep:** `slm-architecture-2026-07`

> [!warning] UNCERTAIN — architecture-fork
> A naive full tokenizer swap may need far more than the Kazakh budget to fully recover base parity (literature suggests re-optimizing a swapped tokenizer toward base parity can want >=50B continuation tokens), though strong init (OMP) recovers most within ~2B. With only 9-10B Kazakh tokens, a poorly-initialized swap risks spending the budget on recovery rather than Kazakh learning.
>
> **Numbers:** >=50B tokens cited for tractable full tokenizer re-optimization; OMP/FOCUS init recovers 'much' with ~2B-token CPT.
> **Relevance:** Concrete budget constraint: at 9-10B tokens either (a) keep Qwen's tokenizer and accept the ~4.7-4.9 fertility hit (knowledge fully intact, cheapest control), or (b) swap with OMP-style init + digit preservation to minimize recovery cost. A ZeTT/FOCUS swap with weak retention is the worst option under this budget.
> **Source:** Tokenizer-optimization survey (emergentmind) + arXiv 2506.06607 recovery experiments · **Sweep:** `slm-architecture-2026-07`

## Related
- [[zero-shot-tokenizer-transfer|Zero-Shot Tokenizer Transfer]] — Competing tokenizer-transfer: ZeTT hypernetwork-predicted embeddings vs OMP training-free transplantation
- [[universal-cross-tokenizer-distillation-via-approximate-likelihood-matching|Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching]] — Both attack the cross-tokenizer barrier; training-free tokenizer transplantation is an alternative to ALM's likelihood matching for…
- [[an-empirical-comparison-of-vocabulary-expansion-and-initialization-approaches|An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language…]] — OMP benchmarks against the WECHSEL/FOCUS init this paper surveys — OMP 99.1% vs FOCUS 73.4% vs WECHSEL 63.0% MMLU
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhst…]] — OMP's caveat — cross-scheme transplant collapses GSM8K -78.7% — directly threatens STEM-heavy KazMMLU numeric reasoning

[[Home]]
