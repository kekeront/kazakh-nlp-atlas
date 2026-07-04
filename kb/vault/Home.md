---
type: "home"
tags: ["moc"]
nodes: 255
papers: 170
sources: 85
topics: 40
claims: 448
---
# Kazakh NLP Atlas — Research Vault

Knowledge base of the Kazakh Frontier Lab. Two pillars: **QymyzLM** (Kazakh SLM,
≤600M active params) and the **best Kazakh text-embedding model**. Every note is
generated from `kb/nodes.jsonl` — do not edit generated notes by hand (use `notes/`);
regenerate with `python scripts/build_vault.py`.

## How to use this vault (Claude Code)
1. Start at the topic map below; open the MoC nearest your design question.
2. MoC "Frontier highlights" = the current best-supported picture per topic.
3. Claim callouts encode evidence status: `[!success] CONFIRMED` / `[!failure] REFUTED`
   / `[!warning] UNCERTAIN` / `[!note] CLAIM` (asserted, unverified). Treat UNCERTAIN
   and REFUTED as not load-bearing for design decisions.
4. `kb_id` in frontmatter is the canonical citation key used by /design-panel and /research-sweep.

> [!warning] Verification coverage ~0.9%
> Only 4/448 claims carry a CONFIRMED/REFUTED/PLAUSIBLE verdict from adversarial review. The rest render as `[!note] CLAIM` — asserted by a single sweep agent and NOT yet audited. Treat unaudited numbers as provisional, not vetted.

## Pillars

### QymyzLM — Generative SLM (≤600M active)

| Topic | Nodes | Uncertain |
| --- | --- | --- |
| [[mla-at-sub-1b-scale]] | 19 | 8 |
| [[sota-slm]] | 17 | 5 |
| [[continual-pt-lowres-qlora-vs-full-cpt-re]] | 16 | 4 |
| [[tokenizer-morphology]] | 16 | 6 |
| [[training-recipes]] | 16 | 5 |
| [[hybrid-efficient-attention-architectures]] | 14 | 6 |
| [[inference-tts]] | 14 | 6 |
| [[attention-kv-architecture-sub-1b]] | 12 | 8 |
| [[residual-stream-stability-qymyzlm-design]] | 12 | 7 |
| [[small-lm-training-recipes-qymyzlm-design]] | 11 | 6 |
| [[tokenizer-agglutinative]] | 11 | 2 |
| [[data-efficiency-10b-kazakh-10b-token-pre]] | 8 | 4 |
| [[kazakh-morphological-segmentation-qualit]] | 8 | 3 |
| [[sparse-memory-2026-engram-lineage-beyond]] | 8 | 7 |
| [[deepseek-tech]] | 7 | 5 |
| [[gla-2-gta-arxiv-2505-21487-zadouri-strau]] | 7 | 1 |
| [[qymyzlm-architecture-fork]] | 7 | 1 |
| [[kazakh-tokenizer-fertility-vs-byte-premi]] | 6 | 3 |
| [[post-hoc-attachment-of-engram-style-cond]] | 6 | 4 |
| [[architecture-fork]] | 5 | 5 |
| [[kv-cache-architecture]] | 5 | 1 |
| [[mla-upcycling-bespoke-tokenizer]] | 5 | 3 |
| [[mla-vs-gqa-convergence-cost]] | 5 | 3 |
| [[does-the-engram-conditional-memory-modul]] | 4 | 4 |
| [[eval-benchmarks]] | 3 | 0 |
| [[slm-architecture]] | 2 | 3 |
| [[llm-alignment-data]] | 1 | 0 |

### Kazakh Text-Embedding Models

| Topic | Nodes | Uncertain |
| --- | --- | --- |
| [[decoder-to-embedder]] | 19 | 2 |
| [[embed-kazakh]] | 15 | 5 |
| [[embed-sota]] | 14 | 4 |
| [[embeddings-training]] | 7 | 0 |
| [[joint-generative-embedding-head-on-one-6]] | 7 | 1 |
| [[embeddings-retrieval]] | 4 | 1 |

### Cross-cutting / Meta

| Topic | Nodes | Uncertain |
| --- | --- | --- |
| [[novelty-check]] | 18 | 15 |
| [[kazakh-turkic-nlp]] | 12 | 9 |
| [[hardware-gate]] | 8 | 2 |
| [[kaggle-t4x2-compute-vram-budget-for-the]] | 8 | 2 |
| [[novelty-check-has-any-2026-preprint-impl]] | 6 | 8 |
| [[parameter-counting-convention-and-iso-si]] | 3 | 4 |
| [[win-bar-protocol-audit]] | 3 | 3 |

## All topics A–Z

| Topic | Focus | Nodes | Papers | Uncertain |
| --- | --- | --- | --- | --- |
| [[architecture-fork]] | The core decision — adapt a strong base (continual pretraining / tokenizer transplant) vs… | 5 | 5 | 5 |
| [[attention-kv-architecture-sub-1b]] | The sub-1B attention/KV frontier has three cheap, scale-independent wins that are… | 12 | 10 | 8 |
| [[continual-pt-lowres-qlora-vs-full-cpt-re]] | For a sub-1B Kazakh CPT the frontier converges on full continued pretraining over… | 16 | 14 | 4 |
| [[data-efficiency-10b-kazakh-10b-token-pre]] | The frontier question is how to assemble and train on a ~9-10B-token Kazakh corpus… | 8 | 7 | 4 |
| [[decoder-to-embedder]] | The topic covers converting causal decoder LMs into text embedders, directly relevant to… | 19 | 16 | 2 |
| [[deepseek-tech]] | The DeepSeek stack supplies QymyzLM's two efficiency levers, but the slice's own math… | 7 | 7 | 5 |
| [[does-the-engram-conditional-memory-modul]] | The frontier question is whether Engram-style conditional memory helps at QymyzLM's ≤600M… | 4 | 4 | 4 |
| [[embed-kazakh]] | Kazakh embedding is a near-greenfield with a thin but concrete evidence base. | 15 | 6 | 5 |
| [[embed-sota]] | The general-purpose SOTA has converged on a reproducible sub-1B recipe: multi-stage… | 14 | 9 | 4 |
| [[embeddings-retrieval]] | The Kazakh embedding frontier is thin and protocol-fragile. | 4 | 0 | 1 |
| [[embeddings-training]] | The frontier converges on one recipe for sub-1B embedders: multi-stage training… | 7 | 7 | 0 |
| [[eval-benchmarks]] | This topic is dominated by operational, inspection-verified facts about how Kazakh eval… | 3 | 1 | 0 |
| [[gla-2-gta-arxiv-2505-21487-zadouri-strau]] | arXiv:2505.21487 (Tri Dao group) is a from-scratch head-to-head on FineWeb-Edu where… | 7 | 2 | 1 |
| [[hardware-gate]] | This topic is the lab's own SM75 (Kaggle T4 / RTX 2070 proxy, cc 7.5, 64KB shared-mem, no… | 8 | 0 | 2 |
| [[hybrid-efficient-attention-architectures]] | The frontier splits into three efficiency levers for a ≤600M Kazakh SLM, all measured but… | 14 | 13 | 6 |
| [[inference-tts]] | The headline result is that compute-optimal test-time scaling lets sub-1B models beat… | 14 | 11 | 6 |
| [[joint-generative-embedding-head-on-one-6]] | The frontier question is whether ONE model ≤600M active params can carry both a… | 7 | 6 | 1 |
| [[kaggle-t4x2-compute-vram-budget-for-the]] | The lab has empirically pinned the Kaggle-free-tier CPT envelope for Qwen3-0.6B-Base… | 8 | 1 | 2 |
| [[kazakh-morphological-segmentation-qualit]] | The established picture: on clean, lab-annotated or synthetic Kazakh data, SUPERVISED… | 8 | 2 | 3 |
| [[kazakh-tokenizer-fertility-vs-byte-premi]] | The frontier here has largely inverted the intuitive story that a better Kazakh tokenizer… | 6 | 5 | 3 |
| [[kazakh-turkic-nlp]] | The established fact is that every published Kazakh SOTA at any scale is an ADAPTATION of… | 12 | 10 | 9 |
| [[kv-cache-architecture]] | The frontier here is cross-layer KV sharing on top of GQA/MQA — reusing K/V across layers… | 5 | 3 | 1 |
| [[llm-alignment-data]] | This topic is anchored by a single node, Qorgau (arxiv:2502.13640, MBZUAI Feb 2025) — the… | 1 | 1 | 0 |
| [[mla-at-sub-1b-scale]] | The frontier splits cleanly into three evidence classes. | 19 | 13 | 8 |
| [[mla-upcycling-bespoke-tokenizer]] | The question — can a ≤1B GQA model be upcycled to MLA when it uses a bespoke Kazakh… | 5 | 5 | 3 |
| [[mla-vs-gqa-convergence-cost]] | The frontier question is whether MLA beats GQA enough to justify it when pretraining a… | 5 | 4 | 3 |
| [[novelty-check]] | The novelty audit converges on one point: every component QymyzLM plans is established… | 18 | 16 | 15 |
| [[novelty-check-has-any-2026-preprint-impl]] | CONFIRMED across the whole 2026 Engram lineage: no preprint keys conditional memory by… | 6 | 6 | 8 |
| [[parameter-counting-convention-and-iso-si]] | The frontier here is a single load-bearing accounting question for QymyzLM: does a… | 3 | 3 | 4 |
| [[post-hoc-attachment-of-engram-style-cond]] | The frontier question is whether QymyzLM can bolt a random-init, deterministic-hash… | 6 | 6 | 4 |
| [[qymyzlm-architecture-fork]] | The fork is how to give Qwen3-0.6B-Base (tied embeddings, 151,936×1024 = 155.58M = 26% of… | 7 | 5 | 1 |
| [[residual-stream-stability-qymyzlm-design]] | This topic maps residual-stream/normalization stability tricks for the from-scratch ~500M… | 12 | 12 | 7 |
| [[slm-architecture]] | This slice frames sub-1B SLM architecture around two competing KV-efficiency mechanisms. | 2 | 2 | 3 |
| [[small-lm-training-recipes-qymyzlm-design]] | The recipe frontier for a ≤600M Kazakh SLM is now sharply forked into two costed paths. | 11 | 11 | 6 |
| [[sota-slm]] | The sub-1B frontier is converged on a handful of architectural facts: DEPTH beats WIDTH… | 17 | 10 | 5 |
| [[sparse-memory-2026-engram-lineage-beyond]] | The Engram/n-gram-memory lineage is a crowded 2026 subfield (Memory Layers, UltraMemV2… | 8 | 8 | 7 |
| [[tokenizer-agglutinative]] | The frontier for tokenizing agglutinative Kazakh converges on a few CONFIRMED points and… | 11 | 10 | 2 |
| [[tokenizer-morphology]] | The load-bearing, near-consensus finding is that a better tokenizer does NOT buy… | 16 | 14 | 6 |
| [[training-recipes]] | The frontier is anchored by one proven Kazakh recipe: Sherkala-8B reached KazMMLU 41.4%… | 16 | 15 | 5 |
| [[win-bar-protocol-audit]] | The audit resolves how the lab's 32.8% KazMMLU baseline and the Sherkala "ceiling"… | 3 | 2 | 3 |
