---
kb_id: "arxiv:2407.13623"
type: "paper"
title: "Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies"
arxiv_id: "2407.13623"
doi: null
hf_repo: null
year: 2024
topics: ["tokenizer-morphology", "tokenizer-agglutinative"]
claims: 3
uncertain_claims: 1
verdicts: []
aliases: ["Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies", "arXiv:2407.13623", "arxiv:2407.13623"]
tags: ["paper", "topic/tokenizer-morphology", "topic/tokenizer-agglutinative"]
---
# Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies

[arXiv](https://arxiv.org/abs/2407.13623)
**Topics:** [[tokenizer-morphology]], [[tokenizer-agglutinative]]

> [!abstract]
> Research on scaling large language models (LLMs) has primarily focused on model parameters and training data size, overlooking the role of vocabulary size. We investigate how vocabulary size impacts LLM scaling laws by training models ranging from 33M to 3B parameters on up to 500B characters with various vocabulary configurations. We propose three complementary approaches for predicting the compu …

## Claims

> [!note] CLAIM — tokenizer-morphology
> Compute-optimal vocabulary scales with non-embedding params via a power law with exponent gamma~=0.83 (vocab params grow slower than model params). For ~300M non-vocab params the predicted optimal vocab is ~83K-91K; for ~70B it is ~212K-231K. Loss vs vocab is U-shaped for any fixed budget: too small hurts compression, too large under-trains rare tokens under limited data.
>
> **Numbers:** gamma~=0.83; 300M non-vocab -> 83K-91K optimal vocab; U-shaped loss; Llama2-70B 'should' have used 216K not 32K
> **Relevance:** For a 500M model this argues optimal vocab is ~90-120K IF data were abundant. But with only ~9-10B tokens (data-constrained), rare tokens in a 100K+ vocab are under-trained, and embeddings eat budget (see next finding). Net: pick vocab from the LOW end of the compute-optimal band and spend the savings on Kazakh coverage.
> **Source:** arXiv:2407.13623 (Scaling Laws with Vocabulary, NeurIPS 2024) · **Sweep:** `slm-architecture-2026-07`

> [!warning] UNCERTAIN — tokenizer-morphology
> Embedding-parameter share is a hard constraint at 500M: with tied embeddings, embedding params = V x d. At d=1536, a 50K vocab = 76.8M params (~15% of 500M); 100K = 153.6M (~31%); 200K (SuperBPE) = 307M (>60%, infeasible). Under a fixed 500M cap, every vocab doubling steals capacity from the transformer body.
>
> **Numbers:** V x d tied: 50K@1536=76.8M (15%), 64K@1536=98.3M (20%), 100K@1536=153.6M (31%), 200K@1536=307M (61%)
> **Relevance:** Quantifies why the vocab-scaling-law 'bigger is better' does NOT transfer to a 500M cap: 200K vocab is impossible and 100K costs a third of the model. Recommends a 48-64K vocab sweet spot (15-20% embedding share) — consistent with SozKZ 50K and Sherkala's ~31K Kazakh delta. This is derived arithmetic (d assumed ~1536), flag as design-dependent.
> **Source:** derived from arXiv:2407.13623 + standard tied-embedding arithmetic · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — tokenizer-agglutinative
> Vocabulary is under-sized at almost all scales; compute-optimal vocab scales as Nv ∝ Nnv^0.83. Interpolated optimum for a ~500M non-embedding model is ~64K-75K tokens. Adopting predicted vocab lifted ARC-C from 29.1 to 32.0 at identical 2.3e21 FLOPs (32K->43K).
>
> **Numbers:** γ≈0.83; 0.3B->62-67K, 0.4B->81-91K, 0.9B->142-154K; ~500M interp ≈70-75K; ARC-C 29.1->32.0 at 32K->43K, same 2.3e21 FLOPs; models 33M-3B on ≤500B chars
> **Relevance:** transferable-untested. Sets the target vocab band for QymyzLM: ~64K (Unigram peaks high per #2, and this law says 500M 'deserves' ~70K). Validates that SozKZ's 50K and argues AGAINST 150K+ multilingual vocabs at 500M (over-allocated) and against SuperBPE's 200K at this scale.
> **Source:** arXiv:2407.13623 (NeurIPS 2024), HTML v3 Table 1 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[scaling-embeddings-outperforms-scaling-experts-in-language-models|Scaling Embeddings Outperforms Scaling Experts in Language Models]] — both address param allocation between embeddings/vocab and the transformer body; disagree on whether scaling embeddings pays off

[[Home]]
