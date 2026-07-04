---
type: "moc"
topic: "kazakh-morphological-segmentation-qualit"
nodes: 8
papers: 2
sources: 6
uncertain_claims: 3
tags: ["moc"]
---
# Topic: kazakh-morphological-segmentation-qualit

The established picture: on clean, lab-annotated or synthetic Kazakh data, SUPERVISED morphological segmenters win big (FEMSeg 92.34% F1, FEMSeg-CRF 92.84%; CSE-guided FEMSeg_kaz 99.62% morph-F1 on 2.33M synthetic wordforms), while UNSUPERVISED segmenters collapse (Morfessor 27.26%, BPE 27.83%, MMSeg 35.22% F1), and MMSeg's Kazakh OOV recall is just 8.52% vs 46.69% on Uyghur — long stems and morphological ambiguity are the culprit. Cross-lingual evidence (QuechuaTok) confirms a load-bearing caveat: low fertility can be a MISLEADING surface-memorization artifact — plain BPE hits fertility 1.636 but only 6.67% morpheme-boundary accuracy, whereas morphology-aware PRPE reaches 83.33% MorphAcc at fertility 1.797 (though on a fragile 15-word eval set). The contested/unresolved core: every high-accuracy Kazakh number is measured on curated/gold/synthetic text — apertium-kaz FST reports ~94.5% NAIVE (coverage, not correctness) dropping to 90.10% on Wikipedia, and the hybrid KazMorphCorpus analyzer needs FST+CRF+KazRoBERTa stacked to reach 92.3% open-vocab (FST alone only 81.5%). NO published number exists for segmenter accuracy on noisy monolingual crawl (CulturaX/HPLT/mC4) — exactly the data QymyzLM targets, where borrowings, code-switching, typos and OOV names dominate. The open question that decides QymyzLM's tokenizer axis: does morphological segmentation quality actually buy DOWNSTREAM accuracy? The direct baseline SozKZ says no — its dedicated low-fertility 50K BPE (2-3x fertility advantage, zero morphology) still loses knowledge QA to an un-adapted Qwen2.5-0.5B (30.3 vs 31.5 MC-QA).

## Frontier highlights
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — Direct baseline: best low-fertility Kazakh BPE, zero morphology, still loses knowledge QA to un-adapted Qwen2.5-0.5B
- [[quechuatok-morphological-boundary-accuracy-as-a-necessary-metric-for-tokenizer|QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer…]] — Cross-lingual proof that low fertility (BPE 1.636) hides 6.67% morph-accuracy; morphology-aware PRPE 83.33% at fert 1.797
- [[mdpi-applied-sciences-14-13-5369-a-benchmark-for|MDPI Applied Sciences 14(13):5369, 'A Benchmark for Morphological Segm…]] — Unsupervised segmenters collapse to ~27% F1 vs supervised 92%; Kazakh OOV recall only 8.52% vs Uyghur 46.69%
- [[frontiers-pmc12741073-hybrid-ai-architectures-for-automatic|Frontiers/PMC12741073 (Hybrid AI architectures for automatic text corr…]] — Affordable FST-only stage just 81.5% open-vocab; 92.3% needs FST+CRF+KazRoBERTa; errors are web-text failure modes
- [[frontiers-pmc12741073-kazmorphcorpus-2025-spec-table-1|Frontiers/PMC12741073 (KazMorphCorpus-2025 spec, Table 1)]] — All high-accuracy Kazakh segmentation is on curated/gold/synthetic; zero measurement on noisy crawl
- [[mdpi-information-17-2-128-doi-10-3390-info17020128|MDPI Information 17(2):128 / doi 10.3390/info17020128, 'Morphology-Awa…]] — 99.62% morph-F1 achieved on 2.33M synthetic harmony wordforms — no OOV or noise-robustness benchmark

## Papers (2)
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[quechuatok-morphological-boundary-accuracy-as-a-necessary-metric-for-tokenizer|QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation in Agglut…]] (2026) — kazakh-morphological-segmentation-qualit

## Sources & findings (6)
- [[frontiers-pmc12741073-hybrid-ai-architectures-for-automatic|Frontiers/PMC12741073 (Hybrid AI architectures for automatic text corr…]] — The 2025 hybrid Kazakh analyzer (KazMorphCorpus-2025) shows the affordable FST-only stage is only 81.5% accurate on OPEN…
- [[mdpi-information-17-2-128-doi-10-3390-info17020128|MDPI Information 17(2):128 / doi 10.3390/info17020128, 'Morphology-Awa…]] — The CSE-guided Kazakh morphology tokenizer's headline segmentation F1 (FEMSeg_kaz_v2 morph_F1 99.62%; v3 95.55% on an ex…
- [[frontiers-pmc12741073-kazmorphcorpus-2025-spec-table-1|Frontiers/PMC12741073 (KazMorphCorpus-2025 spec, Table 1)]] — KazMorphCorpus-2025 and every high-accuracy Kazakh segmentation result are measured on curated/gold/synthetic data, NOT…
- [[mdpi-applied-sciences-14-13-5369-a-benchmark-for|MDPI Applied Sciences 14(13):5369, 'A Benchmark for Morphological Segm…]] — On a clean lab-annotated Kazakh gold set (16,000 train words / 2,000 test words), UNSUPERVISED segmenters collapse: Morf…
- [[mdpi-information-17-2-128-cse-guided-kazakh-tokenizer|MDPI Information 17(2):128 (CSE-guided Kazakh tokenizer, FEMSeg_kaz ar…]] — No paper reports an isolated vowel-harmony suffix-allomorph mis-segmentation rate for Kazakh. The signal is indirect: th…
- [[wiki-apertium-org-wiki-apertium-kaz-apertium-kaz-transducer|wiki.apertium.org/wiki/Apertium-kaz (apertium-kaz transducer stats pag…]] — apertium-kaz FST reports ~94.5% NAIVE coverage (fraction of tokens that receive at least one analysis, NOT correct analy…

[[Home]]
