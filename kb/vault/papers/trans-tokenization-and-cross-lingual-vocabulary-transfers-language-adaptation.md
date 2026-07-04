---
kb_id: "arxiv:2408.04303"
type: "paper"
title: "Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation of LLMs for Low-Resource NLP"
arxiv_id: "2408.04303"
doi: null
hf_repo: null
year: 2024
topics: ["qymyzlm-architecture-fork"]
claims: 2
uncertain_claims: 1
verdicts: []
aliases: ["Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation of LLMs for Low-Resource NLP", "arXiv:2408.04303", "arxiv:2408.04303"]
tags: ["paper", "topic/qymyzlm-architecture-fork"]
---
# Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation of LLMs for Low-Resource NLP

[arXiv](https://arxiv.org/abs/2408.04303)
**Topics:** [[qymyzlm-architecture-fork]]

> [!abstract]
> The development of monolingual language models for low and mid-resource languages continues to be hindered by the difficulty in sourcing high-quality training data. In this study, we present a novel cross-lingual vocabulary transfer strategy, trans-tokenization, designed to tackle this challenge and enable more efficient language adaptation. Our approach focuses on adapting a high-resource monolin …

## Claims

> [!note] CLAIM — qymyzlm-architecture-fork
> [tested-on-Turkic (Tatar, Kipchak — closest major relative of Kazakh)] Trans-tokenization (full vocab swap with embeddings initialized as translation-aligned weighted averages of source-token embeddings) preserves cross-lingual transfer at data budgets from-scratch cannot touch: Tweety-7b-dutch = Mistral-7B with fully swapped Dutch tokenizer, only 417M CPT tokens (40 GPU-h), reaches PPL 11.1 vs 21.2 (normalized) for from-scratch GPT-neo-1.3b-dutch, and beats Mistral-7B on SQuAD-NL 1-shot (25.8% vs 21.3%). For Tatar: swapped Mistral-7B trained on just 107M tokens (41M embeddings-only + 66M with top-2/bottom-2 layers unfrozen) reaches PPL 10.96, 49.34% SART word analogies, and chrF 53.7 (short-text MT with Hydra+BackFT).
>
> **Numbers:** 417M tokens: PPL 11.1 (swap-CPT 7B) vs 21.2 (from-scratch 1.3B, normalized PPL, cross-tokenizer comparability caveat); Tatar: 107M tokens -> PPL 10.96, analogies 49.34%, chrF 53.7±0.2
> **Relevance:** Strongest direct evidence that reinitializing the ENTIRE embedding table does not discard the CPT advantage — the ~440M non-embedding Qwen3 body carries the transfer, demonstrated on a language morphologically/genetically close to Kazakh. Also gives the T4-friendly unfreeze recipe (embeddings first, then top-2+bottom-2 layers).
> **Source:** Trans-Tokenization, arXiv:2408.04303 (COLM 2024), Tables 1, 2, 4, 5, 6 · **Sweep:** `slm-arch-for-kazakh`

> [!warning] UNCERTAIN — qymyzlm-architecture-fork
> [evidence gap — decision-relevant] NO published head-to-head of swap-CPT vs from-scratch exists at <=1B parameters: every quantified swap/replacement result found is 7-9B (Mistral-7B, Llama-2-7B, Llama-3-8B, Gemma2-9B); ZeTT (arXiv:2405.07883) used XLM-R (encoder) and Mistral-7B. At 0.6B the reinitialized tied table is ~26% of ALL params (vs ~2% at 8B untied), so the 7B evidence overstates how much surviving body knowledge remains — the swap tax at sub-1B is unmeasured anywhere. Combined with the KB's SozKZ result (from-scratch 600M + elite tokenizer LOSES to un-adapted Qwen2.5-0.5B on knowledge: MC-QA 30.3 vs 31.5, Belebele 27.0 vs 30.0), the fork still resolves toward swap-CPT, but the sub-1B swap-tax measurement is an open, publishable ablation QymyzLM can claim.
>
> **Numbers:** Reinit fraction: 155.58M/596M = 26.1% (Qwen3-0.6B tied) vs ~1.05B/8.03B = 13% (Llama-3-8B, untied, both matrices) vs 4.2% embedding-only share typical at 7B/32K vocab; swap evidence floor = 7B
> **Relevance:** The design-panel must treat the 60K-swap as supported-by-analogy, not proven at scale: mandate a 300-500M-token pilot (KazMMLU + PPL retention curve vs from-scratch-equivalent control) before locking the Engram budget to the freed 94M.
> **Source:** Absence verified across arXiv/ACL sweeps 2024-2026 (queries EN+RU, incl. Kazakh-local artifacts); scale facts from arXiv:2408.04303, 2412.07633, 2406.11477, 2405.07883; SozKZ arXiv:2603.20854 (KB) · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[zero-shot-tokenizer-transfer]], [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch]]

## Related
- [[zero-shot-tokenizer-transfer|Zero-Shot Tokenizer Transfer]] — Both study full tokenizer swap; ZeTT closes the gap at 7B with <1B tokens but tested only encoder/Mistral-7B, leaving sub-1B swap tax open
- [[facilitating-large-language-model-russian-adaptation-with-learned-embedding|Facilitating large language model Russian adaptation with Learned Embedding Propagation]] — Both reinit embeddings for a vocab swap; LEP learns Russian embeddings, trans-tok uses translation-aligned source averages — rival inits…

[[Home]]
