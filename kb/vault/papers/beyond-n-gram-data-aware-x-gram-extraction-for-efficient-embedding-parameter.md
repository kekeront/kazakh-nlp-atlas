---
kb_id: "arxiv:2604.21724"
type: "paper"
title: "Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling"
arxiv_id: "2604.21724"
doi: null
hf_repo: null
year: 2026
topics: ["novelty-check", "novelty-check-has-any-2026-preprint-impl"]
claims: 2
uncertain_claims: 1
verdicts: []
aliases: ["Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling", "arXiv:2604.21724", "arxiv:2604.21724"]
tags: ["paper", "topic/novelty-check", "topic/novelty-check-has-any-2026-preprint-impl"]
---
# Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling

[arXiv](https://arxiv.org/abs/2604.21724)
**Topics:** [[novelty-check]], [[novelty-check-has-any-2026-preprint-impl]]

> [!abstract]
> Large token-indexed lookup tables provide a compute-decoupled scaling path, but their practical gains are often limited by poor parameter efficiency and rapid memory growth. We attribute these limitations to Zipfian under-training of the long tail, heterogeneous demand across layers, and "slot collapse" that produces redundant embeddings. To address this, we propose X-GRAM, a frequency-aware dynam …

## Claims

> [!warning] UNCERTAIN — novelty-check
> X-gram is the single most dangerous prior-art collision: it is a conditional lookup-embedding memory tested at EXACTLY the user's scale (sub-1.2B), improving downstream accuracy by injecting frequency-aware dynamic n-gram embeddings into attention value streams AND inter-layer residuals with depth-aware gating. This is architecturally very close to 'Engram at layers {2, L/4} injecting into hidden states'.
>
> **Numbers:** 0.73B and 1.15B models; gains up to 3-4 points over strong baselines at matched budget using SMALLER tables; addresses Zipfian tail under-training and 'slot collapse'
> **Relevance:** Directly overlaps the user's Engram-placement contribution. The Kazakh paper must cite X-gram and differentiate on (a) morpheme- vs token/frequency-keyed lookup and (b) agglutinative-language target, or the placement/injection novelty evaporates.
> **Source:** arXiv:2604.21724 (Beyond N-gram: Data-Aware X-gram Extraction for Efficient Embedding Parameter Scaling) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — novelty-check-has-any-2026-preprint-impl
> X-gram does NOT subsume morpheme keys either — its keys are pure token IDs (Qwen3-0.6B vocab, 151,936); the novelty is refining retrieved 1-gram vectors into variable-length local features via multi-scale depthwise SwiGLU ShortConv (kernels {3,5,7} inter-layer, {3,5} attention-value), not any linguistic unit. BUT it is the strongest SMALL-scale n-gram-memory result and directly overlaps the ≤600M target: +4.4pt over vanilla backbone (48.5 vs 44.7 avg) and +3.2 over Engram (47.2) at 0.73B; up to 49.5 at 4x config; 50.8 at 1.15B (+2.3 over Engram); ~1.00-1.02x FLOP overhead. No morphology/multilingual/Turkic evaluation.
>
> **Numbers:** arXiv 2604.21724; 0.73B: X-gram 48.5 vs baseline 44.7 (+4.4), Engram 47.2 (+3.2), MoRT 45.8, Retoken 45.0; 1.15B: 50.8 vs baseline 47.4; val PPL 17.702 vs 18.420 w/o ShortConv
> **Relevance:** X-gram is a mandatory small-scale baseline to beat/cite; its +4.4/+3.2 margins at 0.73-1.15B are the number your Kazakh morpheme-keyed variant will be measured against. It threatens the 'better n-gram features' pitch, not the morpheme claim.
> **Source:** arXiv 2604.21724 (Beyond N-gram: Data-Aware X-gram Extraction for Efficient Embedding Parameter Scaling); code github.com/Longyichen/X-gram · **Sweep:** `slm-architecture-2026-07`

## Related
- [[lngram-n-gram-conditional-memory-in-latent-space|Lngram: N-gram Conditional Memory in Latent Space]] — Both 2026 Engram-extending n-gram memory variants at small scale; X-gram refines token-ID grams via ShortConv, Lngram moves to latent…
- [[memory-grafting-scaling-language-model-pre-training-via-offline-conditional|Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory]] — Both Engram-lineage fixes to n-gram memory; X-gram uses data-aware extraction vs MG's frozen donor hidden-states

[[Home]]
