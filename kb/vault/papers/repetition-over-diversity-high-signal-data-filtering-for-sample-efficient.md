---
kb_id: "arxiv:2604.28075"
type: "paper"
title: "Repetition over Diversity: High-Signal Data Filtering for Sample-Efficient German Language Modeling"
arxiv_id: "2604.28075"
doi: null
hf_repo: null
year: 2026
topics: ["data-efficiency-10b-kazakh-10b-token-pre"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["Repetition over Diversity: High-Signal Data Filtering for Sample-Efficient German Language Modeling", "arXiv:2604.28075", "arxiv:2604.28075"]
tags: ["paper", "topic/data-efficiency-10b-kazakh-10b-token-pre"]
---
# Repetition over Diversity: High-Signal Data Filtering for Sample-Efficient German Language Modeling

[arXiv](https://arxiv.org/abs/2604.28075)
**Topics:** [[data-efficiency-10b-kazakh-10b-token-pre]]

> [!abstract]
> Recent research has shown that filtering massive English web corpora into high-quality subsets significantly improves training efficiency. However, for high-resource non-English languages like German, French, or Japanese, aggressive filtering creates a strategic dilemma: should practitioners prioritize diversity by training once on large amounts of lightly filtered web data, or prioritize quality …

## Claims

> [!note] CLAIM — data-efficiency-10b-kazakh-10b-token-pre
> Quality-filter + multi-epoch repetition beats single-pass diversity for a non-English language (German, from-scratch). From FineWeb-2-DE (496M docs), a DENSE-CORE filter = intersection of Coherence + Information-Value + Educational-Quality classifiers yielded only 5.1% (28B tokens); trained ~3.6 epochs to a 100B budget it beat the RANDOM single-pass 100B baseline by +4.89 avg (39.24 vs 34.35) at 350M, and +5.14 at 1B. Educational-Quality alone (33B, 3.0x) = 38.62.
>
> **Numbers:** 350M @100B: DenseCore 28B unique x3.6ep = 39.24 avg vs Random 34.35 (+4.89); EduQuality 38.62; yields: EduQual 6.1%/33B, DenseCore 5.1%/28B of 496M docs
> **Relevance:** transferable-untested (German is high-resource non-English, NOT Kazakh). Directly motivates building a Kazakh quality classifier + repeating a smaller high-quality core rather than dumping all ~9B raw tokens once (SozKZ's choice). Strongest 2026 evidence for the lab's data plan.
> **Source:** arXiv:2604.28075 (BOLDT / 'Repetition over Diversity'), Tables 1&3 · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — data-efficiency-10b-kazakh-10b-token-pre
> Multi-epoch repetition of a QUALITY-FILTERED core stays beneficial to ~7 epochs, extending the KB's 4-epoch rule for filtered data. BOLDT trained DENSE-CORE to a 200B budget = 7.2 epochs over the 28B subset and STILL gained +2.08 avg at 1B vs the 100B (3.6-epoch) run, with no observed saturation and no loss of instruction-tuning generalization. CRITICAL caveat: a core filtered by WEAK annotator/classifier models ('AA High') repeated 4.8x HURT — repetition only pays on genuinely high-quality data. Curriculum ordering (Phased 50/50 low->high, Sorted ascending edu-score) consistently UNDERPERFORMED a pure high-quality mix.
>
> **Numbers:** 7.2 epochs on 28B core still +2.08 avg at 1B; Muennighoff 4-epoch extended; weak-filter core @4.8x degrades; Phased/Sorted curricula < pure DenseCore
> **Relevance:** transferable-untested. Refines KB's '<=4 epochs ~= fresh tokens' rule: for a strongly-filtered Kazakh core the lab can safely repeat 4-7x, which is essential given only ~9-10B unique kk tokens. Also a design warning: do NOT do a low-quality->high-quality curriculum warmup, and use a STRONG LLM as the quality annotator.
> **Source:** arXiv:2604.28075 (BOLDT), sec 5.1-5.3, Tables 3&4 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[scaling-data-constrained-language-models|Scaling Data-Constrained Language Models]] — Both argue repeated high-signal data rivals fresh tokens; Repetition-over-Diversity extends the ≤4-epoch result
- [[textbooks-are-all-you-need|Textbooks Are All You Need]] — both filter for educational/textbook quality; 2604.28075 shows quality-filter + repetition beats single-pass diversity

[[Home]]
