---
kb_id: "arxiv:2508.08424"
type: "paper"
title: "Rethinking Tokenization for Rich Morphology: The Dominance of Unigram over BPE and Morphological Alignment"
arxiv_id: "2508.08424"
doi: null
hf_repo: null
year: 2025
topics: ["novelty-check", "tokenizer-agglutinative"]
claims: 3
uncertain_claims: 0
verdicts: []
aliases: ["Rethinking Tokenization for Rich Morphology: The Dominance of Unigram over BPE and Morphological Alignment", "arXiv:2508.08424", "arxiv:2508.08424"]
tags: ["paper", "topic/novelty-check", "topic/tokenizer-agglutinative"]
---
# Rethinking Tokenization for Rich Morphology: The Dominance of Unigram over BPE and Morphological Alignment

[arXiv](https://arxiv.org/abs/2508.08424)
**Topics:** [[novelty-check]], [[tokenizer-agglutinative]]

> [!abstract]
> The relationship between tokenizer algorithm (e.g., Byte-Pair Encoding (BPE), Unigram), morphological alignment, tokenization quality (e.g., compression efficiency), and downstream performance remains largely unclear, particularly for languages with complex morphology. In this paper, we conduct a comprehensive evaluation of tokenizers using small-sized BERT models -- from pre-training through fine …

## Claims

> [!note] CLAIM — novelty-check
> Empirical support for the user's Unigram-over-BPE tokenizer choice exists, but with a caveat: Unigram dominates BPE for rich morphology, AND morphological pre-segmentation boosts BPE but NOT Unigram. So combining Unigram with morpheme pre-segmentation may give no gain.
>
> **Numbers:** Telugu (agglutinative) primary; gold segmentations of 600 derivational + 7000 inflectional forms; tokenizer ALGORITHM is the dominant factor, morphological alignment only a secondary/moderate positive correlate
> **Relevance:** Validates SentencePiece Unigram 50K choice. But warns: do not stack morpheme pre-segmentation on top of Unigram expecting gains — put morphology awareness in the model (memory/aux head), not the pre-tokenizer.
> **Source:** arXiv:2508.08424 (Rethinking Tokenization for Rich Morphology: The Dominance of Unigram over BPE) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — tokenizer-agglutinative
> For rich morphology the TOKENIZER ALGORITHM (Unigram vs BPE) dominates downstream quality, far more than explicit morphological alignment. On Telugu (agglutinative) small BERT models, Unigram beats BPE by 8-13 points at every vocab size; Unigram peaks at LARGE vocab (50,277), BPE peaks at SMALL vocab. Hybrid Morfessor-presegmentation helps BPE but NOT Unigram.
>
> **Numbers:** Text-classification task group, naive tokenizer @ vocab 8192/16384/50277: BPE 69.39/66.44/68.57 vs Unigram 77.71/80.06/81.56; gold morpheme set 600 derivational + 7000 inflectional; Spearman(overall-trend, morph-recall)=0.486 (p=0.041)
> **Relevance:** transferable-untested (Telugu, Dravidian agglutinative; NOT Turkic/Kazakh). Strongest current evidence that a 500M Kazakh model should use Unigram (SentencePiece), not BPE, and that chasing morpheme-boundary alignment is secondary to picking Unigram. Contradicts the SozKZ/Sherkala choice of ByteLevel-BPE.
> **Source:** arXiv:2508.08424 (IJCNLP-SRW 2025), PDF table 2, extracted · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — tokenizer-agglutinative
> Extending the KB MorphBPE node: morphological pre-segmentation (Morfessor/analyzer) is only worth it if pairing with BPE — the Telugu study shows hybrid Morfessor+BPE beats naive BPE, but hybrid does NOT help Unigram (Unigram already captures the gains algorithmically).
>
> **Numbers:** Hybrid Morfessor+BPE > naive BPE; hybrid+Unigram ≈ naive Unigram (no consistent gain)
> **Relevance:** transferable-untested. If QymyzLM picks Unigram (per #2/#3), a Kazakh morphological analyzer front-end is largely redundant — saves engineering; if it picks BPE, a Morfessor/analyzer front-end becomes valuable. Resolves a design fork.
> **Source:** arXiv:2508.08424 (IJCNLP-SRW 2025), PDF results text · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[evaluating-morphological-alignment-of-tokenizers-in-70-languages|Evaluating Morphological Alignment of Tokenizers in 70 Languages]] — Both conclude Unigram-LM aligns to morpheme boundaries better than BPE, strongest for agglutinative languages
- [[morphbpe-a-morpho-aware-tokenizer-bridging-linguistic-complexity-for-efficient|MorphBPE: A Morpho-Aware Tokenizer Bridging Linguistic Complexity for Efficient LLM Traini…]] — Unigram-dominance finding qualifies MorphBPE: morph pre-segmentation helps BPE but gives Unigram no consistent gain
- [[quechuatok-morphological-boundary-accuracy-as-a-necessary-metric-for-tokenizer|QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation…]] — Both argue morphology-aware metric matters and unigram/PRPE beat surface BPE on morpheme boundaries in agglutinative LRLs
- [[mingram-a-minimalist-unigram-tokenizer-with-high-compression-and-competitive|MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive Morphologica…]] — MinGram and the Telugu study independently corroborate Unigram-family beats BPE on bits-per-byte across languages

[[Home]]
