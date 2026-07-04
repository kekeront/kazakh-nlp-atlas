---
kb_id: "arxiv:2502.12829"
type: "paper"
title: "KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan"
arxiv_id: "2502.12829"
doi: null
hf_repo: null
year: 2025
topics: ["sota-slm", "kazakh-turkic-nlp", "inference-tts", "win-bar-protocol-audit"]
claims: 6
uncertain_claims: 2
verdicts: []
aliases: ["KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan", "arXiv:2502.12829", "arxiv:2502.12829"]
tags: ["paper", "topic/sota-slm", "topic/kazakh-turkic-nlp", "topic/inference-tts", "topic/win-bar-protocol-audit"]
---
# KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan

[arXiv](https://arxiv.org/abs/2502.12829)
**Topics:** [[sota-slm]], [[kazakh-turkic-nlp]], [[inference-tts]], [[win-bar-protocol-audit]]

> [!abstract]
> Despite having a population of twenty million, Kazakhstan's culture and language remain underrepresented in the field of natural language processing. Although large language models (LLMs) continue to advance worldwide, progress in Kazakh language has been limited, as seen in the scarcity of dedicated models and benchmark evaluations. To address this gap, we introduce KazMMLU, the first MMLU-style …

## Claims

> [!note] CLAIM — sota-slm
> No mainstream sub-1B SLM is trained for Kazakh/Turkic: Falcon-H1 (18 langs) and LFM2 (prioritizes ja/ar/ko/es/fr/de, base zh/it/pt) exclude all Turkic; Qwen3 nominally covers 119 langs incl. Kazakh but still only reaches ~33% KazMMLU at 0.6B; Gemma-3-270M and Llama-3.2-1B are at random (24-25%). Best OPEN KazMMLU results are large: Llama-3.1-70B 55.2%, Gemma-2-27B-IT 54.0%.
>
> **Numbers:** sub-1B on KazMMLU: Qwen3-0.6B 32.8%, others 24-25% (random); best open 55.2% (70B)
> **Relevance:** Confirms the whitespace: a purpose-built 600M Kazakh model beating ~33% and approaching the 40-55% band would be genuinely SOTA-at-scale and novel — no competitor occupies sub-1B Kazakh.
> **Source:** arXiv 2502.12829 (KazMMLU); Falcon-H1 & LFM2 model cards; user grounding · **Sweep:** `slm-architecture-2026-07`

> [!warning] UNCERTAIN — kazakh-turkic-nlp
> As of mid-2026 no published DEDICATED <=1B model reports a strong KazMMLU number; the practical <=1B ceiling is held by general Qwen (user-measured Qwen3-0.6B-Base ~32.8, Qwen2.5-0.5B ~28.8; Qwen2.5-1.5B ~34.3 is >1B). KazMMLU's own paper only tested >=1.1B (Bloom-1.1B lowest at 22.1). No from-scratch or adapted <=600M Kazakh model has published a KazMMLU score above random-to-low-30s.
>
> **Numbers:** Qwen3-0.6B ~32.8; Qwen2.5-0.5B ~28.8; Bloom-1.1B 22.1; random ~25 (4-choice)
> **Relevance:** The competitive target is explicit: beat ~33 KazMMLU (Qwen3-0.6B) to claim SOTA among <=1B. This is a low, reachable bar for a Kazakh-dedicated 600M with Engram memory + English co-training, making the paper's headline claim defensible.
> **Source:** arXiv 2502.12829 (KazMMLU) leaderboard; user-measured baselines in grounding · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-turkic-nlp
> KazMMLU dataset composition (primary eval): 23,000 MCQs, Kazakh 10,969 (48%) / Russian 12,031 (52%), 4 options each. High-school subjects exist in BOTH languages; university/professional subjects (Law, Economics, Medicine) are Russian-ONLY. All models score higher on the Russian subset and higher when prompted in English. Frontier: DeepSeek-V3 76.9, GPT-4o 76.6, Gemma-2-27B 57.4, Llama-3.1-70B 56.2.
>
> **Numbers:** 23K Q (kk 10,969 / ru 12,031); professional=Russian-only; DeepSeek-V3 76.9, Llama-3.1-70B 56.2
> **Relevance:** Report the Kazakh-only subset separately — the Russian-heavy professional split inflates scores and rewards Russian ability, not Kazakh. A Kazakh-specialist 600M should be evaluated and marketed on the ~11K Kazakh questions; co-training Russian helps the ru subset 'for free'.
> **Source:** arXiv 2502.12829, ACL 2025.acl-long.701 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — inference-tts
> Evaluation targets and their TTS-friendliness: KazMMLU (Kazakhstan-specific, STEM+humanities MCQ) and TUMLU/TUMLU-mini (38,139 MCQs, 11 subjects, 8 Turkic languages incl. Kazakh, ACL 2025). Both are multiple-choice with verifiable answers.
>
> **Numbers:** TUMLU: 38,139 MCQs, 11 subjects, 8 Turkic langs; KazMMLU Kazakhstan-specific
> **Relevance:** MCQ format means self-consistency and outcome-reward Best-of-N score answers for free (no PRM) — the cheapest way to demonstrate TTS gains for the arXiv paper on the exact benchmarks the project already uses.
> **Source:** arXiv:2502.12829 (KazMMLU); arXiv:2502.11020 (TUMLU) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[tumlu-a-unified-and-native-language-understanding-benchmark-for-turkic-languages]]

> [!note] CLAIM — win-bar-protocol-audit
> [tested-on-Kazakh] The KazMMLU paper's own main results (Table 4) are yet another protocol: zero-shot, ENGLISH-instruction prompts ('we focus on English-prompted results in the main body'), scored for open models by next-token probability over option letters A-E, averaged over the FULL kk+ru set (Llama-3.1-8B 39.7, Qwen-2.5-7B 42.5, Bloom-1.1B 22.1 = smallest model tested). Its few-shot experiments go only to 3-shot (1/2/3), consistent with the dev split holding exactly 3 exemplars — corroborating that the lab's 3-shot is the dataset's natural few-shot maximum, not an arbitrary choice.
>
> **Numbers:** 0-shot English prompts; letters A-E next-token; full 23K kk+ru; Llama-3.1-8B 39.7 vs Sherkala-protocol 38.3 vs lab protocol n/a; max published few-shot = 3
> **Relevance:** Three distinct published protocols now exist for 'KazMMLU accuracy'; the lab's letter-logit scoring matches the KazMMLU paper's open-model method, while its Kazakh-language 'Жауап:' prompt and kk-only subset are deliberately harder/native — every published table must state all axes.
> **Source:** arXiv:2502.12829 (HTML v2, Table 4, Figure 5, evaluation-setup section) · **Sweep:** `slm-arch-for-kazakh`

> [!warning] UNCERTAIN — win-bar-protocol-audit
> [tested-on-Kazakh] Shot count materially moves KazMMLU scores, so 0-shot and 3-shot numbers cannot be mixed: the KazMMLU paper reports the largest accuracy jump between 0-shot and 1-shot, with e.g. Qwen-2.5-7B-Instruct rising from 47.8% (0-shot) to 58.9% (3-shot) — an ~11pp swing, i.e. larger than the entire 32.8->36 target delta.
>
> **Numbers:** Qwen-2.5-7B-Instruct 47.8 (0-shot) -> 58.9 (3-shot), +11.1pp; 'largest jumps occur between 0-shot and 1-shot'
> **Relevance:** Directly quantifies why the 0-shot 41.4 ceiling vs the 3-shot >=36 target is an invalid comparison: the shot-count confound alone exceeds the planned win margin.
> **Source:** arXiv:2502.12829 (Figure 5, few-shot analysis; exact figures extracted via page summarizer, not read from the PDF table directly) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[sailor-open-language-models-for-south-east-asia|Sailor: Open Language Models for South-East Asia]] — Sailor's exam-flat result (M3Exam -0.05) at 0.5B directly threatens the exam-style KazMMLU target
- [[kazqad-kazakh-open-domain-question-answering-dataset|KazQAD: Kazakh Open-Domain Question Answering Dataset]] — The two Kazakh axes a joint ≤600M head must serve simultaneously — KazQAD (retrieval) and KazMMLU (generation)
- [[hf-qwen-qwen3-0-6b-config|HF Qwen/Qwen3-0.6B config]] — Paper's sub-1B analysis pins Qwen3-0.6B ~32.8 as best sub-1B KazMMLU — the lab's canonical baseline model
- [[qorgau-evaluating-llm-safety-in-kazakh-russian-bilingual-contexts|Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts]] — Companion MBZUAI Kazakh benchmarks: Qorgau measures safety, KazMMLU measures capability — two axes of the same eval suite
- [[training-free-tokenizer-transplantation-via-orthogonal-matching-pursuit|Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit]] — OMP's caveat — cross-scheme transplant collapses GSM8K -78.7% — directly threatens STEM-heavy KazMMLU numeric reasoning

[[Home]]
