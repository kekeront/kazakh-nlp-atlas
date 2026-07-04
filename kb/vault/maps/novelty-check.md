---
type: "moc"
topic: "novelty-check"
nodes: 18
papers: 16
sources: 2
uncertain_claims: 15
tags: ["moc"]
---
# Topic: novelty-check

The novelty audit converges on one point: every component QymyzLM plans is established prior art EXCEPT morpheme-keyed conditional memory. MLA (2405.04434), n-gram/lookup memory (Memory Layers 2412.09764, Engram 2601.07372, X-gram, Tensorizing Engram), morphology-aware tokenizers (MorphBPE 2502.00894, Kazakh MDPI 17(2):128, Mongolian PLM), mHC (2512.24880), byte-level H-Net++ (2508.05628), and Unigram-over-BPE (2508.08424) are all occupied axes. The genuine gap is confirmed: every Engram-lineage paper keys lookup on trailing token-IDs — "suffix n-gram" means last-k token IDs, a naming collision with the linguistic suffix, verbatim across Engram, X-gram, Memory Grafting and Tensorizing — never on morphological stem+suffix units. Contested/REFUTED: the argument that sub-1B DENSE Engram gains transfer to a Kazakh production-vocab model carries verdict REFUTED — the positive dense results used char/tiny vocabs (100, 1024) while the one production-vocab sub-1B datapoint (Memory Grafting 45.03 < MoE 45.62) loses, and Engram's ρ≈75-80% allocation law structurally needs an MoE sparse budget a 600M dense backbone (P_sparse≈0) lacks. SozKZ (2603.20854) is the closest prior art — same ≤600M from-scratch Kazakh target but architecturally vanilla, and it loses knowledge QA to an un-adapted Qwen2.5-0.5B (30.3 vs 31.5), the strongest differentiation opening; X-gram (2604.21724) is the most dangerous collision, a conditional lookup memory at exactly the sub-1.2B target scale (+4.4pt over vanilla, +3.2 over Engram at 0.73B). Open question: whether morpheme-keyed memory actually helps at 600M dense, since the transfer argument is refuted and the token-ID/morpheme naming collision is a reviewer landmine.

## Frontier highlights
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Languag…]] — Defines the one clean novelty gap: morpheme-keyed memory unoccupied; but every Engram config is MoE, no dense sub-1B validation
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — Closest prior art: same from-scratch ≤600M Kazakh target, architecturally vanilla, loses knowledge QA to un-adapted Qwen2.5-0.5B
- [[beyond-n-gram-data-aware-x-gram-extraction-for-efficient-embedding-parameter|Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Sc…]] — Most dangerous collision: conditional lookup memory at exactly sub-1.2B, +4.4pt over vanilla / +3.2 over Engram, still token-ID keyed
- [[tensorizing-engram-sharing-latents-across-n-gram-embeddings-is-beneficial-in|Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LL…]] — REFUTED as transfer argument: dense sub-1B Engram gains only appear under char/vocab-1024 tokenizers, not production vocab
- [[memory-layers-at-scale|Memory Layers at Scale]] — Proof n-gram/lookup memory is a crowded 2026 subfield (6+ papers to 128B), so memory itself cannot be claimed novel
- [[morphbpe-a-morpho-aware-tokenizer-bridging-linguistic-complexity-for-efficient|MorphBPE: A Morpho-Aware Tokenizer Bridging Linguistic Complexity for Efficient…]] — Reference morphology-aware tokenizer tested at 300M/1B, so a Kazakh 'morphology-aware tokenizer' claim is not novel per se

## Papers (16)
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models]] (2026) — deepseek-tech
- [[scaling-embeddings-outperforms-scaling-experts-in-language-models|Scaling Embeddings Outperforms Scaling Experts in Language Models]] (2026) — novelty-check
- [[diffutron-a-masked-diffusion-language-model-for-turkish-language|Diffutron: A Masked Diffusion Language Model for Turkish Language]] (2026) — novelty-check
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] (2026) — tokenizer-morphology
- [[beyond-n-gram-data-aware-x-gram-extraction-for-efficient-embedding-parameter|Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling]] (2026) — novelty-check
- [[tensorizing-engram-sharing-latents-across-n-gram-embeddings-is-beneficial-in|Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs]] (2026) — novelty-check
- [[morphbpe-a-morpho-aware-tokenizer-bridging-linguistic-complexity-for-efficient|MorphBPE: A Morpho-Aware Tokenizer Bridging Linguistic Complexity for Efficient LLM Training Across…]] (2025) — tokenizer-morphology
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting]] (2025) — tokenizer-morphology
- [[improving-low-resource-morphological-inflection-via-self-supervised-objectives|Improving Low-Resource Morphological Inflection via Self-Supervised Objectives]] (2025) — novelty-check
- [[h-net-hierarchical-dynamic-chunking-for-tokenizer-free-language-modelling-in|H-Net++: Hierarchical Dynamic Chunking for Tokenizer-Free Language Modelling in Morphologically-Rich…]] (2025) — novelty-check
- [[rethinking-tokenization-for-rich-morphology-the-dominance-of-unigram-over-bpe|Rethinking Tokenization for Rich Morphology: The Dominance of Unigram over BPE and Morphological Ali…]] (2025) — novelty-check
- [[mhc-manifold-constrained-hyper-connections|mHC: Manifold-Constrained Hyper-Connections]] (2025) — kazakh-turkic-nlp
- [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model|DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model]] (2024) — deepseek-tech
- [[memory-layers-at-scale|Memory Layers at Scale]] (2024) — novelty-check
- [[deepseek-v3-technical-report|DeepSeek-V3 Technical Report]] (2024) — deepseek-tech

## Sources & findings (2)
- [[ieee-xplore-10650812-pre-training-language-model-for|IEEE Xplore 10650812 (Pre-training Language Model for Mongolian with A…]] — The CLOSEST prior on 'morphology-aware ARCHITECTURE for a single agglutinative language' is the Mongolian three-stage ag…
- [[mdpi-information-2026-17-2-128-morphology-aware|MDPI Information 2026, 17(2):128 (Morphology-Aware Segmentation and To…]] — A Kazakh-specific morphology-aware tokenization framework already exists (CSE-guided segmentation, 'The Kazakh Case'), s…

## Related topics
- [[kazakh-turkic-nlp]] — 6 shared nodes
- [[tokenizer-morphology]] — 4 shared nodes
- [[deepseek-tech]] — 3 shared nodes
- [[inference-tts]] — 3 shared nodes
- [[novelty-check-has-any-2026-preprint-impl]] — 3 shared nodes

[[Home]]
