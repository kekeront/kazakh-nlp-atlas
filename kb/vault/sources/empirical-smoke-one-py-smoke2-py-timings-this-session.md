---
kb_id: "title:empirical smoke one py smoke2 py timings this session"
type: "source"
title: "Empirical: smoke_one.py / smoke2.py timings this session"
doi: null
hf_repo: null
year: null
topics: ["hardware-gate"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:empirical smoke one py smoke2 py timings this session"]
tags: ["source", "topic/hardware-gate"]
---
# Empirical: smoke_one.py / smoke2.py timings this session

**Topics:** [[hardware-gate]]

## Source URLs
- Empirical: smoke_one.py / smoke2.py timings this session

## Findings

> [!note] CLAIM — hardware-gate
> First-call Triton compile/autotune cost on SM75 is large and per-session on Kaggle: KDA's first fwd+bwd took 439 s (fp16) / 523 s (bf16); GDN bf16 388 s; fla-Mamba2 34-42 s. Subsequent calls are milliseconds (cache hit). On Kaggle this ~7-9 min tax recurs every session unless TRITON_CACHE_DIR is pointed at persistent storage (/kaggle/working). Flag: transferable-untested.
>
> **Numbers:** KDA first call 439 s fp16, 523 s bf16; GDN 388 s bf16; Mamba2 34/42 s; warm-cache first call 1 s (GDN fp16 rerun)
> **Relevance:** With 30 h/week Kaggle GPU quota and session-based workflow ('session = self-contained increment'), an unmanaged 8-min recompile per session on a hybrid model is a real budget line; must be in the training-recipe spec.
> **Source:** Empirical: smoke_one.py / smoke2.py timings this session · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[kaggle-product-feedback-announcement-notebooks-update-new|Kaggle product-feedback announcement   ([Notebooks update] New GPU (T4…]] — The 7-9 min per-session Triton compile tax compounds the Kaggle session/quota limits described in that announcement

[[Home]]
