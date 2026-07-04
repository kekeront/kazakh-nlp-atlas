---
kb_id: "arxiv:2605.20948"
type: "paper"
title: "Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory"
arxiv_id: "2605.20948"
doi: null
hf_repo: null
year: 2026
topics: ["does-the-engram-conditional-memory-modul", "post-hoc-attachment-of-engram-style-cond"]
claims: 3
uncertain_claims: 0
verdicts: []
aliases: ["Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory", "arXiv:2605.20948", "arxiv:2605.20948"]
tags: ["paper", "topic/does-the-engram-conditional-memory-modul", "topic/post-hoc-attachment-of-engram-style-cond"]
---
# Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory

[arXiv](https://arxiv.org/abs/2605.20948)
**Topics:** [[does-the-engram-conditional-memory-modul]], [[post-hoc-attachment-of-engram-style-cond]]

> [!abstract]
> Scaling conditional memory offers a promising way to increase language-model capacity, but existing methods such as Engram learn large memory tables from scratch during pre-training, making memory scaling expensive and sometimes ineffective. We propose Memory Grafting, a conditional memory scaling method that utilizes frozen hidden states from a grafting model as conditional n-gram memory. Given f …

## Claims

> [!note] CLAIM — does-the-engram-conditional-memory-modul
> There is a DIRECT sub-1B datapoint and it is NEGATIVE: vanilla Engram UNDERPERFORMS its MoE baseline at ~1B scale. Memory Grafting §4.2 states verbatim 'we also observe that vanilla Engram underperforms the MoE baseline in this 1B-scale setting, with 45.03 versus 45.62' (average over 9 benchmarks: ARC-C/E, BoolQ, SIQA, RACE, LAMBADA, WinoGrande, PIQA, HellaSwag). Config: 0.92B total / 0.29B active MoE, 64 routed experts top-4 + 1 shared, 50B tokens. Attributed cause: 'the limited Engram embedding table in 0.9B model, which lead to more hash collisions.'
>
> **Numbers:** vanilla Engram 45.03 vs MoE baseline 45.62 (avg, 9 tasks); 0.92B total / 0.29B active MoE; 50B tokens
> **Relevance:** This is the single most load-bearing fact for the paper: the 0-FLOP hash-lookup gain does NOT survive at ~1B even on an MoE backbone (and 0.29B active is smaller than the planned 600M dense). The central 'Engram lifts a 600M Kazakh model above Qwen3-0.6B 32.8%' claim is directly contradicted by the only near-scale evidence that exists.
> **Source:** arXiv 2605.20948 — Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory, §4.2 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — does-the-engram-conditional-memory-modul
> The small-scale collision problem is FIXABLE, but only by abandoning the live token-ID hash-table Engram the user's design uses. Memory Grafting recovers at the same 1B scale (MG 46.98 vs MoE 45.62 vs vanilla Engram 45.03) via OFFLINE frozen conditional memory with exact longest-match retrieval (no live hashing). Lngram (2605.24869) similarly replaces tokenizer-ID hash keys with learned latent-space discrete keys to remove collisions; smallest config 0.42B active MoE, evaluated at 22B (MoE+Lngram 0.5288 vs MoE+Engram 0.5225 vs MoE 0.5146). Neither offers a dense datapoint.
>
> **Numbers:** Memory Grafting @1B: 46.98 (MG) vs 45.62 (MoE) vs 45.03 (vanilla Engram). Lngram @22B: 0.5288 vs Engram 0.5225 vs MoE 0.5146; Lngram smallest = 0.42B active MoE
> **Relevance:** If conditional memory is to help at 600M, the design must switch to a collision-robust variant (frozen exact-match memory or learned latent keys), which is a materially different, more complex module — changing both the engineering and the novelty framing of the paper.
> **Source:** arXiv 2605.20948 (Memory Grafting §4.2) and arXiv 2605.24869 (Lngram, Table 1) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[lngram-n-gram-conditional-memory-in-latent-space]]

> [!note] CLAIM — post-hoc-attachment-of-engram-style-cond
> [transferable-untested — GAP CONFIRMED] No Engram-lineage paper attaches hash-keyed conditional memory to a pretrained backbone: Memory Grafting explicitly relegates it to future work ('Beyond from-scratch pre-training, the same construction can serve as a post-training and continual-learning strategy' — listed under Future Work, zero experiments), and its own memory is frozen donor hidden-states with only recipient-side projection+gating trained from scratch. Combined with vanilla Engram's negative sub-1B result (45.03 vs MoE 45.62 at 0.92B, attributed to hash collisions in the small table), the specific risk for QymyzLM's setting is NOT gate suppression (refuted at 0.5-1.7B by findings 1-2, both with LEARNED keys/routing) but collision noise in a deterministic-hash table too small for the key space — which no post-hoc experiment anywhere has probed. The lab's ~3B-token kill-switch ablation remains unanswerable from literature.
>
> **Numbers:** MG @0.92B total / 0.29B active MoE, 50B tokens: MG 46.98 vs MoE 45.62 vs vanilla Engram 45.03 (9-task avg); donor models Qwen3.5-35B-A3B, DeepSeek-V2-Lite, GLM-4.7-Flash; posthoc-attach experiments in Engram lineage: 0
> **Relevance:** Confirms the ablation is genuine novelty (publishable even as a negative result) and redirects the experimental hypothesis: instrument for collision rate and slot-usage entropy, not just gate magnitude. Morpheme-keyed addressing (the paper's novelty) directly shrinks the key space and is therefore also a collision mitigation — a causal link worth stating in the paper.
> **Source:** arXiv:2605.20948 (Memory Grafting) Sec 4.2 + appendix Future Work, verified via https://arxiv.org/html/2605.20948; arXiv:2601.07372 (Engram) · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large]]

## Related
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models]] — Memory Grafting is Engram-lineage; slice cites its identical suffix-n-gram gate α=sigmoid(<RMSNorm K,Q>/√d)
- [[a-collision-free-hot-tier-extension-for-engram-style-conditional-memory-a|A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Stud…]] — Both target the small-table hash-collision failure that sinks sub-1B Engram; MG uses offline exact-match, this a collision-free hot-tier
- [[beyond-n-gram-data-aware-x-gram-extraction-for-efficient-embedding-parameter|Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling]] — Both Engram-lineage fixes to n-gram memory; X-gram uses data-aware extraction vs MG's frozen donor hidden-states
- [[lngram-n-gram-conditional-memory-in-latent-space|Lngram: N-gram Conditional Memory in Latent Space]] — Both kill tokenizer-ID hash collisions: MG via offline exact longest-match, Lngram via learned latent discrete keys; MG cites Lngram…
- [[tensorizing-engram-sharing-latents-across-n-gram-embeddings-is-beneficial-in|Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs]] — Tensorizing's positive micro-scale dense gains contrast with Memory Grafting's negative production-vocab sub-1B result (45.03 vs MoE 45.62)

[[Home]]
