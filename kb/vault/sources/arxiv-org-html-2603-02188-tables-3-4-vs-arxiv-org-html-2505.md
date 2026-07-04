---
kb_id: "title:arxiv org html 2603 02188 tables 3 4 vs arxiv org html 2505 21487v1"
type: "source"
title: "arxiv.org/html/2603.02188 (Tables 3-4) vs arxiv.org/html/2505.21487v1"
doi: null
hf_repo: null
year: null
topics: ["gla-2-gta-arxiv-2505-21487-zadouri-strau"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:arxiv org html 2603 02188 tables 3 4 vs arxiv org html 2505 21487v1"]
tags: ["source", "topic/gla-2-gta-arxiv-2505-21487-zadouri-strau"]
---
# arxiv.org/html/2603.02188 (Tables 3-4) vs arxiv.org/html/2505.21487v1

**Topics:** [[gla-2-gta-arxiv-2505-21487-zadouri-strau]]

## Source URLs
- arxiv.org/html/2603.02188 (Tables 3-4) vs arxiv.org/html/2505.21487v1

## Findings

> [!note] CLAIM — gla-2-gta-arxiv-2505-21487-zadouri-strau
> Exactly ONE independent from-scratch reproduction of GLA-2/GLA-4/GTA exists: the MLRA paper (Liu et al., Penn State/UConn/CMU/UCLA, arXiv 2603.02188, Mar 2026, nanoGPT stack, 2.9B params, 98.3B FineWeb-Edu tokens) — and it FLIPS the ordering: MLA beats GLA-2 on both avg validation perplexity (13.727 vs 13.779 across 7 corpora) and 7-task zero-shot average (58.75 vs 58.30). This contradicts the original paper, where GLA-2 beat MLA at every scale (e.g. 876M: ppl 11.293 vs 11.363, downstream 57.5% vs 56.7%). The reproduction is also single-seed. No independent sub-1B reproduction exists at all.
>
> **Numbers:** Independent 2.9B/98.3B-tok run: MLA 13.727 ppl / 58.75% 0-shot vs GLA-2 13.779 / 58.30 vs GLA-4 13.815 / 58.19; original authors' 876M: GLA-2 11.293/57.5 vs MLA 11.363/56.7; 433M: GLA-2 12.456/55.4 vs MLA 12.561/54.9 vs GQA-4 12.922/54.5
> **Relevance:** The sign of the GLA-2-vs-MLA quality delta is not stable across labs — the ~0.05-0.1 ppl / 0.45-0.8pp gaps reverse between the two available runs, confirming these comparisons sit inside seed-level noise. 'GLA-2 actually-best at ~500M' is not supportable.
> **Source:** arxiv.org/html/2603.02188 (Tables 3-4) vs arxiv.org/html/2505.21487v1 · **Sweep:** `mla-sub1b-2026-07`

**Cited KB notes:** [[multi-head-low-rank-attention]]

## Related
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] — No independent sub-1B latent-attention replication exists; 2506.09342 is a separate MLA-at-SLM study, not a rerun

[[Home]]
