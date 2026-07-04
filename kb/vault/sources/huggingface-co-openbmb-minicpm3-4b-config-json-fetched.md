---
kb_id: "hf:openbmb/minicpm3-4b"
type: "source"
title: "huggingface.co/openbmb/MiniCPM3-4B config.json (fetched directly)"
doi: null
hf_repo: "openbmb/MiniCPM3-4B"
year: null
topics: ["mla-sub1b", "mla-at-sub-1b"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["hf:openbmb/minicpm3-4b"]
tags: ["source", "topic/mla-sub1b", "topic/mla-at-sub-1b"]
---
# huggingface.co/openbmb/MiniCPM3-4B config.json (fetched directly)

**Topics:** [[mla-sub1b]], [[mla-at-sub-1b]]

## Source URLs
- huggingface.co/openbmb/MiniCPM3-4B config.json (fetched directly)

## Findings

> [!note] CLAIM — mla-sub1b
> Smallest production kv_lora_rank shipped: MiniCPM3-4B (d_model=2560, 62 layers, 40 heads) uses kv_lora_rank=256, q_lora_rank=768, qk_rope_head_dim=32, qk_nope_head_dim=64 (head_dim 64), vocab 73,448. Cache/token/layer = 256+32 = 288 elements — i.e., a d/10 latent with rope 32 works in a shipped 4B model.
>
> **Numbers:** r_kv=256, r_q=768, rope 32, nope 64, d=2560, 62L, 40h; 288 elem/token/layer
> **Relevance:** Anchor for the lab's aggressive option (KB's MLA r=256+rope64=480MB@32K math): a 256 latent with rope 32 and head_dim 64 is production-proven, just not at 600M.
> **Source:** huggingface.co/openbmb/MiniCPM3-4B config.json (fetched directly) · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-at-sub-1b
> MiniCPM3-4B config.json verified (removes KB partial-[UNVERIFIED]): kv_lora_rank=256, q_lora_rank=768, qk_rope_head_dim=32, qk_nope_head_dim=64, v_head_dim=64, hidden 2560, 40 heads, 62 layers, vocab 73448. Rank ratio 256/2560 = d/10 — same ratio class as DeepSeek-V2 (512/5120=d/10) and V3 (512/7168=d/14). Cache = (256+32)/token/layer = 288 elem.
>
> **Numbers:** kv_lora_rank 256, q_lora 768, rope 32, nope 64, v 64, d=2560, 40h, 62L
> **Relevance:** Only production from-scratch rank-256 model; at 4B, not sub-1B. Shows halved head dims (64/64/32 vs DeepSeek 128/128/64) are how small-d models keep MLA cheap — directly copyable head-dim recipe for a 500M config.
> **Source:** https://huggingface.co/openbmb/MiniCPM3-4B/raw/main/config.json (fetched 2026-07-03) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model|DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model]] — MiniCPM3-4B rank 256 = d/10, same latent ratio class as DeepSeek-V2 (512/5120=d/10)
- [[deepseek-v3-technical-report|DeepSeek-V3 Technical Report]] — MiniCPM3's kv_lora_rank=256 is d/10, same rank-ratio class as DeepSeek-V3's 512/7168=d/14

[[Home]]
