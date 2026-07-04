---
kb_id: "title:cfgs qwen3 0 6b 4gpu yml src mha2mla patching model load py from scratch reinit block"
type: "source"
title: "cfgs/Qwen3-0_6B-4GPU.yml + src/mha2mla/patching_model_load.py (from-sc…"
doi: null
hf_repo: null
year: null
topics: ["mla-at-sub-1b-scale"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["title:cfgs qwen3 0 6b 4gpu yml src mha2mla patching model load py from scratch reinit block"]
tags: ["source", "topic/mla-at-sub-1b-scale"]
---
# cfgs/Qwen3-0_6B-4GPU.yml + src/mha2mla/patching_model_load.py (from-sc…

**Topics:** [[mla-at-sub-1b-scale]]

## Source URLs
- cfgs/Qwen3-0_6B-4GPU.yml + src/mha2mla/patching_model_load.py (from-scratch reinit block)

## Findings

> [!warning] UNCERTAIN — mla-at-sub-1b-scale
> MHA2MLA repo (2025-2026 updates) contains a Qwen3-0.6B config with is_mla_from_scratch=true: attention projections randomly re-initialized (code re-inits all attn proj weights, normal(0, initializer_range)) on the pretrained body, then ~3.1B tokens of training (12000 steps × 8 batch × 4 accum × 4 GPU × 2048 seq); low_rank=64 × n_kv=8 = shared-equivalent latent 512, rope_dim_for_mla=32/head (rope cache 256) → 768 elem/token/layer vs Qwen3-0.6B GQA-8's 2048 = 62.5% cut. No published benchmark scores found for this config (paper v1 predates Qwen3 support).
>
> **Numbers:** shared latent 512 + rope 256 = 768 elem/token/layer; ~3.1B training tokens; qk_norm supported (Qwen3 q_norm/k_norm reordered, 2-norm rope selection unsupported for Qwen3)
> **Relevance:** Closest existing artifact to the lab's exact target (0.6B, Qwen3 baseline the lab must beat) chooses shared 512, not 256 — and shows MLA is mechanically compatible with Qwen3-style QK-norm, which the lab will likely want.
> **Source:** https://github.com/JT-Ushio/MHA2MLA cfgs/Qwen3-0_6B-4GPU.yml + src/mha2mla/patching_model_load.py (from-scratch reinit block) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[qwen3-technical-report|Qwen3 Technical Report]] — Config is Qwen3-0.6B-specific: qk_norm reordering supported, 2-norm rope selection unsupported for Qwen3
- [[huggingface-co-qwen-qwen3-0-6b-base-config-json-fetched-raw|huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-…]] — MHA2MLA from-scratch config re-inits attention on the Qwen3-0.6B-Base body, the lab's canonical target

[[Home]]
