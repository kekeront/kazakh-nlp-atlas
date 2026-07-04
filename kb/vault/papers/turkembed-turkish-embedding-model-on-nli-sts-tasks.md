---
kb_id: "arxiv:2511.08376"
type: "paper"
title: "TurkEmbed: Turkish Embedding Model on NLI & STS Tasks"
arxiv_id: "2511.08376"
doi: null
hf_repo: null
year: 2025
topics: ["embeddings-training"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["TurkEmbed: Turkish Embedding Model on NLI & STS Tasks", "arXiv:2511.08376", "arxiv:2511.08376"]
tags: ["paper", "topic/embeddings-training"]
---
# TurkEmbed: Turkish Embedding Model on NLI & STS Tasks

[arXiv](https://arxiv.org/abs/2511.08376)
**Topics:** [[embeddings-training]]

> [!abstract]
> This paper introduces TurkEmbed, a novel Turkish language embedding model designed to outperform existing models, particularly in Natural Language Inference (NLI) and Semantic Textual Similarity (STS) tasks. Current Turkish embedding models often rely on machine-translated datasets, potentially limiting their accuracy and semantic understanding. TurkEmbed utilizes a combination of diverse datasets …

## Claims

> [!note] CLAIM — embeddings-training
> Turkic evidence (closest family to Kazakh) says beating mE5 is HARD even with a dedicated effort: TR-MTEB built 34.2M weakly-supervised Turkish pairs and trained Turkish-specific models with Matryoshka + two-stage NLI/STS fine-tuning, yet multilingual-E5 variants still LEAD the benchmark; Turkish-specific models are 'improving but not yet surpassing' mE5.
>
> **Numbers:** 34.2M weak Turkish pairs; Matryoshka + MNRL (All-NLI-TR) then CoSENT (STSB-TR); mE5 still #1 on TR-MTEB retrieval
> **Relevance:** TESTED-ON-TURKIC. Sober calibration for the lab's 'beat mE5-large' target: a 34.2M-pair Turkish program did not dethrone mE5 on a same-family agglutinative language. Implies qymyz-embed must lean on (a) KazQAD-domain specialization and (b) distillation/model-soup, not raw pair volume, to win on KazQAD specifically.
> **Source:** TR-MTEB (ACL Findings EMNLP 2025, aclanthology 2025.findings-emnlp.471); TurkEmbed arXiv:2511.08376; TurkEmbed4Retrieval arXiv:2511.07595 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[xnli-evaluating-cross-lingual-sentence-representations|XNLI: Evaluating Cross-lingual Sentence Representations]] — Turkish (sister Turkic) has NLI+STS enabling TurkEmbed; Kazakh has neither, so an equivalent kk supervised-STS embedder is blocked
- [[the-russian-focused-embedders-exploration-rumteb-benchmark-and-russian|The Russian-focused embedders' exploration: ruMTEB benchmark and Russian embedding model d…]] — ruMTEB is the kkMTEB construction template; TurkEmbed is the Turkic-family analogue — both test whether monolingual specialization beats mE5
- [[less-is-more-adapting-text-embeddings-for-low-resource-languages-with-small|Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Scale Noisy S…]] — Turkic sibling: TurkEmbed's 34.2M pairs fail to beat mE5, tempering Less-is-More's claim of cheaply winning on a Kazakh-family LRL
- [[aclanthology-org-2025-findings-emnlp-471-tr-mteb-emnlp-2025|aclanthology.org/2025.findings-emnlp.471 (TR-MTEB, EMNLP 2025 Findings…]] — TurkEmbed is evaluated on TR-MTEB, where mE5 variants still lead retrieval
- [[huggingface-co-nurlykhan-kazembed-v5-apache-2-0|huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)]] — Turkic-sibling target: TurkEmbed is a Turkish embedding model, closest-language comparator for Kazakh

[[Home]]
