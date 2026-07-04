---
kb_id: "title:empirical smoke2 on local rtx 2070 sm75 fla 0 5 1 from pypi github com fla org flash linear attention"
type: "source"
title: "Empirical, this session: smoke2.py on local RTX 2070 (SM75)"
doi: null
hf_repo: null
year: null
topics: ["hardware-gate"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:empirical smoke2 on local rtx 2070 sm75 fla 0 5 1 from pypi github com fla org flash linear attention"]
tags: ["source", "topic/hardware-gate"]
---
# Empirical, this session: smoke2.py on local RTX 2070 (SM75)

**Topics:** [[hardware-gate]]

## Source URLs
- Empirical, this session: smoke2.py on local RTX 2070 (SM75)
- fla 0.5.1 from PyPI (github.com/fla-org/flash-linear-attention)

## Findings

> [!note] CLAIM — hardware-gate
> GATE OPEN: all three kernel families RUN on SM75 in fp16 with finite outputs and gradients. We executed the actual ~30-min smoke test on an RTX 2070 laptop GPU (compute capability (7,5) — identical SM75 codegen target as Kaggle T4, same 64KB shared-memory/SM limit, no bf16 tensor cores) with torch 2.11.0+cu130, triton 3.6.0, flash-linear-attention (fla) 0.5.1: GatedDeltaNet PASS, KimiDeltaAttention (KDA) PASS, fla's Triton Mamba2 PASS, all fwd+bwd, torch.isfinite(out/grad)=True. Flag: transferable-untested (language-agnostic hardware gate; never before run for this lab).
>
> **Numbers:** fp16 fwd+bwd, B=2, T=1024, d=768, 6 heads: KDA 14.2 ms (144,270 tok/s/layer); GatedDeltaNet 144.3 ms (14,196 tok/s/layer); fla-Mamba2 (12 heads, head_dim 128) 245.6 ms (8,338 tok/s/layer); torch SDPA baseline 5.2 ms (397,144 tok/s/layer)
> **Relevance:** Un-blocks the linear/SSM hybrid branch (GDN-H1-style, Falcon-H1-style) and Muon for the design panel: nothing hard-fails on Kaggle T4-class hardware. QLoRA-CPT v1 and from-scratch v2 menus can both legally include these components.
> **Source:** Empirical, this session: smoke2.py on local RTX 2070 (SM75); fla 0.5.1 from PyPI (github.com/fla-org/flash-linear-attention) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[an-empirical-study-of-mamba-based-language-models|An Empirical Study of Mamba-based Language Models]] — fla-Triton Mamba2 runs fwd+bwd on SM75; adds a hardware-gate datapoint to this paper's Mamba LM empirics
- [[gated-delta-networks-improving-mamba2-with-delta-rule|Gated Delta Networks: Improving Mamba2 with Delta Rule]] — GatedDeltaNet from this paper PASSES on SM75 but at 14K tok/s/layer (28-47x SDPA) via fla-0.5.1 fallback configs

[[Home]]
