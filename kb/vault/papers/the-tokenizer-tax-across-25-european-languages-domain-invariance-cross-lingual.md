---
kb_id: "arxiv:2605.24718"
type: "paper"
title: "The Tokenizer Tax Across 25 European Languages: Domain Invariance, Cross-Lingual Few-Shot Effects, and the Ukrainian Penalty"
arxiv_id: "2605.24718"
doi: null
hf_repo: null
year: 2026
topics: ["tokenizer-agglutinative"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["The Tokenizer Tax Across 25 European Languages: Domain Invariance, Cross-Lingual Few-Shot Effects, and the Ukrainian Penalty", "arXiv:2605.24718", "arxiv:2605.24718"]
tags: ["paper", "topic/tokenizer-agglutinative"]
---
# The Tokenizer Tax Across 25 European Languages: Domain Invariance, Cross-Lingual Few-Shot Effects, and the Ukrainian Penalty

[arXiv](https://arxiv.org/abs/2605.24718)
**Topics:** [[tokenizer-agglutinative]]

> [!abstract]
> Tokenizer fertility the number of tokens per word imposes a hidden cost on non-English NLP. We measure fertility for ten foundation models across 25 European languages on parallel text, producing the first controlled tokenizer tax map for the continent. The tax spans 2.5x from English (1.2 tokens/word) to Greek/Maltese (~3.1), following a clear hierarchy: Romance (1.5-1.7), Germanic (1.7-1.9), Sla …

## Claims

> [!note] CLAIM — tokenizer-agglutinative
> Qwen3 (151K vocab) and DeepSeek-V3 (128K) fragment Cyrillic into 8-9 subwords/word while Llama-3.3/Gemma-2 (also ~128K) achieve 3-4; vocab size does NOT predict Cyrillic efficiency — the fraction of Cyrillic-specific merges does. Documents an explicit 'Ukrainian penalty'.
>
> **Numbers:** Qwen3 splits 'вiдповiдальнiсть' into 9 subwords vs 4 for Gemma-2; DeepSeek-V3/Qwen3 8-9 tok/word vs Llama-3.3 3-4, all ~128-151K vocab
> **Relevance:** transferable-untested (Ukrainian/Cyrillic, not Kazakh). Independently corroborates the measured Qwen3 kk fertility 5.3 (#1): the problem is missing Cyrillic merges, not vocab size — so vocab EXPANSION with Kazakh merges (Sherkala recipe) is the fix, not just a bigger multilingual vocab.
> **Source:** arXiv:2605.24718 'The Tokenizer Tax Across 24 European Languages' · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[a-bit-of-a-problem-measurement-disparities-in-dataset-sizes-across-languages|A Bit of a Problem: Measurement Disparities in Dataset Sizes Across Languages]] — Both quantify per-language token/byte cost disparities; Tokenizer Tax measures 25 European langs vs this NLLB/FLORES byte premium
- [[why-do-language-models-perform-worse-for-morphologically-complex-languages|Why do language models perform worse for morphologically complex languages?]] — Tokenizer Tax quantifies the Cyrillic fertility penalty; this paper links high fertility to worse downstream LM quality
- [[own-measurement-transformers-5-5-2-autotokenizer-qwen-qwen3|Own measurement, transformers 5.5.2, AutoTokenizer Qwen/Qwen3-0.6B-Bas…]] — Tax study: Qwen3 fragments Cyrillic 8-9 subw/word; own Kazakh measurement corroborates at 5.3 tok/word via byte fallback

[[Home]]
