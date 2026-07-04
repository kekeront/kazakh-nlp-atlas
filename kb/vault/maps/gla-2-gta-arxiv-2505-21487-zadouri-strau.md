---
type: "moc"
topic: "gla-2-gta-arxiv-2505-21487-zadouri-strau"
nodes: 7
papers: 2
sources: 5
uncertain_claims: 1
tags: ["moc"]
---
# Topic: gla-2-gta-arxiv-2505-21487-zadouri-strau

arXiv:2505.21487 (Tri Dao group) is a from-scratch head-to-head on FineWeb-Edu where GLA-2 (2 latent heads, d_c=2·d_h, RoPE 32) and GTA-4 (tied KV) beat BOTH MLA and GQA-4 at sub-1B: at 876M GLA-2 hits 11.293 ppl/57.5% and GTA-4 11.232/57.6% with ~half GQA-4 cache, while MLA≈GQA parity holds (876M: 11.363 vs 11.340). Two facts hollow this out for the lab. First, the sole independent from-scratch reproduction (MLRA, arXiv:2603.02188, 2.9B/98.3B tok) FLIPS the ordering — MLA beats GLA-2 on both ppl (13.727 vs 13.779) and 0-shot avg (58.75 vs 58.30) — and everything on both sides is single-seed with no error bars, so the seed-noise floor is unmeasured and no independent sub-1B replication exists. Second, GLA-2's cache advantage over MLA is per-device only at TP≥2; for the lab's single-GPU ≤600M regime (TP=1) it collapses to plain MLA's cache with none of the benefit. Adoption is zero (vLLM/llama.cpp/TRT-LLM/SGLang/HF all 0 hits) and the only kernels live in FA3-Hopper (H100+CUDA 12.3, still-open regression #2372) — unrunnable on the canonical Kaggle T4. Open question: does the GLA-2/GTA win survive a multi-seed, sub-1B independent rerun, and is it worth adopting given no TP=1 benefit and no serving path? Current evidence says fall back to plain MLA.

## Frontier highlights
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] — Primary result: GLA-2/GTA-4 beat MLA and GQA-4 at 876M with MLA-class cache and better TP sharding
- [[arxiv-org-html-2603-02188-tables-3-4-vs-arxiv-org-html-2505|arxiv.org/html/2603.02188 (Tables 3-4) vs arxiv.org/html/2505.21487v1]] — Sole independent reproduction FLIPS ordering — MLA>GLA-2 at 2.9B, contradicting every-scale win
- [[arxiv-org-html-2505-21487v1-gla-2-config-h-c-2-d-c-2-d-h|arxiv.org/html/2505.21487v1 (GLA-2 config: h_c=2, d_c=2*d_h per latent…]] — GLA-2 cache win is per-device at TP>=2 only; at lab's single-GPU <=600M it equals plain MLA
- [[github-search-api-over-vllm-project-vllm-ggml-org-llama-cpp|GitHub search API over vllm-project/vllm, ggml-org/llama.cpp, NVIDIA/T…]] — Zero adoption: vLLM/llama.cpp/TRT-LLM/SGLang/HF all 0; official repo 0 downstream reuse
- [[arxiv-org-html-2505-21487v1-arxiv-org-html-2603-02188-both|arxiv.org/html/2505.21487v1 + arxiv.org/html/2603.02188 (both silent o…]] — All runs single-seed, no error bars; seed-noise floor for these variants unmeasured
- [[github-com-dao-ailab-flash-attention-issues-2372|github.com/Dao-AILab/flash-attention/issues/2372]] — Only kernels are FA3-Hopper H100-only with an open v3.0.0 regression — unrunnable on T4

## Papers (2)
- [[multi-head-low-rank-attention|Multi-Head Low-Rank Attention]] (2026) — gla-2-gta-arxiv-2505-21487-zadouri-strau
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] (2025) — mla-sub1b

## Sources & findings (5)
- [[github-search-api-over-vllm-project-vllm-ggml-org-llama-cpp|GitHub search API over vllm-project/vllm, ggml-org/llama.cpp, NVIDIA/T…]] — Zero adoption in any serving stack or released model as of 2026-07-03: vLLM has 0 code hits for grouped_latent/GroupedLa…
- [[arxiv-org-html-2505-21487v1-arxiv-org-html-2603-02188-both|arxiv.org/html/2505.21487v1 + arxiv.org/html/2603.02188 (both silent o…]] — No multi-seed run of any GLA-2/GTA/MLA/GQA comparison exists in either the original paper or the sole reproduction; the…
- [[arxiv-org-html-2505-21487v1-gla-2-config-h-c-2-d-c-2-d-h|arxiv.org/html/2505.21487v1 (GLA-2 config: h_c=2, d_c=2*d_h per latent…]] — GLA-2's cache advantage over MLA exists only per-device under tensor parallelism (TP>=2): total unsharded cache is the s…
- [[arxiv-org-html-2603-02188-tables-3-4-vs-arxiv-org-html-2505|arxiv.org/html/2603.02188 (Tables 3-4) vs arxiv.org/html/2505.21487v1]] — Exactly ONE independent from-scratch reproduction of GLA-2/GLA-4/GTA exists: the MLRA paper (Liu et al., Penn State/UCon…
- [[github-com-dao-ailab-flash-attention-issues-2372|github.com/Dao-AILab/flash-attention/issues/2372]] — The only GLA kernels live in FlashAttention-3 hopper (same lab, not independent), require H100 + CUDA 12.3+, and the too…

[[Home]]
