---
kb_id: "arxiv:2503.19786"
type: "paper"
title: "Gemma 3 Technical Report"
arxiv_id: "2503.19786"
doi: null
hf_repo: "unsloth/gemma-3-270m-it"
year: 2025
topics: ["sota-slm", "hybrid-efficient-attention-architectures", "training-recipes", "slm-architecture", "attention-kv-architecture-sub-1b"]
claims: 6
uncertain_claims: 1
verdicts: []
aliases: ["Gemma 3 Technical Report", "arXiv:2503.19786", "arxiv:2503.19786"]
tags: ["paper", "topic/sota-slm", "topic/hybrid-efficient-attention-architectures", "topic/training-recipes", "topic/slm-architecture", "topic/attention-kv-architecture-sub-1b"]
---
# Gemma 3 Technical Report

[arXiv](https://arxiv.org/abs/2503.19786)
**Topics:** [[sota-slm]], [[hybrid-efficient-attention-architectures]], [[training-recipes]], [[slm-architecture]], [[attention-kv-architecture-sub-1b]]

> [!abstract]
> We introduce Gemma 3, a multimodal addition to the Gemma family of lightweight open models, ranging in scale from 1 to 27 billion parameters. This version introduces vision understanding abilities, a wider coverage of languages and longer context - at least 128K tokens. We also change the architecture of the model to reduce the KV-cache memory that tends to explode with long context. This is achie …

## Claims

> [!note] CLAIM — sota-slm
> Gemma 3 270M deliberately spends ~63% of parameters on embeddings: ~170M embedding params (256K-token SentencePiece vocab) vs ~100M in transformer blocks. 32K context, sliding-window + global interleave, 6T training tokens, IFEval ~51.2%. Designed as a fine-tuning substrate, not a strong base LM — it scores 24.4% (near-random) on KazMMLU.
>
> **Numbers:** 270M total = 170M emb + 100M blocks; vocab 256K; 6T tok; IFEval 51.2%; KazMMLU 24.4%
> **Relevance:** Cautionary datapoint: a 256K multilingual vocab starves the transformer of capacity and yields near-random Kazakh knowledge. Argues AGAINST a giant multilingual vocab for a from-scratch Kazakh SLM — a compact low-fertility vocab (~50K) keeps params in the network.
> **Source:** Google Developers Blog (Introducing Gemma 3 270M); apxml.com/models/gemma-3-270m; arXiv 2503.19786 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — hybrid-efficient-attention-architectures
> Gemma 3 interleaves 5 local sliding-window attention layers per 1 global layer (5:1); local window = 1024 tokens; RoPE base is 10K on local layers and 1M on global layers. This cuts KV-cache overhead from ~60% (global-only) to <15% at 32K context with 'minimal impact on perplexity' vs a 1:1 ratio, and shrinking the window further barely moves perplexity.
>
> **Numbers:** 5:1 ratio; sliding window=1024 tok; RoPE local=10K, global=1M; KV overhead 60%->~15% at 32K; Gemma3-1B: 698M non-embedding params, 32K context, 256K vocab
> **Relevance:** Highest-leverage, lowest-risk change for a dense 500M Kazakh backbone: near-free KV savings that make an 8GB-GPU/CPU deployment viable at long context (KazQAD reading comprehension) without hurting quality. Directly upgrades the current GQA-2 dense design.
> **Source:** arXiv:2503.19786 (Gemma 3 Technical Report), Figures 3-5 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — hybrid-efficient-attention-architectures
> Gemma 3 QAT: finetuning ~5000 steps with targets from the non-quantized BF16 checkpoint (per-channel or per-block int4) reduces the perplexity increase from int4 quantization by 54% and keeps Elo within a few points of BF16. VRAM for weights collapses roughly 4x.
>
> **Numbers:** Gemma3-1B: 2GB (BF16) -> 0.5GB (int4); 4B: 8GB -> 2.6GB; 27B: 54GB -> 14.1GB; -54% perplexity degradation via QAT; ~5000 QAT steps
> **Relevance:** A 500M model becomes ~0.25-0.3GB int4 weights - trivial for an 8GB GPU and CPU-friendly. QAT (not post-training PTQ) is the pragmatic edge-deployment path and is a cheap add-on after pretraining.
> **Source:** arXiv:2503.19786 + Google Developers Blog 'Gemma 3 QAT Models' (developers.googleblog.com) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — training-recipes
> All Gemma 3 sizes are trained with knowledge distillation: 256 logits per token are sampled and weighted by teacher probabilities, student learns via cross-entropy over that sample plus standard next-token loss. Gemma 3-270M was overtrained on 6T tokens (~22,000 tok/param) vs Gemma 3-1B on 2T; 256K vocab, 140+ pretraining languages. 270M reaches IFEval 51.2% vs Qwen2.5-0.5B 42%.
>
> **Numbers:** 256 logits/token sampled; 270M=6T (~22k/param); 1B=2T; vocab 256K; 140+ langs; IFEval 270M 51.2% > Qwen2.5-0.5B 42%
> **Relevance:** Concrete, cheap-to-implement logit-KD recipe (sample 256 teacher logits, not full 50K vocab) that fits limited memory. Shows overtraining a tiny model on 6T tokens materially helps — but requires a teacher that is fluent in Kazakh.
> **Source:** arXiv 2503.19786 Gemma 3 Technical Report · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — slm-architecture
> CORRECTION (provenance): the figure 'Gemma3-270M KazMMLU 24.4%' is the lab's OWN April-2026 measurement (RTX 2070, fp16, 3-shot, qymyzlm baseline table) — NOT a number from Google's blog or arXiv 2503.19786, to which an earlier KB claim mis-attributed it.
>
> **Numbers:** Gemma3-270M: 24.4% KazMMLU 3-shot (lab measurement)
> **Relevance:** Provenance hygiene: measured-by-lab numbers must never masquerade as paper numbers.
> **Source:** qymyzlm README baseline table (measured April 2026); correction of mis-sourced claim in node for arXiv 2503.19786 · **Sweep:** `2026-07-eval-provenance`

> [!warning] UNCERTAIN — attention-kv-architecture-sub-1b
> [transferable-untested] Gemma3-270M's exact sub-300M sliding-window recipe is now pinned from config.json: 18 layers, hidden 640, 4 Q / 1 KV head (MQA), head_dim 256, 15 sliding-window layers (window=512) + 3 full-attention layers at positions {6,12,18} (5:1), rope_theta=1e6 on global / rope_local_base_freq=1e4 on local layers, ctx 32768, vocab 262144. Derived KV math: SWA cache is constant ~7.5 MiB total (2×256×15×512 elem fp16); global layers add 3 KiB/token → @32K total ≈108 MB vs Qwen3-0.6B's ~3.75 GB (~35x smaller) — the strongest existing template for long-context-capable attention at ≤300M.
>
> **Numbers:** 18L, d640, 4Q/1KV, head_dim 256, window 512, 15:3 local:global, theta 1e6/1e4, vocab 262144; KV ≈108 MB@32K vs 3.75 GB (Qwen3-0.6B)
> **Relevance:** Drop-in layer-pattern template for the from-scratch spec; config values verified via mirror rather than the gated google repo (identical-content assumption).
> **Source:** https://huggingface.co/unsloth/gemma-3-270m-it/raw/main/config.json (google org repo is gated 401; unsloth mirror) + arXiv:2503.19786 (KB) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[you-only-cache-once-decoder-decoder-architectures-for-language-models|You Only Cache Once: Decoder-Decoder Architectures for Language Models]] — Both slash KV cache for long context; SWA local:global interleave vs cache-once decoder-decoder — different mechanism, same 32K goal
- [[scaling-embeddings-outperforms-scaling-experts-in-language-models|Scaling Embeddings Outperforms Scaling Experts in Language Models]] — Gemma3-270M spends ~63% of params on 256K-vocab embeddings; this paper argues scaling embeddings beats experts — corroborating allocation
- [[decoder-hybrid-decoder-architecture-for-efficient-reasoning-with-long-generation|Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation]] — Gemma 3n's shared-KV (num_kv_shared_layers=15) is layered on top of Gemma-3's 5:1 local-SWA:global attention pattern
- [[huggingface-co-blog-gemma4-fetched-2026-07-03|huggingface.co/blog/gemma4 (fetched 2026-07-03)]] — Direct Gemma lineage: Gemma 3 -> 3n -> 4, all shipping trailing KV sharing without published quality cost
- [[config-json-via-huggingface-co-unsloth-gemma-3n-e2b-mirror|config.json via huggingface.co/unsloth/gemma-3n-E2B (mirror]] — Gemma-3n's headline 2x prefill speedup is measured against Gemma 3 4B (same lineage, no cross-layer sharing)

[[Home]]
