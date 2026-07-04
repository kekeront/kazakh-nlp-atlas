---
kb_id: "arxiv:2603.05883"
type: "paper"
title: "VerChol -- Grammar-First Tokenization for Agglutinative Languages"
arxiv_id: "2603.05883"
doi: null
hf_repo: null
year: 2026
topics: ["sota-slm", "tokenizer-morphology"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["VerChol -- Grammar-First Tokenization for Agglutinative Languages", "arXiv:2603.05883", "arxiv:2603.05883"]
tags: ["paper", "topic/sota-slm", "topic/tokenizer-morphology"]
---
# VerChol -- Grammar-First Tokenization for Agglutinative Languages

[arXiv](https://arxiv.org/abs/2603.05883)
**Topics:** [[sota-slm]], [[tokenizer-morphology]]

> [!abstract]
> Tokenization is the foundational step in all large language model (LLM) pipelines, yet the dominant approach Byte Pair Encoding (BPE) and its variants is inherently script agnostic and optimized for English like morphology. For agglutinative languages a typological class encompassing the Dravidian family (Tamil, Kannada, Telugu, Malayalam), Turkic languages (Turkish, Azerbaijani, Uzbek), Uralic la …

## Claims

> [!note] CLAIM — sota-slm
> Multilingual BPE/Unigram tokenizers fragment agglutinative languages badly: 2-16 tokens/word for agglutinative morphology vs ~1.2-1.4 for English; Gemma-2 ~2.2 tok/word on Turkish; words like 'evlerimizden' split into non-morphemic subwords. Morpheme-aware / grammar-first hybrid tokenization (root-affix dictionaries + phonological normalization + statistical merge) measurably raises 'pure token' rates on Turkic.
>
> **Numbers:** agglutinative 2-16 tok/word; Turkish ~2.2 (Gemma-2); English 1.2-1.4
> **Relevance:** Directly validates the <2.0 tok/word target as both hard and high-value. A morphology-aware Kazakh tokenizer (respecting vowel-harmony allomorphs and Cyrillic Ә/Ғ/Қ/Ң/Ө/Ұ/Ү/Һ) is the single biggest lever to make ~9-10B Kazakh tokens act like far more effective compute.
> **Source:** arXiv 2603.05883 (VerChol grammar-first tokenization, abstract via search); Gemma-2 tokenizer analyses; arXiv 2605.29992 (Turkish tokenizer surgery) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — tokenizer-morphology
> Kazakh's Cyrillic->Latin transition is legally targeted for ~2031 and real-world text is heavily kk/ru code-switched. Transliteration tools (QazNLTK, national standard) give deterministic Cyrillic<->Latin mapping. VerChol (grammar-first FST tokenization) shows script-agnostic grammar rules can tokenize agglutinative languages, but is only implemented/validated on Tamil, with Turkic listed as future adaptation.
>
> **Numbers:** Latin transition target ~2031; QazNLTK deterministic translit; VerChol validated only on Tamil
> **Relevance:** Dual-script recommendation: train the tokenizer on BOTH Cyrillic and transliterated-Latin Kazakh so shared morphemes map to shared subwords (future-proofs for 2031 and handles mixed input), OR normalize all input to Cyrillic via deterministic transliteration before tokenizing. Reserve explicit vocab budget for Russian + Latin-Kazakh + basic English to cover code-switching.
> **Source:** en.wikipedia.org/wiki/Kazakh_alphabets ; arXiv:2603.05883 (VerChol) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[morpheus-a-morphology-aware-neural-tokenizer-and-word-embedder-for-turkish|Morpheus: A Morphology-Aware Neural Tokenizer and Word Embedder for Turkish]] — Both morphology-aware Turkic tokenizers; VerChol validated only on Tamil, Morpheus built for Turkish
- [[quechuatok-morphological-boundary-accuracy-as-a-necessary-metric-for-tokenizer|QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation…]] — Both argue morphological-boundary accuracy is a necessary tokenizer metric / grammar-first design for low-resource agglutinative languages
- [[mdpi-information-17-2-128-doi-10-3390-info17020128|MDPI Information 17(2):128 / doi 10.3390/info17020128, 'Morphology-Awa…]] — Both grammar/morphology-first tokenization for agglutinative languages, evaluated on curated data rather than noisy crawl

[[Home]]
