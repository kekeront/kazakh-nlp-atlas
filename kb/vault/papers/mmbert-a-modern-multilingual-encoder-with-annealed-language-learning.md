---
kb_id: "arxiv:2509.06888"
type: "paper"
title: "mmBERT: A Modern Multilingual Encoder with Annealed Language Learning"
arxiv_id: "2509.06888"
doi: null
hf_repo: "jhu-clsp/mmBERT-base"
year: 2025
topics: ["embed-sota", "embeddings-training"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["mmBERT: A Modern Multilingual Encoder with Annealed Language Learning", "arXiv:2509.06888", "arxiv:2509.06888"]
tags: ["paper", "topic/embed-sota", "topic/embeddings-training"]
---
# mmBERT: A Modern Multilingual Encoder with Annealed Language Learning

[arXiv](https://arxiv.org/abs/2509.06888)
**Topics:** [[embed-sota]], [[embeddings-training]]

> [!abstract]
> Encoder-only languages models are frequently used for a variety of standard machine learning tasks, including classification and retrieval. However, there has been a lack of recent research for encoder models, especially with respect to multilingual models. We introduce mmBERT, an encoder-only language model pretrained on 3T tokens of multilingual text in over 1800 languages. To build mmBERT we in …

## Claims

> [!note] CLAIM — embed-sota
> mmBERT (JHU, Sep 2025): ModernBERT-architecture multilingual encoder pretrained on 3T tokens covering 1,833 languages via 'annealed language learning' — 1,700+ low-resource languages are added ONLY in the final 100B-token decay phase (with inverse mask-ratio schedule and inverse temperature sampling), which 'boosts performance dramatically' on them; first encoder to beat XLM-R. Phases: 2.3T pretrain (60 langs) -> 600B mid-train at 8192 ctx (110 langs) -> 100B decay (1,833 langs).
>
> **Numbers:** 3T tokens, 1833 languages, 8192 ctx, base ~307M.
> **Relevance:** Two uses: (a) mmBERT-base is the freshest open encoder backbone to contrastively tune for Kazakh; (b) its decay-phase finding maps onto the SLM pretraining plan — concentrated kk exposure late in training is disproportionately effective.
> **Source:** https://arxiv.org/abs/2509.06888; https://huggingface.co/jhu-clsp/mmBERT-base; https://huggingface.co/blog/mmbert · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — embeddings-training
> mmBERT is a 2025 modern multilingual ENCODER whose pretraining EXPLICITLY includes Kazakh — the only fresh encoder backbone in this sweep with confirmed kk coverage. Base 307M (110M non-emb), small 140M (42M non-emb), 256k vocab, 3T tokens, 1833 languages via annealed language learning. Not itself an embedding model (no contrastive head), but a from-scratch backbone option.
>
> **Numbers:** base 307M/110M non-emb, small 140M/42M non-emb; vocab 256k; 3T tokens; 1833 langs incl. kaz; ctx 1024->8192; MTEB v2 multilingual 54.1 (base) vs XLM-R 52.4
> **Relevance:** TESTED-ON-KAZAKH (pretraining coverage only; NO Kazakh embedding eval). Best modern encoder base if the lab wants an encoder path instead of decoder-conversion for v0; 256k vocab helps Kazakh fertility. Caveat: 54.1 MTEB-multilingual is well below mE5/KaLM as an out-of-box embedder — it needs a contrastive fine-tune to compete.
> **Source:** arXiv:2509.06888 (mmBERT, JHU-CLSP); github.com/jhu-clsp/mmBERT · **Sweep:** `slm-arch-for-kazakh`

[[Home]]
