---
kb_id: "arxiv:2510.09947"
type: "paper"
title: "Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation"
arxiv_id: "2510.09947"
doi: null
hf_repo: null
year: 2025
topics: ["tokenizer-morphology"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation", "arXiv:2510.09947", "arxiv:2510.09947"]
tags: ["paper", "topic/tokenizer-morphology"]
---
# Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation

[arXiv](https://arxiv.org/abs/2510.09947)
**Topics:** [[tokenizer-morphology]]

> [!abstract]
> Tokenization is a crucial but under-evaluated step in large language models (LLMs). The standard metric, fertility (the average number of tokens per word), captures compression efficiency but obscures how vocabularies are allocated across languages and domains. We analyze six widely used tokenizers across seven languages and two domains, finding stable fertility for English, high fertility for Chi …

## Claims

> [!note] CLAIM — tokenizer-morphology
> STRR (Single-Token Retention Rate = % of words kept as one token) is a 2025 type-level diagnostic that exposes vocabulary misallocation that average fertility hides (e.g. it localizes which languages are over-fragmented, like Hindi's uniformly lowest STRR). Fertility 'collapses behavior into average tokens per word, masking over-fragmentation.'
>
> **Numbers:** STRR = (1/n) sum 1[|T(w)|=1] x 100; complements fertility; no Turkic numbers reported yet
> **Relevance:** Add STRR (and MorphScore) alongside fertility as evaluation metrics in the paper — reporting only fertility is now considered insufficient by 2025 tokenizer literature. Reviewers will expect the richer intrinsic metric suite.
> **Source:** arXiv:2510.09947 (Beyond Fertility: STRR) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[why-do-language-models-perform-worse-for-morphologically-complex-languages|Why do language models perform worse for morphologically complex languages?]] — Both argue fertility is a weak predictor; STRR proposes a replacement metric for multilingual tokenizer quality
- [[quechuatok-morphological-boundary-accuracy-as-a-necessary-metric-for-tokenizer|QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation…]] — Both refute fertility as a sufficient tokenizer metric; QuechuaTok proposes morpheme-boundary accuracy, Beyond-Fertility proposes STRR
- [[ggml-org-llama-cpp-discussions-3167-4167-8273|ggml-org/llama.cpp Discussions #3167/#4167/#8273]] — Edge tok/s → perceived words/s divides by tokenizer fertility; STRR reframes how to measure that multilingual fertility premium

[[Home]]
