---
kb_id: "hf:blog/davanstrien"
type: "source"
title: "danielvanstrien.xyz FineWeb-C analysis"
doi: null
hf_repo: "blog/davanstrien"
year: null
topics: ["data-efficiency-10b-kazakh-10b-token-pre"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:blog/davanstrien"]
tags: ["source", "topic/data-efficiency-10b-kazakh-10b-token-pre"]
---
# danielvanstrien.xyz FineWeb-C analysis

**Topics:** [[data-efficiency-10b-kazakh-10b-token-pre]]

## Source URLs
- danielvanstrien.xyz FineWeb-C analysis
- huggingface.co/blog/davanstrien/fineweb-c
- FineWeb-Edu classifier notes

## Findings

> [!note] CLAIM — data-efficiency-10b-kazakh-10b-token-pre
> Kazakh is ABSENT from FineWeb-C community educational-quality annotations (91 languages covered; kaz_Cyrl not among them). No FineWeb-Edu-style Kazakh quality classifier exists off the shelf. Cross-lingual transfer of the English FineWeb-Edu classifier onto translated text is documented not to work (picks up surface features that don't survive translation).
>
> **Numbers:** FineWeb-C: 91 languages, ~1,000 samples/lang, >50k annotations total; Kazakh = 0 annotations
> **Relevance:** tested-on-Kazakh (absence confirmed). The lab must BOOTSTRAP its own kk quality classifier (e.g., annotate ~10-20k kk docs with a strong multilingual LLM, train a light regressor on mE5/XLM-R embeddings) — this is the single missing ingredient to apply the German/BOLDT recipe to Kazakh.
> **Source:** danielvanstrien.xyz FineWeb-C analysis; huggingface.co/blog/davanstrien/fineweb-c; FineWeb-Edu classifier notes · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[pretraining-language-models-using-translationese|Pretraining Language Models Using Translationese]] — translationese's tiny native-LM perplexity filter is a viable substitute for the FineWeb-Edu classifier davanstrien shows is absent for…
- [[textbooks-are-all-you-need|Textbooks Are All You Need]] — the Textbooks/FineWeb-Edu educational-quality paradigm has no Kazakh classifier and does not transfer across translation

[[Home]]
