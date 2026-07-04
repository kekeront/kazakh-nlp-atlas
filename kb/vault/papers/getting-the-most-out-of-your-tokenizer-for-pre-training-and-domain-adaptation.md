---
kb_id: "arxiv:2402.01035"
type: "paper"
title: "Getting the most out of your tokenizer for pre-training and domain adaptation"
arxiv_id: "2402.01035"
doi: null
hf_repo: null
year: 2024
topics: ["qymyzlm-architecture-fork"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Getting the most out of your tokenizer for pre-training and domain adaptation", "arXiv:2402.01035", "arxiv:2402.01035"]
tags: ["paper", "topic/qymyzlm-architecture-fork"]
---
# Getting the most out of your tokenizer for pre-training and domain adaptation

[arXiv](https://arxiv.org/abs/2402.01035)
**Topics:** [[qymyzlm-architecture-fork]]

> [!abstract]
> Tokenization is an understudied and often neglected component of modern LLMs. Most published works use a single tokenizer for all experiments, often borrowed from another model, without performing ablations or analysis to optimize tokenization. Moreover, the tokenizer is generally kept unchanged when fine-tuning a base model. In this paper, we show that the size, pre-tokenization regular expressio …

## Claims

> [!note] CLAIM — qymyzlm-architecture-fork
> [transferable-untested (code domain, 7B)] The known cost bar for a zero-regret tokenizer swap is >50B fine-tuning tokens: Dagan et al. report that when fine-tuning on more than 50B tokens one can specialize the tokenizer of a pre-trained LLM (7B, code setting) with no performance cost, gaining generation speed and effective context. Our 10B-token Kazakh ceiling is 5x below this bar, so a residual 'swap tax' at CPT-end should be planned for, partially offset by <=4-epoch data repetition (arXiv:2305.16264, already in KB).
>
> **Numbers:** >50B tokens for cost-free swap (7B models, code domain); lab budget ~9-10B kk tokens (~40B token-equivalents at 4 epochs max)
> **Relevance:** Sets the data-budget risk for the full-swap path: expect measurable but bounded degradation vs an ideal swap; the trans-tokenization/mean-subtoken init (findings 2, 5) is the documented mitigation at low budgets.
> **Source:** Getting the most out of your tokenizer for pre-training and domain adaptation, arXiv:2402.01035 · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[scaling-data-constrained-language-models]]

## Related
- [[teaching-old-tokenizers-new-words-efficient-tokenizer-adaptation-for-pre|Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models]] — Shared method: re-running BPE / tokenizer choice for domain-and-language adaptation before CPT

[[Home]]
