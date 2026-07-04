---
kb_id: "arxiv:2605.24869"
type: "paper"
title: "Lngram: N-gram Conditional Memory in Latent Space"
arxiv_id: "2605.24869"
doi: null
hf_repo: null
year: 2026
topics: ["novelty-check-has-any-2026-preprint-impl", "sparse-memory-2026-engram-lineage-beyond", "post-hoc-attachment-of-engram-style-cond"]
claims: 4
uncertain_claims: 1
verdicts: ["confirmed", "refuted"]
aliases: ["Lngram: N-gram Conditional Memory in Latent Space", "arXiv:2605.24869", "arxiv:2605.24869"]
tags: ["paper", "topic/novelty-check-has-any-2026-preprint-impl", "topic/sparse-memory-2026-engram-lineage-beyond", "topic/post-hoc-attachment-of-engram-style-cond"]
---
# Lngram: N-gram Conditional Memory in Latent Space

[arXiv](https://arxiv.org/abs/2605.24869)
**Topics:** [[novelty-check-has-any-2026-preprint-impl]], [[sparse-memory-2026-engram-lineage-beyond]], [[post-hoc-attachment-of-engram-style-cond]]

> [!abstract]
> Sequence modeling requires both compositional reasoning and local static knowledge retrieval, yet standard Transformers handle both through dense computation. Engram partially decouples retrieval from the backbone, but its token-based keys remain tied to text tokenization and hash compression. We propose Lngram, a latent-space conditional memory module that learns discrete symbols directly from hi …

## Claims

> [!note] CLAIM — novelty-check-has-any-2026-preprint-impl
> Lngram does NOT subsume the morpheme-keyed contribution: it learns latent binary discrete symbols from hidden states via hard-threshold binarization (b=1[z>0], d channels split into R routes of M=4 bits => K=2^M symbols per route), then does temporal n-gram lookup over these LEARNED symbols. It is purely latent/self-learned, has no linguistic/morpheme keys, and is evaluated ONLY on English NLP + vision-language/VLA — never on agglutinative or multilingual text. Its edge over Engram is modest: +0.63pp average (0.5288 vs Engram 0.5225) on a 22B MoE trained on 35B tokens; injected at layers 2 and 12 of 24, ~0.5B params reallocated, <10% activated-param overhead, decode ~6.7% slower.
>
> **Numbers:** arXiv 2605.24869, submitted 2026-05-24; M=4 bits/route; Lngram avg 0.5288 vs Engram 0.5225 (+0.63pp) vs MoE 0.5146 (+1.42pp) at 22B/35B tokens; domain-adapt Qwen3-1.7B +5.54pp BDD
> **Relevance:** Lngram competes with the MOTIVATION ('remove tokenizer-ID dependence') but not the mechanism. Reframe morpheme keys as the linguistically-grounded, interpretable, zero-training-signal alternative to Lngram's learned binarization — and note Lngram's gains are English-only and untested on the vowel-harmony/allomorphy that motivates morpheme keys.
> **Source:** arXiv 2605.24869 (Lngram: N-gram Conditional Memory in Latent Space) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — novelty-check-has-any-2026-preprint-impl
> VERDICT: Neither Lngram nor X-gram subsumes the morpheme-keyed-Engram contribution, and no 2026 preprint has implemented morpheme/suffix-level (morphologically-segmented) conditional memory. However, three forces erode the raw 'first-of-kind' framing and must be answered in-paper: (a) the 'suffix n-gram' naming collision, (b) TOBA LM already applying Engram to an agglutinative language with morpheme-flavored framing, and (c) Lngram's 'learn your own lookup units, drop tokenizer IDs' motivation directly rivaling the argument for hand-specified keys. The surviving, defensible novelty = EXPLICIT morphological-segmentation-keyed memory + vowel-harmony/allomorph-normalized keys + first Turkic/Kazakh benchmarked memory augmentation.
>
> **Numbers:** 3 competing preprints to distinguish (Lngram 2605.24869, X-gram 2604.21724, TOBA 2603.10006); morpheme-KEYED memory count in literature = 0
> **Relevance:** Directly answers the question: the crux holds, but the contribution statement should shift from 'first conditional memory for morphology' to 'first explicit morpheme-segmentation-keyed, allomorphy-aware memory, validated on Turkic', with head-to-head vs X-gram (small-scale SOTA) and an ablation vs Lngram-style learned units.
> **Source:** Synthesis of arXiv 2605.24869, 2604.21724, 2603.10006, 2601.07372, 2606.08347 · **Sweep:** `slm-architecture-2026-07`

> [!failure] REFUTED — sparse-memory-2026-engram-lineage-beyond
> [transferable-untested] Adaptation-time (not from-scratch) memory attachment has exactly ONE published datapoint, and it is positive: Lngram's domain-adaptation of Qwen3-1.7B gained +5.54pp (BDD benchmark, KB). Every other memory result in the lineage — Engram, X-gram, TN-gram, MolGram, Memory Layers, UltraMemV2, Engram-Nine — trains the memory jointly FROM SCRATCH. No paper attaches n-gram memory to a pretrained dense checkpoint during continual pretraining (QymyzLM's actual QLoRA-CPT-on-Qwen3-0.6B setting).
>
> **Numbers:** Adaptation datapoints: 1 (Lngram, +5.54pp BDD on Qwen3-1.7B); from-scratch datapoints: all others.
> **Relevance:** The design panel must treat 'Engram attached during CPT on a frozen/QLoRA Qwen3-0.6B' as an unvalidated regime with a single adjacent positive signal — a cheap secondary novelty claim ('memory grafting onto a multilingual base for a low-resource language') and a mandatory early ablation, since a fresh memory module must learn against an already-converged backbone.
> **Verdict:** REFUTED (framing) — not the only datapoint
> **Verification note:** The "exactly ONE adaptation-time datapoint / literature vacuum" framing is FALSE: Sparse Memory Finetuning (2510.15103, Meta) is a SECOND positive adaptation-time datapoint (inject facts, -11% NQ-F1 forgetting vs -71% LoRA/-89% full FT) — though on a memory-LAYER substrate, not n-gram. The narrow scope "n-gram memory onto a dense checkpoint with no prior memory" survives, but the broad vacuum claim does not.
> **Source:** arXiv:2605.24869 (KB entry, Qwen3-1.7B +5.54pp BDD); absence verified across 2606.08347, 2606.12113, 2601.16531, 2412.09764, 2508.18756 (all from-scratch) · **Sweep:** `slm-arch-for-kazakh`

> [!success] CONFIRMED — post-hoc-attachment-of-engram-style-cond
> [transferable-untested] STRONGEST POSITIVE datapoint: Lngram Table 4 attaches a randomly-initialized ~200M-param latent-keyed conditional-memory module post hoc to converged Qwen3-1.7B-Base with the backbone FROZEN, and the memory alone learns useful domain knowledge — the gate does not suppress it. Sequential recipe (memory-only first, then joint tuning) beats full fine-tuning outright. Caveats: keys are LEARNED latent symbols, not Engram's deterministic token-ID hashes; domain is intelligent-driving QA (never Turkic/multilingual); paper gives zero detail on init/gating/warmup for the attach.
>
> **Numbers:** Frozen backbone + Lngram-only training: BDD 50.59 -> 55.73 (+5.14pp), CNK 78.01 -> 79.39 (+1.38pp); full FT: BDD 56.91, CNK 79.39; sequential (Lngram epoch 1 then joint): BDD 62.45 (+11.86 over base, +5.54 over full FT), CNK 81.02 (+1.63 over full FT); ~200M Lngram params, ~16M driving samples, 3 epochs, all methods same data
> **Relevance:** Direct existence proof for the campaign's central bet: conditional memory attached to an already-converged sub-2B Qwen3 learns useful slots post hoc; the sequential schedule maps 1:1 onto the planned Engram-attach -> QLoRA-CPT pipeline for QymyzLM.
> **Verdict:** CONFIRMED (numbers) — but does NOT support the QymyzLM plan
> **Verification note:** Lngram numbers verified verbatim (Table 4: Qwen3-1.7B-Base frozen, ~200M module, BDD 50.59->55.73 = +5.54pp, sequential>full-FT). BUT decisive disanalogy: Lngram uses LEARNED-LATENT keys EXPLICITLY DESIGNED TO REPLACE Engram deterministic hash keys ("removes the dependence on tokenizer IDs") — it is a critique of the mechanism QymyzLM plans to build, not evidence for it. Also 1.7B (not 0.6B) and narrow driving-QA (not broad Kazakh). Nearest hash-mechanism evidence at ~0.9B (Memory Grafting) is NEGATIVE. The post-hoc Engram-HASH graft onto Qwen3-0.6B for broad Kazakh CPT is a RESEARCH GAMBLE unsupported by direct precedent.
> **Settling experiment:** Qwen3-0.6B-Base, freeze backbone, attach ~50-100M deterministic {2,3}-gram Engram hash table, train memory-only on one high-repetition kk domain slice (few hundred M tokens). Measure (a) memory-only loss vs frozen baseline, (b) gate-scalar hot-vs-cold distribution (does Engram-Nine credit-misassignment appear on hash keys?), (c) in-domain probe + en/ru forgetting probe. Isolates mechanism x scale x gate at ~$0.
> **Source:** arXiv:2605.24869 (Lngram, May 2026), Sec. domain adaptation, Table 4; https://arxiv.org/html/2605.24869 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[beyond-n-gram-data-aware-x-gram-extraction-for-efficient-embedding-parameter|Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling]] — Both 2026 Engram-extending n-gram memory variants at small scale; X-gram refines token-ID grams via ShortConv, Lngram moves to latent…
- [[memory-grafting-scaling-language-model-pre-training-via-offline-conditional|Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory]] — Both kill tokenizer-ID hash collisions: MG via offline exact longest-match, Lngram via learned latent discrete keys; MG cites Lngram…
- [[continual-learning-via-sparse-memory-finetuning|Continual Learning via Sparse Memory Finetuning]] — both adapt memory over a converged backbone; Lngram's frozen-backbone +5.14pp is the lineage's one post-hoc-attach datapoint
- [[adaptive-engram-memory-system-for-indonesian-language-model-generative-ai-based|Adaptive Engram Memory System for Indonesian Language Model: Generative AI Based on TOBA L…]] — TOBA (B) already applies Engram to agglutinative Indonesian with morpheme-flavored framing, eroding A's/lab's morpheme first-of-kind claim
- [[morpheus-a-morphology-aware-neural-tokenizer-and-word-embedder-for-turkish|Morpheus: A Morphology-Aware Neural Tokenizer and Word Embedder for Turkish]] — A's 'learn your own latent lookup units, drop tokenizer IDs' motivation directly rivals the hand-specified morpheme keys of B (Morpheus…

[[Home]]
