---
kb_id: "title:sebastian raschka mla gallery knightli deepseek analyses martinalderson kv cache history"
type: "source"
title: "Sebastian Raschka MLA gallery"
doi: null
hf_repo: null
year: null
topics: ["sota-slm"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:sebastian raschka mla gallery knightli deepseek analyses martinalderson kv cache history"]
tags: ["source", "topic/sota-slm"]
---
# Sebastian Raschka MLA gallery

**Topics:** [[sota-slm]]

## Source URLs
- Sebastian Raschka MLA gallery
- knightli/DeepSeek analyses
- martinalderson KV-cache history

## Findings

> [!note] CLAIM — sota-slm
> MLA (DeepSeek multi-head latent attention) compresses the KV cache far more than GQA while preserving per-head expressiveness: DeepSeek-V3 caches ~70KB/token (MLA) vs 192-328KB/token for GQA models (2.7-4.7x smaller); V2 reported 93% KV reduction vs MHA. MLA reconstructs full-rank per-head K/V from a shared latent (kv_lora_rank), unlike GQA which forces heads in a group to share identical K/V.
>
> **Numbers:** MLA 70KB/tok vs GQA 192-328KB/tok (2.7-4.7x); 93% vs MHA
> **Relevance:** For a 32K-context Kazakh SLM, MLA (e.g. kv_lora_rank 256-512) is a stronger cache-reduction choice than GQA-2 and keeps more attention quality — a concrete upgrade over the current GQA 2:1 plan if implementation cost is acceptable.
> **Source:** Sebastian Raschka MLA gallery; knightli/DeepSeek analyses; martinalderson KV-cache history · **Sweep:** `slm-architecture-2026-07`

## Related
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compressio…]] — X-EcoMLA upcycles pretrained GQA attention into MLA — the conversion path realizing MLA's KV savings
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] — Both push MLA KV compression; this paper tests MLA specifically at SLM scale the gallery only sketches

[[Home]]
