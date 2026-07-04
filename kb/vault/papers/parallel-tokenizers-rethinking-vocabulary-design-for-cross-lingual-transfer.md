---
kb_id: "arxiv:2510.06128"
type: "paper"
title: "Parallel Tokenizers: Rethinking Vocabulary Design for Cross-Lingual Transfer"
arxiv_id: "2510.06128"
doi: null
hf_repo: null
year: 2025
topics: ["kazakh-tokenizer-fertility-vs-byte-premi"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Parallel Tokenizers: Rethinking Vocabulary Design for Cross-Lingual Transfer", "arXiv:2510.06128", "arxiv:2510.06128"]
tags: ["paper", "topic/kazakh-tokenizer-fertility-vs-byte-premi"]
---
# Parallel Tokenizers: Rethinking Vocabulary Design for Cross-Lingual Transfer

[arXiv](https://arxiv.org/abs/2510.06128)
**Topics:** [[kazakh-tokenizer-fertility-vs-byte-premi]]

> [!abstract]
> Tokenization defines the foundation of multilingual language models by determining how words are represented and shared across languages. However, existing methods often fail to support effective cross-lingual transfer because semantically equivalent words are assigned distinct embeddings. For example, "I eat rice" in English and "Ina cin shinkafa" in Hausa are typically mapped to different vocabu …

## Claims

> [!note] CLAIM — kazakh-tokenizer-fertility-vs-byte-premi
> Counter-evidence that tokenizer quality is NOT irrelevant (the other side): Parallel Tokenizers (arXiv 2510.06128) shows improving fertility 1.89 -> 1.57 and parity 1.14 -> 1.07 yielded downstream gains of +0.92/1.28/0.72/1.22 F1 at 100/50/10/1% training-data levels. Effect is real but small (~1 F1), consistent with fertility being a second-order lever, largest in low-data regimes.
>
> **Numbers:** fertility 1.57 vs 1.89; parity 1.07 vs 1.14; downstream +0.72 to +1.28 F1
> **Relevance:** Keeps the finding balanced: pushing fertility below 2.0 gives modest, real downstream gains (especially valuable in Kazakh's low-data regime) but not the multi-point KazMMLU jump a headline 'top accuracy lever' claim would need.
> **Source:** arXiv 2510.06128 'Parallel Tokenizers: Rethinking Vocabulary Design for Cross-Lingual Transfer' (html) · **Sweep:** `slm-architecture-2026-07`

[[Home]]
