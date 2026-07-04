---
type: "moc"
topic: "data-efficiency-10b-kazakh-10b-token-pre"
nodes: 8
papers: 7
sources: 1
uncertain_claims: 4
tags: ["moc"]
---
# Topic: data-efficiency-10b-kazakh-10b-token-pre

The frontier question is how to assemble and train on a ~9-10B-token Kazakh corpus efficiently, since raw Kazakh web is scarce: CulturaX kk ~2.80B, HPLT 2.0 dedup ~1.41B tokens (2503.10267), so SozKZ had to aggregate 18 sources to reach 9.0B (13.7M docs, 48.2% pass, MD5 dedup only). The one direct datapoint is discouraging: SozKZ-600M trained from scratch on 9B tokens for just 1 epoch (15.3:1 tok/param) scores 30.3% MC-QA, BELOW un-adapted Qwen2.5-0.5B (31.5%) — from-scratch loses on knowledge at this budget, while Sherkala's stronger 8B recipe used 45.3B tokens of which 24% of the Kazakh was synthetic English-Wiki MT. Two under-exploited efficiency levers are established off-Kazakh but untested on it: (1) quality-filter + multi-epoch repetition, where a DenseCore 28B subset repeated 7.2 epochs still gained at 1B (2604.28075), extending Muennighoff's 4-epoch data-constrained rule — but ONLY on genuinely high-quality data (weak-filter cores repeated 4.8x HURT, and curriculum ordering underperformed a pure high-quality mix); and (2) synthetic MT data, cheap for low-resource with a tiny native-LM perplexity filter (2403.13638) and scalable to 1.7T tokens (2502.13252), yet never applied to Kazakh/Turkic. The open blocker: no off-the-shelf Kazakh educational-quality classifier exists (FineWeb-C has 0 Kazakh annotations) and the English FineWeb-Edu classifier does not transfer across translation, so whether repetition + MT + native-LM filtering can push a sub-1B Kazakh model above SozKZ's ~30% floor is unresolved.

## Frontier highlights
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — The direct baseline: from-scratch 600M on 9B kk tokens, 1 epoch, 30.3% MC-QA — LOSES to un-adapted Qwen2.5-0.5B
- [[repetition-over-diversity-high-signal-data-filtering-for-sample-efficient|Repetition over Diversity: High-Signal Data Filtering for Sample-Efficient Germa…]] — Quality-filter + repetition beats diversity: 28B DenseCore x7.2 epochs still gaining; weak-filter cores HURT
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resour…]] — Proven kk recipe: 45.3B mix, 24% of Kazakh is synthetic English-Wiki MT, balanced vs English forgetting
- [[an-expanded-massive-multilingual-dataset-for-high-performance-language|An Expanded Massive Multilingual Dataset for High-Performance Language Technolog…]] — Exact kk web token budget: CulturaX 2.80B, HPLT2.0 dedup 1.41B — quantifies the scarcity
- [[pretraining-language-models-using-translationese|Pretraining Language Models Using Translationese]] — MT data nearly free for low-resource (-0.87% NLU) if filtered by a 28M/85M native-LM perplexity
- [[danielvanstrien-xyz-fineweb-c-analysis|danielvanstrien.xyz FineWeb-C analysis]] — No off-shelf Kazakh quality classifier: 0 FineWeb-C annotations; EN FineWeb-Edu filter fails across translation

## Papers (7)
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[repetition-over-diversity-high-signal-data-filtering-for-sample-efficient|Repetition over Diversity: High-Signal Data Filtering for Sample-Efficient German Language Modeling]] (2026) — data-efficiency-10b-kazakh-10b-token-pre
- [[multilingual-language-model-pretraining-using-machine-translated-data|Multilingual Language Model Pretraining using Machine-translated Data]] (2025) — data-efficiency-10b-kazakh-10b-token-pre
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting]] (2025) — tokenizer-morphology
- [[an-expanded-massive-multilingual-dataset-for-high-performance-language|An Expanded Massive Multilingual Dataset for High-Performance Language Technologies (HPLT)]] (2025) — data-efficiency-10b-kazakh-10b-token-pre
- [[fineweb2-one-pipeline-to-scale-them-all-adapting-pre-training-data-processing|FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every Language]] (2025) — data-efficiency-10b-kazakh-10b-token-pre
- [[pretraining-language-models-using-translationese|Pretraining Language Models Using Translationese]] (2024) — data-efficiency-10b-kazakh-10b-token-pre

## Sources & findings (1)
- [[danielvanstrien-xyz-fineweb-c-analysis|danielvanstrien.xyz FineWeb-C analysis]] — Kazakh is ABSENT from FineWeb-C community educational-quality annotations (91 languages covered; kaz_Cyrl not among them…

## Related topics
- [[architecture-fork]] — 2 shared nodes
- [[kazakh-turkic-nlp]] — 2 shared nodes
- [[novelty-check]] — 2 shared nodes
- [[tokenizer-morphology]] — 2 shared nodes

[[Home]]
