---
kb_id: "arxiv:2412.19437"
type: "paper"
title: "DeepSeek-V3 Technical Report"
arxiv_id: "2412.19437"
doi: null
hf_repo: null
year: 2024
topics: ["deepseek-tech", "inference-tts", "novelty-check"]
claims: 6
uncertain_claims: 1
verdicts: []
aliases: ["DeepSeek-V3 Technical Report", "arXiv:2412.19437", "arxiv:2412.19437"]
tags: ["paper", "topic/deepseek-tech", "topic/inference-tts", "topic/novelty-check"]
---
# DeepSeek-V3 Technical Report

[arXiv](https://arxiv.org/abs/2412.19437)
**Topics:** [[deepseek-tech]], [[inference-tts]], [[novelty-check]]

> [!abstract]
> We present DeepSeek-V3, a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2. Furthermore, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for loa …

## Claims

> [!note] CLAIM — deepseek-tech
> Multi-Token Prediction has a capability threshold ~1B-3B: below it MTP does NOT improve generative-task performance and a naive MTP objective can DEGRADE next-token performance for small models (curriculum learning mitigates). DeepSeek-V3 uses 1 sequential MTP module predicting the next 2 tokens; the 2nd-token head reaches >80-85% acceptance, giving ~1.8x speculative-decoding speedup. MTP's training-signal gain (~+2.4% avg) was measured on an 8B-active MoE, not a sub-1B dense model.
>
> **Numbers:** threshold 1-3B; V3: 1 MTP module, depth-1, 2 tokens, >80% accept, 1.8x decode; +2.4% avg @8B-active
> **Relevance:** Warns against relying on MTP for a training-quality boost at 500M (likely null or negative). If used, use it ONLY as an inference speculative-decoding head, or apply a curriculum (NTP-first, add MTP late). Not a KazMMLU lever at this size.
> **Source:** arXiv:2412.19437 (V3), arXiv:2508.19228, MiniCPM4 (arXiv:2506.07900) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[minicpm4-ultra-efficient-llms-on-end-devices]]

> [!note] CLAIM — deepseek-tech
> FP8 training (DeepSeek-V3) uses fine-grained quant: tile-wise 1x128 for activations, block-wise 128x128 for weights (Nc=128), keeping embedding, output head, MoE gating, norms and attention in BF16/FP32; validated at 671B with <0.25% relative error. CRITICAL hardware fact: FP8 tensor cores exist only on Hopper (H100) / Ada / Blackwell. An A100 (Ampere) has NO FP8 support, so the user's '1x A100 40GB spot' budget CANNOT use FP8 training and must train in BF16.
>
> **Numbers:** tile 1x128 act / block 128x128 wt, Nc=128, <0.25% err @671B; A100=no FP8
> **Relevance:** Decisive: remove FP8 from the Kazakh training plan on A100. It is not an available lever on that GPU; BF16 is the target precision. Only relevant if they switch to an H100/H200 spot instance.
> **Source:** arXiv:2412.19437 (DeepSeek-V3); NVIDIA Ampere vs Hopper FP8 support · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — inference-tts
> Self-speculative decoding via multi-token-prediction heads gives lossless speedups: DeepSeek-V3 MTP1 acceptance >80% -> ~1.8x throughput. FastMTP: 2.03x at K=3 draft tokens, mean 2.66 accepted tokens (position acceptance 80/56/36%), single shared MTP head. Medusa: 2.2-2.8x. EAGLE-3: 3.0-6.5x with acceptance nearly flat across draft positions.
>
> **Numbers:** MTP1 >80% acc ~1.8x; FastMTP 2.03x, 2.66 tok; Medusa 2.2-2.8x; EAGLE-3 3.0-6.5x
> **Relevance:** Add MTP/EAGLE-style heads to the 500M Kazakh model for ~1.8-2x lossless edge speedup with no external draft. This is the concrete self-spec design.
> **Source:** arXiv:2412.19437 (DeepSeek-V3); arXiv:2509.18362 (FastMTP); arXiv:2401.10774 (Medusa); arXiv:2503.01840 (EAGLE-3) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — inference-tts
> MTP as a TRAINING objective (predict multiple future tokens per hidden state, DeepSeek-V3 style) improves benchmark quality and data efficiency, not just inference speed — it densifies the training signal and yields richer representations. But at small scale aggressive MTP can degrade base next-token performance unless a curriculum (forward/reverse schedule on number of predicted tokens) or register tokens are used.
>
> **Numbers:** DeepSeek-V3: MTP objective improves eval benchmarks + data efficiency; curriculum needed at small scale
> **Relevance:** Under a 9-10B-token Kazakh data budget, the MTP objective is a double win: better sample efficiency during pretraining AND free self-speculative heads for edge. Use curriculum MTP for the 500M to avoid NTP degradation.
> **Source:** arXiv:2412.19437 (DeepSeek-V3 MTP); MTP-at-small-scale via arXiv:2602.06019 and emergentmind MTP topic · **Sweep:** `slm-architecture-2026-07`

> [!warning] UNCERTAIN — inference-tts
> KV-cache math at the target config (d_model=1536, 24 layers, head_dim=128, fp16, 32K context): GQA-2:1 (6 KV heads, kv_dim=768) ~= 72 KB/token -> 2.25 GB. MLA with kv_lora_rank=256 + rope_dim=64 ~= 15 KB/token -> 480 MB (4.7x smaller, ~79% saved). MLA kv_lora_rank=512 ~= 27 KB/token -> 864 MB (2.6x smaller). (DeepSeek-V3 anchor: MLA 70 KB/token vs GQA 192-328 KB/token = 2.7-4.7x at d=7168.)
>
> **Numbers:** GQA-2:1 72KB/tok=2.25GB@32K; MLA r=256 15KB/tok=480MB (79% saved); MLA r=512 27KB/tok=864MB
> **Relevance:** Drop-in spec: MLA kv_lora_rank=256 (rope 64) cuts the 32K KV cache from 2.25GB to 480MB vs GQA-2:1 at d=1536 — decisive for fitting long Kazakh context on an 8GB edge GPU.
> **Source:** Derivation from stated config; DeepSeek-V3 ratios arXiv:2412.19437 / arXiv:2405.04434 (DeepSeek-V2 MLA) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model]]

> [!note] CLAIM — novelty-check
> Multi-token prediction (MTP) is standard in 2026 (DeepSeek-V3/V4, Qwen3, MiMo) but NO morphology-aware MTP exists. A morpheme-structured MTP head (predict the next STEM then the next SUFFIX(es)) is an unclaimed novelty axis well-suited to agglutinative Kazakh.
>
> **Numbers:** DeepSeek-V3 MTP: D sequential modules, full causal chain per depth; DeepSeek-V4: 1 MTP head (2-token gen/pass); no 'morphology-aware' MTP found in literature
> **Relevance:** Second candidate novelty (complementary to morpheme-keyed memory): an auxiliary morpheme-decomposed MTP objective that densifies training signal along morphological structure. Cite DeepSeek-V3 MTP (2412.19437) and 'Efficient Joint Prediction of Multiple Future Tokens' (2503.21801) as the token-level priors.
> **Source:** arXiv:2412.19437 (DeepSeek-V3); arXiv:2503.21801 (Efficient Joint Prediction of Multiple Future Tokens) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[mixtral-of-experts|Mixtral of Experts]] — Co-cited precedent: DeepSeek-V3 is 'the 671B model' (37B active, 5.5%) — models bracketed by total, not active
- [[fp8-lm-training-fp8-large-language-models|FP8-LM: Training FP8 Large Language Models]] — V3's fine-grained tile/block FP8 recipe builds on FP8-LM; both hit the Hopper-only tensor-core hardware constraint
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] — V3 anchors MLA KV-cache math at d=7168; LMHA re-tests MLA KV savings at the sub-1B scale QymyzLM targets
- [[plm-efficient-peripheral-language-models-hardware-co-designed-for-ubiquitous|PLM: Efficient Peripheral Language Models Hardware-Co-Designed for Ubiquitous Computing]] — PLM-1.8B's rank-512 latent is the same absolute cache as DeepSeek-V3; confirms 1–2B from-scratch uses 512
- [[huggingface-co-openbmb-minicpm3-4b-config-json-fetched|huggingface.co/openbmb/MiniCPM3-4B config.json (fetched directly)]] — MiniCPM3's kv_lora_rank=256 is d/10, same rank-ratio class as DeepSeek-V3's 512/7168=d/14

[[Home]]
