---
kb_id: "arxiv:2505.06708"
type: "paper"
title: "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free"
arxiv_id: "2505.06708"
doi: null
hf_repo: null
year: 2025
topics: ["attention-kv-sub1b-attention-kv-architec"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free", "arXiv:2505.06708", "arxiv:2505.06708"]
tags: ["paper", "topic/attention-kv-sub1b-attention-kv-architec"]
---
# Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free

[arXiv](https://arxiv.org/abs/2505.06708)
**Topics:** [[attention-kv-sub1b-attention-kv-architec]]

> [!abstract]
> Gating mechanisms have been widely utilized, from early models like LSTMs and Highway Networks to recent state space models, linear attention, and also softmax attention. Yet, existing literature rarely examines the specific effects of gating. In this work, we conduct comprehensive experiments to systematically investigate gating-augmented softmax attention variants. Specifically, we perform a com …

## Claims

> [!note] CLAIM — attention-kv-sub1b-attention-kv-architec
> [transferable-untested] Gated attention (head-specific sigmoid gate applied to the SDPA output, 'G1' position; NeurIPS 2025 oral, Qwen team) is the highest-value cheap attention upgrade for a from-scratch ≤600M model: at 1.7B dense / 400B tokens PPL 7.499→7.404, MMLU 50.21→51.15, GSM8K 27.82→28.28; at 15B MoE / 400B tokens PPL 6.026→5.761, MMLU 58.79→60.82, GSM8K 52.92→55.27. Attention sink (first-token attention share) collapses 46.7%→4.8% average (layer 21: 83%→4%); baseline diverges at LR 8.0e-3 where the gated model converges (PPL 7.325); RULER after NTK context extension: 32K 37.94→72.88, 128K 31.65→58.82. Headwise gate costs ~1.6M params and <2% wall-time. Adopted in production by Qwen3-Next. Sink/massive-activation suppression directly reduces fp16 overflow risk (fp16 max 65504) on T4.
>
> **Numbers:** 1.7B: ΔPPL -0.095, ΔMMLU +0.94; 15B MoE: ΔPPL -0.265, ΔMMLU +2.03, ΔGSM8K +2.35; sink 46.7%→4.8%; stable at LR 8e-3; RULER-128K +27.2; +1.6M params headwise, <2% latency
> **Relevance:** Drop-in one-line addition for the from-scratch stack; smallest tested scale is 1.7B so sub-600M effect size is unverified — but it is free (~0.3% params), fp16-stabilizing, and never tested on any Turkic language (clean ablation novelty).
> **Source:** arXiv:2505.06708 (ar5iv full text read) + github.com/qiuzh20/gated_attention · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — attention-kv-sub1b-attention-kv-architec
> [transferable-untested] What matters at 500M/10B-tokens vs what only pays off at scale, synthesized across all verified evidence: (a) QK-norm + SDPA sigmoid gate — stability/quality wins that are cheap and scale-independent (gate's +1-2pp measured at 1.7B+, magnitude at 500M unknown but cost ~0); (b) SWA 3:1-5:1 with window 512-1024 — pure KV/memory win, 'minimal perplexity impact' (Gemma3) and quality-selected (Mellum2), pays off at ANY scale on 16GB cards; (c) MLA — cache win with ±1pp quality noise at sub-1B (KB envelope), engineering cost real (decoupled RoPE, absorption), only worth it if long-context or large-batch eval is a goal; (d) GDN/Mamba2 hybrids — quality gains replicated at 340M-1.3B but kernel-blocked on T4 SM75; (e) MTP, NSA, 25%-attention megahybrids — evidence only at 1.7B-80B, do not spend the 10B-token budget on them.
>
> **Numbers:** scale-independent: QK-norm, SDPA gate (~0 cost), SWA (-35x KV@32K); scale-gated: MTP (≥1-3B, KB), gated-attn effect size (≥1.7B measured), hybrid ratios (≥1.3B)
> **Relevance:** Direct prioritization for the design panel under the 10B-token, T4-only budget.
> **Source:** synthesis of: arXiv:2505.06708, 2503.19786, 2605.31268, 2412.06464, 2505.21487 (KB), 2502.14837 (KB), granite-4.0-h-350m card · **Sweep:** `slm-arch-for-kazakh`

[[Home]]
