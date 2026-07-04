---
kb_id: "arxiv:2602.06942"
type: "paper"
title: "Optimal Turkish Subword Strategies at Scale: Systematic Evaluation of Data, Vocabulary, Morphology Interplay"
arxiv_id: "2602.06942"
doi: null
hf_repo: null
year: 2026
topics: ["tokenizer-morphology"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["Optimal Turkish Subword Strategies at Scale: Systematic Evaluation of Data, Vocabulary, Morphology Interplay", "arXiv:2602.06942", "arxiv:2602.06942"]
tags: ["paper", "topic/tokenizer-morphology"]
---
# Optimal Turkish Subword Strategies at Scale: Systematic Evaluation of Data, Vocabulary, Morphology Interplay

[arXiv](https://arxiv.org/abs/2602.06942)
**Topics:** [[tokenizer-morphology]]

> [!abstract]
> Tokenization is a pivotal design choice for neural language modeling in morphologically rich languages (MRLs) such as Turkish, where productive agglutination challenges both vocabulary efficiency and morphological fidelity. Prior studies have explored tokenizer families and vocabulary sizes but typically (i) vary vocabulary without systematically controlling the tokenizer's training corpus, (ii) p …

## Claims

> [!warning] UNCERTAIN — tokenizer-morphology
> Optimal Turkish subword study (vocab 8K-256K) finds diminishing returns beyond ~128K, and that morphology-aware pretokenization yields small-but-consistent downstream gains (POS/NER/QA/sentiment) over a WordPiece baseline; character-level morphology micro-accuracy 96.19 vs 30.76 for BERTurk shows subword models discard morpheme structure that morph-aware methods preserve.
>
> **Numbers:** vocab 8K-256K, diminishing returns >128K; morph micro-acc 96.19 (char) vs 30.76 (BERTurk); small consistent gains
> **Relevance:** Independent Turkic confirmation that (a) very large vocabs stop helping, and (b) morphology-aware tokenization gives real, if modest, downstream gains — supporting a morphology-supervised Unigram vocab in the 48-64K range for Kazakh rather than chasing 128K+.
> **Source:** arXiv:2602.06942 (Optimal Turkish Subword Strategies at Scale) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[catherinearnett-byte-premium-tool-all-merged-20240223-tsv|catherinearnett/byte-premium-tool (all_merged_20240223.tsv, byte_coef_…]] — Byte-premium data show Latin Turkic near English (tur_latn 1.044); Turkish subword study operates in that low-premium Latin regime

[[Home]]
