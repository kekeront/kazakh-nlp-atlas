---
type: "moc"
topic: "continual-pt-lowres-qlora-vs-full-cpt-re"
nodes: 16
papers: 14
sources: 2
uncertain_claims: 4
tags: ["moc"]
---
# Topic: continual-pt-lowres-qlora-vs-full-cpt-re

For a sub-1B Kazakh CPT the frontier converges on full continued pretraining over LoRA/adapters: BLOOM+1 puts the adapter>full-CPT crossover at ~3B (full wins below it), and LoRA-Learns-Less shows LoRA r=256 at 20B code tokens (HumanEval 0.224) only matches full-FT at 4B (0.218) — ~5x worse data efficiency at the CPT scale that matters here. That verdict is regime-bounded, not universal: LLiMba reverses it at extreme-low-data (11.5M Sardinian tokens, rsLoRA-r256 28.5 BLEU vs full-FT 21.0), so the QLoRA-vs-full call hinges on token budget, not principle. Established supporting recipe: replay at ~25% for a strong English→new-language shift (Ibrahim 405M/10B), embedding-init choice washes out after ~500M CPT tokens, and <1B–2B tokens close a tokenizer-swap/vocab-expansion gap (ZeTT, EEVE). Two things stay genuinely open/contested: LR schedule (the three strongest recipes — re-warm+re-decay, NVIDIA no-warmup η_min-start, Sailor constant 1e-4 — openly CONFLICT and must not be averaged), and whether a 0.6B model can move exam-style KazMMLU at all — Sailor's exact-scale precedent (Qwen1.5-0.5B, ~140B SEA tokens) lifted QA strongly (TydiQA F1 +22.1) but left M3Exam FLAT (−0.05), and no study isolates the minimum Kazakh-token budget for KazMMLU movement at 0.6B. Structural constraint for the lab: EEVE's 7-stage schedule needs untied embeddings, which on tied Qwen3-0.6B-Base costs +155.58M params and breaches the ≤600M cap.

## Frontier highlights
- [[lora-learns-less-and-forgets-less|LoRA Learns Less and Forgets Less]] — Core evidence full-FT beats LoRA in the CPT regime: LoRA r256@20B tok ~ full-FT@4B; learns ~5x less
- [[sailor-open-language-models-for-south-east-asia|Sailor: Open Language Models for South-East Asia]] — Closest 0.5B precedent: 200B-token Qwen1.5-0.5B CPT lifts QA (+22.1 F1) but exams stay FLAT (M3Exam -0.05)
- [[llimba-sardinian-on-a-single-gpu-adapting-a-3b-language-model-to-a-vanishing|LLiMba: Sardinian on a Single GPU -- Adapting a 3B Language Model to a Vanishing…]] — Regime reversal: at 11.5M tokens rsLoRA (28.5 BLEU) beats full-FT (21.0) — bounds LoRA-Learns-Less
- [[reuse-don-t-retrain-a-recipe-for-continued-pretraining-of-language-models|Reuse, Don't Retrain: A Recipe for Continued Pretraining of Language Models]] — LR-schedule evidence CONFLICTS across the 3 strongest recipes — re-warm vs no-warmup vs constant; do not average
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resour…]] — Proven Kazakh CPT recipe (Llama-3.1-8B, 45.3B tok, 3:1:3 mix, KazMMLU 41.4) but 13x cap and cross-protocol
- [[efficient-and-effective-vocabulary-expansion-towards-multilingual-large|Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language…]] — EEVE 7-stage schedule needs untied embeddings — on tied Qwen3-0.6B breaks the 600M cap (+155.58M)

## Papers (14)
- [[estllm-enhancing-estonian-capabilities-in-multilingual-llms-via-continued|EstLLM: Enhancing Estonian Capabilities in Multilingual LLMs via Continued Pretraining and Post-Trai…]] (2026) — continual-pt-lowres-qlora-vs-full-cpt-re
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] (2026) — tokenizer-morphology
- [[llimba-sardinian-on-a-single-gpu-adapting-a-3b-language-model-to-a-vanishing|LLiMba: Sardinian on a Single GPU -- Adapting a 3B Language Model to a Vanishing Romance Language]] (2026) — continual-pt-lowres-qlora-vs-full-cpt-re
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting]] (2025) — tokenizer-morphology
- [[teaching-old-tokenizers-new-words-efficient-tokenizer-adaptation-for-pre|Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models]] (2025) — tokenizer-morphology
- [[efficient-and-effective-vocabulary-expansion-towards-multilingual-large|Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models]] (2024) — continual-pt-lowres-qlora-vs-full-cpt-re
- [[simple-and-scalable-strategies-to-continually-pre-train-large-language-models|Simple and Scalable Strategies to Continually Pre-train Large Language Models]] (2024) — continual-pt-lowres-qlora-vs-full-cpt-re
- [[sailor-open-language-models-for-south-east-asia|Sailor: Open Language Models for South-East Asia]] (2024) — continual-pt-lowres-qlora-vs-full-cpt-re
- [[zero-shot-tokenizer-transfer|Zero-Shot Tokenizer Transfer]] (2024) — tokenizer-morphology
- [[lora-learns-less-and-forgets-less|LoRA Learns Less and Forgets Less]] (2024) — continual-pt-lowres-qlora-vs-full-cpt-re
- [[an-empirical-comparison-of-vocabulary-expansion-and-initialization-approaches|An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language Models]] (2024) — continual-pt-lowres-qlora-vs-full-cpt-re
- [[reuse-don-t-retrain-a-recipe-for-continued-pretraining-of-language-models|Reuse, Don't Retrain: A Recipe for Continued Pretraining of Language Models]] (2024) — continual-pt-lowres-qlora-vs-full-cpt-re
- [[facilitating-large-language-model-russian-adaptation-with-learned-embedding|Facilitating large language model Russian adaptation with Learned Embedding Propagation]] (2024) — continual-pt-lowres-qlora-vs-full-cpt-re
- [[bloom-1-adding-language-support-to-bloom-for-zero-shot-prompting|BLOOM+1: Adding Language Support to BLOOM for Zero-Shot Prompting]] (2022) — continual-pt-lowres-qlora-vs-full-cpt-re

## Sources & findings (2)
- [[huggingface-co-gen2b-irbis-7b-instruct-lora-card-fetched|huggingface.co/Gen2B/Irbis-7b-Instruct_lora (card fetched)]] — [tested-on-Kazakh] Irbis-7b (Gen2B, 2024): community Kazakh adaptation; the Instruct variant is a LoRA fine-tune of thei…
- [[huggingface-co-qwen-qwen3-0-6b-base-config-json-fetched-raw|huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-…]] — Qwen3-0.6B-Base verified config (HF config.json): vocab_size 151,936, hidden 1024, 28 layers, GQA 16 Q/8 KV heads, inter…

## Related topics
- [[tokenizer-morphology]] — 4 shared nodes
- [[kazakh-turkic-nlp]] — 2 shared nodes
- [[novelty-check]] — 2 shared nodes
- [[qymyzlm-architecture-fork]] — 2 shared nodes

[[Home]]
