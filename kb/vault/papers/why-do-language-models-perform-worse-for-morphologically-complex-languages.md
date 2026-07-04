---
kb_id: "arxiv:2411.14198"
type: "paper"
title: "Why do language models perform worse for morphologically complex languages?"
arxiv_id: "2411.14198"
doi: null
hf_repo: null
year: 2024
topics: ["tokenizer-morphology", "kazakh-tokenizer-fertility-vs-byte-premi"]
claims: 4
uncertain_claims: 1
verdicts: []
aliases: ["Why do language models perform worse for morphologically complex languages?", "arXiv:2411.14198", "arxiv:2411.14198"]
tags: ["paper", "topic/tokenizer-morphology", "topic/kazakh-tokenizer-fertility-vs-byte-premi"]
---
# Why do language models perform worse for morphologically complex languages?

[arXiv](https://arxiv.org/abs/2411.14198)
**Topics:** [[tokenizer-morphology]], [[kazakh-tokenizer-fertility-vs-byte-premi]]

> [!abstract]
> Language models perform differently across languages. It has been previously suggested that morphological typology may explain some of this variability (Cotterell et al., 2018). We replicate previous analyses and find additional new evidence for a performance gap between agglutinative and fusional languages, where fusional languages, such as English, tend to have better language modeling performan …

## Claims

> [!note] CLAIM — tokenizer-morphology
> A 70-language + Goldfish study found that the performance gap on morphologically complex languages is NOT caused by tokenization or fertility. Agglutinative languages actually had HIGHER morpheme alignment (MorphScore 66.3%) than fusional (53.3%, p=.008); fertility explained only R^2=0.021 of alignment variance. The real culprit is the 'byte premium' (up to 5x more UTF-8 bytes per content-matched text). When data is scaled by byte premium the gap becomes insignificant.
>
> **Numbers:** agglutinative MorphScore 66.3% vs fusional 53.3% (p=.008); fertility R^2=0.021; byte premium up to 5x; gap insignificant after byte-scaling (t=1.18, p=0.077)
> **Relevance:** Reframes the whole project: Kazakh Cyrillic (~2 bytes/char) means the 9-10B token budget is byte-inflated — effective content is smaller than an equivalent English budget. Lower fertility helps compute/context, but DATA QUANTITY (byte-premium-adjusted) is the dominant lever. Argues for maximizing clean Kazakh data over exotic tokenizer tricks.
> **Source:** arXiv:2411.14198 (Why do LMs perform worse for morphologically complex languages?) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-tokenizer-fertility-vs-byte-premi
> arXiv 2411.14198 finds tokenizer fertility and morphology explain almost none of the cross-lingual performance gap. A regression using tokens-per-word (fertility) and word length as predictors had adjusted R²=0.021 (2.1% of variance). MorphScore (morphological alignment) had NO significant correlation with perplexity: F(1,13)=0.323, p=0.580. Rényi entropy (tokenization quality) explained R²=0.030 vs 0.100 for morphological type, full model R²=0.144. Agglutinative languages had only 3.5% longer sequences on average.
>
> **Numbers:** fertility+word-length adjusted R²=0.021; MorphScore F(1,13)=0.323, p=0.580; Rényi entropy R²=0.030; morph-type R²=0.100; full model R²=0.144; +3.5% sequence length
> **Relevance:** This is the paper's central counter-evidence to a 'fertility<2.0 as top accuracy lever' claim. If fertility explains only ~2% of variance, driving it from 2.0 to <2.0 is not a first-order accuracy move; it is an efficiency/context move.
> **Source:** arXiv 2411.14198 'Why do language models perform worse for morphologically complex languages?', Arnett & Bergen (html full text) · **Sweep:** `slm-architecture-2026-07`

> [!warning] UNCERTAIN — kazakh-tokenizer-fertility-vs-byte-premi
> arXiv 2411.14198 shows the gap is data-quantity driven once byte-premium-adjusted: 'accounting for byte premiums by scaling training data reduces most of the variance previously accounted for by morphological type,' and after byte-premium scaling the performance gap becomes statistically insignificant. Conclusion quote: 'no language is harder or easier for a language model to learn on the basis of its morphological typology. Differences in performance can be attributed to disparities in dataset size.' Byte premiums reach up to 5x for extreme scripts (Khmer at 3 bytes/char).
>
> **Numbers:** gap becomes non-significant after byte-premium scaling (reported t(137.36)=1.180); byte premiums up to 5x vs English
> **Relevance:** This is the load-bearing source behind the question's thesis: the binding constraint is byte-premium-adjusted DATA QUANTITY, not tokenizer fertility. Supports reframing the paper's tokenizer claim to necessary-but-not-sufficient.
> **Source:** arXiv 2411.14198 (html full text) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-tokenizer-fertility-vs-byte-premi
> Kazakh's data-quantity constraint is severe and quantified: in the XLM-R / Common Crawl corpus the Kazakh subcorpus is 117x smaller than English and 5.8x smaller than Turkish. Combined with the 1.76x byte premium, the effective (content-equity) Kazakh data deficit is even larger than the raw ratio implies.
>
> **Numbers:** Kazakh CC subcorpus 117x smaller than English; 5.8x smaller than Turkish
> **Relevance:** Names the actual binding constraint for a Kazakh SLM. The ~9-10B token budget looks reasonable in tokens but represents a small amount of unique content that is further byte-inflated; maximizing unique/clean content and cross-lingual (Turkic/Russian) transfer matters more than shaving fertility below 2.0.
> **Source:** arXiv 2411.14198 / arXiv 2403.00686 (Arnett/Chang/Bergen) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[a-bit-of-a-problem-measurement-disparities-in-dataset-sizes-across-languages]]

## Related
- [[scaling-data-constrained-language-models|Scaling Data-Constrained Language Models]] — Concludes gap is data-quantity driven after byte scaling; grounds it in data-constrained scaling laws
- [[beyond-fertility-analyzing-strr-as-a-metric-for-multilingual-tokenization|Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation]] — Both argue fertility is a weak predictor; STRR proposes a replacement metric for multilingual tokenizer quality
- [[the-tokenizer-tax-across-25-european-languages-domain-invariance-cross-lingual|The Tokenizer Tax Across 25 European Languages: Domain Invariance, Cross-Lingual Few-Shot…]] — Tokenizer Tax quantifies the Cyrillic fertility penalty; this paper links high fertility to worse downstream LM quality
- [[tensorizing-engram-sharing-latents-across-n-gram-embeddings-is-beneficial-in|Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs]] — Tensorizing's high-fertility transfer argument (Kazakh fragmentation mimics tiny-vocab regime) leans on morphological-complexity penalty…
- [[mdpi-applied-sciences-14-13-5369-a-benchmark-for|MDPI Applied Sciences 14(13):5369, 'A Benchmark for Morphological Segm…]] — Kazakh's 8.52% OOV recall and unsupervised-segmenter collapse concretize why LMs perform worse for morphologically complex languages

[[Home]]
