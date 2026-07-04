---
kb_id: "title:mdpi information 17 2 128 cse guided jan 2026 github walsher46 kazakh tokenizer apertium kaz"
type: "source"
title: "MDPI Information 17(2):128 (CSE-guided, Jan 2026)"
doi: null
hf_repo: null
year: null
topics: ["kazakh-turkic-nlp"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:mdpi information 17 2 128 cse guided jan 2026 github walsher46 kazakh tokenizer apertium kaz"]
tags: ["source", "topic/kazakh-turkic-nlp"]
---
# MDPI Information 17(2):128 (CSE-guided, Jan 2026)

**Topics:** [[kazakh-turkic-nlp]]

## Source URLs
- MDPI Information 17(2):128 (CSE-guided, Jan 2026)
- github walsher46/Kazakh-tokenizer
- Apertium-kaz

## Findings

> [!note] CLAIM — kazakh-turkic-nlp
> Morphology-aware tokenization is a validated lever for Kazakh. A CSE-guided (Complete Set of Endings) SentencePiece tokenizer that pre-segments on morpheme boundaries yields shorter sequences and up to ~33% neural training-time reduction; SentencePiece Unigram beats BPE on morpheme-boundary preservation and lower fertility for agglutinative Kazakh. Kazakh morphotactics: 64 theoretical affix slots, only 15 linguistically valid (vowel-harmony/morphophonemic constrained). Open tooling exists: Apertium-kaz transducer + UD Kazakh treebank.
>
> **Numbers:** up to ~33% training-time cut; 64 affix slots, 15 valid; Unigram < BPE fertility
> **Relevance:** Concrete tokenizer upgrade over plain Unigram-50K: pre-segment the training corpus with a CSE/Apertium-kaz morphological analyzer before training SentencePiece-Unigram, so subwords align to real morpheme boundaries. This is the mechanism to actually reach fertility<2.0 AND improve morphological generalization — validate fertility on UD-kaz/Apertium gold segmentation.
> **Source:** MDPI Information 17(2):128 (CSE-guided, Jan 2026); github walsher46/Kazakh-tokenizer; Apertium-kaz · **Sweep:** `slm-architecture-2026-07`

[[Home]]
