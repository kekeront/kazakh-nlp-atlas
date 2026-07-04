---
kb_id: "arxiv:1809.05053"
type: "paper"
title: "XNLI: Evaluating Cross-lingual Sentence Representations"
arxiv_id: "1809.05053"
doi: null
hf_repo: "api/datasets"
year: 2018
topics: ["embed-kazakh"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["XNLI: Evaluating Cross-lingual Sentence Representations", "arXiv:1809.05053", "arxiv:1809.05053"]
tags: ["paper", "topic/embed-kazakh"]
---
# XNLI: Evaluating Cross-lingual Sentence Representations

[arXiv](https://arxiv.org/abs/1809.05053)
**Topics:** [[embed-kazakh]]

> [!abstract]
> State-of-the-art natural language processing systems rely on supervision in the form of annotated data to learn competent models. These models are generally trained on data in a single language (usually English), and cannot be directly used beyond that language. Since collecting data in every language is not realistic, there has been a growing interest in cross-lingual language understanding (XLU)

## Claims

> [!note] CLAIM — embed-kazakh
> No Kazakh STS or NLI dataset exists anywhere: XNLI's 15 languages exclude kk; MUSTS (ACL 2025, the broadest multilingual STS benchmark, 13 languages) verified to not contain Kazakh (full-text check of the PDF); HF dataset API searches for 'kaznli', 'nli kazakh', 'sts kazakh', 'kazsts' all return zero results. The closest artifact is Arailym-tleubayeva/KazakhTextDuplicates (10k-100k, duplicate/plagiarism detection, Mar 2025).
>
> **Numbers:** 0 kk STS datasets; 0 kk NLI datasets; XNLI = 15 langs without kk; MUSTS = 13 langs without kk
> **Relevance:** Biggest single benchmark gap — an embedder cannot even be evaluated on kk semantic similarity today; building KazSTS is a mandatory milestone.
> **Source:** aclanthology.org/2025.acl-short.27 (PDF text extracted); huggingface.co/api/datasets searches 2026-07-03; XNLI arXiv:1809.05053 · **Sweep:** `embeddings-2026-07`

## Related
- [[turkembed-turkish-embedding-model-on-nli-sts-tasks|TurkEmbed: Turkish Embedding Model on NLI & STS Tasks]] — Turkish (sister Turkic) has NLI+STS enabling TurkEmbed; Kazakh has neither, so an equivalent kk supervised-STS embedder is blocked

[[Home]]
