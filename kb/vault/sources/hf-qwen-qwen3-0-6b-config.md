---
kb_id: "title:hf qwen qwen3 0 6b config user provided kazmmlu baseline"
type: "source"
title: "HF Qwen/Qwen3-0.6B config"
doi: null
hf_repo: null
year: null
topics: ["hybrid-efficiency-efficient-attention-se"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:hf qwen qwen3 0 6b config user provided kazmmlu baseline"]
tags: ["source", "topic/hybrid-efficiency-efficient-attention-se"]
---
# HF Qwen/Qwen3-0.6B config

**Topics:** [[hybrid-efficiency-efficient-attention-se]]

## Source URLs
- HF Qwen/Qwen3-0.6B config
- user-provided KazMMLU baseline

## Findings

> [!note] CLAIM — hybrid-efficiency-efficient-attention-se
> Baseline architecture to beat - Qwen3-0.6B: 28 layers, hidden 1024, 16 query heads / 8 KV heads (GQA-2), head_dim 128, FFN 3072, vocab 151,936, 32K context, SwiGLU+RMSNorm+RoPE. It scores KazMMLU 32.8% (best-tier measured ~500M on Kazakh).
>
> **Numbers:** 28L, d=1024, 16Q/8KV heads, head_dim 128, FFN 3072, vocab 151,936, ctx 32K; KazMMLU 32.8%
> **Relevance:** Defines the exact competitor config and the giant-vocab cost (151.9K) the Kazakh model can beat with a compact Kazakh-optimized 50K tokenizer - freeing params for depth/width at equal budget.
> **Source:** HF Qwen/Qwen3-0.6B config; user-provided KazMMLU baseline · **Sweep:** `slm-architecture-2026-07`

## Related
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhst…]] — Paper's sub-1B analysis pins Qwen3-0.6B ~32.8 as best sub-1B KazMMLU — the lab's canonical baseline model
- [[home-altairzhambyl-projects-slms-qymyzlm-evallab-results|/home/altairzhambyl/projects/SLMs/qymyzlm/evallab/results/2026-04-30__…]] — Lab's measured 0.328 confirms the user-provided Qwen3-0.6B KazMMLU baseline figure under a fully specified runner

[[Home]]
