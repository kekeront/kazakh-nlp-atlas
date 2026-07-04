---
kb_id: "doi:10.3389/frai.2025.1708566"
type: "source"
title: "Frontiers/PMC12741073 (Hybrid AI architectures for automatic text corr…"
doi: "10.3389/frai.2025.1708566"
hf_repo: null
year: null
topics: ["kazakh-morphological-segmentation-qualit"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["doi:10.3389/frai.2025.1708566"]
tags: ["source", "topic/kazakh-morphological-segmentation-qualit"]
---
# Frontiers/PMC12741073 (Hybrid AI architectures for automatic text corr…

**Topics:** [[kazakh-morphological-segmentation-qualit]]

## Source URLs
- Frontiers/PMC12741073 (Hybrid AI architectures for automatic text correction in Kazakh, 2025)
- doi 10.3389/frai.2025.1708566

## Findings

> [!note] CLAIM — kazakh-morphological-segmentation-qualit
> The 2025 hybrid Kazakh analyzer (KazMorphCorpus-2025) shows the affordable FST-only stage is only 81.5% accurate on OPEN vocabulary (96% closed-vocab); reaching 92.3% requires stacking FST+CRF+KazRoBERTa. The analyzer's dominant errors are precisely web-text failure modes: words absent from the 15K-stem lexicon (names, borrowings, technical terms), with error mix affix-chain 34.0%, segmentation 31.5%, borrowing 14.9%.
>
> **Numbers:** FST alone open-vocab 81.5%; closed-vocab 96%; FST+CRF 89.0%; FST+CRF+KazRoBERTa 92.3%; KazRoBERTa 90.8% F1 90.7 vs mBERT 82.6%. Lexicon ~15,000 roots + 200 suffixes. Error breakdown: affix-chain 34.0%, segmentation 31.5%, borrowing 14.9%.
> **Relevance:** The segmenter you can actually run at scale (FST) mis-analyzes ~18.5% of open-vocab tokens, concentrated in borrowings/OOV/long-affix-chains — the exact content of web crawl. This directly caps the reliability of morpheme-conditioned n-gram keys.
> **Source:** Frontiers/PMC12741073 (Hybrid AI architectures for automatic text correction in Kazakh, 2025); doi 10.3389/frai.2025.1708566 · **Sweep:** `slm-architecture-2026-07`

## Related
- [[huggingface-co-kz-transformers-kaz-roberta-conversational|huggingface.co/kz-transformers/kaz-roberta-conversational]] — The hybrid analyzer's top-accuracy stage (92.3%) stacks KazRoBERTa on FST+CRF — this is that KazRoBERTa model's card

[[Home]]
