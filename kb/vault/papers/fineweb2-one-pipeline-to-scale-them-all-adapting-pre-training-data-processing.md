---
kb_id: "arxiv:2506.20920"
type: "paper"
title: "FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every Language"
arxiv_id: "2506.20920"
doi: null
hf_repo: null
year: 2025
topics: ["data-efficiency-10b-kazakh-10b-token-pre"]
claims: 2
uncertain_claims: 1
verdicts: []
aliases: ["FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every Language", "arXiv:2506.20920", "arxiv:2506.20920"]
tags: ["paper", "topic/data-efficiency-10b-kazakh-10b-token-pre"]
---
# FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every Language

[arXiv](https://arxiv.org/abs/2506.20920)
**Topics:** [[data-efficiency-10b-kazakh-10b-token-pre]]

> [!abstract]
> Pre-training state-of-the-art large language models (LLMs) requires vast amounts of clean and diverse text data. While the open development of large high-quality English pre-training datasets has seen substantial recent progress, training performant multilingual LLMs remains a challenge, in large part due to the inherent difficulty of tailoring filtering and deduplication pipelines to a large numb …

## Claims

> [!note] CLAIM — data-efficiency-10b-kazakh-10b-token-pre
> FineWeb-2 uses per-language dedup with 'rehydration': it keeps one doc per MinHash cluster but stores minhash_cluster_size, then UPSAMPLES documents by cluster size (per-language weights tuned to each language's cluster-filtering rate) rather than discarding duplicates — shown to improve downstream performance over both keep-all and drop-all-duplicates.
>
> **Numbers:** FineWeb-2: ~20TB/5B docs/1000+ langs; per-language MinHash dedup + cluster-size rehydration/upsampling
> **Relevance:** transferable-untested at Kazakh scale. Concrete upgrade over SozKZ's MD5-exact dedup: adopt MinHash + cluster-size rehydration for the kk pool so the highest-cluster (most-duplicated, often canonical/clean) docs are upsampled — a principled alternative to blind Wikipedia 3x/multidomain 2x upsampling in the KB.
> **Source:** arXiv:2506.20920 (FineWeb2) + HF fineweb-2 README (minhash_cluster_size field, rehydration code on GitHub) · **Sweep:** `slm-arch-for-kazakh`

> [!warning] UNCERTAIN — data-efficiency-10b-kazakh-10b-token-pre
> FineWeb2 (single multilingual pipeline) is reported to outperform CC-100, mC4, CulturaX and HPLT on downstream evals across languages while being substantially larger, and CulturaX<->FineWeb-2 share the most cross-corpus duplication (25.8B tokens overlap globally; C4<->CulturaX 25.5B).
>
> **Numbers:** CulturaX∩FineWeb-2 = 25.8B tok overlap (global); FineWeb2 > CulturaX/HPLT/mC4 on downstream (per-language ablations)
> **Relevance:** transferable-untested for kk specifically. Justifies making FineWeb-2 kk the QUALITY-primary web source and treating CulturaX kk as largely redundant with it (heavy overlap) — dedup CulturaX AGAINST FineWeb-2 rather than adding both naively.
> **Source:** arXiv:2506.20920 (FineWeb2) / HF FineWeb2 card / MarkTechPost summary · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[an-expanded-massive-multilingual-dataset-for-high-performance-language|An Expanded Massive Multilingual Dataset for High-Performance Language Technologies (HPLT)]] — FineWeb2 reports outperforming HPLT/CulturaX downstream and adds per-language rehydration over HPLT's raw Kazakh counts
- [[hplt-3-0-very-large-scale-multilingual-resources-for-llms-and-mt-mono-and-bi|HPLT 3.0: Very Large-Scale Multilingual Resources for LLMs and MT. Mono- and Bi-lingual Da…]] — Overlapping Kazakh web corpora: HPLT notes heavy dedup overlap with FineWeb-2, so naive concatenation double-counts tokens
- [[estllm-enhancing-estonian-capabilities-in-multilingual-llms-via-continued|EstLLM: Enhancing Estonian Capabilities in Multilingual LLMs via Continued Pretraining and…]] — EstLLM refutes FineWeb-2 quality for discriminative tasks — found it full of machine-translated spam by inspection
- [[wiki-apertium-org-wiki-apertium-kaz-apertium-kaz-transducer|wiki.apertium.org/wiki/Apertium-kaz (apertium-kaz transducer stats pag…]] — apertium-kaz FST coverage drops on Wikipedia and is untested on FineWeb2-style crawl — the very noisy pipeline QymyzLM would ingest

[[Home]]
