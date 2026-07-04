---
kb_id: "arxiv:2412.09764"
type: "paper"
title: "Memory Layers at Scale"
arxiv_id: "2412.09764"
doi: null
hf_repo: null
year: 2024
topics: ["novelty-check", "sparse-memory-2026-engram-lineage-beyond"]
claims: 2
uncertain_claims: 1
verdicts: ["confirmed"]
aliases: ["Memory Layers at Scale", "arXiv:2412.09764", "arxiv:2412.09764"]
tags: ["paper", "topic/novelty-check", "topic/sparse-memory-2026-engram-lineage-beyond"]
---
# Memory Layers at Scale

[arXiv](https://arxiv.org/abs/2412.09764)
**Topics:** [[novelty-check]], [[sparse-memory-2026-engram-lineage-beyond]]

> [!abstract]
> Memory layers use a trainable key-value lookup mechanism to add extra parameters to a model without increasing FLOPs. Conceptually, sparsely activated memory layers complement compute-heavy dense feed-forward layers, providing dedicated capacity to store and retrieve information cheaply. This work takes memory layers beyond proof-of-concept, proving their utility at contemporary scale. On downstre …

## Claims

> [!note] CLAIM — novelty-check
> n-gram / lookup memory in LMs is now a CROWDED 2026 subfield, not a novel axis. Beyond DeepSeek Engram (the user's base), at least 6 distinct 2025-2026 papers scale explicit embedding/lookup memory: Meta 'Memory Layers at Scale' (product-key memory, sparse KV lookup, no extra FLOPs), UltraMemV2, 'Scaling Embeddings Outperforms Scaling Experts', Tensorizing Engram, X-gram, Mixture of Lookup Key-Value Experts. A Kazakh paper CANNOT claim conditional n-gram memory itself as new — only a language/morphology-specific instantiation.
>
> **Numbers:** Memory Layers at Scale: up to 128B memory params, pretrained to 1T tokens, beats dense models with >2x compute and MoE at matched compute+params; ICLR'25
> **Relevance:** Kills any 'we introduce n-gram memory for LMs' framing. The paper must position Engram as prior art and claim only the morpheme-conditioned variant + Kazakh evaluation as new.
> **Source:** arXiv:2412.09764 (Memory Layers at Scale); arXiv:2601.07372 (DeepSeek Engram, user's cite) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large]]

> [!success] CONFIRMED — sparse-memory-2026-engram-lineage-beyond
> [transferable-untested] Memory Layers at Scale (Meta) is the strongest DENSE sub-400M factual-knowledge evidence in the whole memory literature — product-key (learned keys, no n-gram hashing), value pool SHARED across 3 memory layers that replace FFNs (stride 4 at 134M, stride 8 larger), key dim = d_model/2 (two half-key sets), value dim = d_model, 2^20 values at base scales, trained 1T tokens (Llama2 32K tokenizer). At 134M dense the memory variant ~3.5x's NaturalQuestions and ~2.4x's TriviaQA, beating iso-param MoE and PEER.
>
> **Numbers:** 134M: dense NQ 0.91 / TQA 7.7 -> Memory 2.1/16.31 -> Memory+ 3.16/18.77; MoE 2.49/13.08; PEER 2.46/16.34. 373M: dense 2.58/17.68 -> Memory+ 5.76/28.10; MoE 3.99/19.94; PEER 5.1/26.39. Custom CUDA EmbeddingBag: ~3TB/s fwd vs PyTorch 400GB/s, ~6x end-to-end kernel speedup. Memory pool at 134M is ~2^20 x 768 ~= 0.8B params (derived from stated dims, not printed in paper — uncertain).
> **Relevance:** The mandatory ablation arm for the design panel: product-key memory has dense small-scale FACTUAL gains that Engram-lineage never showed (Engram's sub-1B datapoint is negative, MoE-only). But two transfer caveats: 1T training tokens (100x our budget) and a memory pool ~6x the backbone (blows the <=600M total footprint unless shrunk to ~2^17-2^18 values). Kernel is open-sourced; bandwidth-bound lookups are fine on T4's 320GB/s.
> **Verdict:** CONFIRMED (gains) + FOOTPRINT CORRECTION
> **Verification note:** Table-1 dense factual gains verified verbatim (134M dense NQ0.91/TQA7.7 -> Memory+ 3.16/18.77; 373M -> 5.76/28.10). BUT re-derived footprint: shared pool = 2^20 x d_model. At 134M (d=768): 805M params = 6.0x backbone => 937M TOTAL (matches paper Table 1, 937M, delta 2M). At 373M (d=1024): 1.07B pool => ~1.45B total. So "134M dense + PKM" is a ~0.94B-total artifact — OUTSIDE the <=600M-total class, same P_tot trap as Engram. Gains obtained at 1T tokens (x100 our budget) with table >=2^20; NO datapoint below 2^20 slots or below 1T tokens at these scales. <=600M total allows only 2^19.2 values — off the bottom of every curve. PKM is NOT a cheap <=600M arm.
> **Settling experiment:** If PKM considered: our ablation tables 2^17/2^18/2^19 x d_model at 10B kk tokens on Kazakh factual-QA probe, memory counted in P_tot. Gain vanishing below 2^20 or below ~100B tokens => footprint trap.
> **Source:** arXiv:2412.09764 (HTML v2, Table 1 fetched 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[deepseekmoe-towards-ultimate-expert-specialization-in-mixture-of-experts|DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models]] — Memory Layers beats iso-param DeepSeekMoE-style MoE at 134M/373M on NQ/TQA — memory vs experts as competing sparse axes
- [[scaling-embeddings-outperforms-scaling-experts-in-language-models|Scaling Embeddings Outperforms Scaling Experts in Language Models]] — Both scale explicit embedding/lookup memory as a sparsity axis; parallel lineage entries to Memory Layers' product-key result
- [[continual-learning-via-sparse-memory-finetuning|Continual Learning via Sparse Memory Finetuning]] — A sparsely finetunes the Berges-et-al memory-layer models B introduces; B is the from-scratch substrate A adapts (best-case bound, not…

[[Home]]
