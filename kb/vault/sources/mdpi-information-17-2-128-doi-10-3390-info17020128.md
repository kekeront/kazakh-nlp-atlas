---
kb_id: "doi:10.3390/info17020128"
type: "source"
title: "MDPI Information 17(2):128 / doi 10.3390/info17020128, 'Morphology-Awa…"
doi: "10.3390/info17020128"
hf_repo: null
year: null
topics: ["kazakh-morphological-segmentation-qualit"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["doi:10.3390/info17020128"]
tags: ["source", "topic/kazakh-morphological-segmentation-qualit"]
---
# MDPI Information 17(2):128 / doi 10.3390/info17020128, 'Morphology-Awa…

**Topics:** [[kazakh-morphological-segmentation-qualit]]

## Source URLs
- MDPI Information 17(2):128 / doi 10.3390/info17020128, 'Morphology-Aware Segmentation and Tokenization for Turkic Languages: A CSE-Guided Framework'

## Findings

> [!note] CLAIM — kazakh-morphological-segmentation-qualit
> The CSE-guided Kazakh morphology tokenizer's headline segmentation F1 (FEMSeg_kaz_v2 morph_F1 99.62%; v3 95.55% on an external manual test, 3.48% edit distance) is achieved on 2.33M SYNTHETIC harmony-generated wordforms plus a 284,707-sentence web-collected PARALLEL corpus — clean/curated, not noisy monolingual crawl. No OOV rate and no noise-robustness benchmark are reported. Token-count gain is modest: 113,142 (BPE_Kaz) vs 130,605 (mT5) on 4,999 sentences (~13% fewer).
>
> **Numbers:** FEMSeg_kaz_v2 morph_F1 99.62% (P 99.58/R 99.67, 2,329,377 wordforms); v3 95.55% F1, edit distance 3.48%; train corpus 284,707 sentences; vocab 32k (16k/50k options); BPE_Kaz 113,142 vs mT5 130,605 tokens.
> **Relevance:** The 95-99% segmentation F1 that would justify morphology-constrained tokenization is unverified at web-crawl noise; it is on synthetic + parallel data. Do not assume it transfers to raw CulturaX/HPLT.
> **Source:** MDPI Information 17(2):128 / doi 10.3390/info17020128, 'Morphology-Aware Segmentation and Tokenization for Turkic Languages: A CSE-Guided Framework' · **Sweep:** `slm-architecture-2026-07`

## Related
- [[morpheus-a-morphology-aware-neural-tokenizer-and-word-embedder-for-turkish|Morpheus: A Morphology-Aware Neural Tokenizer and Word Embedder for Turkish]] — Morpheus is Turkish-only; the Kazakh CSE-guided segmenter is the Kazakh analog to source morpheme keys
- [[verchol-grammar-first-tokenization-for-agglutinative-languages|VerChol -- Grammar-First Tokenization for Agglutinative Languages]] — Both grammar/morphology-first tokenization for agglutinative languages, evaluated on curated data rather than noisy crawl

[[Home]]
