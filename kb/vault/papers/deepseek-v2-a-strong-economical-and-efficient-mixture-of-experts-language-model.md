---
kb_id: "arxiv:2405.04434"
type: "paper"
title: "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model"
arxiv_id: "2405.04434"
doi: null
hf_repo: null
year: 2024
topics: ["deepseek-tech", "hybrid-efficiency-efficient-attention-se", "kazakh-turkic-nlp", "novelty-check"]
claims: 6
uncertain_claims: 2
verdicts: []
aliases: ["DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model", "arXiv:2405.04434", "arxiv:2405.04434"]
tags: ["paper", "topic/deepseek-tech", "topic/hybrid-efficiency-efficient-attention-se", "topic/kazakh-turkic-nlp", "topic/novelty-check"]
---
# DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

[arXiv](https://arxiv.org/abs/2405.04434)
**Topics:** [[deepseek-tech]], [[hybrid-efficiency-efficient-attention-se]], [[kazakh-turkic-nlp]], [[novelty-check]]

> [!abstract]
> We present DeepSeek-V2, a strong Mixture-of-Experts (MoE) language model characterized by economical training and efficient inference. It comprises 236B total parameters, of which 21B are activated for each token, and supports a context length of 128K tokens. DeepSeek-V2 adopts innovative architectures including Multi-head Latent Attention (MLA) and DeepSeekMoE. MLA guarantees efficient inference …

## Claims

> [!note] CLAIM — deepseek-tech
> MLA (DeepSeek-V2, arXiv 2405.04434) reduces KV cache 93.3% vs the MHA baseline (DeepSeek-67B) and in ablations OUTPERFORMS MHA, MQA and GQA on downstream benchmarks while using far less cache; it enabled 5.76x higher generation throughput. KV cache per token per layer = (d_c + d_h_rope) elements; with d_c=512, d_h_rope=64 that is 576 elements = 4.5*d_h, i.e. roughly the cache of GQA with ~2.25 groups but with MHA-or-better quality.
>
> **Numbers:** 93.3% cache cut; 5.76x throughput; cache = d_c+d_h_rope = 576 elem/token/layer (~GQA-2.25)
> **Relevance:** Core case for swapping the user's GQA-2 for MLA: MLA matches/beats full MHA quality at ~GQA-2.25 cache. The quality-not-just-memory angle matters more than raw cache at 500M/short-context.
> **Source:** arXiv:2405.04434 (DeepSeek-V2); the '2.25 groups' is derived from the 4.5*d_h formula · **Sweep:** `slm-architecture-2026-07`

> [!warning] UNCERTAIN — deepseek-tech
> DeepSeek-V2 MLA exact config: d_model=5120, n_heads=128, per-head d_h=128, kv_lora_rank d_c=512, q_lora_rank=1536, decoupled qk_rope_head_dim=64, qk_nope_head_dim=128, v_head_dim=128. RoPE is DECOUPLED: only a 64-dim slice of q/k carries RoPE, the rest is compressed and RoPE-free, which is what lets the latent be cached. DeepSeek-V3 keeps the same d_c=512, q_lora_rank=1536, rope_dim=64 at d_model=7168.
>
> **Numbers:** d_c=512, q_lora_rank=1536, rope_dim=64, nope_dim=128, v_dim=128, n_h=128, d_h=128
> **Relevance:** Gives exact ratios to scale down. d_c/d_model ~= 0.1 -> for the Kazakh d_model~1536, a proportional kv_lora_rank ~= 192-256 with decoupled rope_dim 32-64. Concrete numbers to put in the spec, not 'consider MLA'.
> **Source:** arXiv:2405.04434 (V2), arXiv:2412.19437 (V3) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[deepseek-v3-technical-report]]

> [!note] CLAIM — hybrid-efficiency-efficient-attention-se
> MLA vs GQA at the KV-cache level: DeepSeek's ablations show MLA matches/beats MHA perplexity while GQA loses ~0.5 and MQA ~1.5 perplexity; MLA stores ~70KB/token vs 192-328KB/token for GQA models (2.7-4.7x smaller cache) by compressing all K/V into one low-rank latent instead of sharing heads.
>
> **Numbers:** MLA cache ~70KB/tok vs GQA 192-328KB/tok (2.7-4.7x); GQA +0.5 / MQA +1.5 perplexity vs MHA
> **Relevance:** MLA is the highest-quality-per-KV-byte option, but its advantage grows with context length and model size; at 500M with short Kazakh sequences the simpler GQA-2 already captures most of the benefit. MLA becomes worth the complexity only if long-context (32K KazQAD) is a hard requirement.
> **Source:** arXiv:2405.04434 (DeepSeek-V2) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-turkic-nlp
> MLA gives a concrete cache win over the user's planned GQA-2. DeepSeek-V2 MLA config: kv_lora_rank d_c=512, decoupled-RoPE per-head dim d_h^R=64, q_lora_rank 1536, v/qk head dim 128, 128 heads, d=5120. KV cache per token = (d_c + d_h^R)*L = 576*L elements — equivalent to GQA with only 2.25 groups, a 93.3% reduction vs MHA, while scoring STRONGER than MHA (GQA/MQA lose quality to save cache; MLA does not).
>
> **Numbers:** d_c=512, d_h^R=64 -> 576*L elem/token = GQA-2.25 groups; 93.3% less than MHA; stronger than MHA
> **Relevance:** Actionable swap: replace GQA-2 with MLA. At d~1280-1536 for a 600M model, set kv_lora_rank~256-320 and qk_rope_head_dim~32-64; cache per token ~ (288-384)*L vs GQA-2's ~2*n_kv*d_head*L. This roughly halves-to-quarters the KV cache vs GQA-2 with equal-or-better quality, freeing A100-40GB memory for longer ctx or larger batch.
> **Source:** arXiv 2405.04434 (DeepSeek-V2), html v5 architecture tables · **Sweep:** `slm-architecture-2026-07`

> [!warning] UNCERTAIN — novelty-check
> MLA (multi-head latent attention) is absent from the user's current design (they use GQA 2:1) and would be a concrete, quantifiable efficiency upgrade — but MLA itself is not novel, so it can support but not carry the paper.
>
> **Numbers:** MLA vs GQA-8: ~2x smaller KV cache; MLA vs MHA: ~8-9x smaller (~512 latent values/token vs 4096); DeepSeek-V3 70KB/token vs 192-328KB/token for GQA models (2.7-4.7x)
> **Relevance:** For a 500-600M Kazakh SLM (d~1536), swapping GQA-2 for MLA (kv_lora_rank ~256-512) yields ~2-4x KV-cache reduction, aiding long agglutinative sequences on the A100-40GB spot budget. Add as an efficiency ablation, not a headline claim.
> **Source:** arXiv:2405.04434 (DeepSeek-V2 MLA); compression figures aggregated from MLA analyses (uncertain on exact kk-scale numbers) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — novelty-check
> No paper combines MLA + sparse/lookup memory + morphology-aware tokenization in a single model for any language. Each pair exists separately (memory+MoE, morphology+tokenizer, MLA+memory in DeepSeek), but the triple — purpose-built for one low-resource agglutinative language at sub-1B — is unoccupied.
>
> **Numbers:** Extensive search (multiple formulations) returned zero hits for the combined triple at SLM scale
> **Relevance:** The paper's defensible novelty is the COMBINATION + morpheme-conditioning + Kazakh target, not any single component. State this explicitly as the contribution and cite each component's origin to preempt reviewer novelty objections.
> **Source:** Synthesis across arXiv:2405.04434, 2601.07372, 2502.00894, 2603.20854 (no combined prior found) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[simple-and-scalable-strategies-to-continually-pre-train-large-language-models|Simple and Scalable Strategies to Continually Pre-train Large Language Models]] — DeepSeek-V2 scales Ibrahim's replay recipe: 30% replay + non-decayed checkpoint for 6T-token CPT
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Trans…]] — That work converts existing MHA models to V2-style MLA for economical inference — builds on this MLA formulation
- [[multi-head-low-rank-attention|Multi-Head Low-Rank Attention]] — Multi-Head Low-Rank Attention is a successor to V2's MLA; competing low-rank KV-compression at equal cache
- [[tensor-product-attention-is-all-you-need|Tensor Product Attention Is All You Need]] — TPA synthesis: DeepSeek-V2's MLA>MHA/MQA/GQA ablation does not transfer monotonically below 1B
- [[huggingface-co-openbmb-minicpm3-4b-config-json-fetched|huggingface.co/openbmb/MiniCPM3-4B config.json (fetched directly)]] — MiniCPM3-4B rank 256 = d/10, same latent ratio class as DeepSeek-V2 (512/5120=d/10)

[[Home]]
