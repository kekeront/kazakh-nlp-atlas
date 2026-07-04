---
kb_id: "arxiv:2603.28554"
type: "paper"
title: "Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model"
arxiv_id: "2603.28554"
doi: null
hf_repo: null
year: 2026
topics: ["decoder-to-embedder", "joint-generative-embedding-head-on-one-6"]
claims: 2
uncertain_claims: 1
verdicts: []
aliases: ["Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model", "arXiv:2603.28554", "arxiv:2603.28554"]
tags: ["paper", "topic/decoder-to-embedder", "topic/joint-generative-embedding-head-on-one-6"]
---
# Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model

[arXiv](https://arxiv.org/abs/2603.28554)
**Topics:** [[decoder-to-embedder]], [[joint-generative-embedding-head-on-one-6]]

> [!abstract]
> Visual document understanding typically requires separate retrieval and generation models, doubling memory and system complexity. We present Hydra, a dual-head approach that provides both ColBERT-style late-interaction retrieval and autoregressive generation from a single vision-language model. A single LoRA adapter, trained only for retrieval, is toggled at inference: enabling it produces multi-v …

## Claims

> [!warning] UNCERTAIN — decoder-to-embedder
> Counter-evidence at OUR scale: Hydra (2026) ran a controlled ablation of GritLM-style joint training at 0.8B and 4B and found joint training matched retrieval-only on retrieval but its generation mode COLLAPSED (in their LoRA setting). Their fix is the adapter pattern: base weights stay byte-for-byte identical for generation (426/426 tensors), a LoRA (r=32) switches the model into retrieval mode.
>
> **Numbers:** 59.1% peak-GPU-memory reduction at 0.8B (5.79GB to 2.37GB) vs running two models; generation exactly preserved.
> **Relevance:** Directly answers the paper's key question at ~500M scale: full GRIT joint training is risky below 1B; a retrieval LoRA/adapter on the frozen generative backbone gets unification benefits without gambling the generative deliverable.
> **Source:** arXiv 2603.28554 (Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model) · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — joint-generative-embedding-head-on-one-6
> [transferable-untested] The only controlled joint-vs-separate experiment near our scale says joint training breaks generation at 0.8B: Hydra (arXiv:2603.28554v3, 2026) ran GritLM-style joint retrieval+generation training at 0.8B and 4B and found it matched retrieval-only training on retrieval while its generation mode COLLAPSED (in their LoRA setting). Their fix — keep the base generative weights frozen (426/426 LM tensors byte-for-byte identical) and switch into retrieval mode via a LoRA adapter — preserves generation exactly and still halves deployment memory vs two co-resident models. Caveat: vision-language document-retrieval setting (Qwen-family VLM backbones), not text-only MTEB-style embedding; never tested on Kazakh or any LRL.
>
> **Numbers:** LoRA r=32, alpha=32; peak GPU memory at 0.8B: 5.79 GB -> 2.37 GB (-59.1%) vs two models; at 4B: 28.85 -> 10.77 GB (-62.7%); 426/426 base tensors unchanged
> **Relevance:** Directly answers the architecture fork at the closest published scale to 600M: on current evidence the safe shared-backbone design is frozen QymyzLM + retrieval-mode LoRA (~0 active-param overhead, zero KazMMLU risk, fits T4x2 fp16), not a GRIT-style joint loss.
> **Source:** arXiv:2603.28554 (Hydra, v3, fetched 2026-07-04); extends existing KB node (previously [UNVERIFIED], now verified) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[generative-representational-instruction-tuning|Generative Representational Instruction Tuning]] — Hydra's controlled 0.8B/4B ablation refutes GRIT's 'joint training lossless' — generation collapses at our scale under LoRA joint training
- [[lora-learns-less-and-forgets-less|LoRA Learns Less and Forgets Less]] — Hydra's frozen-base + r=32 LoRA retrieval mode banks on exactly the 'LoRA forgets less' property this paper quantifies

[[Home]]
