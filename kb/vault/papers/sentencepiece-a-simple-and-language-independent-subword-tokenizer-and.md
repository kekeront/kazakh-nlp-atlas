---
kb_id: "arxiv:1808.06226"
type: "paper"
title: "SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing"
arxiv_id: "1808.06226"
doi: null
hf_repo: null
year: 2018
topics: ["tokenizer-agglutinative"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing", "arXiv:1808.06226", "arxiv:1808.06226"]
tags: ["paper", "topic/tokenizer-agglutinative"]
---
# SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing

[arXiv](https://arxiv.org/abs/1808.06226)
**Topics:** [[tokenizer-agglutinative]]

> [!abstract]
> This paper describes SentencePiece, a language-independent subword tokenizer and detokenizer designed for Neural-based text processing, including Neural Machine Translation. It provides open-source C++ and Python implementations for subword units. While existing subword segmentation tools assume that the input is pre-tokenized into word sequences, SentencePiece can train subword models directly fr …

## Claims

> [!warning] UNCERTAIN — tokenizer-agglutinative
> Normalization pipeline for Kazakh Cyrillic: SentencePiece/Unigram defaults to Unicode NFKC; NFKC+casefold has documented Turkic lowercasing hazards (dotted/dotless i, compatibility folding differs between NFKD/NFKC), which matter for kk/ru code-switching and Latin-transition text.
>
> **Numbers:** SentencePiece default = NFKC; issue #6680 shows NFD/NFKD vs NFC/NFKC produce different lowercased forms for Turkish and 'probably other languages'
> **Relevance:** transferable-untested for Kazakh specifically. Recommend NFC (compose, preserve 42 Kazakh letters Ә Ғ Қ Ң Ө Ұ Ү Һ) over NFKC compatibility decomposition, plus a Kazakh-aware casefold that does not collapse kk/ru homoglyphs — to avoid silently merging distinct Kazakh graphemes during CPT. No measured Kazakh normalization study found.
> **Source:** HF tokenizers normalizer docs + huggingface/transformers issue #6680; SentencePiece arXiv:1808.06226 (NFKC default) · **Sweep:** `slm-arch-for-kazakh`

[[Home]]
