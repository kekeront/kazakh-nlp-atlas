---
kb_id: "arxiv:2403.13638"
type: "paper"
title: "Pretraining Language Models Using Translationese"
arxiv_id: "2403.13638"
doi: null
hf_repo: null
year: 2024
topics: ["data-efficiency-10b-kazakh-10b-token-pre"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Pretraining Language Models Using Translationese", "arXiv:2403.13638", "arxiv:2403.13638"]
tags: ["paper", "topic/data-efficiency-10b-kazakh-10b-token-pre"]
---
# Pretraining Language Models Using Translationese

[arXiv](https://arxiv.org/abs/2403.13638)
**Topics:** [[data-efficiency-10b-kazakh-10b-token-pre]]

> [!abstract]
> In this paper, we explore the utility of translationese as synthetic data created using machine translation for pre-training language models (LMs) for low-resource languages (LRLs). Our simple methodology consists of translating large amounts of web-crawled monolingual documents (clean) into the LRLs, followed by filtering the translated documents using tiny LMs trained on small but clean LRL data …

## Claims

> [!note] CLAIM — data-efficiency-10b-kazakh-10b-token-pre
> Filtered translationese for LOW-resource pretraining costs almost nothing vs clean data, if you filter with a tiny native LM. Translating 5B English tokens into Hindi/Gujarati/Marathi (IndicTrans2), then filtering with 28M/85M-param native LMs by perplexity (skip first 10 tok, score up to 1024 tok/doc), gave only -0.87% NLU and -2.35% NLG vs clean-data pretraining; adding ~10% clean native data (100-200M tokens) closed most of the remaining gap.
>
> **Numbers:** 5B MT tokens; tiny-LM filter (28M/85M); filtered synthetic vs clean: NLU -0.87%, NLG -2.35%; +10% clean closes gap
> **Relevance:** transferable-untested (Indic, not Turkic). Gives a concrete, cheap recipe for the synthetic portion: MT English->kk, filter with a small native-kk LM, and always append >=10% clean native kk to kill translationese. Bounds the synthetic risk that Sherkala took at 24% of its Kazakh mix.
> **Source:** arXiv:2403.13638 (Pretraining LMs Using Translationese, EMNLP 2024) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Settin…]] — translationese's cheap low-resource MT-filtering result predicts Sherkala's 24% synthetic-MT Kazakh works at low cost
- [[danielvanstrien-xyz-fineweb-c-analysis|danielvanstrien.xyz FineWeb-C analysis]] — translationese's tiny native-LM perplexity filter is a viable substitute for the FineWeb-Edu classifier davanstrien shows is absent for…

[[Home]]
