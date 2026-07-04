---
kb_id: "arxiv:2512.03989"
type: "paper"
title: "Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models"
arxiv_id: "2512.03989"
doi: null
hf_repo: null
year: 2025
topics: ["tokenizer-morphology", "continual-pt-lowres-qlora-vs-full-cpt-re"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models", "arXiv:2512.03989", "arxiv:2512.03989"]
tags: ["paper", "topic/tokenizer-morphology", "topic/continual-pt-lowres-qlora-vs-full-cpt-re"]
---
# Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models

[arXiv](https://arxiv.org/abs/2512.03989)
**Topics:** [[tokenizer-morphology]], [[continual-pt-lowres-qlora-vs-full-cpt-re]]

> [!abstract]
> Tokenizer adaptation plays an important role in adapting pre-trained language models to new domains or languages. In this work, we address two complementary aspects of this process: vocabulary extension and pruning. The common approach to extension trains a new tokenizer on domain-specific text and appends the tokens that do not overlap with the existing vocabulary, which often results in many tok …

## Claims

> [!note] CLAIM — tokenizer-morphology
> For adding language-specific tokens to a pretrained model, 'continued BPE training' (re-run BPE on in-domain text starting from the existing merges) beats naive append because it avoids unreachable tokens; embeddings init via Fast Vocabulary Transfer (copy overlaps, average decompositions). For Cyrillic-script languages this gave 5.1-11.2% extra compression over naive extension; adapting Llama-3.2-1B/3B on 24B chars (50% target/50% English) recovered downstream parity and cut training time 26%.
>
> **Numbers:** Cyrillic 5.1-11.2% compression gain over naive; +1-4K Estonian tokens = 3.3-3.8% (Qwen 9.6%); 24B chars recovers parity; -26% train time
> **Relevance:** Precise recipe if grafting Kazakh tokens onto an existing tokenizer: use continued-BPE + FVT, budget ~24B characters (~byte-premium-adjusted) of 50/50 Kazakh/English to recover. Concrete numbers for the paper's methods section.
> **Source:** arXiv:2512.03989 (Teaching Old Tokenizers New Words) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested] 'Continued BPE training' (Dec 2025) supersedes the Sherkala-style train-separate-tokenizer-and-append-merges procedure: re-running the BPE algorithm on target-language data starting from the pretrained tokenizer's merge table gives up to 9.6% better bytes-per-token than naive extension at equal added-token budget, improves 72.9–100% of 70 tested languages, produces far fewer unreachable/unused tokens (4–4.7% fewer), and cuts continued-pretraining time by 26%. Tested on Llama-3/Llama-2/Qwen-2.5/Mistral-Nemo tokenizers with 1K–32K added tokens; downstream evaluated on Llama-3.2-1B/3B with FVT (subword-mean) embedding init.
>
> **Numbers:** ≤9.6% bytes/token gain vs naive extension; win rate 72.9–100% over 70 langs; 1K–32K added tokens; 26% CPT-time reduction
> **Relevance:** Drop-in upgrade for the tokenizer work package: if the panel picks expansion (not swap), extend Qwen3's tokenizer via continued BPE on the 9–10B-token Kazakh corpus, not Sherkala's merge-append. Whether Kazakh is among the 70 languages is unconfirmed.
> **Source:** arXiv:2512.03989 (Teaching Old Tokenizers New Words), HTML v1 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[getting-the-most-out-of-your-tokenizer-for-pre-training-and-domain-adaptation|Getting the most out of your tokenizer for pre-training and domain adaptation]] — Shared method: re-running BPE / tokenizer choice for domain-and-language adaptation before CPT

[[Home]]
