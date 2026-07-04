---
kb_id: "arxiv:2403.00686"
type: "paper"
title: "A Bit of a Problem: Measurement Disparities in Dataset Sizes Across Languages"
arxiv_id: "2403.00686"
doi: null
hf_repo: null
year: 2024
topics: ["kazakh-tokenizer-fertility-vs-byte-premi"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["A Bit of a Problem: Measurement Disparities in Dataset Sizes Across Languages", "arXiv:2403.00686", "arxiv:2403.00686"]
tags: ["paper", "topic/kazakh-tokenizer-fertility-vs-byte-premi"]
---
# A Bit of a Problem: Measurement Disparities in Dataset Sizes Across Languages

[arXiv](https://arxiv.org/abs/2403.00686)
**Topics:** [[kazakh-tokenizer-fertility-vs-byte-premi]]

> [!abstract]
> How should text dataset sizes be compared across languages? Even for content-matched (parallel) corpora, UTF-8 encoded text can require a dramatically different number of bytes for different languages. In our work, we define the byte premium between two languages as the ratio of bytes used to encode content-matched text in those languages. We compute byte premiums for 1155 languages, and we use li …

## Claims

> [!note] CLAIM — kazakh-tokenizer-fertility-vs-byte-premi
> The exact Kazakh (Cyrillic) byte premium relative to English is 1.76x measured on NLLB parallel text and 1.88x on FLORES-200 (byte_coef_nllb=1.7646, byte_coef_flores=1.8764; English=1.0 by definition). Crucially the premium is script-driven, NOT morphology-driven: each Kazakh Cyrillic character costs ~1.80 UTF-8 bytes (bytes_per_char_nllb=1.7977 vs English 1.0034), while Kazakh uses slightly FEWER characters than English for content-matched text (char_coef_nllb=0.9751 < 1.0) because agglutination compresses meaning. So byte premium ≈ 0.975 chars × 1.80 bytes/char ≈ 1.76.
>
> **Numbers:** kaz_cyrl byte premium 1.7646 (NLLB) / 1.8764 (FLORES-200); bytes/char 1.7977; char coef 0.9751; English reference 1.0
> **Relevance:** This is the exact Kazakh-specific number missing from the literature. It shows the corpus is ~1.76-1.88x byte-inflated relative to English purely due to Cyrillic 2-byte encoding, and that morphology does NOT inflate character count. It quantifies exactly how byte-inflated the ~9-10B-token budget is when compared to English on a byte-equity basis.
> **Source:** catherinearnett/byte-premium-tool (all_merged_20240223.tsv, GitHub) + arXiv 2403.00686 'A Bit of a Problem: Measurement Disparities in Dataset Sizes across Languages', Arnett/Chang/Bergen, SIGUL 2024 · **Sweep:** `slm-architecture-2026-07`

## Related
- [[the-tokenizer-tax-across-25-european-languages-domain-invariance-cross-lingual|The Tokenizer Tax Across 25 European Languages: Domain Invariance, Cross-Lingual Few-Shot…]] — Both quantify per-language token/byte cost disparities; Tokenizer Tax measures 25 European langs vs this NLLB/FLORES byte premium

[[Home]]
