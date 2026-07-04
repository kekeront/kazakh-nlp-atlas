---
kb_id: "hf:deepseek-ai/deepseek-v2-lite"
type: "source"
title: "huggingface.co/deepseek-ai/DeepSeek-V2-Lite config.json (fetched direc…"
doi: null
hf_repo: "deepseek-ai/DeepSeek-V2-Lite"
year: null
topics: ["mla-sub1b", "mla-at-sub-1b-scale"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["hf:deepseek-ai/deepseek-v2-lite"]
tags: ["source", "topic/mla-sub1b", "topic/mla-at-sub-1b-scale"]
---
# huggingface.co/deepseek-ai/DeepSeek-V2-Lite config.json (fetched direc…

**Topics:** [[mla-sub1b]], [[mla-at-sub-1b-scale]]

## Source URLs
- huggingface.co/deepseek-ai/DeepSeek-V2-Lite config.json (fetched directly)

## Findings

> [!note] CLAIM — mla-sub1b
> Smallest official DeepSeek MLA config (DeepSeek-V2-Lite, 15.7B total / 2.4B active, d_model=2048, 27 layers, 16 heads) drops query compression: kv_lora_rank=512, q_lora_rank=null, qk_rope_head_dim=64, qk_nope_head_dim=128, v_head_dim=128, vocab 102,400. Consistent with GLA-paper small models (q uncompressed): q compression is a large-scale param-saving trick, not needed sub-2B.
>
> **Numbers:** d=2048/27L/16h; r_kv=512, r_q=null, rope 64, nope 128, v 128
> **Relevance:** Drop-in precedent for the lab spec: at d_model<=2048 set q_lora_rank=null; extends the KB's partially-unverified DeepSeek per-component dims with a verified small-scale variant.
> **Source:** huggingface.co/deepseek-ai/DeepSeek-V2-Lite config.json (fetched directly) · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-at-sub-1b-scale
> DeepSeek-V2-Lite — the smallest shipped pure-MLA production model with 32K context — uses exactly kv_lora_rank=512 at hidden_size=2048 (d_c = d/4, the geometry a 600M model would copy), but has NO published needle/RULER/LongBench results; its 32K context comes from YaRN extension after 4K pretraining, and its model-card evals are short-context only (MMLU/BBH/C-Eval). Even the production precedent for the lab's target config lacks 32K quality measurement.
>
> **Numbers:** config.json: hidden 2048, 27 layers, 16 heads, kv_lora_rank=512, q_lora_rank=null, qk_rope_head_dim=64, qk_nope_head_dim=128, v_head_dim=128, max_position_embeddings=163840, YaRN factor 40 (mscale 0.707); card: 16B total/2.4B active, 5.7T tokens, pretrain seq len 4K, stated 32K context
> **Relevance:** Validates the exact rank-512+rope-64 config at small hidden dims (2048, adjacent to the lab's 1536-2048) as production-viable, and shows the cheap path (pretrain 4K -> YaRN to 32K) — but confirms the quality-at-32K question is unanswered even by DeepSeek at this scale. Note q_lora_rank=null: at small scale DeepSeek dropped query compression, a config simplification the lab should copy.
> **Source:** huggingface.co/deepseek-ai/DeepSeek-V2-Lite (config.json + model card) · **Sweep:** `mla-sub1b-2026-07`

[[Home]]
