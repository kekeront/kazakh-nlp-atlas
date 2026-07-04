---
kb_id: "title:mdpi applied sciences 14 13 5369 a benchmark for morphological segmentation in uyghur and kazakh tables incl oov table 8"
type: "source"
title: "MDPI Applied Sciences 14(13):5369, 'A Benchmark for Morphological Segm…"
doi: null
hf_repo: null
year: null
topics: ["kazakh-morphological-segmentation-qualit"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:mdpi applied sciences 14 13 5369 a benchmark for morphological segmentation in uyghur and kazakh tables incl oov table 8"]
tags: ["source", "topic/kazakh-morphological-segmentation-qualit"]
---
# MDPI Applied Sciences 14(13):5369, 'A Benchmark for Morphological Segm…

**Topics:** [[kazakh-morphological-segmentation-qualit]]

## Source URLs
- MDPI Applied Sciences 14(13):5369, 'A Benchmark for Morphological Segmentation in Uyghur and Kazakh' (Tables incl. OOV Table 8)

## Findings

> [!note] CLAIM — kazakh-morphological-segmentation-qualit
> On a clean lab-annotated Kazakh gold set (16,000 train words / 2,000 test words), UNSUPERVISED segmenters collapse: Morfessor 27.26% F1, BPE 27.83% F1, MMSeg 35.22% F1; only SUPERVISED models reach FEMSeg 92.34% / FEMSeg-CRF 92.84% F1. Critically, MMSeg's OOV recall on Kazakh is just 8.52% (vs 46.69% on Uyghur), attributed to long stems and morphological ambiguity.
>
> **Numbers:** Kazakh gold: Morfessor F1 27.26%, BPE 27.83%, MMSeg 35.22%, FEMSeg 92.34%, FEMSeg-CRF 92.84%. MMSeg Kazakh OOV recall 8.52% vs Uyghur 46.69%. Data 16K train / 2K test words, 5,686 morpheme types, lab-annotated (not web).
> **Relevance:** This is the single strongest quantitative signal against the plan: unsupervised Kazakh segmentation is near-useless (~27% F1) and even the best model generalizes to unseen stems at only 8.52% recall. Web crawl is overwhelmingly OOV, so naive corpus-wide morpheme keys would be systematically wrong on novel words.
> **Source:** MDPI Applied Sciences 14(13):5369, 'A Benchmark for Morphological Segmentation in Uyghur and Kazakh' (Tables incl. OOV Table 8) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[why-do-language-models-perform-worse-for-morphologically-complex-languages|Why do language models perform worse for morphologically complex languages?]] — Kazakh's 8.52% OOV recall and unsupervised-segmenter collapse concretize why LMs perform worse for morphologically complex languages
- [[improving-low-resource-morphological-inflection-via-self-supervised-objectives|Improving Low-Resource Morphological Inflection via Self-Supervised Objectives]] — Both tackle low-resource Kazakh/agglutinative morphology under scarce annotation; benchmark quantifies OOV failure this method aims to fix

[[Home]]
