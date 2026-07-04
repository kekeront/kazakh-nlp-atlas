---
kb_id: "arxiv:2412.06464"
type: "paper"
title: "Gated Delta Networks: Improving Mamba2 with Delta Rule"
arxiv_id: "2412.06464"
doi: null
hf_repo: null
year: 2024
topics: ["attention-kv-sub1b-attention-kv-architec"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Gated Delta Networks: Improving Mamba2 with Delta Rule", "arXiv:2412.06464", "arxiv:2412.06464"]
tags: ["paper", "topic/attention-kv-sub1b-attention-kv-architec"]
---
# Gated Delta Networks: Improving Mamba2 with Delta Rule

[arXiv](https://arxiv.org/abs/2412.06464)
**Topics:** [[attention-kv-sub1b-attention-kv-architec]]

> [!abstract]
> Linear Transformers have gained attention as efficient alternatives to standard Transformers, but their performance in retrieval and long-context tasks has been limited. To address these limitations, recent work has explored two distinct mechanisms: gating for adaptive memory control and the delta update rule for precise memory modifications. We observe that these mechanisms are complementary: gat …

## Claims

> [!note] CLAIM — attention-kv-sub1b-attention-kv-architec
> [transferable-untested] Gated DeltaNet ICLR 2025 head-to-head at 1.3B / 100B FineWeb-Edu tokens (Llama2 32K tokenizer, 4K train length, SWA window 2K in hybrids): Wiki ppl / 9-task zero-shot avg — Transformer++ 18.53/52.25, Mamba2 16.56/54.89, DeltaNet 17.71/52.14, Gated DeltaNet 16.42/55.32, Samba 16.13/54.00, GDN-H1 (GDN+SWA alternating) 16.07/56.40, GDN-H2 (Mamba2+GDN+SWA) 15.91/56.18. On real-world recall tasks truncated to 2K (SWDE/SQuAD/FDA/TQA/NQ/Drop avg): Transformer++ 37.0 vs GDN 30.6 vs GDN-H1 39.0 vs GDN-H2 40.1 — hybrids beat the pure transformer even on recall. Training throughput at 1.3B/H100: Transformer++ fastest at 2K×16 (~55K tok/s, FA2 kernel) but collapses to ~26K at 16K×2 while GDN-H1 holds ~52K.
>
> **Numbers:** 1.3B/100B: GDN-H1 16.07 ppl / 56.40 avg vs Transformer++ 18.53 / 52.25 (+4.15pp); recall avg GDN-H2 40.1 vs T++ 37.0; throughput crossover ≥4K ctx
> **Relevance:** Quality case for a GDN-hybrid from-scratch variant is real at 1.3B — but its throughput edge assumes FA2/Triton kernels absent-or-unverified on T4 (see FA2 finding), and the 400M-scale rows were not captured; treat as v2 option, not v1.
> **Source:** arXiv:2412.06464 (ICLR 2025 camera-ready PDF read, Tables 3-4, Fig.3) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[an-empirical-study-of-mamba-based-language-models|An Empirical Study of Mamba-based Language Models]] — GDN improves Mamba2 with the delta rule; the empirical Mamba study is the from-scratch SSM baseline it beats at 1.3B
- [[nemotron-h-a-family-of-accurate-and-efficient-hybrid-mamba-transformer-models|Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models]] — Both Mamba-transformer hybrids; Nemotron-H sets KB's ~7-8% attention floor, above which GDN's 3:1-2:1 ratios sit
- [[kimi-linear-an-expressive-efficient-attention-architecture|Kimi Linear: An Expressive, Efficient Attention Architecture]] — Kimi Linear's 3:1 hybrid pairs full-MLA with KDA, a gated-delta-rule linear layer from this Gated DeltaNet line
- [[huggingface-co-qwen-qwen3-5-0-8b-config-json-fetched|huggingface.co/Qwen/Qwen3.5-0.8B config.json (fetched directly)]] — Qwen3.5-0.8B's 3:1 linear layers ARE Gated DeltaNet — it chose hybrid-linear + GQA-2 over MLA for 256K context
- [[empirical-this-session-tmp-claude-1000-home-altairzhambyl-69058ff0|Empirical, this session: /tmp/claude-1000/-home-altairzhambyl-projects…]] — GatedDeltaNet from this paper PASSES on SM75 but at 14K tok/s/layer (28-47x SDPA) via fla-0.5.1 fallback configs

[[Home]]
