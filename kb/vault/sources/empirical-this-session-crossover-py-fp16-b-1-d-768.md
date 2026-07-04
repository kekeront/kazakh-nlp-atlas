---
kb_id: "title:empirical crossover fp16 b 1 d 768"
type: "source"
title: "Empirical, this session: crossover.py (fp16, B=1, d=768)"
doi: null
hf_repo: null
year: null
topics: ["hardware-gate"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:empirical crossover fp16 b 1 d 768"]
tags: ["source", "topic/hardware-gate"]
---
# Empirical, this session: crossover.py (fp16, B=1, d=768)

**Topics:** [[hardware-gate]]

## Source URLs
- Empirical, this session: crossover.py (fp16, B=1, d=768)

## Findings

> [!note] CLAIM — hardware-gate
> THROUGHPUT INVERSION at training-relevant context lengths: on SM75 the classic linear-attention speed motivation is inverted. torch SDPA (softmax attention, fp16) is FASTER per layer than every linear kernel up to at least T=8192; KDA only breaks even around T~12-16K (extrapolated from linear-vs-quadratic trend). For a 10B-token CPT run at ctx 1024-4096, a KDA layer costs 2.7-4.8x an SDPA layer; fla-0.5.1 GatedDeltaNet and Mamba2 layers cost 28-47x SDPA (they appear to hit fallback/small-block Triton configs under the 64KB shared-memory limit). If a hybrid is specced for v2, KDA is currently the only fla linear kernel with acceptable SM75 throughput. Flag: transferable-untested.
>
> **Numbers:** fwd+bwd per layer — T=2048: KDA 13.5 ms vs SDPA 4.3 ms (3.1x); T=4096: 26.0 vs 12.6 ms (2.1x); T=8192: 51.3 vs 42.1 ms (1.2x); KDA throughput flat ~151-160K tok/s/layer (linear scaling confirmed), SDPA decays 480K->194K tok/s/layer
> **Relevance:** The panel should not adopt a hybrid for THROUGHPUT on T4x2 — only for quality (+4.2pp GDN-H1-class) or KV-cache reasons; and the 10B-token compute budget must price linear layers at 2-5x attention cost at our context lengths.
> **Source:** Empirical, this session: crossover.py (fp16, B=1, d=768) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[native-sparse-attention-hardware-aligned-and-natively-trainable-sparse-attention|Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention]] — NSA claims hardware-aligned attention; node shows fla linear kernels are hardware-MISaligned on SM75 (28-47x SDPA, 64KB fallback)
- [[nemotron-h-a-family-of-accurate-and-efficient-hybrid-mamba-transformer-models|Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models]] — Node gates hybrid design: Mamba2 costs 28-47x SDPA on SM75, so a Nemotron-H-style Mamba2-Transformer hybrid is T4-infeasible
- [[kimi-linear-an-expressive-efficient-attention-architecture|Kimi Linear: An Expressive, Efficient Attention Architecture]] — Refutes Kimi Linear's linear-attn speed premise on SM75: its KDA only beats SDPA at T~12-16K, far above CPT ctx 1024-4096

[[Home]]
