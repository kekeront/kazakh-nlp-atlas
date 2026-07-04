---
kb_id: "hf:qwen/qwen3-0.6b-base"
type: "source"
title: "huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-…"
doi: null
hf_repo: "Qwen/Qwen3-0.6B-Base"
year: null
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re", "qymyzlm-architecture-fork"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["hf:qwen/qwen3-0.6b-base"]
tags: ["source", "topic/continual-pt-lowres-qlora-vs-full-cpt-re", "topic/qymyzlm-architecture-fork"]
---
# huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-…

**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]], [[qymyzlm-architecture-fork]]

## Source URLs
- huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-04)
- param arithmetic re-derived here

## Findings

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> Qwen3-0.6B-Base verified config (HF config.json): vocab_size 151,936, hidden 1024, 28 layers, GQA 16 Q/8 KV heads, intermediate 3072, max_position 32,768, tie_word_embeddings=TRUE, torch_dtype bfloat16. Derived param math: single tied embedding table = 151,936×1024 = 155.58M params (~26% of 596M). Every +1K new vocab tokens = +1.05M params; a Sherkala-scale +31.5K expansion = +32.3M → ~628M, BREACHING the ≤600M active cap. Conversely, a tokenizer SWAP to a ~60K Kazakh-centric vocab frees ≈94M params (155.6M→61.4M) of budget headroom. Also: checkpoint ships bf16; T4 (no bf16) requires fp16 cast or fp32 master weights — loss-scale stability must be validated.
>
> **Numbers:** 151,936×1024=155.58M tied; +31,510 tokens=+32.27M; 60K-vocab swap saves ~94M; GQA 16/8; ctx 32,768
> **Relevance:** Hard design constraint: vocab expansion trades directly against the 600M active budget; tokenizer replacement is the only path that hits fertility <2.0 AND gains param headroom (e.g., for Engram tables).
> **Source:** huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-04); param arithmetic re-derived here · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — qymyzlm-architecture-fork
> [re-derived parameter math, ground truth for the panel] Qwen3-0.6B-Base config verified from HF: vocab 151,936, hidden 1024, 28 layers, GQA 16Q/8KV, intermediate 3072, tie_word_embeddings=true. Tied table = 151,936x1024 = 155.58M (26.1% of ~596M). Full swap to 60K Kazakh vocab: table 61.44M, total ~502M -> frees ~94.1M for Engram under the 600M ACTIVE cap; fp16 optimizer/embedding memory on T4x2 also drops ~188MB (fp16 weights) + optimizer states. Sherkala-style expansion +31.5K: table 187.8M, total ~628M — breaks cap. VRCP iso-replacement: 155.58M unchanged, total 596M — cap kept, nothing freed.
>
> **Numbers:** 151,936x1024=155,582,464; 60,000x1024=61,440,000; delta=94,142,464; expansion 183,436x1024=187.8M (+32.2M over cap-relevant baseline)
> **Relevance:** Only the full-swap path simultaneously satisfies fertility <2.0, <=600M active, and the ~94M Engram allowance; expansion and untying are arithmetically excluded, independent of any quality argument.
> **Source:** huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] — Lab's GQA-8x128 baseline; 2505 shows GQA-4 approx MLA at sub-1B, motivating MLA over Qwen3-0.6B's GQA-8
- [[defeating-the-training-inference-mismatch-via-fp16|Defeating the Training-Inference Mismatch via FP16]] — the untested fp16-CPT stability claim is precisely about this bf16-native checkpoint the lab plans to adapt
- [[huggingface-co-datasets-mbzuai-kazmmlu-dataset-inspection|huggingface.co/datasets/MBZUAI/KazMMLU (dataset inspection 2026-07-03)]] — Qwen3-0.6B-Base is the model scored 32.8% on this benchmark — the canonical generative target to beat
- [[cfgs-qwen3-0-6b-4gpu-yml-src-mha2mla-patching-model-load-py|cfgs/Qwen3-0_6B-4GPU.yml + src/mha2mla/patching_model_load.py (from-sc…]] — MHA2MLA from-scratch config re-inits attention on the Qwen3-0.6B-Base body, the lab's canonical target
- [[huggingface-smol-training-playbook-via-crawl-gist-github|HuggingFace Smol Training Playbook (via crawl: gist.github.com/uncleco…]] — Evidence that production sub-1B MLA adoption is zero: Qwen3-0.6B is a shipped GQA model, no MLA arm

[[Home]]
