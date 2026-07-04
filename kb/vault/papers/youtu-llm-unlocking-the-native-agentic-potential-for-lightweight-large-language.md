---
kb_id: "arxiv:2512.24618"
type: "paper"
title: "Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models"
arxiv_id: "2512.24618"
doi: null
hf_repo: null
year: 2025
topics: ["mla-at-sub-1b-scale"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models", "arXiv:2512.24618", "arxiv:2512.24618"]
tags: ["paper", "topic/mla-at-sub-1b-scale"]
---
# Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models

[arXiv](https://arxiv.org/abs/2512.24618)
**Topics:** [[mla-at-sub-1b-scale]]

> [!abstract]
> We introduce Youtu-LLM, a lightweight yet powerful language model that harmonizes high computational efficiency with native agentic intelligence. Unlike typical small models that rely on distillation, Youtu-LLM (1.96B) is pre-trained from scratch to systematically cultivate reasoning and planning capabilities. The key technical advancements are as follows: (1) Compact Architecture with Long-Contex …

## Claims

> [!note] CLAIM — mla-at-sub-1b-scale
> Production adoption of dense MLA at small scale exists at 1.96B: Tencent Youtu-LLM (Dec 2025) is a dense-MLA on-device model pretrained on ~10.84T tokens with exactly DeepSeek-V2-Lite MLA dims scaled at d_model=2048: 32 layers, 16 heads, kv_lora_rank=512, q_lora_rank=1536, qk_rope_head_dim=64, qk_nope_head_dim=128, v_head_dim=128, vocab 128,256, ctx 131,072. Its own ablation, 1B-param models from scratch @500B tokens: MLA-1B beats GQA-1B on everything reported — Wiki ppl 15.4 vs 16.5, Chinese MC 37.4 vs 35.6, English MC 50.7 vs 49.6, Chinese gen 7.2 vs 6.0, English gen 18.5 vs 17.8. Stated rationale: MLA's larger intermediate projections add expressiveness under constrained param budgets; MoE rejected for on-device I/O cost.
>
> **Numbers:** 1.96B, 10.84T tokens; d=2048/32L/16h, r_kv=512, r_q=1536, rope 64, nope 128; ablation 1B@500B tok: ppl 15.4 vs 16.5, en-MC 50.7 vs 49.6, zh-MC 37.4 vs 35.6
> **Relevance:** Strongest pro-MLA from-scratch datapoint near 1B and the clearest published rationale for MLA in small on-device models — directly citable in the lab's design-spec justification.
> **Source:** arXiv 2512.24618 (Youtu-LLM), abstract + Section 3.1.2/Table 5 + Table 4, HTML v1 · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[huggingface-co-deepseek-ai-deepseek-ocr-config-json-fetched|huggingface.co/deepseek-ai/DeepSeek-OCR config.json (fetched directly)]] — Opposite production choices near sub-2B: DeepSeek-OCR ships MLA DISABLED (~570M active MoE) while Youtu-LLM ships dense MLA at 1.96B…

[[Home]]
