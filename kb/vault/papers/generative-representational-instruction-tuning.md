---
kb_id: "arxiv:2402.09906"
type: "paper"
title: "Generative Representational Instruction Tuning"
arxiv_id: "2402.09906"
doi: null
hf_repo: null
year: 2024
topics: ["decoder-to-embedder", "joint-generative-embedding-head-on-one-6"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["Generative Representational Instruction Tuning", "arXiv:2402.09906", "arxiv:2402.09906"]
tags: ["paper", "topic/decoder-to-embedder", "topic/joint-generative-embedding-head-on-one-6"]
---
# Generative Representational Instruction Tuning

[arXiv](https://arxiv.org/abs/2402.09906)
**Topics:** [[decoder-to-embedder]], [[joint-generative-embedding-head-on-one-6]]

> [!abstract]
> All text-based language problems can be reduced to either generation or embedding. Current models only perform well at one or the other. We introduce generative representational instruction tuning (GRIT) whereby a large language model is trained to handle both generative and embedding tasks by distinguishing between them through instructions. Compared to other open models, our resulting GritLM 7B …

## Claims

> [!note] CLAIM — decoder-to-embedder
> GRIT (GritLM-7B) proves one model CAN do both generation and embedding with no loss at 7B: joint training matched generative-only and embedding-only specialists, and unification speeds up RAG >60% on long documents via KV-cache reuse. Ablations show the failure of NOT training jointly: a generative-only 7B scores only ~41.2 on MTEB; an embedding-only model generates at random (~25 MMLU).
>
> **Numbers:** GritLM-7B: MTEB 66.8 + generative avg 55.5; RAG speedup >60%; joint training needs ~2x batch memory (interleaved gen+emb batches).
> **Relevance:** The strongest argument FOR a single shared backbone — but all evidence is at 7B, not 500M.
> **Source:** arXiv 2402.09906 (Generative Representational Instruction Tuning, ICLR 2024) · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — joint-generative-embedding-head-on-one-6
> [transferable-untested] At 7B the joint-vs-separate question is settled in favor of joint (GRIT: GritLM-7B matches embedding-only and generative-only specialists, MTEB 66.8 + generative avg 55.5, >60% RAG speedup via KV-cache reuse), and scaling 7B->8x7B trades embedding for generation (66.8->65.7 MTEB, 55.5->65.7 generative). But GRIT's own ablations exist ONLY at 7B+; no GRIT replication below 7B is published as of 2026-07, and per the KB there is still no recipe integrating contrastive objectives INTO pretraining at any scale (closest: LLM-JEPA arXiv:2509.14252, exploratory).
>
> **Numbers:** GritLM-7B: MTEB 66.8, generative avg 55.5; 8x7B: 65.7/65.7; joint training ~2x batch memory
> **Relevance:** The 7B result is the reason 'joint head' is on the table at all, but it does not license the design at 600M — Hydra's 0.8B collapse is the nearer datapoint, so the panel should treat GRIT-style joint loss at 600M as a research hypothesis, not a default.
> **Source:** arXiv:2402.09906 (GRIT) — KB node cross-checked against arXiv abstract/search 2026-07-04; KB node on LLM-JEPA · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[llm-jepa-large-language-models-meet-joint-embedding-predictive-architectures]]

## Related
- [[hydra-unifying-document-retrieval-and-generation-in-a-single-vision-language|Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model]] — Hydra's controlled 0.8B/4B ablation refutes GRIT's 'joint training lossless' — generation collapses at our scale under LoRA joint training

[[Home]]
