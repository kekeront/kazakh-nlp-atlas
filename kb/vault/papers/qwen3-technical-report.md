---
kb_id: "arxiv:2505.09388"
type: "paper"
title: "Qwen3 Technical Report"
arxiv_id: "2505.09388"
doi: null
hf_repo: "Qwen/Qwen3-0.6B-Base"
year: 2025
topics: ["sota-slm", "training-recipes", "attention-kv-sub1b-attention-kv-architec", "residual-stream-stability-qymyzlm-design", "small-lm-training-recipes-qymyzlm-design"]
claims: 6
uncertain_claims: 0
verdicts: []
aliases: ["Qwen3 Technical Report", "arXiv:2505.09388", "arxiv:2505.09388"]
tags: ["paper", "topic/sota-slm", "topic/training-recipes", "topic/attention-kv-sub1b-attention-kv-architec", "topic/residual-stream-stability-qymyzlm-design", "topic/small-lm-training-recipes-qymyzlm-design"]
---
# Qwen3 Technical Report

[arXiv](https://arxiv.org/abs/2505.09388)
**Topics:** [[sota-slm]], [[training-recipes]], [[attention-kv-sub1b-attention-kv-architec]], [[residual-stream-stability-qymyzlm-design]], [[small-lm-training-recipes-qymyzlm-design]]

> [!abstract]
> In this work, we present Qwen3, the latest version of the Qwen model family. Qwen3 comprises a series of large language models (LLMs) designed to advance performance, efficiency, and multilingual capabilities. The Qwen3 series includes models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion. A key innovation in Qwen3 is the integration …

## Claims

> [!note] CLAIM — sota-slm
> Qwen3-0.6B-Base: 28 layers, hidden 1024, 16 query / 8 KV heads (GQA 2:1), FFN 3072, vocab 151,669 (BBPE), 32K context, 0.44B non-embedding params, tied embeddings, trained on 36T tokens across 119 languages. Adds QK-Norm and removes QKV-bias to stabilize small-scale training. Measured 32.8% on KazMMLU (user's grounding) — the strongest sub-1B baseline on Kazakh.
>
> **Numbers:** 28L, d1024, 16Q/8KV, vocab151669, 32K ctx, 36T tok, 119 langs, non-emb 0.44B
> **Relevance:** This is THE boundary to beat on Kazakh at ~600M. Its edge comes from 36T tokens + QK-Norm, not exotic architecture; the paper must beat 32.8% KazMMLU with ~3500x fewer Kazakh tokens, so tokenizer efficiency and transfer must carry the gap.
> **Source:** HF Qwen/Qwen3-0.6B-Base card; arXiv 2505.09388 (Qwen3 Technical Report) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — training-recipes
> Qwen3 (the user's strongest measured ~500M baseline at 32.8% KazMMLU) was pretrained on 36T tokens over 119 languages in 3 stages: ~30T general (4K ctx) -> ~5T STEM/coding/reasoning/synthetic (4K) -> long-context (32K). Qwen3-0.6B thus sees ~60,000 tokens/param (extreme deployment overtraining) and its thinking mode comes from a strong-to-weak distillation pipeline (off-policy then on-policy).
>
> **Numbers:** 36T tokens, 119 langs; 30T+5T+long-ctx; Qwen3-0.6B ~60,000 tok/param; KazMMLU 32.8% (user-measured)
> **Relevance:** Explains why beating Qwen3-0.6B on a ~$264 budget can't be won on raw token count — it must be won on Kazakh data density, tokenizer fertility (<2.0), and targeted architecture. The distillation-thinking pipeline is the template if adding a Kazakh reasoning mode.
> **Source:** arXiv 2505.09388 Qwen3 Technical Report · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — attention-kv-sub1b-attention-kv-architec
> [tested-on-Kazakh, via lab baseline] Qwen3-0.6B-Base attention is FROZEN for the QLoRA-CPT track and its exact config is now pinned from HF config.json: 28 layers, hidden 1024, 16 Q / 8 KV heads (GQA-2:1), head_dim 128, QK-Norm, rope_theta=1,000,000, max_position_embeddings=32768, intermediate 3072, tied embeddings, torch_dtype bfloat16, config vocab_size=151936 (KB's 151,669 is the tokenizer's real token count; 151936 is the padded embedding rows — clarification, not a conflict). Derived KV math: 2×8×128×28 = 57,344 elem/token = 112 KiB/token fp16 → ~0.94 GB per sequence @8K, ~3.75 GB @32K (consistent with KB's Kinetics 3.5GB node). On a 16GB T4 with ~1.5GB fp16 weights this caps 3-shot eval batching and rules out long-context work in track 1.
>
> **Numbers:** 28L, d1024, 16Q/8KV, head_dim 128, theta=1e6, ctx 32768, vocab_size 151936; KV = 112 KiB/tok fp16; 0.94 GB@8K, 3.75 GB@32K per seq
> **Relevance:** Every KV/latency property of the CPT deliverable is fixed by this config; design-panel must treat attention changes as from-scratch-only (or post-hoc MLA conversion per KB MHA2MLA/X-EcoMLA nodes) and budget T4 eval memory from these numbers.
> **Source:** https://huggingface.co/Qwen/Qwen3-0.6B-Base/raw/main/config.json (fetched 2026-07-04) + arXiv:2505.09388 (KB) + derived arithmetic · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — residual-stream-stability-qymyzlm-design
> [transferable-untested] Qwen3 (our CPT backbone) removed Qwen2's QKV-bias and added QK-Norm specifically for training stability; QK-Norm constrains query/key dynamic range, suppressing attention-logit outliers (Qwen3 shows significantly lower activation kurtosis than Qwen2.5) and preventing FP16 numerical overflow. The 'now' path (QLoRA-CPT of Qwen3-0.6B-Base in fp16 on T4) therefore already carries the key fp16 attention safeguard — no architectural stability intervention is needed or possible on the CPT path; residual-stream findings in this sweep apply to the from-scratch path only.
>
> **Numbers:** QKV-bias removed, QK-Norm added (per-head RMSNorm on Q and K); lower kurtosis vs Qwen2.5; fp16 overflow prevention
> **Relevance:** Scopes the design panel correctly: memory/attention/residual innovations are from-scratch-only decisions; the QLoRA-CPT track's fp16 risk on T4 reduces to standard dynamic loss scaling + data dedup, since the frozen 4-bit backbone already has QK-norm. Prevents wasted panel time on retrofitting stability tricks into CPT.
> **Source:** arXiv:2505.09388 (Qwen3 Technical Report, Sec. architecture; search-verified 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — small-lm-training-recipes-qymyzlm-design
> [tested-on-Kazakh (as lab-measured baseline)] Qwen3-0.6B-Base, the CPT target, verified config from tech report: 28 layers, 16Q/8KV heads (GQA), tied embeddings, 32K context, vocab 151,669 byte-level BPE, QK-Norm in attention, SwiGLU+RoPE+pre-RMSNorm. Pretrained ~36T tokens in 3 stages (>30T general @ seq 4096; ~5T reasoning-heavy; hundreds of B long-context @ 32K). Lab already measured it at 32.8% KazMMLU 3-shot.
>
> **Numbers:** 28L, 16Q/8KV, vocab 151,669, tied emb, 36T tokens (30T+5T+~0.x T)
> **Relevance:** (a) QK-norm is already inside Qwen3-0.6B — fp16 CPT on T4 inherits its attention-logit stability for free; (b) 151,669-token vocab with tied embeddings ≈ 155M embedding params at d=1024, ~26% of total — vocabulary surgery (Kazakh-focused vocab swap/prune) is the single biggest active-param lever for the ≤600M budget; (c) 36T-token base explains why the 32.8% KazMMLU bar is beatable mainly through Kazakh data, not general recipe.
> **Source:** arXiv:2505.09388 (Qwen3 Technical Report), Table 1 + Sec. 3; lab KB baseline table · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] Qwen3's production strong-to-weak distillation pipeline covers 0.6B students (Qwen3-0.6B itself is a distilled student): phase 1 off-policy distillation on teacher outputs (/think + /no_think modes), phase 2 on-policy distillation — student generates sequences, then minimizes KL to teacher (Qwen3-32B or 235B-A22B) logits. Reported cost: ~1/10 the GPU hours of the full 4-stage post-training pipeline with better results. No per-pair benchmark table is published.
>
> **Numbers:** students 0.6B-14B + 30B-A3B; teachers 32B/235B-A22B; 1/10 GPU hours vs 4-stage RL pipeline
> **Relevance:** The best published sub-1B post-training recipe on free-compute budgets: after Kazakh CPT, on-policy logit-KL from any strong SAME-TOKENIZER teacher replaces RL. For QymyzLM the only same-tokenizer teachers are larger Qwen3 models (1.7B/4B fit T4 inference in 4-bit) — but their Kazakh quality is the bottleneck; untested for Kazakh.
> **Source:** arXiv:2505.09388, Sec. 4 (strong-to-weak distillation) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[peri-ln-revisiting-normalization-layer-in-the-transformer-architecture|Peri-LN: Revisiting Normalization Layer in the Transformer Architecture]] — Both target residual/attention stability at scale; Qwen3 uses QK-Norm, Peri-LN repositions the norm
- [[reusing-overtrained-language-models-saturates-scaling|Reusing Overtrained Language Models Saturates Scaling]] — Qwen3-0.6B is overtrained ~60k tok/param; this paper warns overtrained models saturate when reused as CPT init — direct risk to the…
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] — KazByte adapts this exact Qwen3-0.6B backbone to Kazakh via a byte-level adapter
- [[cfgs-qwen3-0-6b-4gpu-yml-src-mha2mla-patching-model-load-py|cfgs/Qwen3-0_6B-4GPU.yml + src/mha2mla/patching_model_load.py (from-sc…]] — Config is Qwen3-0.6B-specific: qk_norm reordering supported, 2-norm rope selection unsupported for Qwen3
- [[mdpi-make-8-5-128|MDPI MAKE 8(5):128]] — Qolda is a Qwen3-4B adaptation that beats its own backbone; Qwen3 is the base model it adapts

[[Home]]
