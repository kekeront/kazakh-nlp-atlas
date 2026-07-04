---
kb_id: "arxiv:2603.20854"
type: "paper"
title: "SozKZ: Training Efficient Small Language Models for Kazakh from Scratch"
arxiv_id: "2603.20854"
doi: null
hf_repo: null
year: 2026
topics: ["tokenizer-morphology", "kazakh-turkic-nlp", "inference-tts", "novelty-check", "kazakh-morphological-segmentation-qualit", "architecture-fork", "parameter-counting-convention-and-iso-si", "kazakh-tokenizer-fertility-vs-byte-premi", "embed-sota", "attention-kv-architecture-sub-1b", "residual-stream-stability-qymyzlm-design", "data-efficiency-10b-kazakh-10b-token-pre"]
claims: 15
uncertain_claims: 2
verdicts: []
aliases: ["SozKZ: Training Efficient Small Language Models for Kazakh from Scratch", "arXiv:2603.20854", "arxiv:2603.20854"]
tags: ["paper", "topic/tokenizer-morphology", "topic/kazakh-turkic-nlp", "topic/inference-tts", "topic/novelty-check", "topic/kazakh-morphological-segmentation-qualit", "topic/architecture-fork", "topic/parameter-counting-convention-and-iso-si", "topic/kazakh-tokenizer-fertility-vs-byte-premi", "topic/embed-sota", "topic/attention-kv-architecture-sub-1b", "topic/residual-stream-stability-qymyzlm-design", "topic/data-efficiency-10b-kazakh-10b-token-pre"]
---
# SozKZ: Training Efficient Small Language Models for Kazakh from Scratch

[arXiv](https://arxiv.org/abs/2603.20854)
**Topics:** [[tokenizer-morphology]], [[kazakh-turkic-nlp]], [[inference-tts]], [[novelty-check]], [[kazakh-morphological-segmentation-qualit]], [[architecture-fork]], [[parameter-counting-convention-and-iso-si]], [[kazakh-tokenizer-fertility-vs-byte-premi]], [[embed-sota]], [[attention-kv-architecture-sub-1b]], [[residual-stream-stability-qymyzlm-design]], [[data-efficiency-10b-kazakh-10b-token-pre]]

> [!abstract]
> Kazakh, a Turkic language spoken by over 22 million people, remains underserved by existing multilingual language models, which allocate minimal capacity to low-resource languages and employ tokenizers ill-suited to agglutinative morphology. We present SozKZ, a family of Llama-architecture language models (50M-600M parameters) trained entirely from scratch on 9 billion tokens of Kazakh text with a …

## Claims

> [!note] CLAIM — tokenizer-morphology
> SozKZ-600M trains a ByteLevel-BPE tokenizer of 50,257 tokens exclusively on ~9B Kazakh tokens and reports a '2-3x fertility advantage over multilingual tokenizers' but publishes no absolute fertility number. Downstream it scores MC-QA 30.3%, Belebele 27.0%, SIB-200 25.5% — below multilingual Qwen-1.5B (MC-QA 37.1%) despite the far better tokenizer.
>
> **Numbers:** vocab 50,257; ~9B Kazakh tokens; 2-3x fertility advantage; MC-QA 30.3 / Belebele 27.0 / SIB-200 25.5; Qwen-1.5B MC-QA 37.1
> **Relevance:** Direct precedent at the exact target size/data. Key lesson: a great monolingual tokenizer alone does NOT beat larger multilingual models — the tokenizer is necessary but not sufficient; the from-scratch 600M/9B recipe underperforms. The paper the user must exceed.
> **Source:** arXiv:2603.20854 (SozKZ) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-turkic-nlp
> SozKZ (the closest prior art: from-scratch Kazakh 50M-600M) does NOT beat a general Qwen2.5-0.5B on knowledge QA. SozKZ-600M (587M, 22 layers, d=1280, 20 heads MHA, ctx 2048, ffn 4480, 50K BPE, 9B tokens) scores: cultural MC-QA 30.3, Belebele-kaz 27.0, SIB-200 25.5. Qwen2.5-0.5B scores 31.5 / 30.0 / 19.1; Llama-3.2-1B 32.0 / 26.7 / 20.1. SozKZ only wins on SIB-200 topic classification. It was NEVER evaluated on KazMMLU.
>
> **Numbers:** SozKZ-600M: MCQA 30.3, Belebele 27.0, SIB-200 25.5; Qwen2.5-0.5B 31.5/30.0/19.1; Llama-3.2-1B 32.0/26.7/20.1
> **Relevance:** CRITICAL reframing: the grounding note 'SozKZ ~30% KazMMLU' is wrong — that 30.3 is cultural QA, and it LOSES to Qwen2.5-0.5B on knowledge. Pure from-scratch at 600M has not beaten a strong general 0.5B on knowledge. This argues strongly for continued-pretrain/vocab-surgery on a Qwen-0.6B base as a hedge, or for the Engram memory being the differentiator that from-scratch SozKZ lacked.
> **Source:** arXiv 2603.20854 (SozKZ), html Table 1-2; corroborated in 2603.27859 Table 6 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — inference-tts
> Tokenizer fertility compounds across FOUR inference axes simultaneously. At 32K context: bespoke fertility 2.0 yields 16,000 effective Kazakh words vs 6,667 at multilingual fertility 4.8 (2.4x more). Generation at 40 tok/s: 20 words/s vs 8.3 words/s (2.4x faster perceived). KV entries per word and pretraining tokens per word also scale ~2.4x. SozKZ used ByteLevel BPE, 50,257 vocab, 9B tokens, claiming 2-3x fertility advantage over multilingual tokenizers.
>
> **Numbers:** fertility 2.0 vs 4.8: 16,000 vs 6,667 words @32K; 20 vs 8.3 words/s @40 tok/s; ~2.4x on all axes
> **Relevance:** The tokenizer is the single highest-leverage inference decision for Kazakh — hitting <2.0 fertility multiplies effective context in words, halves cache/word, and speeds words/s, all at once. Report 'effective context in WORDS', not tokens.
> **Source:** Derivation; SozKZ arXiv:2603.20854; fertility framing arXiv:2602.19174 (TurkicNLP) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — novelty-check
> The CLOSEST prior on 'sub-1B model purpose-built from scratch for one low-resource agglutinative language' is SozKZ — but it is architecturally VANILLA (Llama backbone, 50K BPE, no memory, no morphology module). This is the user's strongest differentiation opening: same target, same scale, zero architectural novelty.
>
> **Numbers:** SozKZ 600M: 9B Kazakh tokens, 50K BPE (fertility ~2.0); 30.3% Kazakh MC QA (vs Llama-3.2-1B 32.0%), 27.0% Belebele, 25.5% SIB-200
> **Relevance:** The paper's headline can be 'first architecturally-novel sub-1B Kazakh SLM' and must beat SozKZ-600M's 30.3% MC QA / 25.5% SIB-200 to be credible. SozKZ is the primary quantitative baseline to exceed.
> **Source:** arXiv:2603.20854 (SozKZ) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-morphological-segmentation-qualit
> The direct baseline SozKZ (600M) already reaches ~30.3% on Kazakh cultural MC-QA (NOT KazMMLU -- the paper does not report KazMMLU) with a plain ByteLevel BPE (50,257 vocab) and NO morphological segmentation, trained on 9B tokens from the identical noisy sources you target (CulturaX, HPLT 2.0, mC4, MADLAD-400, mOSCAR, Wikipedia; cleaned to 13.7M docs, 48.2% pass), claiming a 2-3x fertility advantage over multilingual tokenizers.
>
> **Numbers:** SozKZ-600M 587M params, 9.0B tokens, BPE vocab 50,257, 2-3x fertility advantage, cultural MC-QA ~30.3% (not KazMMLU). Data cleaned to 13.7M docs (48.2% pass rate). No morphology used.
> **Relevance:** Confirms that on the SAME noisy corpora, plain BPE already gets low fertility and ~30% KazMMLU without morphology. So the morphology angle must beat this on a morphology-specific metric under noise, not on fertility — and morpheme-conditioned memory must add value on top of, not instead of, a robust BPE fallback.
> **Source:** arXiv 2603.20854 'SozKZ: Training Efficient Small Language Models for Kazakh from Scratch' (Mar 2026) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — architecture-fork
> The single most on-point datapoint says from-scratch loses on knowledge: SozKZ-600M (from-scratch, ~9B Kazakh tokens, dedicated 50,257 ByteLevel BPE with a stated 2-3x fertility advantage) scores 30.3% on Kazakh multiple-choice cultural QA and 27.0 Belebele, BELOW Qwen2.5-0.5B (31.5 MC QA, 30.0 Belebele) which had NO Kazakh training; from-scratch only wins SIB-200 topic classification (25.5 vs 19.1). So a smaller, un-adapted Qwen base already out-knows the best from-scratch 600M.
>
> **Numbers:** SozKZ-600M: 30.3 MC QA / 27.0 Belebele / 25.5 SIB-200. Qwen2.5-0.5B: 31.5 / 30.0 / 19.1. Llama-3.2-1B: 32.0 / 26.7 / 20.1. Trained on 8xH100 for the 600M run.
> **Relevance:** Directly implies Qwen3-0.6B-Base at 32.8% KazMMLU is a stronger knowledge starting point than a from-scratch 600M can reach within 9-10B tokens. SozKZ used the same recipe class the paper proposes minus the novel modules.
> **Source:** arXiv 2603.20854 (SozKZ), Table 2 · **Sweep:** `slm-architecture-2026-07`

> [!warning] UNCERTAIN — architecture-fork
> SozKZ's reported knowledge benchmark is a cultural multiple-choice QA set (labelled 'MC QA'), NOT KazMMLU itself; the paper does not report KazMMLU. The grounding's 'SozKZ ~30% KazMMLU' should be read as ~30% on a cultural MC-QA proxy, so the head-to-head vs Qwen3-0.6B-Base on KazMMLU specifically remains unpublished.
>
> **Numbers:** SozKZ evaluates on: MC cultural QA, Belebele, SIB-200 only. Vocab 50,257 ByteLevel BPE, ~9B Kazakh tokens.
> **Relevance:** Confirms the user's premise that no published Kazakh KazMMLU head-to-head (from-scratch vs adapted-Qwen) exists; the paper can BE that experiment. Prevents mis-citing SozKZ as a KazMMLU result.
> **Source:** arXiv 2603.20854 (SozKZ), Table 2 + benchmark section · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — parameter-counting-convention-and-iso-si
> All three named Kazakh/peer comparators are DENSE, so for them total == active; there is no sparse/inactive budget to hide the memory. Qwen3-0.6B: 0.6B total / 0.44B non-embedding (~0.16B tied embedding, vocab ~151,936), 28 layers, GQA 16Q:8KV — every param is active. SozKZ 600M: dense Llama, 50K BPE, 9B tokens, all 600M active. Gemma3-270M: 270M total = 170M embedding (256K vocab) + 100M transformer, dense. Comparing a ~500M-active/~1B-total model to these on 'params' is only apples-to-apples on the ACTIVE axis; on the TOTAL/footprint axis the user model is 1.7x-3.7x larger than these peers.
>
> **Numbers:** Qwen3-0.6B 0.6B tot/0.44B non-emb; SozKZ 600M dense; Gemma3-270M 270M (170M emb + 100M blocks). All total==active. User ~1.0B total vs 0.27-0.6B.
> **Relevance:** Because the peers are dense, a reviewer's default 'params' means total, and the user model is one size class up (~1B) — Qwen3-0.6B/SozKZ/Gemma3-270M stop being the right comparators under iso-total.
> **Source:** HF Qwen/Qwen3-0.6B model card; arXiv 2603.20854 (SozKZ); Google Developers Blog 'Introducing Gemma 3 270M' + apxml.com/models/gemma-3-270m · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — parameter-counting-convention-and-iso-si
> The 'beats every best-tier ~500M SLM' claim does NOT survive an iso-TOTAL comparison: at ~1B total the honest peer set is the ~1B dense models, where the measured bar is much higher than the 500M models. From the user's own measured baselines: at ~1B total the true peers are Llama-3.2-1B (25.1% KazMMLU), Gemma3-1B-it (28.7%), and the still-larger Qwen2.5-1.5B (34.3%). Qwen3-0.6B (32.8%) and SozKZ-600M (~30%) sit BELOW the user's total-param class, so beating them does not establish superiority over iso-total peers. The claim is true on the active/FLOP axis but a reviewer will re-bracket the model into the 1B class, where 'beats every 500M SLM' is a category error.
>
> **Numbers:** ~1B-total peers: Llama-3.2-1B 25.1%, Gemma3-1B-it 28.7%; next up Qwen2.5-1.5B 34.3%. 500M peers (below user's total class): Qwen3-0.6B 32.8%, SozKZ-600M ~30%, Gemma3-270M 24.4%.
> **Relevance:** Central quantitative claim is at reviewer risk exactly as flagged: the target-beating comparison must be re-run vs ~1B models, or the model must be shrunk to actually be <=600M total.
> **Source:** User grounding (measured KazMMLU 5-shot, Kazakh subset, 9,870 Q); peer sizes per HF cards / arXiv 2603.20854 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-tokenizer-fertility-vs-byte-premi
> SozKZ (the referenced from-scratch Kazakh SLM) empirically corroborates that a great tokenizer does not buy accuracy: SozKZ-600M uses a dedicated ByteLevel-BPE 50K tokenizer with a 2-3x fertility advantage over multilingual tokenizers, trained on ~9B Kazakh tokens (15.3:1 data:param), yet scores only MC QA 30.3% / Belebele 27.0% / SIB-200 25.5% — LOSING to Qwen2.5-0.5B (MC QA 31.5% / Belebele 30.0%) which tokenizes Kazakh ~5x worse. Best tokenizer, no accuracy win.
>
> **Numbers:** SozKZ-600M: MC QA 30.3%, Belebele 27.0%, SIB-200 25.5%; Qwen2.5-0.5B: MC QA 31.5%, Belebele 30.0%, SIB-200 19.1%; SozKZ fertility advantage 2-3x; data:param 15.3:1
> **Relevance:** Direct Kazakh-domain evidence that fertility is not the dominant accuracy lever — a from-scratch model with an excellent Kazakh tokenizer still loses to an off-the-shelf model with terrible Kazakh fertility. Strongest single corroboration that the qymyzlm/KazLLM-v2 headline tokenizer claim needs hedging.
> **Source:** arXiv 2603.20854 'SozKZ: Training Efficient Small Language Models for Kazakh from Scratch' (html) + Table 6 in arXiv 2603.27859 · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter]]

> [!warning] UNCERTAIN — embed-sota
> Competitor scan side-finding: two 2026 arXiv papers already target Kazakh SLMs — 'SozKZ: Training Efficient Small Language Models for Kazakh from Scratch' (2603.20854) and 'KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter' (2603.27859); neither appears to ship an embedding model, so the embedding deliverable remains unclaimed territory, but the generative track's 'first/novel' claims must cite and differentiate from them.
>
> **Relevance:** Novelty-positioning risk for the overall paper; the embedding gap strengthens deliverable (2) as the differentiator.
> **Source:** https://arxiv.org/pdf/2603.20854; https://arxiv.org/html/2603.27859 (titles/abstracts surfaced in search; full contents not fetched — outside embed domain) · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — attention-kv-architecture-sub-1b
> [tested-on-Kazakh] The only from-scratch Kazakh SLM family, SozKZ (587M: 22 layers, hidden 1280, 20 attention heads, intermediate 4480, ctx 2048, vocab 50257, tied embeddings, LlamaForCausalLM with SwiGLU+RoPE+RMSNorm, bf16 mixed precision on 8×8 H100), uses completely vanilla attention — no GQA config, no QK-norm, no SWA, no MLA, 2K context only, and zero attention-related ablations. Combined with Sherkala-8B being stock Llama-3.1 attention (KB), NO non-vanilla attention mechanism of any kind has ever been ablated or even trained on Kazakh: the entire attention axis of this sweep is transferable-untested, which makes even a small-scale GQA-vs-MLA-vs-gated ablation on the lab's 9-10B-token corpus a first-on-Kazakh publishable result.
>
> **Numbers:** SozKZ-600M: 587M, 22L, d1280, 20 heads, ffn 4480, ctx 2048, vocab 50257, 9B tokens, 15:1 tok/param
> **Relevance:** Defines the competitive floor (vanilla MHA @2K ctx) the from-scratch design must beat, and certifies the novelty claim for QymyzLM's attention ablation section.
> **Source:** arXiv:2603.20854 (HTML Table 1 + text, fetched) + arXiv:2503.01493 (KB) · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately]]

> [!note] CLAIM — residual-stream-stability-qymyzlm-design
> [tested-on-Kazakh] SozKZ (the only published from-scratch Kazakh SLM family, 50M-600M, 9B tokens, 50K BPE) uses PLAIN Llama architecture with none of the 2025-26 residual-stream/stability innovations (no Peri-LN, no value residual, no LNS, no HC, no QK-norm mentioned). 600M reaches 30.3% Kazakh cultural QA. Consequence: EVERY technique in this sweep is untested on Kazakh; SozKZ is simultaneously the baseline recipe to beat at iso-data (9B tok ~ our ceiling) and proof that the from-scratch ablation space is unclaimed.
>
> **Numbers:** 50M-600M, 9B tokens, 50K BPE, fertility ~2.0 (KB); 600M: 30.3% Kazakh cultural QA, 25.5% SIB-200; scaling 22.8%->30.3% (50M->600M)
> **Relevance:** Direct paper positioning: 'SozKZ recipe + measured stability/residual kit at iso-data' is a publishable delta on its own, and SozKZ's clean Llama baseline means any gain we ablate (Peri-LN, value residual, LNS) is attributable. Also confirms 9B Kazakh tokens is a demonstrated-feasible from-scratch budget.
> **Source:** arXiv:2603.20854 (SozKZ; search-verified 2026-07-04; architecture claim from abstract 'Llama-architecture') · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — data-efficiency-10b-kazakh-10b-token-pre
> SozKZ built the largest known monolingual Kazakh pretraining corpus by aggregating 18 web/curated sources (CulturaX, HPLT 2.0, mC4, MADLAD-400, mOSCAR, CC-100, Kazakh Wikipedia, kz-transformers/multidomain-kazakh-dataset). Raw = 28.4M docs; a 9-stage RULE-BASED cleaning pipeline (NFC, control-char removal, whitespace collapse, min-length >=50 chars, URL density <=5/1000 chars, HTML tags <=5, Kazakh char-ratio filter, langID kk-only, MD5 EXACT dedup within+cross-source vs 12.4M multidomain hashes) kept 13.7M docs (48.2% pass rate) = ~9.0B tokens under a 50K BPE tokenizer. Trained 1 epoch only, tokens/param 15.3:1 for the 600M.
>
> **Numbers:** 18 sources; 28.4M raw docs -> 13.7M kept (48.2%) -> ~9.0B tokens (50K BPE); MD5 exact dedup only; 1 epoch; 9.0B/587M = 15.3:1
> **Relevance:** This is the concrete from-scratch Kazakh data ceiling and pipeline the lab can reuse. Two exploitable gaps: (a) only MD5 EXACT dedup (no MinHash fuzzy dedup) and (b) NO model-based quality filter and (c) only 1 epoch — all three are where 2026 English/German recipes add the most value.
> **Source:** arXiv:2603.20854 (SozKZ), sec 3.1/3.4 · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — data-efficiency-10b-kazakh-10b-token-pre
> SozKZ-600M (from-scratch, ~9.0B kk tokens, dedicated 50K Kazakh BPE) scores BELOW our Qwen3-0.6B target on knowledge: MC QA (kk-socio-cultural, 7,111 Q, 4-choice, 0-shot logit-scored) 30.3% vs Qwen-0.5B 31.5%, Llama-3.2-1B 32.0%, Qwen-1.5B 37.1%; Belebele-kk 27.0% (near 25% floor for all sub-3B); SIB-200-kk 25.5% (beats all multilingual up to 2B incl Qwen-1.5B 11.8%, Gemma-2B 20.1% — tokenizer/lexical win). MC QA scaled 22.8%(50M)->30.3%(600M), no saturation.
>
> **Numbers:** SozKZ-600M: MC QA 30.3 / Belebele 27.0 / SIB-200 25.5; Qwen-0.5B 31.5/30.0/19.1; from-scratch 9B tokens 0-shot
> **Relevance:** Direct evidence that 9B tokens from-scratch at 600M does NOT beat Qwen3-0.6B on knowledge QA — confirms the lab's continual-PT-from-Qwen3 default over from-scratch. SIB-200 result shows a Kazakh tokenizer alone buys large gains on lexical tasks.
> **Source:** arXiv:2603.20854 (SozKZ), Table 2 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[scaling-data-constrained-language-models|Scaling Data-Constrained Language Models]] — Data-constrained + T4 feasibility argues against from-scratch; SozKZ is the executed Kazakh-from-scratch counterpoint
- [[datacomp-lm-in-search-of-the-next-generation-of-training-sets-for-language|DataComp-LM: In search of the next generation of training sets for language models]] — DCLM 400M-1x is the specified recipe analog; SozKZ is the real Kazakh from-scratch execution to compare against
- [[a-systematic-study-of-cross-layer-kv-sharing-for-efficient-llm-inference|A Systematic Study of Cross-Layer KV Sharing for Efficient LLM Inference]] — Both train Kazakh/small LMs from scratch; cross-layer KV sharing is a candidate cut for SozKZ-scale from-scratch models
- [[adaptive-engram-memory-system-for-indonesian-language-model-generative-ai-based|Adaptive Engram Memory System for Indonesian Language Model: Generative AI Based on TOBA L…]] — TOBA is the dense+Engram+agglutinative analog; SozKZ-600M is the Kazakh from-scratch SLM a morpheme-Engram would augment
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] — SozKZ uses fully vanilla MHA; latent MHA at small scale is an untested efficiency upgrade the Kazakh attention axis lacks

[[Home]]
