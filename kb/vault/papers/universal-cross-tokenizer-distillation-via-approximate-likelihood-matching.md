---
kb_id: "arxiv:2503.20083"
type: "paper"
title: "Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching"
arxiv_id: "2503.20083"
doi: null
hf_repo: null
year: 2025
topics: ["mla-upcycling-bespoke-tokenizer"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching", "arXiv:2503.20083", "arxiv:2503.20083"]
tags: ["paper", "topic/mla-upcycling-bespoke-tokenizer"]
---
# Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching

[arXiv](https://arxiv.org/abs/2503.20083)
**Topics:** [[mla-upcycling-bespoke-tokenizer]]

> [!abstract]
> Distillation has shown remarkable success in transferring knowledge from a Large Language Model (LLM) teacher to a student LLM. However, current distillation methods require similar tokenizers between the teacher and the student, restricting their applicability to only a small subset of teacher-student pairs. In this work, we develop a principled cross-tokenizer distillation method to solve this c …

## Claims

> [!note] CLAIM — mla-upcycling-bespoke-tokenizer
> No published work combines cross-tokenizer distillation with MLA upcycling. Cross-tokenizer KD is now its own maturing subfield — ALM/Approximate Likelihood Matching (arXiv:2503.20083), byte-level-interface distillation BLD (arXiv:2604.07466), BPE-recursive likelihood scoring (arXiv:2512.14954), on-policy cross-family distillation (arXiv:2606.09456) — but multiple targeted searches (English formulations, MLA/GQA2MLA/upcycling x cross-tokenizer/vocabulary) return zero papers applying any of these to attention-architecture conversion. Sherkala-8B-as-teacher for MLA upcycling of a bespoke-tokenizer Kazakh SLM would be an unclaimed combination.
>
> **Numbers:** 0 hits for the intersection; 4+ active cross-tokenizer KD methods exist independently
> **Relevance:** The lab cannot cite any precedent that cross-tokenizer KD rescues deep MLA compression — treating it as a working assumption would be unfounded; treating it as a paper contribution is open novelty space.
> **Source:** Absence result across arXiv/OpenReview searches 2026-07-03; cross-tokenizer KD primaries: arXiv:2503.20083, 2604.07466, 2512.14954, 2606.09456 · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[zero-shot-tokenizer-transfer|Zero-Shot Tokenizer Transfer]] — Both cross-tokenizer transfer; ALM distillation is an alternative to ZeTT's hypernetwork for swapping vocab
- [[how-can-we-effectively-expand-the-vocabulary-of-llms-with-0-01gb-of-target|How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Target Language Text?]] — Yamaguchi finds low-data full replacement catastrophically fails; ALM cross-tokenizer distillation offers a training-signal route to…
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Settin…]] — Sherkala-8B as a cross-tokenizer teacher for MLA upcycling of a bespoke-tokenizer Kazakh SLM is the unclaimed combination this node flags
- [[training-free-tokenizer-transplantation-via-orthogonal-matching-pursuit|Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit]] — Both attack the cross-tokenizer barrier; training-free tokenizer transplantation is an alternative to ALM's likelihood matching for…
- [[strong-teacher-not-needed-on-distillation-in-llm-pretraining|Strong Teacher Not Needed? On Distillation in LLM Pretraining]] — Both on KD; cross-tokenizer distillation enables teacher/student across vocabularies, complementing the weak-teacher-suffices finding

[[Home]]
