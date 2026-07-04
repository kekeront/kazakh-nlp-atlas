---
kb_id: "arxiv:2606.08347"
type: "paper"
title: "Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs"
arxiv_id: "2606.08347"
doi: null
hf_repo: null
year: 2026
topics: ["novelty-check", "novelty-check-has-any-2026-preprint-impl", "sparse-memory-2026-engram-lineage-beyond"]
claims: 5
uncertain_claims: 2
verdicts: ["refuted"]
aliases: ["Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs", "arXiv:2606.08347", "arxiv:2606.08347"]
tags: ["paper", "topic/novelty-check", "topic/novelty-check-has-any-2026-preprint-impl", "topic/sparse-memory-2026-engram-lineage-beyond"]
---
# Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs

[arXiv](https://arxiv.org/abs/2606.08347)
**Topics:** [[novelty-check]], [[novelty-check-has-any-2026-preprint-impl]], [[sparse-memory-2026-engram-lineage-beyond]]

> [!abstract]
> Modern language models represent text using discrete token-level embeddings, which forces recurring multi-token patterns to be learned implicitly across Transformer layers. Both Over-tokenized Transformers and Engram attempt to address this limitation by explicitly incorporating multi-token (n-gram) memories. However, they rely on separate hash tables for each n-gram order, which introduces hash c …

## Claims

> [!warning] UNCERTAIN — novelty-check
> Tensorizing Engram directly extends the user's exact base component (DeepSeek Engram) by tensor-factorizing n-gram embeddings to share latents across n-gram orders, reducing parameter count. Any user claim about 'efficient n-gram memory tables' must account for this.
>
> **Numbers:** 2MB PDF; reports parameter reduction vs full n-gram embedding matrices while maintaining performance; multiple scales up to ~1B (exact percentages not extracted — PDF truncated)
> **Relevance:** The user's {2,3}-gram hash tables at ~512M sparse params are exactly what Tensorizing Engram compresses. Cite it; consider adopting latent-sharing to cut the 512M sparse footprint (relevant for a $264 single-A100 budget).
> **Source:** arXiv:2606.08347 (Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — novelty-check-has-any-2026-preprint-impl
> The memory-augmentation field is confirmed to move roughly monthly and NONE of the variants touches Turkic/Kazakh/agglutinative evaluation: Engram (Jan 2026, scaled to 27B) -> X-gram (Apr) -> Lngram + Memory Grafting (May) -> Tensorizing Engram (Jun 6, CP-decomposition latent sharing) -> Morpheus (Jun). Adjacent memory-layer lines (UltraMemV2 scaling to 120B, arXiv 2508.18756; Mixture of Chapters, arXiv 2603.21096; Mixture of Lookup Key-Value Experts, arXiv 2512.09723) are all token-ID / learned-slot keyed, no morphology.
>
> **Numbers:** Tensorizing Engram 2606.08347 (Jun 6 2026): TN-gram 48M params val BPB 1.071 vs Engram 60M/1.070 at 18 layers; UltraMemV2 2508.18756 (120B); Mixture of Chapters 2603.21096
> **Relevance:** Confirms the novelty-check's 'crowded, monthly-moving' concern and justifies re-running this exact search at camera-ready. As of now the morpheme axis is still unclaimed, but a morpheme/latent-unit variant could land any month — ship soon and keep the search query on file.
> **Source:** arXiv 2606.08347 (Tensorizing Engram); 2508.18756 (UltraMemV2); 2603.21096 (Mixture of Chapters); 2512.09723 (Mixture of Lookup Key-Value Experts) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[ultramemv2-memory-networks-scaling-to-120b-parameters-with-superior-long]]

> [!note] CLAIM — sparse-memory-2026-engram-lineage-beyond
> [transferable-untested] Tensorizing Engram (fills KB's [UNVERIFIED] entry) provides the first CONTROLLED dense+Engram datapoints at micro scale: plain dense GPT backbones (9L d=512 GQA 8Q:4KV; 18L d=1024), FineWeb, ~3.1B tokens (6,000 steps x 524,288-token batches), tiny vocab 1,024 (plus 8,192 ablation). Vanilla Engram ATTACHED to dense improves both scales; TN-gram (CP decomposition, rank R=1024/1800, latents shared across n-gram orders N in {2..5}, insertion layers {1,7}) matches Engram BPB with ~21-27% fewer memory params and better CORE.
>
> **Numbers:** 9L: raw BPB 1.251/CORE 0.060 -> Engram +26M params 1.209/0.072 -> TN-gram +19M 1.208/0.083. 18L: raw 1.086/0.107 -> Engram +60M 1.070/0.115 -> TN-gram +48M 1.071/0.120. MC avg 33.48->35.44 (9L), 36.85->37.82 (18L). Most gains reached by N=5.
> **Relevance:** Directly de-risks QymyzLM's biggest architecture question (does Engram help a DENSE sub-600M backbone at all): yes at 3B tokens on dense — the regime closest to our 10B-token Kazakh budget. CP factorization is a drop-in ~25% table-param saving inside the <=600M total cap. Caveat: vocab 1,024 = very high fertility; gains may partially come from sub-lexical tokens (which is actually Kazakh-analogous).
> **Source:** arXiv:2606.08347 (HTML v1, fetched 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — sparse-memory-2026-engram-lineage-beyond
> [transferable-untested] Micro-scale Engram configs across the lineage converge on a shrunken template far below the original 27B config (K=8 heads, d_mem=1280, 2.26M slots): at <=200M dense scale the working configs are K=2-4 heads x 64d per head, n-grams {2,3} (MolGram extends to 4-6 for character tokens), 0.4-1M slots, 2-3 insertion sites in the first half of the network (layers {1,7}, {2,4,6}, [1,4]), one table SHARED across sites. Quality-per-memory-param at this scale: TN-gram 19M memory params bought -0.043 BPB and +0.023 CORE on a 9L backbone; Engram-Nine's 128M table on 185M backbone (0.69:1 memory:backbone) trained stably on a single 40GB GPU.
>
> **Numbers:** K=2-4, 64d/head, n={2,3} (to 6 for char-level), slots 400K-1M prime-sized, 2-3 shared insertion sites; TN-gram: 19M params -> deltaBPB -0.043; memory:backbone ratios used: 0.10-0.73:1 dense.
> **Relevance:** This is the drop-in parameter template for the design panel: a ~100-150M-param shared table (K=2-4 x 64d, ~500K-1M slots, injected at layers ~{2, L/3, L/2}) keeps QymyzLM's TOTAL footprint at ~550-600M with a ~450M backbone — inside the size class, unlike the KB's earlier 512M-table sketch that ballooned to ~1B total.
> **Source:** arXiv:2606.08347; 2606.12113; 2601.16531 (configs read from primary sources 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

> [!failure] REFUTED — sparse-memory-2026-engram-lineage-beyond
> [transferable-untested] The high-fertility regime is where sub-1B memory gains are demonstrated: both positive dense results use tokenizers that fragment words far more than production BPE (TN-gram: vocab 1,024; MolGram: vocab 100 character-level), so {2..5}-token n-grams span sub-word/word-level units — while the one NEGATIVE sub-1B result (Memory Grafting's vanilla-Engram 45.03 vs MoE 45.62, KB) used a production-vocab MoE. Under a Kazakh tokenizer at fertility ~2.0 tok/word (SozKZ-class), {2,3}-token grams cover roughly 1-1.5 words = stem+suffix-chain windows — structurally the same sub-lexical regime where the dense gains appeared. Never tested on any natural high-fertility language.
>
> **Numbers:** Positive dense results: vocab 100 and 1,024; negative sub-1B result: production vocab MoE; Kazakh target fertility <2.0 tok/word means 2-3-token grams ~= 1-1.5 words.
> **Relevance:** This is the sharpest published-evidence argument FOR putting Engram-style memory in a Kazakh SLM specifically (and it doubles as the paper's motivation section): Kazakh's agglutinative fertility naturally places token n-grams at intra-word granularity, matching the regime where dense memory gains exist. It is also honestly untested — flag as the campaign's central empirical bet.
> **Verdict:** REFUTED (as transfer argument)
> **Verification note:** Refute-first pass: the "fertility ~2.0 => Kazakh benefits like vocab 100-8192" step is a CATEGORY ERROR — positive dense memory results exist only at starved vocab (100-8192, English/SMILES), a vocab-fragmentation axis, NOT morphological fertility at a 32-50K production vocab. ZERO positive dense result at vocab >=30K; the one sub-1B production-vocab datapoint (Memory Grafting 2605.20948, MoE, vocab 128256) is NEGATIVE for vanilla Engram (45.03<45.62). TN-gram dense BPB gain is single-seed (1337, no std) and DECAYS with scale (-0.043@28M -> -0.015@227M), extrapolating to <=0.008 at 600M (inside noise). Steelman: vocab-8192 ablation persists => "memory helps Kazakh" is PLAUSIBLE-BUT-UNTESTED, not disproven.
> **Settling experiment:** Engram {2,3}-grams K=8 ~26M table on ~100M dense GPT + 32K Kazakh BPE (fertility 1.4-2.0), ~1B kk tokens, >=3 seeds, vs ISO-PARAM/ISO-FLOP dense baseline (spend 26M on width, not raw). Pillar SUPPORTED only if dBPB<=-0.01 and CI excludes 0. ~10-15 T4 GPU-h.
> **Source:** arXiv:2606.08347 (vocab 1,024); 2606.12113 (vocab 100); 2605.20948 (negative datapoint, KB) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[why-do-language-models-perform-worse-for-morphologically-complex-languages|Why do language models perform worse for morphologically complex languages?]] — Tensorizing's high-fertility transfer argument (Kazakh fragmentation mimics tiny-vocab regime) leans on morphological-complexity penalty…
- [[ultramemv2-memory-networks-scaling-to-120b-parameters-with-superior-long|UltraMemV2: Memory Networks Scaling to 120B Parameters with Superior Long-Context Learning]] — both scale/compress memory networks; UltraMemV2 learned-slot keyed to 120B, TN-gram CP-factorizes n-gram tables, neither morpheme
- [[memory-grafting-scaling-language-model-pre-training-via-offline-conditional|Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory]] — Tensorizing's positive micro-scale dense gains contrast with Memory Grafting's negative production-vocab sub-1B result (45.03 vs MoE 45.62)
- [[augmenting-molecular-language-models-with-local-n-gram-memory|Augmenting Molecular Language Models with Local $n$-gram Memory]] — both micro-scale dense Engram configs on fragmenting vocabs; MolGram char-level n={4,6}, TN-gram CP-shares latents across orders

[[Home]]
