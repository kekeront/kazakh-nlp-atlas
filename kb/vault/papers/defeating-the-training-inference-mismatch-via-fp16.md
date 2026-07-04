---
kb_id: "arxiv:2510.26788"
type: "paper"
title: "Defeating the Training-Inference Mismatch via FP16"
arxiv_id: "2510.26788"
doi: null
hf_repo: null
year: 2025
topics: ["kaggle-t4x2-compute-vram-budget-for-the"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["Defeating the Training-Inference Mismatch via FP16", "arXiv:2510.26788", "arxiv:2510.26788"]
tags: ["paper", "topic/kaggle-t4x2-compute-vram-budget-for-the"]
---
# Defeating the Training-Inference Mismatch via FP16

[arXiv](https://arxiv.org/abs/2510.26788)
**Topics:** [[kaggle-t4x2-compute-vram-budget-for-the]]

> [!abstract]
> Reinforcement learning (RL) fine-tuning of large language models (LLMs) often suffers from instability due to the numerical mismatch between the training and inference policies. While prior work has attempted to mitigate this issue through algorithmic corrections or engineering alignments, we show that its root cause lies in the floating point precision itself. The widely adopted BF16, despite its …

## Claims

> [!warning] UNCERTAIN — kaggle-t4x2-compute-vram-budget-for-the
> [transferable-untested; stability risk] fp16 CPT of the bf16-native Qwen3-0.6B checkpoint at lr~1e-4 has NO published success or failure report on any hardware — it must be pilot-tested. Documented adjacent evidence, both directions: (a) Qwen2-VL fp16 inference produced inf/NaN probability tensors and gibberish (huggingface/transformers#33294, fixed by PR #33312), and Qwen3-8B LoRA fine-tuning on Kaggle GPUs hit NaN at steps 1-211 with fp16-related settings at lr=1e-3, issue unresolved (unslothai/unsloth#3155); (b) arXiv:2510.26788 ('Defeating the Training-Inference Mismatch via FP16', 2025) argues BF16's rounding error — not FP16's range — was the real instability source in RL fine-tuning and reports more stable optimization after switching TO fp16 with standard framework support. Also measured: torch GradScaler refuses pure-fp16 parameters ('Attempting to unscale FP16 gradients') — the recipe must use AMP autocast with fp32 master weights (adds 2.38GB, included in VRAM budget above) or manual static loss scaling.
>
> **Numbers:** fp16 max 65,504; NaN at steps 1/69/211 (unsloth#3155, lr 1e-3); fp32 master +2.38GB for 596M params; our 12-step fp16 pilot at 4K ctx: finite losses, no overflow (too short to be conclusive)
> **Relevance:** The entire Kaggle plan rides on fp16 (T4 has no bf16); a 1-2h on-platform pilot (few hundred steps, lr 1e-4, dynamic loss scaling, overflow-skip counting) is a mandatory gate before committing weeks of quota.
> **Source:** https://github.com/huggingface/transformers/issues/33294; https://github.com/unslothai/unsloth/issues/3155; arXiv:2510.26788; lab GradScaler reproduction · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[small-scale-proxies-for-large-scale-transformer-training-instabilities|Small-scale proxies for large-scale Transformer training instabilities]] — Both target fp16 numerical stability; relevant to the T4's forced fp16 regime this claim flags as never ablated at sub-1B
- [[peri-ln-revisiting-normalization-layer-in-the-transformer-architecture|Peri-LN: Revisiting Normalization Layer in the Transformer Architecture]] — both target fp16 numerical stability; Peri-LN keeps hidden states below FP16 max architecturally
- [[muon-is-scalable-for-llm-training|Muon is Scalable for LLM Training]] — Muon's fp16 Newton-Schulz is unvalidated on T4; this node argues fp16 training is viable, testing that gap
- [[huggingface-co-qwen-qwen3-0-6b-base-config-json-fetched-raw|huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-…]] — the untested fp16-CPT stability claim is precisely about this bf16-native checkpoint the lab plans to adapt
- [[empirical-muon-ns-py-and-smoke2-py-this-session-torch-2-11|Empirical: muon_ns.py and smoke2.py this session (torch 2.11.0+cu130,…]] — Converging fp16>bf16 prescription: node's reason is SM75 tensor-core absence, this paper's is defeating train-inference mismatch

[[Home]]
