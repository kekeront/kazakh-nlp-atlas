---
type: "moc"
topic: "qymyzlm-architecture-fork"
nodes: 7
papers: 5
sources: 2
uncertain_claims: 1
tags: ["moc"]
---
# Topic: qymyzlm-architecture-fork

The fork is how to give Qwen3-0.6B-Base (tied embeddings, 151,936×1024 = 155.58M = 26% of ~596M params) a Kazakh tokenizer under a ≤600M ACTIVE cap. Param math is CONFIRMED ground truth: a full swap to a ~60K Kazakh vocab shrinks the table to 61.4M and frees ~94M for Engram, while a Sherkala-style +31.5K expansion (→187.8M, ~628M total) breaks the cap, and EEVE's staged freezing is structurally incompatible with tied weights (untying costs +155.58M). Three viable paths survive: plain TIED expansion works (Yamaguchi, Gemma2-9B, up to 1.57x speedup) but costs 5.3–18.7pp of source-language knowledge; iso-size REPLACEMENT (VRCP) gains 2.2x JA efficiency at ZERO added params; and full trans-tokenization swap+CPT retains base advantage at tiny budgets, the only Turkic-tested route (Tatar Mistral-7B, 107M tokens → PPL 10.96). The decisive open question is a measurement gap: NO published swap-vs-from-scratch head-to-head exists at ≤1B, where the reinitialized table is ~26% of params vs ~2% at 8B, so the sub-1B "swap tax" is unmeasured — a publishable ablation QymyzLM can claim, with the swap cost bar (Dagan's >50B tokens) sitting 5x above the lab's ~10B-token Kazakh ceiling.

## Frontier highlights
- [[trans-tokenization-and-cross-lingual-vocabulary-transfers-language-adaptation|Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation o…]] — Only Turkic-tested swap (Tatar, 107M tok) AND flags the decision-relevant sub-1B swap-tax evidence gap
- [[huggingface-co-qwen-qwen3-0-6b-base-config-json-fetched-raw|huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-…]] — Re-derived param ground truth: 26% tied table; 60K swap frees ~94M, +31.5K expansion breaks cap
- [[efficient-and-effective-vocabulary-expansion-towards-multilingual-large|Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language…]] — EEVE 7-stage schedule structurally incompatible with tied embeddings; untying breaks the 600M cap
- [[how-can-we-effectively-expand-the-vocabulary-of-llms-with-0-01gb-of-target|How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Target Langu…]] — Tied plain expansion works (1.57x) but low-data full replacement fails; expansion costs 5–19pp source knowledge
- [[vrcp-nozaki-et-al-2nd-sumeval-workshop-2025-aclanthology|VRCP, Nozaki et al., 2nd SUMEval Workshop 2025, aclanthology.org/2025.…]] — Third path: iso-size replacement, 2.2x JA efficiency at zero added params, GPU footprint unchanged
- [[chocollama-lessons-learned-from-teaching-llamas-dutch|ChocoLlama: Lessons Learned From Teaching Llamas Dutch]] — Swap+CPT beats kept tokenizer at 32B tokens, but LoRA-CPT alone gives ~0 gain on strong multilingual base

## Papers (5)
- [[getting-the-most-out-of-your-tokenizer-for-pre-training-and-domain-adaptation|Getting the most out of your tokenizer for pre-training and domain adaptation]] (2024) — qymyzlm-architecture-fork
- [[efficient-and-effective-vocabulary-expansion-towards-multilingual-large|Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models]] (2024) — continual-pt-lowres-qlora-vs-full-cpt-re
- [[how-can-we-effectively-expand-the-vocabulary-of-llms-with-0-01gb-of-target|How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Target Language Text?]] (2024) — qymyzlm-architecture-fork
- [[trans-tokenization-and-cross-lingual-vocabulary-transfers-language-adaptation|Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation of LLMs for Low-Resou…]] (2024) — qymyzlm-architecture-fork
- [[chocollama-lessons-learned-from-teaching-llamas-dutch|ChocoLlama: Lessons Learned From Teaching Llamas Dutch]] (2024) — qymyzlm-architecture-fork

## Sources & findings (2)
- [[huggingface-co-qwen-qwen3-0-6b-base-config-json-fetched-raw|huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-…]] — Qwen3-0.6B-Base verified config (HF config.json): vocab_size 151,936, hidden 1024, 28 layers, GQA 16 Q/8 KV heads, inter…
- [[vrcp-nozaki-et-al-2nd-sumeval-workshop-2025-aclanthology|VRCP, Nozaki et al., 2nd SUMEval Workshop 2025, aclanthology.org/2025.…]] — [transferable-untested (JA/ZH, Llama-2-7B untied)] A third path the fork omitted — iso-size vocabulary REPLACEMENT (VRCP…

## Related topics
- [[continual-pt-lowres-qlora-vs-full-cpt-re]] — 2 shared nodes

[[Home]]
