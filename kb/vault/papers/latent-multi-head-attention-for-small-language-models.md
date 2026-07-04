---
kb_id: "arxiv:2506.09342"
type: "paper"
title: "Latent Multi-Head Attention for Small Language Models"
arxiv_id: "2506.09342"
doi: null
hf_repo: null
year: 2025
topics: ["hybrid-efficiency-efficient-attention-se", "mla-vs-gqa-pretraining-cost-and-converge", "mla-at-sub-1b-scale", "mla-at-sub-1b"]
claims: 4
uncertain_claims: 2
verdicts: []
aliases: ["Latent Multi-Head Attention for Small Language Models", "arXiv:2506.09342", "arxiv:2506.09342"]
tags: ["paper", "topic/hybrid-efficiency-efficient-attention-se", "topic/mla-vs-gqa-pretraining-cost-and-converge", "topic/mla-at-sub-1b-scale", "topic/mla-at-sub-1b"]
---
# Latent Multi-Head Attention for Small Language Models

[arXiv](https://arxiv.org/abs/2506.09342)
**Topics:** [[hybrid-efficiency-efficient-attention-se]], [[mla-vs-gqa-pretraining-cost-and-converge]], [[mla-at-sub-1b-scale]], [[mla-at-sub-1b]]

> [!abstract]
> We present the first comprehensive study of latent multi-head attention (MLA) for small language models, revealing interesting efficiency-quality trade-offs. Training 30M-parameter GPT models on 100,000 synthetic stories, we benchmark three architectural variants: standard multi-head attention (MHA), MLA, and MLA with rotary positional embeddings (MLA+RoPE). Our key finding is that MLA+RoPE with h …

## Claims

> [!note] CLAIM — hybrid-efficiency-efficient-attention-se
> MLA specifically studied at SMALL scale (30M-202M params): a decoupled MLA+RoPE with latent rank r=d/2 gives a 45% KV-cache reduction at only +0.3% validation loss and 1.4x decode speedup; r=d/4 gives ~87.5% reduction but +4.4% loss. MLA needs the decoupled-RoPE variant - without RoPE it underperforms by 3-5%. (Paper did not benchmark GQA directly.)
>
> **Numbers:** r=d/2: 45% KV cut, +0.3% loss, 1.4x speed; r=d/4: 87.5% cut, +4.4% loss; scale tested 30M-202.7M
> **Relevance:** If MLA is adopted for the Kazakh model at d_model~1536, set kv_lora_rank ~= d/2 (~768) with a decoupled RoPE dim (~64). This is the only MLA-at-sub-600M data point; r=d/4 is too lossy for a knowledge model.
> **Source:** arXiv:2506.09342 (Latent Multi-Head Attention for Small Language Models) · **Sweep:** `slm-architecture-2026-07`

> [!warning] UNCERTAIN — mla-vs-gqa-pretraining-cost-and-converge
> Only datapoint below 25B tokens: the latent-MHA-for-SLMs paper trained 17.5M-202.7M models for ~3.3B tokens (50K steps x batch 128 x ctx 512, derived) on 100K synthetic TinyStories-style stories. Decoupled-RoPE MLA at r=d/2 converged to within +0.3% val loss of MHA (2.154 vs 2.147 at 9L-512d); r=d/4 degraded +4.4% (2.241); MLA WITHOUT decoupled RoPE degraded +2.2-3.2%. No GQA arm; no training-time numbers.
>
> **Numbers:** ~3.3B tokens (derived: 50000*128*512); val loss MHA 2.147, MLA+RoPE r=d/2 2.154 (+0.3%), r=d/4 2.241 (+4.4%), MLA no-RoPE r=d 2.216 (+3.2%)
> **Relevance:** Suggests MLA (decoupled-RoPE, r>=d/2) converges fine even at ~3B tokens — inside the lab's 9-30B Kazakh budget — but on synthetic English data at toy scale, so it is supporting, not decisive, evidence.
> **Source:** arXiv 2506.09342 (HTML v1) — extends existing KB entry with the token-budget arithmetic and exact losses · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-at-sub-1b-scale
> Both from-scratch sub-1B MLA studies trained and evaluated at short context only — zero long-context evidence. The dedicated SLM-MLA paper trained at 512-token context (17.5M-202.7M params, TinyStories-style data) with validation loss + GPT-4-judged generations as the only evals; EG-MLA trained 120M-1.8B models from scratch on 50B ClimbMix tokens at ctx 2048/4096 with kv latent dims 16-512 and ran only short reasoning benchmarks (PIQA/ARC/HellaSwag/WinoGrande/SIQA/MMLU, WikiText103/LAMBADA) — no RULER/needle/LongBench/long-ppl.
>
> **Numbers:** 2506.09342: ctx=512; r=d/2 -> 45% KV cut, +0.3% val loss; r=d/4 -> 87.5% cut, +4.4% loss; r=d/8 -> +10.3% loss. EG-MLA: 120M/645-951M/1.19-1.8B models, 50B tokens, ctx 2048 & 4096, kv dims {16,64,128,256,512}
> **Relevance:** Directly answers the research question: the lab's 32K KV-cache justification for MLA rests on a regime no sub-1B study has ever measured. Also pins the safe rank floor: r=d/4 already costs +4.4% loss at 200M scale.
> **Source:** arXiv 2506.09342 (html v1, Sec. setup); arXiv 2509.16686 (html v1, Appendix G + eval section) · **Sweep:** `mla-sub1b-2026-07`

**Cited KB notes:** [[eg-mla-embedding-gated-multi-head-latent-attention-for-scalable-and-efficient]]

> [!warning] UNCERTAIN — mla-at-sub-1b
> The 30M-202M small-scale MLA paper (KB entry arXiv:2506.09342) also uses PER-HEAD latents, not DeepSeek shared rank: K_h = X W_h^(K↓) W_h^(K↑) with W_h^(K↓) ∈ R^{d×r} per head, r ∈ {d_k, d_k/2, d_k/4} where d_k=d/H (e.g. r=64/32/16 at d=512, H=8). Trained from scratch but only on ~TinyStories (~100K synthetic stories, 50K steps). r=d_k/2: val loss 2.154 vs 2.147 baseline (+0.3%), 0.0159 vs 0.0288 MB/token (45% cut); r=d_k/4: 2.241 (+4.4%), 0.0080 MB/token (=72% cut by arithmetic). KB CONFLICT: KB records '87.5% reduction' for r=d/4; the fetched MB/token values give 72% — both reported, do not average.
>
> **Numbers:** 17.5M-202.7M params, d∈{256,512,768,1024}, TinyStories ~50M tokens; +0.3% loss at total-equivalent latent d/2, +4.4% at d/4, +10.3% at d/8
> **Relevance:** Weakens this paper as evidence for shared-rank MLA at 500M: per-head latents + toy corpus. Its 'quality cliff below total d/4' is the only sub-1B signal on where compression breaks — at d=1536 that cliff estimate is total latent ~384.
> **Source:** arXiv:2506.09342 (arxiv.org/html/2506.09342v1) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[deepseek-v3-technical-report|DeepSeek-V3 Technical Report]] — V3 anchors MLA KV-cache math at d=7168; LMHA re-tests MLA KV savings at the sub-1B scale QymyzLM targets
- [[long-context-aware-upcycling-a-new-frontier-for-hybrid-llm-scaling|Long-Context Aware Upcycling: A New Frontier for Hybrid LLM Scaling]] — From-scratch sub-1B MLA trained at ctx 512 only; long-context upcycling addresses the missing evidence
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — SozKZ uses fully vanilla MHA; latent MHA at small scale is an untested efficiency upgrade the Kazakh attention axis lacks
- [[arxiv-org-html-2603-02188-tables-3-4-vs-arxiv-org-html-2505|arxiv.org/html/2603.02188 (Tables 3-4) vs arxiv.org/html/2505.21487v1]] — No independent sub-1B latent-attention replication exists; 2506.09342 is a separate MLA-at-SLM study, not a rerun
- [[sebastian-raschka-mla-gallery|Sebastian Raschka MLA gallery]] — Both push MLA KV compression; this paper tests MLA specifically at SLM scale the gallery only sketches

[[Home]]
