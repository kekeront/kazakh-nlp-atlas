---
kb_id: "arxiv:2507.06378"
type: "paper"
title: "Evaluating Morphological Alignment of Tokenizers in 70 Languages"
arxiv_id: "2507.06378"
doi: null
hf_repo: null
year: 2025
topics: ["tokenizer-morphology"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Evaluating Morphological Alignment of Tokenizers in 70 Languages", "arXiv:2507.06378", "arxiv:2507.06378"]
tags: ["paper", "topic/tokenizer-morphology"]
---
# Evaluating Morphological Alignment of Tokenizers in 70 Languages

[arXiv](https://arxiv.org/abs/2507.06378)
**Topics:** [[tokenizer-morphology]]

> [!abstract]
> While tokenization is a key step in language modeling, with effects on model training and performance, it remains unclear how to effectively evaluate tokenizer quality. One proposed dimension of tokenizer quality is the extent to which tokenizers preserve linguistically meaningful subwords, aligning token boundaries with morphological boundaries within a word. We expand MorphScore (Arnett & Bergen …

## Claims

> [!note] CLAIM — tokenizer-morphology
> MorphScore-style evaluation across 70 languages finds Unigram-LM tokenization aligns with morpheme boundaries substantially better than BPE, especially for agglutinative languages (Turkish, Kazakh, Finnish, Hungarian); larger vocabularies improve alignment. The tool is released as MorphScore (code + HF datasets).
>
> **Numbers:** Unigram > BPE morpheme alignment; effect strongest for agglutinative family; alignment rises with vocab size
> **Relevance:** Direct tokenizer-type recommendation: prefer SentencePiece Unigram over BPE for Kazakh (matches the user's current Unigram choice). Provides an off-the-shelf intrinsic metric (MorphScore) to report in the paper alongside fertility.
> **Source:** arXiv:2507.06378 (Evaluating Morphological Alignment of Tokenizers in 70 Languages) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[morphbpe-a-morpho-aware-tokenizer-bridging-linguistic-complexity-for-efficient|MorphBPE: A Morpho-Aware Tokenizer Bridging Linguistic Complexity for Efficient LLM Traini…]] — Both quantify tokenizer morphological alignment; 70-language study contextualizes MorphBPE's per-language consistency-F1 gains
- [[rethinking-tokenization-for-rich-morphology-the-dominance-of-unigram-over-bpe|Rethinking Tokenization for Rich Morphology: The Dominance of Unigram over BPE and Morphol…]] — Both conclude Unigram-LM aligns to morpheme boundaries better than BPE, strongest for agglutinative languages
- [[quechuatok-morphological-boundary-accuracy-as-a-necessary-metric-for-tokenizer|QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation…]] — Shared method — morphological-alignment/boundary-accuracy of tokenizers; QuechuaTok on one LRL, this paper across 70 languages

[[Home]]
