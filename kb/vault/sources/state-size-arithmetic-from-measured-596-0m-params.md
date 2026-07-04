---
kb_id: "title:state size arithmetic from measured 596 0m params kaggle disk limit from platform documentation notebook environment not re verified this session"
type: "source"
title: "State-size arithmetic from measured 596.0M params"
doi: null
hf_repo: null
year: null
topics: ["kaggle-t4x2-compute-vram-budget-for-the"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["title:state size arithmetic from measured 596 0m params kaggle disk limit from platform documentation notebook environment not re verified this session"]
tags: ["source", "topic/kaggle-t4x2-compute-vram-budget-for-the"]
---
# State-size arithmetic from measured 596.0M params

**Topics:** [[kaggle-t4x2-compute-vram-budget-for-the]]

## Source URLs
- State-size arithmetic from measured 596.0M params
- Kaggle disk limit from platform documentation/notebook environment (not re-verified this session)

## Findings

> [!warning] UNCERTAIN — kaggle-t4x2-compute-vram-budget-for-the
> [derived; transferable-untested] Checkpoint/restart overhead across 12h session boundaries is manageable but disk-bound: full resumable state = fp16 weights 1.19GB + fp32 master 2.38GB + Adam m,v 4.77GB + RNG/data cursor ≈ 8.4GB, so Kaggle's ~20GB persistent /kaggle/working holds at most 2 such checkpoints (5 with 8-bit Adam, state ~3.6GB). At >=3 restarts per 30h week and ~5-15 min per save+resume+data-reposition, overhead is ~2-5% of quota — restarts do not change the infeasibility verdict, they only shave another few percent off the 0.31-0.53B tok/week ceiling. Streaming-dataset cursor recovery (skip-to-step) must be implemented explicitly or each restart silently re-trains the head of the corpus.
>
> **Numbers:** 8.4GB full state (3.6GB w/ 8-bit Adam); ~20GB persistent disk => 2 (or 5) checkpoints; >=3 restarts/week; ~2-5% quota overhead
> **Relevance:** Defines the mandatory engineering scaffolding (checkpoint rotation + data cursor) for any multi-week Kaggle run; with 8-bit Adam the whole state fits comfortably, another argument for it.
> **Source:** State-size arithmetic from measured 596.0M params; Kaggle disk limit from platform documentation/notebook environment (not re-verified this session) · **Sweep:** `slm-arch-for-kazakh`

[[Home]]
