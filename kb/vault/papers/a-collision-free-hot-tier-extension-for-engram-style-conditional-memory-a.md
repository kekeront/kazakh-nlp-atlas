---
kb_id: "arxiv:2601.16531"
type: "paper"
title: "A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Study of Training Dynamics"
arxiv_id: "2601.16531"
doi: null
hf_repo: null
year: 2026
topics: ["sparse-memory-2026-engram-lineage-beyond"]
claims: 3
uncertain_claims: 1
verdicts: []
aliases: ["A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Study of Training Dynamics", "arXiv:2601.16531", "arxiv:2601.16531"]
tags: ["paper", "topic/sparse-memory-2026-engram-lineage-beyond"]
---
# A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Study of Training Dynamics

[arXiv](https://arxiv.org/abs/2601.16531)
**Topics:** [[sparse-memory-2026-engram-lineage-beyond]]

> [!abstract]
> We investigate whether high-frequency key collisions are a primary bottleneck in Engram-style conditional memory. To isolate the effect of collisions, we introduce Engram-Nine, a collision-free hot-tier extension that maps the most frequent n-grams through a Minimal Perfect Hash Function (MPHF) while retaining the original multi-head hashed lookup as a cold tier. Under a strictly iso-parameter set …

## Claims

> [!warning] UNCERTAIN — sparse-memory-2026-engram-lineage-beyond
> [transferable-untested] Engram-Nine (post-KB, Jan 2026): under strict iso-parameter control on a DENSE GPT-2 backbone, eliminating high-frequency hash collisions via a Minimal-Perfect-Hash hot tier gives NO significant validation-loss benefit — collisions act as implicit regularization, and the gate misassigns credit (favors hot n-grams even after cold positions become lower-loss). Setup: ~185M dense GPT-2 (12L, d=768, DeepSeek-V3 tokenizer 128,815 vocab), Engram at layers {2,4,6} with ONE SHARED table set across all three layers (per-layer independent gating/conv/projection, ~1.6M params), n={2,3}, K=2 heads, 64d/head, 128M memory params, FineWeb-Edu, only ~82M training tokens, 1x A100-40GB.
>
> **Numbers:** Hash-500K val loss 4.4809 (std 0.0082) vs collision-free Nine-100/400K 4.4799 (std 0.0123) — delta 0.001, not significant; Hash-300K 4.4825 comparable. MPHF adds 11-12% throughput penalty (~1910 -> ~1693 tok/s). Coverage: top-100K 2-grams cover ~55% of training queries, 3-grams ~23%. Hot/cold flip at iter 2000-3000 across all configs.
> **Relevance:** Directly counters the Memory Grafting narrative (KB) that hash collisions are the sub-1B killer — at 185M dense, removing high-frequency collisions buys nothing. Design implication: spend ZERO budget on collision-free indexing/MPHF machinery; DO copy the shared-table-across-insertion-layers trick (3 injection sites for one 128M table) — the single best param-efficiency lever for a <=600M model. Caveat: 82M tokens is severely undertrained (val loss 4.48) and it is a single-author preprint.
> **Source:** arXiv:2601.16531v2 (PDF read in full, pages 1-8) · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — sparse-memory-2026-engram-lineage-beyond
> [gap re-verified open as of 2026-07-04] Fresh multi-formulation searches (Engram follow-ups July 2026; morpheme-aware memory agglutinative 2026) confirm ZERO published work keys conditional/lookup memory on morphological units. All post-KB Engram-lineage entries are non-morphological: Engram-Nine (2601.16531, collision study, token-ID n-grams), CXL memory pooling (2603.10087, datacenter hardware tiering of Engram tables), User-as-Engram (2606.19172, per-user parametric edits), Dual-level Engram for generative recommendation (2605.11447), MolGram (2606.12113, character n-grams). The morpheme-keyed + vowel-harmony-normalized + Turkic-benchmarked contribution remains unoccupied.
>
> **Numbers:** morpheme-KEYED conditional-memory papers found: 0 (KB count confirmed); 5 new lineage entries checked, all token-ID/character/user-keyed.
> **Relevance:** The paper's core novelty claim survives the six months since the KB was written. Nearest encroachments to monitor: MolGram (sub-lexical character keys) and Morpheus (Turkic morpheme segmentation) — a merger of the two by anyone else would close the gap.
> **Source:** WebSearch sweeps 2026-07-04 + arXiv:2601.16531, 2603.10087, 2606.19172, 2605.11447, 2606.12113 · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — sparse-memory-2026-engram-lineage-beyond
> [transferable-untested, derived] Host-offload machinery is UNNECESSARY at QymyzLM scale on Kaggle T4: an Engram-Nine-sized shared table (128M params) is 256MB fp16 and a 300M-param table is 600MB — both trivially VRAM-resident within T4's 16GB alongside a 600M fp16 model (~1.2GB) + QLoRA optimizer state. Engram's deterministic indexing (indices depend only on input token IDs — restated verbatim in Engram-Nine) still pays off on T4 as CPU-side index precomputation in the dataloader, not as offload. The Engram '<3% overhead' offload result targets 100B-scale tables over NVMe; Meta's 3TB/s kernel numbers are HBM-class, but EmbeddingBag lookups at k<=32 are bandwidth-trivial at T4's 320GB/s GDDR6.
>
> **Numbers:** 128M-param table = 256MB fp16; 300M = 600MB; T4 16GB VRAM / 320GB/s; Engram-Nine MPHF alternative costs 11-12% throughput (avoid); Meta kernel 3TB/s vs 400GB/s PyTorch on HBM GPUs.
> **Relevance:** Removes an entire engineering track from the design spec: no GPU-host cache hierarchy, no NVMe tiering. The only offload-adjacent work worth doing on T4x2 is precomputing n-gram indices on CPU during data loading (deterministic, free). Frees engineering budget for the morpheme-key ablation.
> **Source:** arXiv:2601.16531 (determinism restated); arXiv:2601.07372 (<3% @ 100B, KB); arXiv:2412.09764 (kernel numbers); T4 specs: 16GB GDDR6, 320GB/s, PCIe 3.0 · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large]], [[memory-layers-at-scale]]

## Related
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models]] — Direct Engram extension: collision-free hot-tier fixes the multiplicative-XOR hash collisions of this base design
- [[memory-grafting-scaling-language-model-pre-training-via-offline-conditional|Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory]] — Both target the small-table hash-collision failure that sinks sub-1B Engram; MG uses offline exact-match, this a collision-free hot-tier
- [[vrcp-nozaki-et-al-2nd-sumeval-workshop-2025-aclanthology|VRCP, Nozaki et al., 2nd SUMEval Workshop 2025, aclanthology.org/2025.…]] — VRCP holds vocab size constant (155.58M table, zero freed) — unlike a shrinking swap it yields no headroom for Engram, a tradeoff against…

[[Home]]
