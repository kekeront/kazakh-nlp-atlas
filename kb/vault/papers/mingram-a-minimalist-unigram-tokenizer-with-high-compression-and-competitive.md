---
kb_id: "arxiv:2606.27019"
type: "paper"
title: "MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive Morphological Alignment"
arxiv_id: "2606.27019"
doi: null
hf_repo: null
year: 2026
topics: ["tokenizer-agglutinative"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive Morphological Alignment", "arXiv:2606.27019", "arxiv:2606.27019"]
tags: ["paper", "topic/tokenizer-agglutinative"]
---
# MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive Morphological Alignment

[arXiv](https://arxiv.org/abs/2606.27019)
**Topics:** [[tokenizer-agglutinative]]

> [!abstract]
> The Unigram tokenizer uses an elegant representation which makes it straightforward to edit vocabularies, but its training is comparatively heavy and complex. We introduce MinGram (Minimalist Unigram), which keeps the token-list representation but simplifies training using a BPE-derived seed vocabulary, Hard EM on a minimum-token path, and a single flat score-pruning step. This removes the suffix …

## Claims

> [!note] CLAIM — tokenizer-agglutinative
> Unigram-family tokenizers beat BPE in bits-per-byte across six languages in controlled downstream LM training; MinGram (a minimalist Unigram: BPE-seed + Hard-EM min-token path + single flat prune) compresses better than both BPE and standard Unigram while keeping high morphological alignment.
>
> **Numbers:** 6 languages; MinGram > BPE and > standard Unigram on compression; Unigram-family (incl. MinGram) consistently lower bits-per-byte than BPE
> **Relevance:** transferable-untested. Corroborates finding #2 (Unigram>BPE) with a compression-oriented variant that recovers BPE-level fertility — a candidate tokenizer recipe for Kazakh that avoids the usual Unigram fertility penalty.
> **Source:** arXiv:2606.27019 (Sander Land, 2026) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[rethinking-tokenization-for-rich-morphology-the-dominance-of-unigram-over-bpe|Rethinking Tokenization for Rich Morphology: The Dominance of Unigram over BPE and Morphol…]] — MinGram and the Telugu study independently corroborate Unigram-family beats BPE on bits-per-byte across languages

[[Home]]
