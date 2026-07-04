---
kb_id: "arxiv:2405.07883"
type: "paper"
title: "Zero-Shot Tokenizer Transfer"
arxiv_id: "2405.07883"
doi: null
hf_repo: null
year: 2024
topics: ["tokenizer-morphology", "continual-pt-lowres-qlora-vs-full-cpt-re"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["Zero-Shot Tokenizer Transfer", "arXiv:2405.07883", "arxiv:2405.07883"]
tags: ["paper", "topic/tokenizer-morphology", "topic/continual-pt-lowres-qlora-vs-full-cpt-re"]
---
# Zero-Shot Tokenizer Transfer

[arXiv](https://arxiv.org/abs/2405.07883)
**Topics:** [[tokenizer-morphology]], [[continual-pt-lowres-qlora-vs-full-cpt-re]]

> [!abstract]
> Language models (LMs) are bound to their tokenizer, which maps raw text to a sequence of vocabulary items (tokens). This restricts their flexibility: for example, LMs trained primarily on English may still perform well in other natural and programming languages, but have vastly decreased efficiency due to their English-centric tokenizer. To mitigate this, we should be able to swap the original LM …

## Claims

> [!note] CLAIM — tokenizer-morphology
> Zero-Shot Tokenizer Transfer (ZeTT) trains a hypernetwork that predicts embeddings for ANY target tokenizer, letting you swap in a Kazakh-optimized tokenizer on a pretrained model with only 1-3% accuracy loss, fully recoverable with <1B tokens of continued training; it outperforms FOCUS. FOCUS itself initializes new embeddings as a fastText-similarity-weighted mean of overlapping tokens.
>
> **Numbers:** 1-3% accuracy retention gap; <1B tokens to fully recover; beats FOCUS baseline
> **Relevance:** Enables a strong alternative to from-scratch: take Qwen3-0.6B-Base (best baseline, 32.8%), transplant a low-fertility Kazakh Unigram tokenizer via ZeTT/FOCUS, continue-train on 9-10B Kazakh tokens. Inherits Qwen's reasoning while fixing fertility — likely beats both SozKZ-from-scratch and vanilla continued-pretraining.
> **Source:** arXiv:2405.07883 (ZeTT); arXiv:2305.14481 (FOCUS) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested] ZeTT (Zero-Shot Tokenizer Transfer): a hypernetwork predicts embeddings for an ARBITRARY new tokenizer; on Mistral-7B and XLM-R the swapped model stays close to original performance and 'the remaining gap can be quickly closed by continued training on less than 1B tokens'. Hypernetworks trained on base models transfer to fine-tuned variants. Complementary cheap path: NorMistral's 3-stage swap (KB) needed only 1,000 frozen-body embedding-only steps before full CPT.
>
> **Numbers:** <1B tokens to close swap gap at 7B; hypernetwork training cost not budgeted here
> **Relevance:** Makes full tokenizer replacement (needed for fertility <2.0; expansion only reached 2.04 at Sherkala) a bounded-cost option inside a ~10B-token budget; untested at 0.6B and on Kazakh Cyrillic.
> **Source:** arXiv:2405.07883 (ZeTT, Minixhofer et al.); NorMistral arXiv:2412.06484 (KB, not re-verified) · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[small-languages-big-models-a-study-of-continual-training-on-languages-of-norway]]

## Related
- [[universal-cross-tokenizer-distillation-via-approximate-likelihood-matching|Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching]] — Both cross-tokenizer transfer; ALM distillation is an alternative to ZeTT's hypernetwork for swapping vocab
- [[training-free-tokenizer-transplantation-via-orthogonal-matching-pursuit|Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit]] — Competing tokenizer-transfer: ZeTT hypernetwork-predicted embeddings vs OMP training-free transplantation
- [[trans-tokenization-and-cross-lingual-vocabulary-transfers-language-adaptation|Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation of LLMs for…]] — Both study full tokenizer swap; ZeTT closes the gap at 7B with <1B tokens but tested only encoder/Mistral-7B, leaving sub-1B swap tax open

[[Home]]
