---
kb_id: "arxiv:2409.05152"
type: "paper"
title: "OneGen: Efficient One-Pass Unified Generation and Retrieval for LLMs"
arxiv_id: "2409.05152"
doi: null
hf_repo: null
year: 2024
topics: ["joint-generative-embedding-head-on-one-6"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["OneGen: Efficient One-Pass Unified Generation and Retrieval for LLMs", "arXiv:2409.05152", "arxiv:2409.05152"]
tags: ["paper", "topic/joint-generative-embedding-head-on-one-6"]
---
# OneGen: Efficient One-Pass Unified Generation and Retrieval for LLMs

[arXiv](https://arxiv.org/abs/2409.05152)
**Topics:** [[joint-generative-embedding-head-on-one-6]]

> [!abstract]
> Despite the recent advancements in Large Language Models (LLMs), which have significantly enhanced the generative capabilities for various NLP tasks, LLMs still face limitations in directly handling retrieval tasks. However, many practical applications demand the seamless integration of both retrieval and generation. This paper introduces a novel and efficient One-pass Generation and retrieval fra …

## Claims

> [!note] CLAIM — joint-generative-embedding-head-on-one-6
> [transferable-untested] The positive joint-training evidence does NOT extend below 1.5B: OneGen (arXiv:2409.05152) is the smallest published model where unified generation+retrieval did not impair generation — smallest backbone Qwen2-1.5B. On multi-hop QA at 1.5B, joint self-retrieval matched or beat the Contriever pipeline (2WIKI EM 68.32 -> 73.84, F1 72.66 -> 77.44; HotpotQA EM 48.55 -> 48.75) and matched pipeline retrieval Recall@1 (72.70 vs 72.41). Generative-impairment control (Llama2-7B, Mention Detection avg F1 across 7 datasets): SFT-only 71.1 vs OneGen 71.5 — no degradation. Its retrieval is special-token contextual embedding, not a standalone MTEB-grade dense embedder.
>
> **Numbers:** Qwen2-1.5B 2WIKI EM 68.32->73.84, F1 72.66->77.44; MD avg F1 71.1 (SFT) vs 71.5 (OneGen); trained on 60K instances (1% of baselines' data)
> **Relevance:** Combined with Hydra, brackets the open gap exactly around our budget: joint works at >=1.5B, collapses (in one LoRA setting) at 0.8B, and NO datapoint exists at <=600M — a genuine, publishable experiment slot for QymyzLM, but too risky to be the market embedding vehicle.
> **Source:** arXiv:2409.05152 (OneGen, EMNLP 2024 Findings; PDF Tables 3, 7 read 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — joint-generative-embedding-head-on-one-6
> [transferable-untested] If joint training is attempted, the contrastive loss choice materially protects generation: OneGen's ablation found hyperparameter-free pairwise BPR consistently beats InfoNCE, which the authors attribute to InfoNCE's restrictiveness 'potentially limiting the LLM's generative capabilities'; BPR also works with gradient accumulation (no GradCache large-batch requirement) — critical on T4x2 16GB fp16 where GRIT-style interleaved batches need ~2x batch memory (per existing KB GRIT node).
>
> **Numbers:** avg F1, BPR vs InfoNCE: Entity Linking 64.0 vs 61.8; Entity Disambiguation 86.5 vs 84.5; Mention Detection 71.5 vs 70.7
> **Relevance:** Concrete recipe knob for the design panel: InfoNCE+GradCache batch-512 (mE5/Less-is-More recipe) is fine for a SEPARATE encoder fine-tune, but for any joint experiment on Kaggle T4s BPR is both cheaper and safer for the generative pillar.
> **Source:** arXiv:2409.05152 Table 4 + Sec 3.2; KB node on GRIT (arXiv:2402.09906) · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[generative-representational-instruction-tuning]]

## Related
- [[nv-embed-improved-techniques-for-training-llms-as-generalist-embedding-models|NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models]] — Both turn a decoder LLM into a retriever; NV-Embed drops the causal mask for pure embedding, OneGen keeps it for joint gen+retrieval via…

[[Home]]
