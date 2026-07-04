---
type: "moc"
topic: "tokenizer-morphology"
nodes: 16
papers: 14
sources: 2
uncertain_claims: 6
tags: ["moc"]
---
# Topic: tokenizer-morphology

The load-bearing, near-consensus finding is that a better tokenizer does NOT buy knowledge accuracy for Kazakh: SozKZ-600M's dedicated 50K ByteLevel-BPE (2-3x fertility advantage, ~9B tokens) still scores 30.3% MC-QA, BELOW un-adapted Qwen2.5-0.5B's 31.5% and Llama-3.2-1B's 32.0%, and the 70-language study (2411.14198) finds fertility+MorphScore explain only R²=0.021 of the cross-lingual gap — the real drivers are the byte premium (Kazakh 1.76x, up to 5x for extreme scripts) and data quantity (Kazakh CommonCrawl 117x smaller than English). The established Kazakh recipe is Sherkala's +25% vocab extension (128,256→159,766) with WECHSEL/text-embedding-3-large init, which halves fertility 4.73→2.04 tok/word; continued-BPE-training (2512.03989) now supersedes its train-separate-and-append-merges with +9.6% bytes/token, fewer unreachable tokens, and −26% CPT time. Contested: whether morphology-aware pretokenization pays off — MorphBPE reports large morph-consistency-F1 gains (HU 0.87 vs 0.13 BPE) and faster convergence at 300M/1B, but MUTANT explicitly TESTED and REJECTED it for 22 Indic languages (latency/brittleness), keeping only regex pretok (38-40% of the gain); Unigram-LM meanwhile beats BPE on morpheme alignment for agglutinative families. Vocabulary sizing is a hard design constraint: the scaling law (γ≈0.83) predicts ~64-75K optimal vocab for a 500M non-embedding model, yet tied embeddings at that vocab consume 15-31% of a ≤600M active budget. Open question for QymyzLM: since tokenizer quality does not move knowledge accuracy, is any Kazakh-specific tokenizer investment beyond a fertility-<2.0 vocab extension worth the transformer capacity it steals — and is fertility even the right target (vs STRR, byte premium)?

## Frontier highlights
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — Closest prior art: from-scratch 600M Kazakh with best-in-class 2-3x fertility tokenizer still LOSES knowledge to un-adapted Qwen2.5-0.5B
- [[why-do-language-models-perform-worse-for-morphologically-complex-languages|Why do language models perform worse for morphologically complex languages?]] — Morphology+fertility explain only R²=0.021 of cross-lingual gap; byte premium & data quantity are the real drivers
- [[scaling-laws-with-vocabulary-larger-models-deserve-larger-vocabularies|Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies]] — Vocab scales Nv∝Nnv^0.83 → ~64-75K for 500M, but tied embeddings then eat 15-31% of a ≤600M budget
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resour…]] — Proven Kazakh recipe: +25% vocab extension cuts fertility 4.73→2.04, WECHSEL init, 45.3B-token CPT
- [[morphbpe-a-morpho-aware-tokenizer-bridging-linguistic-complexity-for-efficient|MorphBPE: A Morpho-Aware Tokenizer Bridging Linguistic Complexity for Efficient…]] — Reference morphology-aware tokenizer (morph-constrained merges) — makes a naive 'morph-aware for Kazakh' claim non-novel
- [[teaching-old-tokenizers-new-words-efficient-tokenizer-adaptation-for-pre|Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-traine…]] — Continued-BPE-training supersedes append-merges: +9.6% bytes/token, fewer dead tokens, −26% CPT time

## Papers (14)
- [[optimal-turkish-subword-strategies-at-scale-systematic-evaluation-of-data|Optimal Turkish Subword Strategies at Scale: Systematic Evaluation of Data, Vocabulary, Morphology I…]] (2026) — tokenizer-morphology
- [[verchol-grammar-first-tokenization-for-agglutinative-languages|VerChol -- Grammar-First Tokenization for Agglutinative Languages]] (2026) — sota-slm
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] (2026) — tokenizer-morphology
- [[morphbpe-a-morpho-aware-tokenizer-bridging-linguistic-complexity-for-efficient|MorphBPE: A Morpho-Aware Tokenizer Bridging Linguistic Complexity for Efficient LLM Training Across…]] (2025) — tokenizer-morphology
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting]] (2025) — tokenizer-morphology
- [[superbpe-space-travel-for-language-models|SuperBPE: Space Travel for Language Models]] (2025) — tokenizer-morphology
- [[evaluating-morphological-alignment-of-tokenizers-in-70-languages|Evaluating Morphological Alignment of Tokenizers in 70 Languages]] (2025) — tokenizer-morphology
- [[beyond-fertility-analyzing-strr-as-a-metric-for-multilingual-tokenization|Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation]] (2025) — tokenizer-morphology
- [[mutant-a-recipe-for-multilingual-tokenizer-design|MUTANT: A Recipe for Multilingual Tokenizer Design]] (2025) — tokenizer-morphology
- [[teaching-old-tokenizers-new-words-efficient-tokenizer-adaptation-for-pre|Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models]] (2025) — tokenizer-morphology
- [[zero-shot-tokenizer-transfer|Zero-Shot Tokenizer Transfer]] (2024) — tokenizer-morphology
- [[scaling-laws-with-vocabulary-larger-models-deserve-larger-vocabularies|Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies]] (2024) — tokenizer-morphology
- [[why-do-language-models-perform-worse-for-morphologically-complex-languages|Why do language models perform worse for morphologically complex languages?]] (2024) — tokenizer-morphology

## Sources & findings (2)
- [[apertium-github-io-apertium-kaz|apertium.github.io/apertium-kaz]] — Kazakh has production-grade morpheme-segmentation resources: apertium-kaz (finite-state morphological transducer + CG di…
- [[frontiers-ai-2025-frai-2025-1538165-ukrainian-tokenization|Frontiers AI 2025, frai.2025.1538165 (Ukrainian tokenization efficienc…]] — Cyrillic fertility across major tokenizers (Ukrainian Brown corpus, similar Cyrillic profile to Kazakh): Llama-3.1 1.88,…

## Related topics
- [[continual-pt-lowres-qlora-vs-full-cpt-re]] — 4 shared nodes
- [[novelty-check]] — 4 shared nodes
- [[kazakh-tokenizer-fertility-vs-byte-premi]] — 3 shared nodes
- [[kazakh-turkic-nlp]] — 3 shared nodes
- [[tokenizer-agglutinative]] — 3 shared nodes

[[Home]]
