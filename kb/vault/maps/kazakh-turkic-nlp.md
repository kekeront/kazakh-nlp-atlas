---
type: "moc"
topic: "kazakh-turkic-nlp"
nodes: 12
papers: 10
sources: 2
uncertain_claims: 9
tags: ["moc"]
---
# Topic: kazakh-turkic-nlp

The established fact is that every published Kazakh SOTA at any scale is an ADAPTATION of a strong base, never from-scratch: Sherkala-8B is a continual-pretrain of Llama-3.1-8B (45.3B tokens, 3:1:3 kk:(ru+tr):en, vocab +25% to 159,766, Kazakh fertility 4.73->2.04) reaching KazMMLU 41.4 chat / 51.6 base, and Qolda (Qwen3-4B) hits 60.37 zero-shot and beats its own backbone. At <=1B nothing dedicated beats general Qwen3-0.6B's ~32.8% KazMMLU; the lab's target is +3.2pp over that. The contested/refuted result is that a great tokenizer does not buy accuracy: from-scratch SozKZ-600M (dedicated 50K ByteLevel-BPE, 2-3x fertility advantage, ~9B tokens) scores only MC-QA 30.3 / Belebele 27.0, LOSING to un-adapted Qwen2.5-0.5B (31.5 / 30.0); and broad multilingual coverage actively HURTS Kazakh (Aya Expanse collapses to 15.7% by emitting Kyrgyz). Corpus supply is a hard ceiling at ~9-10B unique Kazakh tokens (HPLT 3.0 7.34B, SozKZ 9B, FineWeb-2 ~1.8B). The open question is whether architectural novelty can push a <=600M-ACTIVE model past the baseline: no non-vanilla attention (GQA/MLA/gated) has EVER been trained on Kazakh, and no memory mechanism keys on morphemes -- but Engram/mHC are validated only on MoE >=3B, and counting the memory table pushes a dense-plus-table model into the ~1B-TOTAL class where the real peers (Qwen2.5-1.5B 34.3) are stronger.

## Frontier highlights
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — Closest prior art: from-scratch SozKZ-600M (best-in-class Kazakh tokenizer) still LOSES knowledge QA to un-adapted Qwen2.5-0.5B
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resour…]] — Kazakh SOTA and ceiling reference: Llama-3.1-8B continual-PT -> KazMMLU 51.6 base / 41.4 chat; adaptation, not architecture
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge o…]] — Primary eval defining the bar: Qwen3-0.6B 32.8%, best open 55.2% (70B); shot count swings scores ~11pp
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Languag…]] — Engram conditional memory: beats iso-param/iso-FLOP MoE at 27B via O(1) n-gram lookup, but only MoE, never dense/sub-1B
- [[left-behind-cross-lingual-transfer-as-a-bridge-for-low-resource-languages-in|Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in La…]] — Refutes free cross-lingual transfer: Kazakh-Kyrgyz proximity leaks generation (Aya Expanse 15.7% Kazakh vs 82.3% English)
- [[mdpi-make-8-5-128|MDPI MAKE 8(5):128]] — Adaptation beats from-scratch: Qolda (Qwen3-4B) 60.37 zero-shot -> 76.0 with RAG, outperforms its backbone

## Papers (10)
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models]] (2026) — deepseek-tech
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[left-behind-cross-lingual-transfer-as-a-bridge-for-low-resource-languages-in|Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models]] (2026) — kazakh-turkic-nlp
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] (2026) — tokenizer-morphology
- [[tumlu-a-unified-and-native-language-understanding-benchmark-for-turkic-languages|TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages]] (2025) — sota-slm
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan]] (2025) — sota-slm
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting]] (2025) — tokenizer-morphology
- [[hplt-3-0-very-large-scale-multilingual-resources-for-llms-and-mt-mono-and-bi|HPLT 3.0: Very Large-Scale Multilingual Resources for LLMs and MT. Mono- and Bi-lingual Data, Multil…]] (2025) — kazakh-turkic-nlp
- [[mhc-manifold-constrained-hyper-connections|mHC: Manifold-Constrained Hyper-Connections]] (2025) — kazakh-turkic-nlp
- [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model|DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model]] (2024) — deepseek-tech

## Sources & findings (2)
- [[mdpi-information-17-2-128-cse-guided-jan-2026|MDPI Information 17(2):128 (CSE-guided, Jan 2026)]] — Morphology-aware tokenization is a validated lever for Kazakh. A CSE-guided (Complete Set of Endings) SentencePiece toke…
- [[mdpi-make-8-5-128|MDPI MAKE 8(5):128]] — Qolda (ISSAI, Qwen3-4B base, 4.3B params) is the strongest recent Kazakh SLM data point above 1B: zero-shot ~60.37 avg a…

## Related topics
- [[novelty-check]] — 6 shared nodes
- [[inference-tts]] — 3 shared nodes
- [[tokenizer-morphology]] — 3 shared nodes
- [[architecture-fork]] — 2 shared nodes
- [[continual-pt-lowres-qlora-vs-full-cpt-re]] — 2 shared nodes

[[Home]]
