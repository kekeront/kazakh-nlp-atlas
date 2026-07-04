---
type: "moc"
topic: "novelty-check-has-any-2026-preprint-impl"
nodes: 6
papers: 6
sources: 0
uncertain_claims: 8
tags: ["moc"]
---
# Topic: novelty-check-has-any-2026-preprint-impl

CONFIRMED across the whole 2026 Engram lineage: no preprint keys conditional memory by morphological units — a morpheme-segmented (stem+suffix) lookup memory count in the literature is 0. The load-bearing finding is a terminology trap: "suffix n-gram" in Engram (2601.07372), Memory Grafting (2605.20948), X-gram (2604.21724) and Tensorizing Engram (2606.08347) always means trailing TOKEN-ID tuples of the context, never linguistic suffixes. The three genuine erosions of "first-of-kind" are (a) that naming collision, (b) TOBA LM (2603.10006), which applies UNMODIFIED Engram to a 2,843-unit syllable vocab and post-hoc interprets the 2/3-gram pathways as "morpheme structures" without any segmenter, and (c) Lngram (2605.24869), whose "learn your own latent lookup symbols, drop tokenizer IDs" motivation directly rivals hand-specified morpheme keys (+0.63pp over Engram at 22B). Morpheme-aware tokenizers for Turkic DO exist and are recent — Morpheus (2606.18717, Turkish, MorphScore F1 0.61), MorphBPE, VerChol, the Kazakh CSE-guided segmenter — so morpheme keys are feasible to source, but none feeds a conditional-memory table. The surviving defensible novelty = explicit morphological-segmentation-keyed memory with vowel-harmony/allomorph-normalized keys, and the first Turkic/Kazakh-benchmarked memory augmentation; the open question is whether keyed morphemes beat Lngram's learned latent units and whether any of the sub-1B token-ID results transfer to a natural high-fertility language.

## Frontier highlights
- [[lngram-n-gram-conditional-memory-in-latent-space|Lngram: N-gram Conditional Memory in Latent Space]] — VERDICT node: neither Lngram nor X-gram subsumes morpheme keys; names the 3 competing preprints to distinguish
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Languag…]] — The base component: confirms 'suffix n-gram' = token-ID tuples, not morphology — the reviewer landmine
- [[beyond-n-gram-data-aware-x-gram-extraction-for-efficient-embedding-parameter|Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Sc…]] — Most dangerous sub-1B collision: token-ID n-gram memory at 0.73/1.15B beating Engram +3.2pt at matched budget
- [[adaptive-engram-memory-system-for-indonesian-language-model-generative-ai-based|Adaptive Engram Memory System for Indonesian Language Model: Generative AI Based…]] — TOBA LM: only dense+Engram+agglutinative artifact, 'morpheme-flavored' framing but no segmenter
- [[morpheus-a-morphology-aware-neural-tokenizer-and-word-embedder-for-turkish|Morpheus: A Morphology-Aware Neural Tokenizer and Word Embedder for Turkish]] — Morpheus proves morpheme-aware Turkic tokenizers exist (F1 0.61) yet none feeds a memory table
- [[tensorizing-engram-sharing-latents-across-n-gram-embeddings-is-beneficial-in|Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LL…]] — Field moves monthly; first controlled micro-scale dense+Engram datapoints, none Turkic

## Papers (6)
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models]] (2026) — deepseek-tech
- [[adaptive-engram-memory-system-for-indonesian-language-model-generative-ai-based|Adaptive Engram Memory System for Indonesian Language Model: Generative AI Based on TOBA LM for Bata…]] (2026) — does-the-engram-conditional-memory-modul
- [[beyond-n-gram-data-aware-x-gram-extraction-for-efficient-embedding-parameter|Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling]] (2026) — novelty-check
- [[lngram-n-gram-conditional-memory-in-latent-space|Lngram: N-gram Conditional Memory in Latent Space]] (2026) — novelty-check-has-any-2026-preprint-impl
- [[tensorizing-engram-sharing-latents-across-n-gram-embeddings-is-beneficial-in|Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs]] (2026) — novelty-check
- [[morpheus-a-morphology-aware-neural-tokenizer-and-word-embedder-for-turkish|Morpheus: A Morphology-Aware Neural Tokenizer and Word Embedder for Turkish]] (2026) — novelty-check-has-any-2026-preprint-impl

## Related topics
- [[sparse-memory-2026-engram-lineage-beyond]] — 4 shared nodes
- [[novelty-check]] — 3 shared nodes
- [[does-the-engram-conditional-memory-modul]] — 2 shared nodes
- [[post-hoc-attachment-of-engram-style-cond]] — 2 shared nodes

[[Home]]
