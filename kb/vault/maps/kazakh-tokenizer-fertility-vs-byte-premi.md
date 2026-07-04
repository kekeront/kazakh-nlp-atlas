---
type: "moc"
topic: "kazakh-tokenizer-fertility-vs-byte-premi"
nodes: 6
papers: 5
sources: 1
uncertain_claims: 3
tags: ["moc"]
---
# Topic: kazakh-tokenizer-fertility-vs-byte-premi

The frontier here has largely inverted the intuitive story that a better Kazakh tokenizer buys accuracy. CONFIRMED: the Kazakh cross-lingual gap is driven by the script-based byte premium (kaz_cyrl 1.76x on NLLB / 1.88x on FLORES, ~1.80 UTF-8 bytes/char, arxiv:2403.00686), not by fertility or morphology — a 70-language study finds fertility explains only R²=0.021 of alignment variance and MorphScore has no significant correlation with perplexity (F(1,13)=0.323, p=0.580), with the gap becoming insignificant once training data is byte-premium-scaled (arxiv:2411.14198). This is corroborated empirically: SozKZ-600M ships a dedicated 50K ByteLevel-BPE with a 2-3x fertility advantage yet scores MC-QA 30.3% / Belebele 27.0%, LOSING to Qwen2.5-0.5B (31.5 / 30.0) which tokenizes Kazakh ~5x worse (arxiv:2603.20854). The CONTESTED counter-evidence is Parallel Tokenizers, which shows improving fertility 1.89→1.57 yields a real but small +0.72-1.28 F1, largest in low-data regimes (arxiv:2510.06128) — so fertility is a second-order lever, not a null one. Open questions: whether a morphology-aware or byte-level tokenizer (KazByte's BLT-style adapter remains a proposal with ZERO results, arxiv:2603.27859) can convert the ~2.4x efficiency/context win into accuracy, and whether the planned Latin-script transition — which would nearly halve the premium (tur_latn 1.044 vs kaz_cyrl 1.76) — changes the calculus.

## Frontier highlights
- [[why-do-language-models-perform-worse-for-morphologically-complex-languages|Why do language models perform worse for morphologically complex languages?]] — Fertility explains only R²=0.021 of gap; byte premium (up to 5x) is the real driver, not morphology
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — SozKZ: 2-3x-better tokenizer, still loses knowledge QA to Qwen2.5-0.5B — decouples tokenizer from accuracy
- [[a-bit-of-a-problem-measurement-disparities-in-dataset-sizes-across-languages|A Bit of a Problem: Measurement Disparities in Dataset Sizes Across Languages]] — Exact Kazakh byte premium 1.76x/1.88x; script-driven (1.80 bytes/char), NOT agglutination
- [[parallel-tokenizers-rethinking-vocabulary-design-for-cross-lingual-transfer|Parallel Tokenizers: Rethinking Vocabulary Design for Cross-Lingual Transfer]] — Counter-evidence: fertility 1.89→1.57 does buy +0.72-1.28 F1, second-order lever largest in low-data
- [[catherinearnett-byte-premium-tool-all-merged-20240223-tsv|catherinearnett/byte-premium-tool (all_merged_20240223.tsv, byte_coef_…]] — Premium is pure script effect: Latin transition would halve it (tur_latn 1.044 vs kaz_cyrl 1.76)
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] — KazByte BLT-style byte adapter frames fertility as efficiency lever; a proposal with NO results yet

## Papers (5)
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] (2026) — tokenizer-morphology
- [[parallel-tokenizers-rethinking-vocabulary-design-for-cross-lingual-transfer|Parallel Tokenizers: Rethinking Vocabulary Design for Cross-Lingual Transfer]] (2025) — kazakh-tokenizer-fertility-vs-byte-premi
- [[a-bit-of-a-problem-measurement-disparities-in-dataset-sizes-across-languages|A Bit of a Problem: Measurement Disparities in Dataset Sizes Across Languages]] (2024) — kazakh-tokenizer-fertility-vs-byte-premi
- [[why-do-language-models-perform-worse-for-morphologically-complex-languages|Why do language models perform worse for morphologically complex languages?]] (2024) — tokenizer-morphology

## Sources & findings (1)
- [[catherinearnett-byte-premium-tool-all-merged-20240223-tsv|catherinearnett/byte-premium-tool (all_merged_20240223.tsv, byte_coef_…]] — Because the Kazakh byte premium is entirely script-driven, the planned Latin-script transition (~2031) would nearly HALV…

## Related topics
- [[tokenizer-morphology]] — 3 shared nodes
- [[inference-tts]] — 2 shared nodes
- [[kazakh-turkic-nlp]] — 2 shared nodes
- [[novelty-check]] — 2 shared nodes

[[Home]]
