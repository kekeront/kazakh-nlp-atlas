---
kb_id: "title:wiki apertium org wiki apertium kaz apertium kaz transducer stats page"
type: "source"
title: "wiki.apertium.org/wiki/Apertium-kaz (apertium-kaz transducer stats pag…"
doi: null
hf_repo: null
year: null
topics: ["kazakh-morphological-segmentation-qualit"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:wiki apertium org wiki apertium kaz apertium kaz transducer stats page"]
tags: ["source", "topic/kazakh-morphological-segmentation-qualit"]
---
# wiki.apertium.org/wiki/Apertium-kaz (apertium-kaz transducer stats pag…

**Topics:** [[kazakh-morphological-segmentation-qualit]]

## Source URLs
- wiki.apertium.org/wiki/Apertium-kaz (apertium-kaz transducer stats page)

## Findings

> [!note] CLAIM — kazakh-morphological-segmentation-qualit
> apertium-kaz FST reports ~94.5% NAIVE coverage (fraction of tokens that receive at least one analysis, NOT correct analysis) with 36,595 stems, but this is measured only on clean edited corpora: Bible 95.29%, Azattyq news 95.07%, and Wikipedia (wp2013, 18.2M words) just 90.10%. There is NO published coverage measurement on true noisy web crawl (CulturaX/HPLT/mC4), which is dominated by borrowings, kk/ru code-switching, typos and OOV names.
>
> **Numbers:** 36,595 stems (27,433 vanilla); overall ~94.5%; Wikipedia 90.10%; Bible 95.29%; news 95.07%; Quran 96.71%. 150 CG disambiguation rules. Naive coverage != correct.
> **Relevance:** Naive coverage is an upper bound: on cleaner-than-crawl Wikipedia it is already only 90.1%, and it counts any analysis, not the correct one. Morpheme n-gram keys built naively over CulturaX/HPLT would be corrupted on exactly the OOV/borrowing/code-switch tokens that dominate web text.
> **Source:** wiki.apertium.org/wiki/Apertium-kaz (apertium-kaz transducer stats page) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[fineweb2-one-pipeline-to-scale-them-all-adapting-pre-training-data-processing|FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every…]] — apertium-kaz FST coverage drops on Wikipedia and is untested on FineWeb2-style crawl — the very noisy pipeline QymyzLM would ingest

[[Home]]
