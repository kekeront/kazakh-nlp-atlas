---
kb_id: "arxiv:2606.23943"
type: "paper"
title: "QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation in Agglutinative Low-Resource Languages"
arxiv_id: "2606.23943"
doi: null
hf_repo: null
year: 2026
topics: ["kazakh-morphological-segmentation-qualit", "tokenizer-agglutinative"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation in Agglutinative Low-Resource Languages", "arXiv:2606.23943", "arxiv:2606.23943"]
tags: ["paper", "topic/kazakh-morphological-segmentation-qualit", "topic/tokenizer-agglutinative"]
---
# QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation in Agglutinative Low-Resource Languages

[arXiv](https://arxiv.org/abs/2606.23943)
**Topics:** [[kazakh-morphological-segmentation-qualit]], [[tokenizer-agglutinative]]

> [!abstract]
> Tokenization is a foundational step in NLP pipelines, yet standard evaluation metrics such as fertility rate fail to capture morphological correctness for agglutinative languages. We present QuechuaTok, a systematic benchmark comparing four tokenization strategies - BPE, Unigram LM, WordPiece, and a morphology-aware PRPE tokenizer - for Southern Quechua (quz), a low-resource agglutinative language …

## Claims

> [!note] CLAIM — kazakh-morphological-segmentation-qualit
> Cross-lingual evidence (Southern Quechua, another agglutinative LRL) shows fertility<2.0 is achieved by plain BPE WITHOUT any morphology (BPE 1.636 at 16k) but that BPE scores only 6.67% morphological boundary accuracy — pure surface-form memorization. The morphology-aware PRPE tokenizer gets 83.33% MorphAcc at fertility 1.797. Caveat: MorphAcc is computed on only a 15-word evaluation set, so absolute numbers are statistically fragile.
>
> **Numbers:** BPE: fert 2.233/1.918/1.636 at 4k/8k/16k, MorphAcc constant 6.67%; Unigram MorphAcc 66.67%@4k -> 26.67%@8k -> 33.33%@16k; PRPE fert 1.797, MorphAcc 83.33%; OOV ~0% (byte_fallback). Eval set = 15 words.
> **Relevance:** Kills 'fertility<2.0' as the tokenizer's defensible edge: plain BPE already hits it. The only morphology-based differentiator is boundary accuracy (MorphAcc / Morphological Consistency F1) — which for Kazakh remains unproven on noisy text. Frame the tokenizer contribution around boundary quality, not fertility.
> **Source:** arXiv 2606.23943 'QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation in Agglutinative Low-Resource Languages' (Jun 2026), Tables 1 & 3 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — tokenizer-agglutinative
> In agglutinative low-resource tokenization no single tokenizer wins all metrics, and low fertility can be a MISLEADING artifact of surface memorization. On Quechua: PRPE gets highest morpheme-boundary accuracy 83.33%; Unigram-4k lowest perplexity (1344); BPE-16k lowest fertility (1.636) but WORST morpheme accuracy (6.67%).
>
> **Numbers:** PRPE MBA 83.33%; Unigram-4k ppl 1344 (lowest); BPE-16k fertility 1.636 (lowest) but MBA 6.67% (worst)
> **Relevance:** tested-on-agglutinative (Quechua). Warns the lab that the fertility<2.0 target alone is insufficient/gameable — BPE hits low fertility by memorizing surface forms while destroying morpheme boundaries. Add morpheme-boundary accuracy/F1 as a second tokenizer acceptance metric for Kazakh.
> **Source:** arXiv:2606.23943 'QuechuaTok' · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[verchol-grammar-first-tokenization-for-agglutinative-languages|VerChol -- Grammar-First Tokenization for Agglutinative Languages]] — Both argue morphological-boundary accuracy is a necessary tokenizer metric / grammar-first design for low-resource agglutinative languages
- [[evaluating-morphological-alignment-of-tokenizers-in-70-languages|Evaluating Morphological Alignment of Tokenizers in 70 Languages]] — Shared method — morphological-alignment/boundary-accuracy of tokenizers; QuechuaTok on one LRL, this paper across 70 languages
- [[rethinking-tokenization-for-rich-morphology-the-dominance-of-unigram-over-bpe|Rethinking Tokenization for Rich Morphology: The Dominance of Unigram over BPE and Morphol…]] — Both argue morphology-aware metric matters and unigram/PRPE beat surface BPE on morpheme boundaries in agglutinative LRLs
- [[beyond-fertility-analyzing-strr-as-a-metric-for-multilingual-tokenization|Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation]] — Both refute fertility as a sufficient tokenizer metric; QuechuaTok proposes morpheme-boundary accuracy, Beyond-Fertility proposes STRR
- [[mdpi-information-2026-17-2-128-morphology-aware|MDPI Information 2026, 17(2):128 (Morphology-Aware Segmentation and To…]] — Quechua morpheme-boundary metric transfers to the Kazakh Turkic segmentation case both are agglutinative LRL tokenizer eval

[[Home]]
