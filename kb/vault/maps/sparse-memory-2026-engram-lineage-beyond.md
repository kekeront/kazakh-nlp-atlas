---
type: "moc"
topic: "sparse-memory-2026-engram-lineage-beyond"
nodes: 8
papers: 8
sources: 0
uncertain_claims: 7
tags: ["moc"]
---
# Topic: sparse-memory-2026-engram-lineage-beyond

The Engram/n-gram-memory lineage is a crowded 2026 subfield (Memory Layers, UltraMemV2, Tensorizing Engram, Lngram, X-gram, MolGram, Engram-Nine), so conditional lookup-memory itself is CONFIRMED not novel — only a morphology/Turkic-specific instantiation is open, and searches re-confirm ZERO published work keys memory on morphological units. What is established at sub-1B DENSE scale: Memory Layers gives ~3.5x NaturalQuestions gains at 134M (product-key, value pool shared across 3 FFN-replacing layers); Tensorizing Engram supplies the first controlled micro-scale datapoints (TN-gram matches Engram BPB with ~21-27% fewer memory params via CP decomposition); MolGram is the smallest validated instance (6.7M, char vocab 100). Two framing claims are REFUTED: the "only adaptation-time datapoint" framing (Lngram's frozen-backbone attach to Qwen3-1.7B gains +5.54pp BDD, CONFIRMED numbers but on driving-QA, not Turkic), and the high-fertility transfer argument (both positive dense results used tiny vocab 100/1,024, and the one production-vocab sub-1B result — Memory Grafting — was negative 45.03 vs MoE 45.62). Engram-Nine adds two useful negatives: collision-free MPHF hot-tier gives NO significant val-loss benefit (collisions act as implicit regularization) at 11-12% throughput cost, and host-offload is unnecessary at QymyzLM's T4 scale (a 128M-300M table is 256-600MB fp16, VRAM-resident). The open question is whether explicit morpheme-segmented + vowel-harmony-normalized keys — sourceable now from Turkic segmenters like Morpheus/VerChol/Kazakh CSE — actually buy accuracy on a dense sub-600M Kazakh model, which no paper has tested.

## Frontier highlights
- [[a-collision-free-hot-tier-extension-for-engram-style-conditional-memory-a|A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Contr…]] — Two clean negatives: collision-free hot-tier = no val-loss gain (collisions regularize); T4 host-offload unnecessary
- [[tensorizing-engram-sharing-latents-across-n-gram-embeddings-is-beneficial-in|Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LL…]] — First controlled dense micro-scale Engram: TN-gram matches BPB at ~21-27% fewer params; high-fertility transfer REFUTED
- [[lngram-n-gram-conditional-memory-in-latent-space|Lngram: N-gram Conditional Memory in Latent Space]] — Only adaptation-time attach datapoint (frozen Qwen3-1.7B +5.54pp) but latent keys, driving-QA — not the QymyzLM plan
- [[memory-layers-at-scale|Memory Layers at Scale]] — Strongest dense sub-400M factual evidence: ~3.5x NQ at 134M via product-key memory, beats iso-param MoE
- [[adaptive-engram-memory-system-for-indonesian-language-model-generative-ai-based|Adaptive Engram Memory System for Indonesian Language Model: Generative AI Based…]] — Only dense+Engram+agglutinative artifact (TOBA LM) but no morpheme segmenter, training-loss-only, uncontrolled
- [[morpheus-a-morphology-aware-neural-tokenizer-and-word-embedder-for-turkish|Morpheus: A Morphology-Aware Neural Tokenizer and Word Embedder for Turkish]] — Morpheme-aware Turkic tokenizer exists (F1 0.61) — morpheme keys are sourceable, yet no memory table uses them

## Papers (8)
- [[a-collision-free-hot-tier-extension-for-engram-style-conditional-memory-a|A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Study of Train…]] (2026) — sparse-memory-2026-engram-lineage-beyond
- [[adaptive-engram-memory-system-for-indonesian-language-model-generative-ai-based|Adaptive Engram Memory System for Indonesian Language Model: Generative AI Based on TOBA LM for Bata…]] (2026) — does-the-engram-conditional-memory-modul
- [[lngram-n-gram-conditional-memory-in-latent-space|Lngram: N-gram Conditional Memory in Latent Space]] (2026) — novelty-check-has-any-2026-preprint-impl
- [[tensorizing-engram-sharing-latents-across-n-gram-embeddings-is-beneficial-in|Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs]] (2026) — novelty-check
- [[augmenting-molecular-language-models-with-local-n-gram-memory|Augmenting Molecular Language Models with Local $n$-gram Memory]] (2026) — sparse-memory-2026-engram-lineage-beyond
- [[morpheus-a-morphology-aware-neural-tokenizer-and-word-embedder-for-turkish|Morpheus: A Morphology-Aware Neural Tokenizer and Word Embedder for Turkish]] (2026) — novelty-check-has-any-2026-preprint-impl
- [[ultramemv2-memory-networks-scaling-to-120b-parameters-with-superior-long|UltraMemV2: Memory Networks Scaling to 120B Parameters with Superior Long-Context Learning]] (2025) — sparse-memory-2026-engram-lineage-beyond
- [[memory-layers-at-scale|Memory Layers at Scale]] (2024) — novelty-check

## Related topics
- [[novelty-check-has-any-2026-preprint-impl]] — 4 shared nodes
- [[novelty-check]] — 2 shared nodes

[[Home]]
