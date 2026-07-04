---
kb_id: "title:derived from lab measurement t4bench2 py t4bench3 py kaggle quota product feedback 361104 flops basis 6n 3 58e9 tok 33 checkpoint recompute cross check vs kb from scratch derivation"
type: "source"
title: "Derived from lab measurement (t4bench2.py/t4bench3.py) + Kaggle quota…"
doi: null
hf_repo: null
year: null
topics: ["kaggle-t4x2-compute-vram-budget-for-the"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:derived from lab measurement t4bench2 py t4bench3 py kaggle quota product feedback 361104 flops basis 6n 3 58e9 tok 33 checkpoint recompute cross check vs kb from scratch derivation"]
tags: ["source", "topic/kaggle-t4x2-compute-vram-budget-for-the"]
---
# Derived from lab measurement (t4bench2.py/t4bench3.py) + Kaggle quota…

**Topics:** [[kaggle-t4x2-compute-vram-budget-for-the]]

## Source URLs
- Derived from lab measurement (t4bench2.py/t4bench3.py) + Kaggle quota (product-feedback/361104)
- FLOPs basis 6N=3.58e9/tok (+~33% checkpoint recompute)
- cross-check vs KB from-scratch derivation

## Findings

> [!note] CLAIM — kaggle-t4x2-compute-vram-budget-for-the
> [verdict] The recommended 20-25B tokens-seen CPT does NOT fit the Kaggle quota — dead on arrival. At the measured 1.5-2.5k tok/s/GPU and ~1.9x DDP scaling, a T4x2 pair delivers ~2.9-4.9k tok/s => 0.31-0.53B tokens per 30h week => 20-25B tokens needs ~38-81 weeks of 100% quota consumption. Even a hyper-optimized pipeline at 10k tok/s pair (2x our best per-GPU number, unproven on T4) needs ~556-694 wall-hours = 19-23 weeks. Internal-consistency red flag: the KB's from-scratch estimate (256-650 T4-hrs, ~9B tokens) was already declared infeasible, yet 20-25B-token CPT costs 2-4x MORE FLOPs than that run — full-parameter CPT FLOPs do not shrink because the init is pretrained. Feasible Kaggle-only envelope: ~3.8-6.4B tokens-seen per 12-week campaign.
>
> **Numbers:** 0.31-0.53B tok/week; 20B tok = 38-65 wk (25B = 47-81 wk); best-case 10k tok/s => 556 h = 18.5 wk; feasible 12-wk budget ~3.8-6.4B tok
> **Relevance:** Kills the 20-25B-token plan as-is; the design panel must either re-scope tokens-seen to <=4-6B (which, per arXiv:2305.16264, still allows <=4 clean epochs never being the binding constraint — compute is) or secure non-Kaggle compute.
> **Source:** Derived from lab measurement (t4bench2.py/t4bench3.py) + Kaggle quota (product-feedback/361104); FLOPs basis 6N=3.58e9/tok (+~33% checkpoint recompute); cross-check vs KB from-scratch derivation · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[scaling-data-constrained-language-models|Scaling Data-Constrained Language Models]] — feasible ~3.8-6.4B-token envelope must be spent under data-constrained scaling (repeat-epoch value bounds)
- [[simple-and-scalable-strategies-to-continually-pre-train-large-language-models|Simple and Scalable Strategies to Continually Pre-train Large Language Models]] — budget bounds the CPT recipe this paper recommends; 20-25B tok-seen exceeds the Kaggle quota by ~40-80x
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] — KazByte adapts Qwen to Kazakh via byte adapter — an alternative low-compute path under the same T4 constraint
- [[github-com-dao-ailab-flash-attention-issues-2372|github.com/Dao-AILab/flash-attention/issues/2372]] — GLA kernels need H100+CUDA12.3; lab's canonical compute is Kaggle T4 (sm75) — GLA/GTA unrunnable there
- [[nvidia-com-en-us-data-center-tesla-t4-official-spec-page|nvidia.com/en-us/data-center/tesla-t4/ (official spec page, fetched 20…]] — T4=21%-of-A100 ceiling here underpins the 6N-FLOPs T4 compute-budget/token derivation in that node

[[Home]]
