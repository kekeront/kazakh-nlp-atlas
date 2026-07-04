---
kb_id: "hf:ibm-granite/granite-4.0-h-350m"
type: "source"
title: "model card +"
doi: null
hf_repo: "ibm-granite/granite-4.0-h-350m"
year: null
topics: ["attention-kv-sub1b-attention-kv-architec"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["hf:ibm-granite/granite-4.0-h-350m"]
tags: ["source", "topic/attention-kv-sub1b-attention-kv-architec"]
---
# model card +

**Topics:** [[attention-kv-sub1b-attention-kv-architec]]

## Source URLs
- model card +

## Findings

> [!warning] UNCERTAIN — attention-kv-sub1b-attention-kv-architec
> [transferable-untested] Closest published same-data hybrid-vs-transformer head-to-head inside the lab's size class: IBM Granite 4.0 Nano (Oct 2025, Apache-2.0, ~15T tokens). Granite-4.0-H-350M (340M; 4 attention + 28 Mamba2 layers ≈1:7, d768, 12 attn heads, 48 Mamba2 heads, MLP 2048) vs Granite-4.0-350M pure transformer (instruct variants): MMLU 5-shot 36.21 vs 35.01 (+1.20), IFEval avg 61.63 vs 55.4 (+6.23), GSM8K 8-shot 39.27 vs 30.71 (+8.56), HumanEval 38 vs 39 (-1). Caveats: not iso-architecture-controlled (layer counts differ), instruct-tuned checkpoints, training token count not in the card.
>
> **Numbers:** H-350M vs 350M: MMLU 36.21/35.01, IFEval 61.63/55.4, GSM8K 39.27/30.71, HumanEval 38/39; arch 4 attn + 28 Mamba2, d768, 340M params
> **Relevance:** Only sub-600M evidence that a Mamba2-heavy hybrid matches/beats an iso-brand transformer on knowledge and wins big on math/IF — but gains may partly be data/recipe, and Mamba2 kernels on T4 SM75 are the same unverified risk.
> **Source:** https://huggingface.co/ibm-granite/granite-4.0-h-350m model card + https://huggingface.co/blog/ibm-granite/granite-4-nano · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[an-empirical-study-of-mamba-based-language-models|An Empirical Study of Mamba-based Language Models]] — Granite-4-H-350M is a 7:1 Mamba2:attention hybrid; empirical Mamba study is its architectural lineage and closest same-family baseline

[[Home]]
