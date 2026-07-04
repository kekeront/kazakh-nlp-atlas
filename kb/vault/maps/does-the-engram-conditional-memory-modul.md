---
type: "moc"
topic: "does-the-engram-conditional-memory-modul"
nodes: 4
papers: 4
sources: 0
uncertain_claims: 4
tags: ["moc"]
---
# Topic: does-the-engram-conditional-memory-modul

The frontier question is whether Engram-style conditional memory helps at QymyzLM's ≤600M dense scale, and the literature answers NO with direct evidence. Engram is CONFIRMED to work only at MoE scale ≥568M active: it beats an iso-param/iso-FLOP MoE at 27B (MMLU +3.0, BBH +5.0) via O(1) hashed n-gram lookup at ~0 extra FLOPs, but its own U-shaped ρ-law keeps 75-80% of the sparse budget in routed experts, so the allocation framework structurally requires MoE and ρ=0 (pure dense+Engram) is never tested. The one direct sub-1B datapoint is NEGATIVE — Memory Grafting reports vanilla Engram at 45.03 vs its MoE baseline 45.62 at 0.92B, attributed to hash collisions in a table too small for the key space — and it only recovers (46.98) by abandoning the live token-ID hash table for offline exact-match memory, mirrored by Lngram's learned latent keys. TOBA-LM is the sole dense+agglutinative artifact (1.2B dense GPT-2 + 500K×768 table) but its evidence is uncontrolled convergence-speed, not a with/without ablation, and it only post-hoc reinterprets syllable n-grams as "morphemes" without any segmenter. On param-counting, the memory table is fully counted in P_tot, pushing a 500M dense backbone + ~512M table to ~1B total — outside the ≤600M class the Qwen3-0.6B/SozKZ peer group is measured by. The open question — whether deterministic-hash collision noise sinks a small table on a dense backbone at the lab's ~3B-token kill-switch ablation — is unanswerable from literature: zero post-hoc-attach experiments exist in the entire Engram lineage.

## Frontier highlights
- [[memory-grafting-scaling-language-model-pre-training-via-offline-conditional|Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Mem…]] — The only direct sub-1B datapoint, and it's NEGATIVE: vanilla Engram 45.03 vs MoE 45.62, collision-bound
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Languag…]] — Source paper: zero dense config; ρ-law keeps 75-80% in MoE experts, so framework structurally needs routing
- [[adaptive-engram-memory-system-for-indonesian-language-model-generative-ai-based|Adaptive Engram Memory System for Indonesian Language Model: Generative AI Based…]] — Only dense+agglutinative Engram (TOBA-LM 1.2B), but loss-only, uncontrolled, no morpheme segmenter
- [[mhc-manifold-constrained-hyper-connections|mHC: Manifold-Constrained Hyper-Connections]] — The paired residual-stream choice (mHC) also has NO sub-3B and NO dense validation — smallest tested is 3B MoE

## Papers (4)
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models]] (2026) — deepseek-tech
- [[adaptive-engram-memory-system-for-indonesian-language-model-generative-ai-based|Adaptive Engram Memory System for Indonesian Language Model: Generative AI Based on TOBA LM for Bata…]] (2026) — does-the-engram-conditional-memory-modul
- [[memory-grafting-scaling-language-model-pre-training-via-offline-conditional|Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory]] (2026) — does-the-engram-conditional-memory-modul
- [[mhc-manifold-constrained-hyper-connections|mHC: Manifold-Constrained Hyper-Connections]] (2025) — kazakh-turkic-nlp

## Related topics
- [[kazakh-turkic-nlp]] — 2 shared nodes
- [[novelty-check]] — 2 shared nodes
- [[novelty-check-has-any-2026-preprint-impl]] — 2 shared nodes
- [[post-hoc-attachment-of-engram-style-cond]] — 2 shared nodes

[[Home]]
