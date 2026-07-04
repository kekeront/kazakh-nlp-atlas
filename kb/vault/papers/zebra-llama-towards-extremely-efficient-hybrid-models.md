---
kb_id: "arxiv:2505.17272"
type: "paper"
title: "Zebra-Llama: Towards Extremely Efficient Hybrid Models"
arxiv_id: "2505.17272"
doi: null
hf_repo: null
year: 2025
topics: ["mla-upcycling-bespoke-tokenizer"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["Zebra-Llama: Towards Extremely Efficient Hybrid Models", "arXiv:2505.17272", "arxiv:2505.17272"]
tags: ["paper", "topic/mla-upcycling-bespoke-tokenizer"]
---
# Zebra-Llama: Towards Extremely Efficient Hybrid Models

[arXiv](https://arxiv.org/abs/2505.17272)
**Topics:** [[mla-upcycling-bespoke-tokenizer]]

> [!abstract]
> With the growing demand for deploying large language models (LLMs) across diverse applications, improving their inference efficiency is crucial for sustainable and democratized access. However, retraining LLMs to meet new user-specific requirements is prohibitively expensive and environmentally unsustainable. In this work, we propose a practical and scalable alternative: composing efficient hybrid …

## Claims

> [!warning] UNCERTAIN — mla-upcycling-bespoke-tokenizer
> AMD's own follow-up confirms the same-tokenizer-teacher dependence at 1B: Zebra-Llama-1B (4 MLA + 12 Mamba2 layers, post-training adaptation of Llama-3.2-1B-Instruct with intermediate-layer distillation from an 8B teacher) reaches 3.91% KV size (~25.6x) and claims '100% of average zero-shot performance', but its DPO card shows MMLU dropping 46.09 -> 37.91 (-8.2 pts) even with the 8B teacher — deep-compression conversions remain lossy on knowledge-heavy tasks, which is exactly what KazMMLU measures.
>
> **Numbers:** KV 3.91% of baseline; MMLU 0.4609 -> 0.3791; arc_challenge acc_norm 0.3797 -> 0.4232; teacher = 8B same-tokenizer
> **Relevance:** Even with the strongest published recipe and a big teacher, 1B-scale deep KV compression costs ~8 MMLU points — a red flag for a KazMMLU-targeted 600M model considering aggressive conversion.
> **Source:** HF amd/Zebra-Llama-1B-4MLA-12Mamba-DPO model card; arXiv:2505.17272 (Zebra-Llama); ROCm blog AMD-HybridLM · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[long-context-aware-upcycling-a-new-frontier-for-hybrid-llm-scaling|Long-Context Aware Upcycling: A New Frontier for Hybrid LLM Scaling]] — Both are hybrid-model upcycling of pretrained transformers; long-context-aware upcycling extends the frontier Zebra-Llama's short-eval…
- [[kimi-linear-an-expressive-efficient-attention-architecture|Kimi Linear: An Expressive, Efficient Attention Architecture]] — Both hybridize attention with linear layers; Kimi Linear reports full-MLA beats its own hybrid on RULER-128K, Zebra collapses

[[Home]]
