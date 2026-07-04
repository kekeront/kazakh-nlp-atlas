---
kb_id: "arxiv:2503.01493"
type: "paper"
title: "Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting"
arxiv_id: "2503.01493"
doi: null
hf_repo: "issai/LLama-3.1-KazLLM-1.0-8B"
year: 2025
topics: ["tokenizer-morphology", "kazakh-turkic-nlp", "training-recipes", "novelty-check", "architecture-fork", "continual-pt-lowres-qlora-vs-full-cpt-re", "data-efficiency-10b-kazakh-10b-token-pre", "win-bar-protocol-audit"]
claims: 14
uncertain_claims: 1
verdicts: []
aliases: ["Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting", "arXiv:2503.01493", "arxiv:2503.01493"]
tags: ["paper", "topic/tokenizer-morphology", "topic/kazakh-turkic-nlp", "topic/training-recipes", "topic/novelty-check", "topic/architecture-fork", "topic/continual-pt-lowres-qlora-vs-full-cpt-re", "topic/data-efficiency-10b-kazakh-10b-token-pre", "topic/win-bar-protocol-audit"]
---
# Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting

[arXiv](https://arxiv.org/abs/2503.01493)
**Topics:** [[tokenizer-morphology]], [[kazakh-turkic-nlp]], [[training-recipes]], [[novelty-check]], [[architecture-fork]], [[continual-pt-lowres-qlora-vs-full-cpt-re]], [[data-efficiency-10b-kazakh-10b-token-pre]], [[win-bar-protocol-audit]]

> [!abstract]
> Llama-3.1-Sherkala-8B-Chat, or Sherkala-Chat (8B) for short, is a state-of-the-art instruction-tuned open generative large language model (LLM) designed for Kazakh. Sherkala-Chat (8B) aims to enhance the inclusivity of LLM advancements for Kazakh speakers. Adapted from the LLaMA-3.1-8B model, Sherkala-Chat (8B) is trained on 45.3B tokens across Kazakh, English, Russian, and Turkish. With 8 billion …

## Claims

> [!note] CLAIM — tokenizer-morphology
> Sherkala-8B (Kazakh) extended Llama-3.1's 128,256 vocab to 159,766 (+25%, +31.5K tokens) by training monolingual BPE for Kazakh/Russian/Turkish and merging the most frequent non-overlapping tokens. This cut Kazakh fertility from 4.73 to 2.04 tok/word (-56.8%), Russian 2.56->2.21, Turkish 2.23->1.82. It is the strongest published Kazakh model (KazMMLU 41.4).
>
> **Numbers:** vocab 128,256->159,766 (+31,510); Kazakh fertility 4.73->2.04; Russian 2.56->2.21; Turkish 2.23->1.82; +31.5K tokens sufficed to halve Kazakh fertility
> **Relevance:** Proves ~2.0 tok/word for Kazakh is achievable with only ~10-30K Kazakh-specific tokens grafted onto a base vocab; the user's <2.0 target is realistic. Also validates vocab-expansion path if warm-starting from a strong base model.
> **Source:** arXiv:2503.01493 (Llama-3.1-Sherkala-8B-Chat) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — tokenizer-morphology
> Sherkala initialized new Kazakh/Russian/Turkish token embeddings with a WECHSEL-style semantic-similarity method: for each new token, average the embeddings of its top-5 most similar base-vocab tokens, where similarity is computed with OpenAI text-embedding-3-large. Training mix was 45.3B tokens at Kk:Ru+Tr:En = 3:1:3 (Kazakh 19.45B, English 19.45B, Russian+Turkish 6.4B).
>
> **Numbers:** top-5 averaged; 45.3B tokens; Kazakh 19.45B / English 19.45B / Ru+Tr 6.4B; ratio 3:1:3
> **Relevance:** Concrete, copyable embedding-init recipe for any new-token grafting. The 1:1 Kazakh:English balance (not Kazakh-dominant) is a notable design choice to avoid catastrophic forgetting of the base model's reasoning.
> **Source:** arXiv:2503.01493 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-turkic-nlp
> Sherkala-Chat-8B is the current Kazakh SOTA at its scale and defines the KazMMLU bar: base model 51.6, chat 41.4 (5-shot avg). Its KazMMLU baselines: Llama-3.1(-8B) 38.3, Qwen-2.5(-7B) 35.1, ISSAI Llama-3.1-KazLLM-1.0 37.0, BLOOM-7.1B 29.3. Belebele-kaz 30.6, HellaSwag-kk 55.2, PIQA-kk 65.9. It is an ADAPTATION of Llama-3.1-8B, not from-scratch.
>
> **Numbers:** 8B params; KazMMLU base 51.6 / chat 41.4; baselines 38.3/35.1/37.0/29.3; Belebele 30.6
> **Relevance:** Sets the realistic ceiling a <=600M model must 'approach': ~41 chat / ~51 base at 8B. A 600M model landing in the mid-30s would already beat all general <=1B baselines; landing near 40 would be paper-worthy.
> **Source:** arXiv 2503.01493 (Sherkala-Chat), html v2 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-turkic-nlp
> Sherkala's tokenizer recipe is directly reusable and hits the user's fertility<2.0 target: expanded Llama-3.1 vocab 128,256 -> 159,766 (+31,510 tokens, +25%), cutting Kazakh fertility from 4.73 to 2.04 tok/word (-56.8%). New embeddings initialized via WECHSEL using OpenAI text-embedding-3-large, top-k=5, applied to input AND output layers. Continued-pretrain: LR 1.5e-4, 4M-token global batch, 8192 ctx, AdamW (b1 0.9, b2 0.95, wd 0.1), grad clip 1.0.
>
> **Numbers:** vocab 128256->159766 (+31510); fertility 4.73->2.04; WECHSEL k=5; LR 1.5e-4; batch 4M; ctx 8192
> **Relevance:** Concrete, proven numbers to drop into the tokenizer+init spec. WECHSEL embedding init (not random) is the standard for new Kazakh tokens; the user's SentencePiece-Unigram-50K plan should target ~2.0 fertility, and vocab of ~50-60K is consistent with Sherkala's added-token count for Kazakh.
> **Source:** arXiv 2503.01493, extracted config tables · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-turkic-nlp
> Sherkala's 45.3B-token data mix is the proven Kazakh recipe: Kazakh 19.45B (43%) / English 19.45B (43%) / Russian+Turkish 6.4B (14%). 76% of the Kazakh corpus is real web (Wikipedia, CommonCrawl, CulturaX, news); 24% is SYNTHETIC (English Wikipedia machine-translated to Kazakh). English/Russian/Turkish from The Pile + CommonCrawl.
>
> **Numbers:** 45.3B total; kk 19.45B / en 19.45B / ru+tr 6.4B; 24% of Kazakh is synthetic MT
> **Relevance:** Confirms the winning mix is ~40% English co-training + controlled Russian/Turkish (NOT broad multilinguality), plus ~24% synthetic to fill the knowledge gap. The user's 9-10B pure-Kazakh plan should add English + a synthetic-translation slice; English co-data at this ratio is load-bearing for KazMMLU knowledge.
> **Source:** arXiv 2503.01493 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — training-recipes
> Sherkala-8B (the Kazakh SOTA at 41.4% KazMMLU) is a continual pretrain of Llama-3.1-8B on 45.3B tokens: 19.45B Kazakh + 19.45B English + 6.4B Russian+Turkish, i.e. a 3:1:3 Kazakh:(Ru+Tr):English mix explicitly chosen to avoid English catastrophic forgetting. Tokenizer extended +25% with new Kazakh subwords, new embeddings initialized as weighted averages of nearest base embeddings; LSH dedup + language-specific cleaning.
>
> **Numbers:** 45.3B tokens total; 19.45B kk + 19.45B en + 6.4B (ru+tr); 3:1:3 mix; tokenizer +25%; KazMMLU 41.4%
> **Relevance:** A proven-for-Kazakh data mix and the strongest realistic Kazakh distillation teacher. The 3:1:3 ratio is a concrete starting point; the embedding-init-by-nearest-neighbor trick applies if extending a base tokenizer instead of training Unigram-50K from scratch.
> **Source:** arXiv 2503.01493 Sherkala-Chat 8B (arxiv.org/html/2503.01493v2) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — novelty-check
> Sherkala (the KazMMLU SOTA reference at 41.4%) is a Llama-3.1-8B CONTINUED-pretraining model with 25% vocab extension — not a from-scratch architecture and 13x the user's param budget. It is a score target, not an architectural competitor.
>
> **Numbers:** Llama-3.1-8B backbone, +25% Kazakh vocab, 45.3B tokens (kk/en/ru/tr), 8192 ctx, KazMMLU 41.4%
> **Relevance:** Frames the ceiling: the user's sub-600M model 'approaching much larger models' should be measured against Sherkala-8B (41.4%) and Qwen3-0.6B-Base (32.8%). Beating Qwen3-0.6B decisively and closing part of the gap to Sherkala is the credible target.
> **Source:** arXiv:2503.01493 (Sherkala-Chat) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — architecture-fork
> Field-wide prior: every published Kazakh SOTA at any size is an adaptation of a strong base, none from-scratch. Sherkala-8B = continual pretraining of Llama-3.1-8B (45.3B tokens, 19.45B Kazakh) -> 41.4% KazMMLU; Qolda(-AVL) = Qwen3-4B / Qwen3-VL-4B adaptation -> 69.47% KazMMLU and beats its own backbone. KazByte proposes adapting Qwen2.5-7B but is a position paper ('empirical validation is ongoing', no results yet).
>
> **Numbers:** Sherkala-8B 41.4% KazMMLU (continual, Llama-3.1-8B). Qolda-AVL 69.47% KazMMLU (Qwen3-VL-4B base), outperforms backbone. KazByte: no numbers reported.
> **Relevance:** A from-scratch novel-architecture headline must beat this adaptation prior, not assume it. It also means a defensible SOTA-<=1B KazMMLU claim very likely does NOT require the novel Engram/mHC/MLA modules — adapting Qwen3-0.6B-Base is the higher-probability route to the headline number.
> **Source:** arXiv 2503.01493 (Sherkala); MDPI 10.3390/bdcc10060192 + HF issai/Qolda; arXiv 2603.27859 (KazByte, position-only) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter]]

> [!warning] UNCERTAIN — continual-pt-lowres-qlora-vs-full-cpt-re
> [tested-on-Kazakh] ISSAI KazLLM-1.0-8B (Dec 2024): Llama-3.1-8B customized primarily via instruction-tuning per its HF card ('customized by ISSAI to improve helpfulness'); NO tokenizer change (Kazakh fertility stays ~4.73); license CC BY-NC 4.0 (non-commercial). Press claims a 150B-token multilingual corpus (kk/ru/en/tr) but the card does not document CPT token counts. Independent measurement (Sherkala paper): KazMMLU 37.0 vs Sherkala-8B chat 41.4. Card's own leaderboard: kk avg 56.85, en avg 76.4, ru avg 61.4 (custom task suite, not KazMMLU).
>
> **Numbers:** 8B params; KazMMLU 37.0; CC BY-NC 4.0; 150B-token corpus claim [card-unconfirmed]
> **Relevance:** The national-flagship 8B without tokenizer surgery scores 4.4pp below Sherkala WITH tokenizer surgery — evidence that fertility/tokenizer work, not just data volume, drives Kazakh exam gains. Its NC license also leaves the open-license niche empty for QymyzLM.
> **Source:** huggingface.co/issai/LLama-3.1-KazLLM-1.0-8B (card fetched); issai.nu.edu.kz/kazllm; KazMMLU 37.0 from arXiv:2503.01493 (KB) · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — data-efficiency-10b-kazakh-10b-token-pre
> Sherkala-8B (current kk SOTA, 41.4% KazMMLU) used a 45.3B continual-PT mix of kk:en:(ru+tr) = 3:1:3 (Kazakh 19.45B / English 19.45B / Russian+Turkish 6.4B), of which 24% of the Kazakh (~4.7B) was SYNTHETIC English-Wikipedia machine-translated to Kazakh; explicitly balanced to avoid English catastrophic forgetting.
>
> **Numbers:** 45.3B: kk 19.45B (24% synthetic MT) / en 19.45B / ru+tr 6.4B; ratio 3:1:3
> **Relevance:** tested-on-Kazakh. The only proven-at-SOTA Kazakh mixing ratio and synthetic fraction. But it targets an 8B model preserving English; a Kazakh-first 600M on limited compute should tilt far more toward kk (see recommendations). Caps synthetic at ~24% of kk as a safe SOTA-validated ceiling.
> **Source:** arXiv:2503.01493 (Sherkala) [via lab KB, verified] · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — win-bar-protocol-audit
> [tested-on-Kazakh] The Sherkala ceiling numbers are ZERO-shot, not few-shot, and use a different scoring rule: 'We adopt the LM-Evaluation-Harness framework to evaluate each model in a zero-shot setting... the answer is determined by selecting the concatenated string with the highest normalized log-likelihood' (full answer-string log-likelihood normalization, not letter-logit). Table 4: Sherkala (8B, base) 51.6, Sherkala-Chat (8B) 41.4, Llama-3.1-8B 38.3, Qwen-2.5-7B 35.1, KazLLM-1.0-8B 37.0. KB CONFLICT: the existing KB node labels 41.4 as '5-shot avg' — that is wrong per the paper text; it is 0-shot. The 41.4 ceiling is therefore cross-protocol on THREE axes vs the lab number: shots (0 vs 3), scoring (normalized string log-lik vs letter-logit), and model type (chat vs base).
>
> **Numbers:** Sherkala base 51.6 / chat 41.4 (instruct-tuning -10.2pp); Llama-3.1-8B 38.3; Qwen-2.5-7B 35.1; KazLLM-1.0 37.0; all 0-shot
> **Relevance:** Any published '+Xpp vs Sherkala' claim using 41.4 without re-running Sherkala in evallab is uncomparable; also fixes a KB error that would propagate into the paper.
> **Source:** arXiv:2503.01493 (HTML v2, Section on downstream evaluation + Table 4) · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — win-bar-protocol-audit
> [tested-on-Kazakh] Sherkala's KazMMLU evaluation subset MATCHES the lab's: the paper describes KazMMLU as '9.8K high-school-level multiple-choice questions' with a test set of 9,870 examples — exactly the lab's 12-subject Kazakh-language test split (9,870 questions), not the full 23K kk+ru set. So split and subset are aligned between the 41.4/51.6 ceiling and the 32.8 baseline; only shot count, scoring rule, and base-vs-chat differ.
>
> **Numbers:** 9,870 test questions in both protocols; KazMMLU total 23,000 (kk 10,969 / ru 12,031)
> **Relevance:** Narrows the cross-protocol gap to exactly two measurable axes (shots, scoring) plus chat-vs-base — a single evallab re-run of Sherkala closes it entirely.
> **Source:** arXiv:2503.01493 (HTML v2) cross-checked against MBZUAI/KazMMLU dataset inspection in KB (9,870 kk test questions) and evallab N_TEST_QUESTIONS=9870 · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — win-bar-protocol-audit
> [tested-on-Kazakh] The 'ISSAI KazLLM 37.0' figure is NOT from a different suite: it is the Llama-3.1-KazLLM-1.0-8B row of Sherkala's own Table 4, i.e. measured under Sherkala's 0-shot normalized-log-likelihood protocol on the same 9,870-question set. It is therefore directly comparable to 41.4/51.6 but NOT to the lab's 32.8.
>
> **Numbers:** KazLLM-1.0 (8B) = 37.0, 0-shot, Sherkala protocol
> **Relevance:** Removes one alleged fourth protocol from the comparability problem; the ceiling family (51.6/41.4/38.3/37.0/35.1) is internally consistent and can be imported as one cross-protocol block.
> **Source:** arXiv:2503.01493 Table 4 · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — win-bar-protocol-audit
> [tested-on-Kazakh] Base-vs-chat direction is confirmed and large at 8B: Sherkala-8B base 51.6 vs Sherkala-Chat-8B 41.4 under identical protocol — instruction tuning costs -10.2pp on KazMMLU. Since QymyzLM is a base-style model (QLoRA-CPT on Qwen3-0.6B-Base), the honest published ceiling reference for base-to-base framing is 51.6, not 41.4; citing only 41.4 as 'ceiling' overstates proximity to SOTA by ~10pp.
>
> **Numbers:** 51.6 (base) vs 41.4 (chat), delta -10.2pp, same protocol
> **Relevance:** Changes the paper's framing: the CLAUDE.md 'ceiling reference Sherkala-8B 41.4' silently compares the lab's base model to a chat model; a reviewer will re-bracket against the 51.6 base number.
> **Source:** arXiv:2503.01493 Table 4 (both rows, same 0-shot protocol) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[pretraining-language-models-using-translationese|Pretraining Language Models Using Translationese]] — translationese's cheap low-resource MT-filtering result predicts Sherkala's 24% synthetic-MT Kazakh works at low cost
- [[qorgau-evaluating-llm-safety-in-kazakh-russian-bilingual-contexts|Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts]] — Qorgau evaluates Kazakh LLM safety (best open = KazLLM-70B 87.5%); Sherkala is the SOTA Kazakh LLM whose safety this benchmark would score
- [[an-empirical-comparison-of-vocabulary-expansion-and-initialization-approaches|An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language…]] — Sherkala's WECHSEL top-5 embedding init is one vocab-expansion initialization method empirically compared in this study
- [[huggingface-co-datasets-mbzuai-kazmmlu-dataset-inspection|huggingface.co/datasets/MBZUAI/KazMMLU (dataset inspection 2026-07-03)]] — Sherkala's 9,870-Q eval subset equals the dataset's Kazakh-language test split, aligning ceiling and baseline on subset
- [[universal-cross-tokenizer-distillation-via-approximate-likelihood-matching|Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching]] — Sherkala-8B as a cross-tokenizer teacher for MLA upcycling of a bespoke-tokenizer Kazakh SLM is the unclaimed combination this node flags

[[Home]]
