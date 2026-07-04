---
kb_id: "arxiv:2503.11132"
type: "paper"
title: "X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression"
arxiv_id: "2503.11132"
doi: null
hf_repo: "amd/X-EcoMLA-1B8B-fixed-kv64-DPO"
year: 2025
topics: ["mla-sub1b", "mla-at-sub-1b-scale", "mla-at-sub-1b", "mla-upcycling-at-1b-under-a-bespoke-toke", "slm-architecture"]
claims: 6
uncertain_claims: 2
verdicts: []
aliases: ["X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression", "arXiv:2503.11132", "arxiv:2503.11132"]
tags: ["paper", "topic/mla-sub1b", "topic/mla-at-sub-1b-scale", "topic/mla-at-sub-1b", "topic/mla-upcycling-at-1b-under-a-bespoke-toke", "topic/slm-architecture"]
---
# X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression

[arXiv](https://arxiv.org/abs/2503.11132)
**Topics:** [[mla-sub1b]], [[mla-at-sub-1b-scale]], [[mla-at-sub-1b]], [[mla-upcycling-at-1b-under-a-bespoke-toke]], [[slm-architecture]]

> [!abstract]
> Multi-head latent attention (MLA) is designed to optimize KV cache memory through low-rank key-value joint compression. Rather than caching keys and values separately, MLA stores their compressed latent representations, reducing memory overhead while maintaining the performance. While MLA improves memory efficiency without compromising language model accuracy, its major limitation lies in its inte …

## Claims

> [!note] CLAIM — mla-sub1b
> X-EcoMLA (AMD): Llama3.2-1B-Instruct upcycled to MLA via SVD init + post-training distillation. kv_lora_rank=128, q_lora_rank=1344, rope_dims=32 -> 6.4x KV compression (15.6% size) with avg score 52.94 vs 52.85 baseline (no loss), using 3.6B tokens / ~70 MI300 GPU-hours with a Llama3.1-8B teacher; kv_lora_rank=64, q_lora_rank=1424, rope 32 -> 10.6x compression (9.4%), 52.47 avg (<0.4pp drop), 7B tokens / ~140 GPU-h. Teacher size drives compression achievable: 1B teacher 1.9x@53.04, 3B 3.6x@54.08, 8B 6.4x@55.13.
>
> **Numbers:** r_kv=128/q=1344/rope=32: 6.4x, 52.94 vs 52.85, 3.6B tok, 70 GPU-h; r_kv=64/q=1424: 10.6x, 52.47, 7B tok, 140 GPU-h
> **Relevance:** De-risk path for the lab: pretrain plain GQA, convert to MLA post-hoc for ~1 GPU-day at 600M scale — keeps the architecture bet reversible; also shows rank 64-128 suffices at ~1B WITH distillation (not from scratch).
> **Source:** arXiv 2503.11132 (X-EcoMLA), HTML v3 Table 2; HF amd/X-EcoMLA-1B8B-fixed-kv64-DPO · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-at-sub-1b-scale
> X-EcoMLA is the exact-rank precedent: kv rank 512 (the lab's candidate rank) at Llama3.2-1B-Instruct (1.24B) is quality-NEUTRAL on short tasks after cheap distillation — but the paper contains no long-context evaluation of any kind (no LongBench/RULER/needle/passkey), so rank-512-at-1B remains unmeasured beyond short context.
>
> **Numbers:** r_kv=512, r_q=864, d_qk=32, rope_dim=32; 6.4x KV compression (15.6% of orig): avg 52.94 vs baseline 52.77 (9 zero-shot LM-harness tasks); 10.6x (9.4%): 52.68; cost 3.6B tokens/70 MI300 GPU-hrs (6.4x) or 7B tokens/140 GPU-hrs (10.6x)
> **Relevance:** Best config anchor for the lab (rank 512 + decoupled rope 32 at ~1B, near the lab's hidden-size regime) and proof the short-context side is cheap to retain — while confirming the 32K quality side is a genuine open gap, not an overlooked result.
> **Source:** arXiv 2503.11132 (html v2, Table 2 + eval section) · **Sweep:** `mla-sub1b-2026-07`

> [!warning] UNCERTAIN — mla-at-sub-1b
> Adjacent conversion evidence at 1.24B: X-EcoMLA (AMD) upcycles Llama-3.2-1B-Inst to MLA via SVD init + distillation with fixed r_kv=512, r_q=854, d_qk_rope=32; with an 8B teacher it reports 6.4x KV cache compression at 100% of the baseline average LM-Harness score; released extreme variants go to kv64 (amd/X-EcoMLA-1B8B-fixed-kv64-DPO). 6.4x on Llama3.2-1B GQA-8 (1024 elem) = 160 elem/token/layer, consistent with a kv128+rope32 variant.
>
> **Numbers:** fixed setting r_kv=512, r_q=854, rope 32; 6.4x compression at 100% score retention (8B teacher); dynamic-rank threshold 0.95
> **Relevance:** Shows ~1B-scale models tolerate effective latents down to ~128-160 elem WHEN distilled from a big teacher — a mitigation path if the lab picks aggressive r=256 and sees regression (distill from Sherkala-8B or Qwen3-8B). Not from-scratch evidence; exact per-variant scores unverified.
> **Source:** arXiv:2503.11132 (X-EcoMLA) + https://huggingface.co/amd/X-EcoMLA-1B8B-fixed-kv64-DPO · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-upcycling-at-1b-under-a-bespoke-toke
> X-EcoMLA's own Table 2 confirms the mission premise exactly: upcycling Llama3.2-1B-Instruct (GQA baseline avg 52.85 on LM Harness) with ITSELF as teacher (self-distillation, r_kv=512, r_q=864) reaches KV size 53.1% = 1.88x compression at avg 53.04 (parity, slightly above baseline). Deeper compression at parity requires larger same-tokenizer teachers: 3B teacher r_kv=256 -> 28.1% KV (3.6x) avg 52.91; 8B teacher r_kv=128 -> 15.6% (6.4x) avg 52.94 @3.6B tokens; 8B teacher r_kv=64 -> 9.4% (10.6x) avg 52.47 @3.6B tokens (paper claims <0.1% drop with 7B tokens). Distillation is KL divergence on output logits, so teacher and student must share a vocabulary; all experiments are same-family Llama. MLA student uses decoupled rope dim d_r=32; KV % is relative to the already-GQA Llama3.2-1B cache.
>
> **Numbers:** baseline 52.85; self-distill 1.88x/53.04; 3B teacher 3.6x/52.91; 8B teacher 6.4x/52.94 and 10.6x/52.47 @3.6B tok (70-140 MI300 GPU-hrs); rope_dim=32
> **Relevance:** With the lab's custom <2.0-fertility Kazakh tokenizer no larger same-tokenizer teacher will exist, so the lossless X-EcoMLA path caps at ~1.9x KV compression — the 6.4-10.6x headline is unreachable for the lab via this route.
> **Source:** arXiv:2503.11132v3 (X-EcoMLA, AMD), Tables 1-2; HF amd/X-EcoMLA-1B8B-fixed-kv64-DPO · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-upcycling-at-1b-under-a-bespoke-toke
> Verdict on the research question: the X-EcoMLA de-risk path survives a bespoke tokenizer only in weakened form. Published options at <=1B with no larger same-tokenizer teacher: (a) ~1.9x KV compression lossless via self-distillation (X-EcoMLA, own model as teacher — tokenizer trivially shared); (b) ~3.2x at ~-1.2 to -1.7 avg pts, or 5.3-8x at -2.7 to -4.6 pts, teacher-free (MHA2MLA, needs only own pretraining data); (c) 6.4-10.6x lossless is published ONLY with a 3-8x-larger same-tokenizer teacher, which cannot exist for the lab. Cross-tokenizer rescue: zero published results. Broader MLA-at-500M status per KB + this run: from-scratch MLA is proven at 30M-202M (r=d/2: 45% KV cut, +0.3% loss, arXiv:2506.09342) and at 1B (EG-MLA); CONVERSION to MLA at sub-1B is proven-but-lossy; lossless deep conversion at sub-1B is untested.
>
> **Numbers:** hedge repriced: 1.9x lossless / 3.2x @ -1.7 pts / 6.4-10.6x unreachable without same-tokenizer big teacher
> **Relevance:** Directly reprices 'Recommendation 6 reversible bet': pretrain-GQA-convert-later is a real but ~2x-lossless hedge, not a 6-10x one; if the Kinetics KV bottleneck (Qwen3-0.6B: 3.5GB KV @32K vs 1.2GB weights) demands >=4x, MLA must be chosen at pretraining time.
> **Source:** Synthesis of arXiv:2503.11132v3, 2502.14837, 2506.09342, 2509.16686, 2603.17946 + absence searches · **Sweep:** `mla-sub1b-2026-07`

**Cited KB notes:** [[latent-multi-head-attention-for-small-language-models]]

> [!warning] UNCERTAIN — slm-architecture
> CORRECTION/conflict flag: the KB node for X-EcoMLA (arXiv 2503.11132) attributes the same 6.4x KV-cache compression result to mutually exclusive configurations across its claims (kv_lora_rank=128 with r_q=1344 vs r_kv=512 with r_q=864 vs r_q=854; baseline quoted as both 52.85 and 52.77). Until the paper is re-read and one mapping confirmed, every specific config-to-ratio mapping in that node is to be treated as unverified; only the coarse claim 'X-EcoMLA reports up to 6.4x KV compression via post-hoc MLA conversion' stands.
>
> **Numbers:** conflicting: kv_lora_rank 128 vs 512; r_q 1344 vs 864 vs 854; baseline 52.85 vs 52.77
> **Relevance:** Intra-node conflict resolution debt — flag until re-derived from the paper.
> **Source:** internal KB audit (professor review 2026-07-03) of node arxiv:2503.11132; arXiv 2503.11132 · **Sweep:** `2026-07-eval-provenance`

## Related
- [[eg-mla-embedding-gated-multi-head-latent-attention-for-scalable-and-efficient|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] — X-EcoMLA converts to MLA at 1.24B; EG-MLA is the from-scratch MLA-at-1B endpoint the conversion path is judged against
- [[long-context-aware-upcycling-a-new-frontier-for-hybrid-llm-scaling|Long-Context Aware Upcycling: A New Frontier for Hybrid LLM Scaling]] — X-EcoMLA reports no long-context eval; long-context-aware upcycling targets exactly this gap
- [[strong-teacher-not-needed-on-distillation-in-llm-pretraining|Strong Teacher Not Needed? On Distillation in LLM Pretraining]] — X-EcoMLA finds bigger same-tokenizer teacher unlocks deeper lossless compression; 'Strong Teacher Not Needed' contests teacher-strength…
- [[ggml-org-llama-cpp-howto-add-model-md-discussion-16770|ggml-org/llama.cpp HOWTO-add-model.md + Discussion #16770]] — MLA export breaks mainline GGUF (ik_llama.cpp fork only); X-EcoMLA's upcycled MLA inherits this deployment penalty
- [[sebastian-raschka-mla-gallery|Sebastian Raschka MLA gallery]] — X-EcoMLA upcycles pretrained GQA attention into MLA — the conversion path realizing MLA's KV savings

[[Home]]
