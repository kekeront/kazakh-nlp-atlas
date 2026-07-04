---
kb_id: "title:apertium github io apertium kaz frontiers 2025 frai 2025 1708566 hybrid kazakh analyzer"
type: "source"
title: "apertium.github.io/apertium-kaz"
doi: null
hf_repo: null
year: null
topics: ["tokenizer-morphology"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:apertium github io apertium kaz frontiers 2025 frai 2025 1708566 hybrid kazakh analyzer"]
tags: ["source", "topic/tokenizer-morphology"]
---
# apertium.github.io/apertium-kaz

**Topics:** [[tokenizer-morphology]]

## Source URLs
- apertium.github.io/apertium-kaz
- Frontiers 2025 (frai.2025.1708566) hybrid Kazakh analyzer

## Findings

> [!note] CLAIM — tokenizer-morphology
> Kazakh has production-grade morpheme-segmentation resources: apertium-kaz (finite-state morphological transducer + CG disambiguator, compatible across Turkic), plus a 2025 hybrid FST+CRF+KazRoBERTa analyzer and KazMorphCorpus-2025 (150,000 sentences, >2M tokens across fiction/news/social/Wikipedia/spoken).
>
> **Numbers:** KazMorphCorpus-2025: 150K sentences, >2M tokens; apertium-kaz FST transducer
> **Relevance:** Removes MorphBPE's main obstacle for Kazakh — you can generate gold morpheme boundaries at scale to train a morphology-constrained Unigram/BPE tokenizer, a genuinely novel contribution vs SozKZ's vanilla ByteLevel-BPE and vs Sherkala's frequency merges.
> **Source:** apertium.github.io/apertium-kaz ; Frontiers 2025 (frai.2025.1708566) hybrid Kazakh analyzer · **Sweep:** `slm-architecture-2026-07`

## Related
- [[morphbpe-a-morpho-aware-tokenizer-bridging-linguistic-complexity-for-efficient|MorphBPE: A Morpho-Aware Tokenizer Bridging Linguistic Complexity for Efficient LLM Traini…]] — apertium-kaz FST + KazMorphCorpus-2025 supply the gold morpheme segmentation that MorphBPE-style tokenizers require to run on Kazakh

[[Home]]
