---
kb_id: "arxiv:2509.16686"
type: "paper"
title: "EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs"
arxiv_id: "2509.16686"
doi: null
hf_repo: null
year: 2025
topics: ["deepseek-tech", "mla-at-sub-1b"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs", "arXiv:2509.16686", "arxiv:2509.16686"]
tags: ["paper", "topic/deepseek-tech", "topic/mla-at-sub-1b"]
---
# EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs

[arXiv](https://arxiv.org/abs/2509.16686)
**Topics:** [[deepseek-tech]], [[mla-at-sub-1b]]

> [!abstract]
> Reducing the key-value (KV) cache size is a crucial step toward enabling efficient inference in large language models (LLMs), especially under latency and memory constraints. While Multi-Head Attention (MHA) offers strong representational power, it incurs significant memory overhead. Recent work on Multi-head Latent Attention (MLA) mitigates this by compressing KV representations into a shared lat …

## Claims

> [!note] CLAIM — deepseek-tech
> MLA at sub-1B DOES transfer but with caveats. EG-MLA (arXiv 2509.16686) runs MLA at 1B and cuts KV cache to 1.54K elements/token (91.6% vs MHA) while retaining accuracy. TransMLA (arXiv 2502.07864) proves any GQA model is convertible to MLA and MLA's expressivity strictly exceeds GQA at equal cache. BUT practitioner consensus (Raschka, and others) is that below ~100B, GQA is easier to tune/get right; MLA stays competitive and can slightly beat MHA. So MLA is a quality-neutral-to-positive, cache-negative swap that costs engineering effort (decoupled RoPE + weight-absorption at inference).
>
> **Numbers:** EG-MLA @1B: 1.54K elem/token, 91.6% cut; TransMLA: MLA expressivity >= GQA at equal cache
> **Relevance:** Green-lights MLA for the 500M Kazakh model but sets expectations: expect quality parity-to-small-gain, not a KazMMLU jump. Keep GQA-2 as the low-risk fallback. Budget time for the decoupled-RoPE + matrix-absorption implementation.
> **Source:** arXiv:2509.16686 (EG-MLA), arXiv:2502.07864 (TransMLA), Raschka LLM gallery · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — mla-at-sub-1b
> MINIMUM SHARED RANK PROVEN FROM SCRATCH BELOW 1B: kv_lora_rank=256 (plain DeepSeek-style MLA) at 120M params, and 64 with EG-MLA's token-embedding gating. EG-MLA trains from scratch on 50B ClimbMix tokens: MLA-Base (12L, d=768, shared kv_lora_rank=256 + decoupled rope 64, qk 64+64/v 64 head dims, cache 3.84K elem/token total = (256+64)×12 layers) scores 43.84 avg over PIQA/ARC-C/ARC-E/HellaSwag/WinoGrande/SIQA/MMLU; EG-MLA-kv64 (cache 1.54K elem = (64+64)×12) scores 44.33 (+0.49 over rank-256 MLA); EG-MLA-kv256 44.46. This is the only located from-scratch sub-1B run with a DeepSeek-style shared rank below 512.
>
> **Numbers:** 120M, 50B tokens, rank 256 = d/3 at d=768; kv64 variant needs extra gating-embedding table (154M params for emb256, offloadable); cache 3.84K→1.54K→0.96K elem/token for kv256/kv64/kv16
> **Relevance:** Directly legitimizes the 'aggressive r=256' option's existence at sub-1B — but note EG-MLA's proven ratio is rank=d/3 at 120M; the lab's r=256 at d=1536 is d/6, i.e. relatively MORE compressed than the proven sub-1B point. Table 1 (per fetch) lacks an MHA/GQA control, so absolute MLA-vs-MHA quality at 120M is not anchored here.
> **Source:** arXiv:2509.16686 (EG-MLA), Table 1 + Table 7 appendix config (arxiv.org/html/2509.16686v1) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Trans…]] — Both target MLA at ~1B; EG-MLA builds MLA from scratch whereas MHA2MLA adapts pretrained GQA, trading data cost for accuracy
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compressio…]] — X-EcoMLA converts to MLA at 1.24B; EG-MLA is the from-scratch MLA-at-1B endpoint the conversion path is judged against
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] — EG-MLA gates MLA with embeddings; builds on the sub-1B MLA config this paper pins (kv_lora, decoupled rope)
- [[multi-head-low-rank-attention|Multi-Head Low-Rank Attention]] — MLRA trains GLA-2 with added gating; EG-MLA gates MLA embeddings — same gate-the-latent-attention trend

[[Home]]
