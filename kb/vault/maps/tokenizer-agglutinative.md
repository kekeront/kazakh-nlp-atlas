---
type: "moc"
topic: "tokenizer-agglutinative"
nodes: 11
papers: 10
sources: 1
uncertain_claims: 2
tags: ["moc"]
---
# Topic: tokenizer-agglutinative

The frontier for tokenizing agglutinative Kazakh converges on a few CONFIRMED points and one live dispute. Algorithm choice dominates: Unigram beats BPE by 8-13 points on Telugu and gives lower bits-per-byte across 6 languages (arxiv:2508.08424, arxiv:2606.27019), and explicit morphological pre-segmentation helps BPE but NOT Unigram — so a Unigram+Morfessor hybrid likely buys nothing. Vocabulary is systematically under-sized: the γ≈0.83 scaling law puts a ~500M non-embedding model's optimum at ~64-75K tokens (arxiv:2407.13623), but under a hard 500M param cap tied embeddings at 200K would eat >60% of capacity, and the measured problem is concrete — Qwen3-0.6B's own tokenizer explodes real Kazakh prose to ~5.3 tok/word via byte fallback (own measurement), worse than Llama-3.1's 4.73, and the Tokenizer Tax study shows Cyrillic fragmentation is driven by Cyrillic-specific merge share, not raw vocab size (arxiv:2605.24718). The open dispute is tokenizer-free/byte-level: BLT says large-patch byte models start BELOW BPE at 1B and only cross over at larger scale (arxiv:2412.09871), while H-Net++ claims dynamic chunking already beats BPE on morph-rich Persian at 252M/1.4B-tokens (arxiv:2508.05628) — making a byte angle for Kazakh non-novel but contested at the exact sub-1B scale QymyzLM lives in. SuperBPE's superword gains are real but demonstrated only at 8B/200K vocab, and MUTANT's Indic port got just +1.5% downstream while rejecting morphology-aware pretokenization for latency/brittleness — a caution against over-engineering.

## Frontier highlights
- [[scaling-laws-with-vocabulary-larger-models-deserve-larger-vocabularies|Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies]] — γ≈0.83 vocab scaling law: ~500M non-embed optimum is 64-75K tokens; sets the QymyzLM vocab budget
- [[rethinking-tokenization-for-rich-morphology-the-dominance-of-unigram-over-bpe|Rethinking Tokenization for Rich Morphology: The Dominance of Unigram over BPE a…]] — Unigram beats BPE 8-13pts on agglutinative Telugu; algorithm dominates, morph pre-seg helps BPE not Unigram
- [[byte-latent-transformer-patches-scale-better-than-tokens|Byte Latent Transformer: Patches Scale Better Than Tokens]] — BLT: byte/large-patch models start BELOW BPE at 1B — byte-only is not competitive at QymyzLM scale
- [[h-net-hierarchical-dynamic-chunking-for-tokenizer-free-language-modelling-in|H-Net++: Hierarchical Dynamic Chunking for Tokenizer-Free Language Modelling in…]] — H-Net++ contests BLT: tokenizer-free dynamic chunking beats BPE on morph-rich Persian at 252M
- [[own-measurement-transformers-5-5-2-autotokenizer-qwen-qwen3|Own measurement, transformers 5.5.2, AutoTokenizer Qwen/Qwen3-0.6B-Bas…]] — Qwen3-0.6B tokenizer hits ~5.3 tok/word on Kazakh Cyrillic via byte fallback — the concrete backbone problem
- [[mutant-a-recipe-for-multilingual-tokenizer-design|MUTANT: A Recipe for Multilingual Tokenizer Design]] — MUTANT ports SuperBPE to 22 Indic langs: only +1.5% downstream, and REJECTED morphology-aware pretok

## Papers (10)
- [[the-tokenizer-tax-across-25-european-languages-domain-invariance-cross-lingual|The Tokenizer Tax Across 25 European Languages: Domain Invariance, Cross-Lingual Few-Shot Effects, a…]] (2026) — tokenizer-agglutinative
- [[quechuatok-morphological-boundary-accuracy-as-a-necessary-metric-for-tokenizer|QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation in Agglut…]] (2026) — kazakh-morphological-segmentation-qualit
- [[mingram-a-minimalist-unigram-tokenizer-with-high-compression-and-competitive|MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive Morphological Alignmen…]] (2026) — tokenizer-agglutinative
- [[superbpe-space-travel-for-language-models|SuperBPE: Space Travel for Language Models]] (2025) — tokenizer-morphology
- [[h-net-hierarchical-dynamic-chunking-for-tokenizer-free-language-modelling-in|H-Net++: Hierarchical Dynamic Chunking for Tokenizer-Free Language Modelling in Morphologically-Rich…]] (2025) — novelty-check
- [[rethinking-tokenization-for-rich-morphology-the-dominance-of-unigram-over-bpe|Rethinking Tokenization for Rich Morphology: The Dominance of Unigram over BPE and Morphological Ali…]] (2025) — novelty-check
- [[mutant-a-recipe-for-multilingual-tokenizer-design|MUTANT: A Recipe for Multilingual Tokenizer Design]] (2025) — tokenizer-morphology
- [[scaling-laws-with-vocabulary-larger-models-deserve-larger-vocabularies|Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies]] (2024) — tokenizer-morphology
- [[byte-latent-transformer-patches-scale-better-than-tokens|Byte Latent Transformer: Patches Scale Better Than Tokens]] (2024) — tokenizer-agglutinative
- [[sentencepiece-a-simple-and-language-independent-subword-tokenizer-and|SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text P…]] (2018) — tokenizer-agglutinative

## Sources & findings (1)
- [[own-measurement-transformers-5-5-2-autotokenizer-qwen-qwen3|Own measurement, transformers 5.5.2, AutoTokenizer Qwen/Qwen3-0.6B-Bas…]] — Qwen3-0.6B-Base's own tokenizer (the planned CPT backbone) tokenizes real Kazakh Cyrillic prose at fertility ~5.3 tok/wo…

## Related topics
- [[tokenizer-morphology]] — 3 shared nodes
- [[novelty-check]] — 2 shared nodes

[[Home]]
