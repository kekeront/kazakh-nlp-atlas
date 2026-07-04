---
kb_id: "arxiv:2605.03229"
type: "paper"
title: "Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetuning"
arxiv_id: "2605.03229"
doi: null
hf_repo: null
year: 2026
topics: ["post-hoc-attachment-of-engram-style-cond"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetuning", "arXiv:2605.03229", "arxiv:2605.03229"]
tags: ["paper", "topic/post-hoc-attachment-of-engram-style-cond"]
---
# Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetuning

[arXiv](https://arxiv.org/abs/2605.03229)
**Topics:** [[post-hoc-attachment-of-engram-style-cond]]

> [!abstract]
> Adapting a pretrained language model to a new task often hurts the general capabilities it already had, a problem known as catastrophic forgetting. Sparse Memory Finetuning (SMF) tries to avoid this by adding key-value memory layers to the model and, on each training step, updating only the small set of memory rows that the current batch reads most heavily. We re-implement SMF on Qwen-2.5-0.5B-Ins …

## Claims

> [!note] CLAIM — post-hoc-attachment-of-engram-style-cond
> [transferable-untested] Post-hoc memory retrofit is validated at EXACTLY the lab's scale (Qwen2.5-0.5B-Instruct) and the integration mode is decisive: ADDITIVE attach (keep pretrained MLP, add alpha*mem with learnable scalar alpha initialized to 0.01) learns the target task with forgetting probes at-or-below base, while REPLACEMENT (discard MLP, insert memory) is Pareto-dominated. Product-key memory (PKM) at layers {6,12,18}, M=16,384 slots/layer, d=896, 4 query heads, top-k=16, key dim 256, ~52M memory params (~44M values); Stage-1 'dense retrofit' trains ONLY memory params, 2 epochs on 50,000 OpenAssistant responses, LR 5e-4, batch 16. Quote: 'Preserving the pretrained MLP path matters at this scale: replacement memory, which discards the MLP, lies off both Pareto frontiers.'
>
> **Numbers:** Base Qwen2.5-0.5B: MedMCQA 0.344+-0.002, WikiText PPL 13.146, TriviaQA 0.256. Additive sparse (KL): MedMCQA 0.369 (+2.5pp), PPL 12.723 (BELOW base), TriviaQA 0.252 (-0.4pp). Additive +S (KL): 0.378 (+3.4pp), PPL 13.139, TriviaQA 0.223. Replacement (KL/TF-IDF): MedMCQA 0.354/0.355 (+1.0-1.1pp only), PPL 16.5-16.6 (+26%), TriviaQA 0.179/0.207 (-5 to -8pp). LoRA r16: 0.390, PPL 15.470, TriviaQA 0.193; full FT: 0.398, PPL 18.907 (+44%), TriviaQA 0.163
> **Relevance:** Answers the gate-suppression fear at 0.5B: randomly-init memory attached to converged Qwen 0.5B is NOT ignored — it trains and helps — provided (a) it is added alongside, not instead of, pretrained paths and (b) its output enters through a near-zero learnable scalar. Gives the exact safe-attach recipe and layer/slot config for the QymyzLM kill-switch ablation.
> **Source:** arXiv:2605.03229v2 (Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetuning, ICML 2026 FoGen workshop, Jun 8 2026), Tables 1-3; code github.com/prakharg55/SMF-ICML-FG; PDF saved at /home/altairzhambyl/.claude/projects/-home-altairzhambyl-projects-SLMs-basic/98053e10-7c62-465c-acd3-b6c763138a63/tool-results/webfetch-1783151033937-k0irsd.pdf · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[lora-learns-less-and-forgets-less|LoRA Learns Less and Forgets Less]] — Both frame the learn-vs-forget tradeoff; SMF positions itself as low-forgetting alternative to LoRA AND full-FT
- [[continually-adding-new-languages-to-multilingual-language-models|Continually Adding New Languages to Multilingual Language Models]] — Both target low-forgetting language addition; LayRA = layer-selective LoRA vs sparse-memory finetuning — competing forgetting-mitigation…

[[Home]]
