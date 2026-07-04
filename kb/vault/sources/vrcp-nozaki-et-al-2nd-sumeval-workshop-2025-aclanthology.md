---
kb_id: "title:vrcp nozaki et al 2nd sumeval workshop 2025 aclanthology org 2025 sumeval 2 5 pdf tables 1 4"
type: "source"
title: "VRCP, Nozaki et al., 2nd SUMEval Workshop 2025, aclanthology.org/2025.…"
doi: null
hf_repo: null
year: null
topics: ["qymyzlm-architecture-fork"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:vrcp nozaki et al 2nd sumeval workshop 2025 aclanthology org 2025 sumeval 2 5 pdf tables 1 4"]
tags: ["source", "topic/qymyzlm-architecture-fork"]
---
# VRCP, Nozaki et al., 2nd SUMEval Workshop 2025, aclanthology.org/2025.…

**Topics:** [[qymyzlm-architecture-fork]]

## Source URLs
- VRCP, Nozaki et al., 2nd SUMEval Workshop 2025, aclanthology.org/2025.sumeval-2.5.pdf (Tables 1-4)

## Findings

> [!note] CLAIM — qymyzlm-architecture-fork
> [transferable-untested (JA/ZH, Llama-2-7B untied)] A third path the fork omitted — iso-size vocabulary REPLACEMENT (VRCP): keep vocab size constant, replace low-frequency source-unique tokens with target-language tokens, preserve token IDs+embeddings for the common vocabulary (12,137 of 32K kept for JA), init new tokens as the arithmetic mean of their source-subtoken embeddings, then CPT with <5% English mixed in. Result: 2.2x JA / 1.8x ZH token-efficiency gain with ZERO added parameters and GPU footprint identical to base (52.78GB vs 54.57-57.35GB for expansion); task performance matches expansion (JA avg .672 vs .668/.658) and beats it on generation/summarization (XLSum-JA .734 vs .712 unchanged); unchanged tokenizer still highest on JA classification avg (.691).
>
> **Numbers:** JA LPT 0.851 -> 1.838 chars/token (2.16x), ZH 0.705 -> 1.257; vocab held at 32,000 (15,293 JA tokens, 12,137 common); JA avg .672 (VRCP) vs .668 (expand 16K) / .658 (expand 32K) / .691 (unchanged); XLSum-JA .737 (VRCP no-embed-replace) vs .712
> **Relevance:** Applied to Qwen3-0.6B: replace ~50-80K low-frequency CJK/English tokens inside the existing 151,936 vocab with Kazakh BPE tokens — fertility fix toward <2.0 with the tied 155.58M table unchanged (600M cap kept, but 94M NOT freed for Engram). This is the low-risk fallback if the full-60K-swap pilot shows an unacceptable swap tax; never tested on a tied-embedding model or agglutinative language.
> **Source:** VRCP, Nozaki et al., 2nd SUMEval Workshop 2025, aclanthology.org/2025.sumeval-2.5.pdf (Tables 1-4) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[a-collision-free-hot-tier-extension-for-engram-style-conditional-memory-a|A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Stud…]] — VRCP holds vocab size constant (155.58M table, zero freed) — unlike a shrinking swap it yields no headroom for Engram, a tradeoff against…

[[Home]]
