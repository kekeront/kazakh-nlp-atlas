---
kb_id: "arxiv:2402.14714"
type: "paper"
title: "Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models"
arxiv_id: "2402.14714"
doi: null
hf_repo: null
year: 2024
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re", "qymyzlm-architecture-fork"]
claims: 3
uncertain_claims: 0
verdicts: []
aliases: ["Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models", "arXiv:2402.14714", "arxiv:2402.14714"]
tags: ["paper", "topic/continual-pt-lowres-qlora-vs-full-cpt-re", "topic/qymyzlm-architecture-fork"]
---
# Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models

[arXiv](https://arxiv.org/abs/2402.14714)
**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]], [[qymyzlm-architecture-fork]]

> [!abstract]
> This report introduces \texttt{EEVE-Korean-v1.0}, a Korean adaptation of large language models that exhibit remarkable capabilities across English and Korean text understanding. Building on recent highly capable but English-centric LLMs, such as SOLAR-10.7B and Phi-2, where non-English texts are inefficiently processed with English-centric tokenizers, we present an efficient and effective vocabula …

## Claims

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested] EEVE staged vocab-expansion recipe: add 8,960 Korean tokens (32,000→40,960), init INPUT embeddings as mean of constituent-subword embeddings, init OUTPUT embeddings as the FIRST subword's output embedding (so new-token logits start aligned with the old decomposition), then 7 stages of selective freezing: (1) new input embs only → (2) new output embs only → (3) both new embs → (4) ALL output embs → (5) new input + all output → (6) all layers (via QLoRA) → (7) body-only 'cool-down' (all except embeddings). Boosted Korean within ~2B tokens on SOLAR-10.7B and Phi-2 (2.8B); #1 Korean pre-trained model on Open Ko-LLM leaderboard, Jan 2024.
>
> **Numbers:** +8,960 tokens; final vocab 40,960; ~2B training tokens; corpus 3.2M docs/6.7GB; smallest tested backbone 2.8B (Phi-2)
> **Relevance:** The cheapest published vocab-expansion path within a Kaggle-scale budget (2B tokens). CAVEAT for the panel: Qwen3-0.6B has TIED embeddings, so EEVE's separate input/output staging is impossible without untying (+155.6M params) — a tied-weights variant of this recipe is untested anywhere.
> **Source:** arXiv:2402.14714 (EEVE) — stages and init verified verbatim from PDF text · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested] Token-budget envelope for measurable gains when adapting ≤1.5B-class models: ~2B tokens suffice for vocab-expansion integration (EEVE, 2.8–10.8B); <1B closes a full tokenizer-swap gap at 7B (ZeTT); ~1.2B tokens/language taught Galician/Swahili/Urdu to 7–8B bases (LayRA, KB); but 140B SEA tokens at 0.5B moved QA strongly and exams not at all (Sailor); and 20B code tokens at 7B raised HumanEval by +14.4pp absolute over base (LoRA-learns-less full-FT). No published study isolates 'minimum Kazakh tokens for KazMMLU movement at 0.6B' — the lab's ~10B-token corpus with ≤4-epoch repetition (KB: 2305.16264) supports an effective budget of ~20–40B tokens-seen.
>
> **Numbers:** 2B (vocab integration) / <1B (swap realign) / 1.2B per language (LayRA) / 140B→0 exam pts at 0.5B; 9–10B kk corpus ×4 epochs ≈ 36–40B tokens-seen ceiling
> **Relevance:** Feasibility anchor for the compute plan: the tokenizer/embedding work fits in the first 1–2B tokens; the KazMMLU-moving phase must be data-quality-driven (instruction-augmented + synthetic textbook MT à la Sherkala's 24%) inside a ≤40B tokens-seen budget.
> **Source:** synthesis of arXiv:2402.14714, 2405.07883, 2509.11414 (KB), 2404.03608, 2405.09673, 2305.16264 (KB) · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — qymyzlm-architecture-fork
> [transferable-untested (Korean, 10.7B/2.7B untied)] EEVE staged expansion is structurally incompatible with tied embeddings: its 7-stage schedule trains new INPUT embeddings only (stage 1), then new input+output (stage 3), then old OUTPUT embeddings (stage 4) — requiring independent embedding and lm_head matrices. Demonstrated only on untied SOLAR-10.7B and Phi-2 (2B tokens sufficed for Korean). On Qwen3-0.6B, enabling EEVE means untying (+155.58M params, total ~752M — breaks the cap). Ecosystem corroboration: Unsloth automatically UNTIES embed_tokens/lm_head when new tokens are added for PEFT training. No published work runs an EEVE-style staged schedule on tied weights.
>
> **Numbers:** 7 stages; stage-1 new-input-only, stage-3 new input+output, stage-4 old-output; 2B tokens for Korean proficiency; untie cost on Qwen3-0.6B = +151,936x1024 = +155.58M params
> **Relevance:** Kills the EEVE branch of the fork under the 600M cap — but finding 4 shows staging is unnecessary anyway (joint tied training works), so nothing of value is lost.
> **Source:** EEVE, arXiv:2402.14714; Unsloth untying behavior reported in arXiv:2508.15390 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[how-can-we-effectively-expand-the-vocabulary-of-llms-with-0-01gb-of-target|How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Target Language Text?]] — Both parameter-efficient vocab-expansion recipes for new languages; EEVE staged-freeze vs 0.01GB-target expansion
- [[an-empirical-comparison-of-vocabulary-expansion-and-initialization-approaches|An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language…]] — Both study vocab-expansion init; EEVE's staged freezing needs untied embeddings (breaks 0.6B cap) where the empirical study just compares…

[[Home]]
