---
kb_id: "arxiv:2601.07372"
type: "paper"
title: "Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models"
arxiv_id: "2601.07372"
doi: null
hf_repo: null
year: 2026
topics: ["deepseek-tech", "kazakh-turkic-nlp", "novelty-check", "does-the-engram-conditional-memory-modul", "parameter-counting-convention-and-iso-si", "novelty-check-has-any-2026-preprint-impl", "post-hoc-attachment-of-engram-style-cond"]
claims: 18
uncertain_claims: 2
verdicts: []
aliases: ["Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models", "arXiv:2601.07372", "arxiv:2601.07372"]
tags: ["paper", "topic/deepseek-tech", "topic/kazakh-turkic-nlp", "topic/novelty-check", "topic/does-the-engram-conditional-memory-modul", "topic/parameter-counting-convention-and-iso-si", "topic/novelty-check-has-any-2026-preprint-impl", "topic/post-hoc-attachment-of-engram-style-cond"]
---
# Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models

[arXiv](https://arxiv.org/abs/2601.07372)
**Topics:** [[deepseek-tech]], [[kazakh-turkic-nlp]], [[novelty-check]], [[does-the-engram-conditional-memory-modul]], [[parameter-counting-convention-and-iso-si]], [[novelty-check-has-any-2026-preprint-impl]], [[post-hoc-attachment-of-engram-style-cond]]

> [!abstract]
> While Mixture-of-Experts (MoE) scales capacity via conditional computation, Transformers lack a native primitive for knowledge lookup, forcing them to inefficiently simulate retrieval through computation. To address this, we introduce conditional memory as a complementary sparsity axis, instantiated via Engram, a module that modernizes classic $N$-gram embedding for O(1) lookup. By formulating the …

## Claims

> [!note] CLAIM — deepseek-tech
> Engram (arXiv 2601.07372) config: max n-gram order 3, instantiated with n-grams {2,3}; memory embedding dim d_mem=1280; K=8 independent hash heads per n-gram order; prime-sized buckets addressed by multiplicative-XOR hashing; retrieved embeddings are gated by the hidden state then passed through a depthwise Conv1D. In the two flagship models Engram sits at exactly two layers: layers 2 and 15.
>
> **Numbers:** n-grams {2,3}; d_mem=1280; K=8 hash heads; layers {2,15}; vocab/slots 2,262,400 (27B) and 7,239,680 (40B)
> **Relevance:** This is the exact spec the user's KazLLM-v2 borrows. Confirms {2,3}-gram choice and gives a concrete d_mem (1280) and K=8 hashing scheme to drop into the Kazakh design instead of guessing.
> **Source:** arXiv:2601.07372 (Conditional Memory via Scalable Lookup), HTML v1 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — deepseek-tech
> The MOST scale-relevant Engram experiment: a 3B-total MoE backbone with only 568M ACTIVE params, 12 layers, with a 1.6B-param Engram memory ({2,3}-grams). Pure MoE baseline validation loss 1.808; single Engram at layer 2 = 1.770; splitting the same 1.6B memory into TWO modules at layers 2 and 6 = 1.768 (best). So the paper's own small ablation used layers {2,6}, not {2,L/4}.
>
> **Numbers:** 568M active, 12 layers, 1.6B Engram; val loss 1.808 (MoE) -> 1.770 (L2) -> 1.768 (L2+L6); delta -0.040 nats
> **Relevance:** Directly validates the user's plan at ~568M active. Recommends layer placement {2,6} for a 12-layer net and confirms two smaller split modules beat one big module. But note: backbone was MoE, not dense Llama.
> **Source:** arXiv:2601.07372, Section 6.2 / Figure 5 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — deepseek-tech
> Engram benchmark deltas vs an ISO-parameter, ISO-FLOP MoE-27B baseline (both 26.7B total / 3.8B active; Engram trades 17 routed experts, 72->55, for 5.7B memory params): MMLU +3.0, CMMLU +4.0, BBH +5.0, ARC-Challenge +3.7, DROP +3.3, HumanEval +3.0, MATH +2.4, GSM8K +2.2; multi-query NIAH 84.2 -> 97.0. Gains are LARGER on reasoning/code (BBH +5.0) than on pure knowledge (MMLU +3.0). (Abstract quotes MMLU +3.4; the detailed table says +3.0.)
>
> **Numbers:** MMLU +3.0, CMMLU +4.0, BBH +5.0, ARC +3.7, HumanEval +3.0, MATH +2.4, GSM8K +2.2, NIAH 84.2->97.0
> **Relevance:** Quantifies expected upside. The reasoning-heavy gains matter because KazMMLU is knowledge-heavy; a +3 to +4 MMLU-class lift is the plausible ceiling of the Engram contribution, and it comes at 0 added FLOPs.
> **Source:** arXiv:2601.07372, main results table · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — deepseek-tech
> Engram mechanism equations: per-slot gating scalar alpha_t = sigmoid( RMSNorm(h_t)^T RMSNorm(k_t) / sqrt(d) ) modulates retrieved value; then Y = SiLU(Conv1D(RMSNorm(V_tilde))) + V_tilde, with depthwise Conv1D kernel width w=4 and dilation = max n-gram order, SiLU activation and a residual. Lookups are O(1): a constant number of slots retrieved per token, so growing the table raises total params with ZERO extra per-token FLOPs.
>
> **Numbers:** conv kernel w=4, dilation=3 (max n-gram), gating via RMSNorm dot-product/sqrt(d); 0 extra FLOPs
> **Relevance:** Exact math needed to reimplement Engram correctly for Kazakh (the conv+gating is what makes it beat a raw hash-embedding table like OverEncoding). The 0-FLOP property is the whole reason it fits a $264 single-GPU budget.
> **Source:** arXiv:2601.07372, method section · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — deepseek-tech
> Engram memory-scaling is a clean power law: on the fixed 568M-active backbone, validation loss improves log-linearly as embedding slots grow from 2.58e5 to 1.0e7. Optimal compute allocation is a U-shape peaking at rho ~= 75-80% of the sparse budget on MoE (i.e. reallocate ~20-25% of sparse params to Engram); at a 6e20-FLOP budget (9.9B total, 993M active) val loss improves 1.7248 (pure MoE, rho=100%) -> 1.7109 near rho~=80%.
>
> **Numbers:** slots 2.58e5->1.0e7 log-linear; optimal rho 75-80%; 1.7248->1.7109 (delta 0.0139) at 9.9B total
> **Relevance:** Tells the user how big to make the Kazakh hash tables (bigger monotonically helps, budget-permitting) and that ~20-25% of any sparse budget is the sweet spot for memory vs compute. Their ~512M memory is on the small side of the validated 2.58e5-1e7 slot range.
> **Source:** arXiv:2601.07372, Sections 3.1-3.2 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — deepseek-tech
> Param-accounting caveat: every published Engram result is on an MoE backbone (3.8B or 993M or 568M ACTIVE), never a dense model, and Engram's memory (5.7B in the 27B) is counted OUTSIDE the active/FLOP budget. If the Kazakh peer group (Qwen3-0.6B, SozKZ-600M, Gemma3-270M) is measured by TOTAL params, a 500M dense backbone + ~512M Engram table = ~1B total params, which is outside the <=600M size class even though FLOPs stay at 500M.
>
> **Numbers:** 500M dense + 512M Engram = ~1.0B total params vs <=600M claimed class
> **Relevance:** A fairness/framing risk for the arXiv paper: reviewers will flag that beating 500M dense models with a 1B-total (memory-augmented) model is not iso-size. Either report active-params honestly and argue the 0-FLOP axis, or shrink the table to stay <=600M total.
> **Source:** arXiv:2601.07372 (param tables) vs project grounding · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-turkic-nlp
> Engram (the user's conditional-memory choice) is verified real and validated at scale: suffix N-grams of canonicalized tokens hashed via K multiplicative-XOR heads into prime-sized embedding tables, O(1) lookup, ~0 extra FLOPs, deterministic addressing enables host-memory prefetch. Scaled to 27B, it BEATS a strictly iso-parameter and iso-FLOP MoE baseline (gains in knowledge retrieval, reasoning, code/math). Introduces a U-shaped 'Sparsity Allocation' scaling law trading neural compute (MoE) vs static memory (Engram).
>
> **Numbers:** 27B scale, beats iso-param/iso-FLOP MoE; K multiplicative-XOR hash heads; prime-sized tables; O(1)
> **Relevance:** Strong support for keeping Engram as the differentiator vs from-scratch SozKZ. The U-shaped scaling law is the concrete tuning knob: at 600M, size the n-gram hash tables against neural params along that curve rather than fixing ~512M sparse params arbitrarily. Knowledge-retrieval gains map directly to KazMMLU.
> **Source:** arXiv 2601.07372 (Conditional Memory via Scalable Lookup / Engram) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — novelty-check
> NO published work does MORPHEME-conditioned n-gram/lookup memory in a modern decoder LM. All 2026 memory-augmented LMs (Engram, X-gram, Memory Layers, UltraMemV2, MolGram) key their lookup on TOKEN or BYTE n-grams / frequency, never on morphological units (stem+suffix). Classic morpheme n-gram LMs exist only in pre-neural ASR (e.g., Uyghur morpheme LMs, syllable-level agglutinative LM). This is the cleanest genuine novelty gap for the paper.
>
> **Numbers:** Prior morpheme-LM art is pre-2020 and non-neural: arXiv:2003.01509 (Uyghur morpheme ASR LM), arXiv:1708.05515 (syllable-level neural LM)
> **Relevance:** This is the recommended core novelty: key the Engram lookup on Kazakh morpheme n-grams (stem, case/possessive/person suffix sequences) rather than SentencePiece token n-grams. It is defensible as first-of-kind and is intrinsically motivated by agglutination + vowel harmony (suffix allomorph sharing).
> **Source:** Synthesis of arXiv:2601.07372, 2604.21724, 2412.09764, 2606.12113 (all token/byte-keyed) + arXiv:2003.01509, 1708.05515 (pre-neural morpheme LMs) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — does-the-engram-conditional-memory-modul
> The original Engram paper contains ZERO dense+Engram configuration. Dense-4B (4.1B total / 3.8B active) appears ONLY as a no-Engram baseline (MMLU 48.6, TriviaQA 33.0). Every Engram-ATTACHED model is MoE: Engram-27B and Engram-40B (both 3.8B active, MoE+Engram), plus the compute-matched allocation regimes with 568M active (P_tot≈5.7B, 2e20 FLOPs) and 993M active (P_tot≈9.9B, 6e20 FLOPs) — all MoE. The ρ-allocation framework (ρ = fraction of inactive-parameter budget to MoE experts) structurally requires routed experts; ρ=0 (pure dense+Engram) is never tested.
>
> **Numbers:** Dense-4B baseline (no Engram): MMLU 48.6, CMMLU 47.9, BBH 42.8, ARC-C 59.3, HumanEval 26.8, MATH 15.2, TriviaQA 33.0. Min active in any Engram config: 568M (MoE)
> **Relevance:** Confirms the premise: no dense sub-1B (or any dense) Engram datapoint exists. The user's 600M dense design extrapolates entirely off the validated axis; the module is architecturally framed as a complement to MoE routing, not a dense-model booster.
> **Source:** arXiv 2601.07372 — Conditional Memory via Scalable Lookup, Table 1 + §3.1 (sparsity allocation) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — does-the-engram-conditional-memory-modul
> The optimal sparsity allocation keeps the MAJORITY of inactive budget in MoE experts, not in Engram: the U-shaped law's optimum sits at ρ≈75-80% (fraction to MoE experts), i.e. Engram is deliberately the minority axis complementing MoE. Engram is introduced as 'Conditional Memory, a complement to Conditional Computation in MoE.'
>
> **Numbers:** optimal ρ≈75-80% of inactive budget to MoE experts; Engram gets the remaining ~20-25%
> **Relevance:** The design's own scaling law is defined relative to a routed-expert budget. In a pure dense 600M model there is no MoE expert axis to trade against, so the U-shaped optimum and its benefit are undefined — the gain is entangled with MoE by construction, not merely by which scales were tested.
> **Source:** arXiv 2601.07372 — Conditional Memory via Scalable Lookup, §3 (Sparsity Allocation / U-shaped law) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — does-the-engram-conditional-memory-modul
> The 'Engram is the primary carrier of factual knowledge' evidence (suppressing Engram collapses TriviaQA to ~29%, 29-44% across factual benchmarks) is a post-hoc inference-time suppression on the full Engram-27B MoE model — NOT a small/dense result. It shows Engram is load-bearing when it already works at 27B MoE; it says nothing about whether it forms useful knowledge memory at 600M dense. Combined with the 1B underperformance datapoint, the load-bearing role at scale does not transfer down.
>
> **Numbers:** TriviaQA retains 29% of original; factual benchmarks retain 29-44%; measured on Engram-27B (26.7B total / 3.8B active MoE, 5.7B Engram embedding, 2,262,400 slots)
> **Relevance:** Prevents mis-citing the suppression ablation as evidence Engram will carry Kazakh facts at 600M. The knowledge-carrying property is demonstrated only where the module already has a multi-million-slot table and MoE support at 27B.
> **Source:** arXiv 2601.07372 — Conditional Memory via Scalable Lookup, §6.3 (Engram suppression ablation) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — does-the-engram-conditional-memory-modul
> The smallest Engram-ATTACHED reference config in the original paper is a 12-layer 3B MoE with 0.56B active + a 1.6B Engram table, N={2,3}, Engram inserted at layers 2 and 6 — this is the config the user's design mirrors (Engram at layers {2, L/4}), and it is MoE, not dense. The full-scale instantiation uses N up to 3, 8 hash heads, d_mem=1280, and 2.26M-7.24M slots — far larger tables than a 600M dense model could afford at the user's ~512M sparse-param budget.
>
> **Numbers:** Reference ablation: 3B MoE, 0.56B active, +1.6B Engram, N={2,3}, layers 2 & 6, 8 heads, d_mem=1280. 27B table: 2,262,400 slots; 40B table: 7,239,680 slots
> **Relevance:** The layer-placement recipe the user copied comes from an MoE config. Table size is a first-order driver of the collision problem; a 600M dense budget forces a much smaller table, pushing collisions higher — exactly the failure mode blamed for the 1B underperformance, and worse for agglutinative Kazakh's huge surface-form inventory.
> **Source:** arXiv 2601.07372 — Conditional Memory via Scalable Lookup, §4.1 / Appendix A · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — parameter-counting-convention-and-iso-si
> The Engram paper defines THREE parameter metrics and explicitly counts the memory table as part of TOTAL params. Section 3.1: P_tot = total trainable params (excluding only vocab embedding & LM head); P_act = activated params per token (this alone determines FLOPs); P_sparse = P_tot - P_act = the 'inactive/free budget'. The Engram table lives in P_sparse: 'For Engram, only a constant number of slots are retrieved per token, so scaling the number of embedding slots increases P_tot without increasing per-token FLOPs.' So a ~512M Engram table adds ~0 FLOPs but is fully counted in P_tot. There is NO convention in the source paper under which the table is not a parameter — even its generous P_tot (which drops vocab) still includes the whole table.
>
> **Numbers:** 3 metrics: P_tot, P_act, P_sparse=P_tot-P_act. User model under P_tot (excl vocab) ~= 450M backbone + 512M table = ~960M; on-disk total incl. embedding ~= 1.0B; P_act ~= 500M.
> **Relevance:** The only convention that yields '<=600M' is P_act (active/FLOP). Under total params — the metric reviewers use to size-class SLMs, and the metric the Engram paper itself headlines — the model is ~1B, not 500M.
> **Source:** arXiv 2601.07372 (Cheng et al., DeepSeek-AI, Jan 2026), Sec 3.1 'Compute-matched formulation' · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — parameter-counting-convention-and-iso-si
> Engram's OWN headline comparison is iso-TOTAL-parameter AND iso-FLOP simultaneously — it never claims a memory-augmented model beats a model with fewer TOTAL params. Abstract: 'we scale Engram to 27B parameters, achieving superior performance over a strictly iso-parameter and iso-FLOPs MoE baseline.' Sec 3.1 protocol keeps BOTH P_tot and P_act fixed: at C=2e20 FLOPs P_tot~=5.7B & P_act=568M (baseline 106 experts); at C=6e20 FLOPs P_tot~=9.9B & P_act=993M (baseline 99 experts), constant P_tot/P_act~=10. Therefore invoking Engram to justify 'beats 500M with a 1B-total model' contradicts the source: Engram's framing would require comparing the user's ~1B-total model against a ~1B-total baseline.
>
> **Numbers:** iso-P_tot: 5.7B (568M active) and 9.9B (993M active); MoE baselines with same total AND same FLOPs; sparsity ratio P_tot/P_act ~= 10.
> **Relevance:** The paper cannot lean on Engram precedent to escape iso-total comparison — DeepSeek explicitly does iso-total. deepseek-tech's objection is correct and is baked into the very paper being cited.
> **Source:** arXiv 2601.07372, Abstract + Sec 3.1 'Experimental protocol' · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — parameter-counting-convention-and-iso-si
> Engram's 0-FLOP argument addresses COMPUTE only, not memory footprint — and SLM reviewers weight footprint heavily. The Engram table is real stored weights so large the paper OFFLOADS it off-GPU: Sec 2.5 / abstract, 'offloading a 100B-parameter table to host memory incurs negligible overhead (<3%)', with a multi-level cache hierarchy (GPU HBM -> host DRAM -> NVMe SSD). For an on-device Kazakh SLM this is decisive: a 512M table at fp16 is ~1GB, at INT8 ~0.5GB of extra storage the device must hold. By contrast Gemma3-270M's entire pitch is footprint — INT4 QAT ~125-240MB, 'runs on your phone', 0.75% battery for 25 conversations on a Pixel 9 Pro. So on the memory axis the user model is not remotely in the 270-600M class regardless of the FLOP story.
>
> **Numbers:** Engram tables offloaded to host/NVMe (<3% overhead for a 100B table); 512M table ~1GB fp16 / ~0.5GB int8; Gemma3-270M INT4 ~125MB, full-precision ~0.5GB.
> **Relevance:** If the paper's selling point is 'efficient on-device Kazakh SLM', the total/footprint axis is the one reviewers weigh most, and the 0-FLOP defense does not answer it. Must report the table's on-disk bytes at train + quantized precision.
> **Source:** arXiv 2601.07372 Sec 2.5 + Abstract; Google Developers Blog + localaimaster.com/models/gemma-3-270m · **Sweep:** `slm-architecture-2026-07`

> [!warning] UNCERTAIN — parameter-counting-convention-and-iso-si
> Engram's own U-shaped scaling law both (a) shows the user's ~512M table is NOT oversized on the efficiency axis, and (b) shows the user is OUTSIDE the regime the law validates. Optimum is rho ~= 75-80% (val loss 1.7248 at pure MoE -> 1.7109 at rho~=80%, delta 0.0139), i.e. reallocate ~20-25% of the SPARSE budget to Engram. In the 10B regime that optimum is Engram ~= (1-0.80) x P_sparse ~= 0.2 x (9.9B-993M) ~= 1.03B of memory on 993M active — a ~1:1-to-1.8:1 memory:active ratio. The user's ~512M table on ~500M active (~1:1) is thus in-range for capability. BUT the law is derived on an MoE backbone with a large P_sparse to reallocate; a DENSE 500M backbone has P_sparse ~= 0, so adding Engram is pure ADDITION to total, not a reallocation — the user is applying the ratio outside its validated setting.
>
> **Numbers:** Optimum rho~=75-80%; delta val-loss 0.0139 (10B regime); Engram-optimal memory ~1.03B on 993M active (~1:1); user 512M on ~500M active (~1:1) is in-range for efficiency but adds to a dense (P_sparse~=0) backbone.
> **Relevance:** Tells the sizing decision: the table is fine for capability-per-FLOP, so the ONLY reason to shrink it is the total-param/footprint claim. To be honestly <=600M TOTAL, a ~440M backbone leaves only ~100-160M for the table (a ~3-5x shrink), or shrink the backbone to ~350-400M and give ~150-200M to Engram.
> **Source:** arXiv 2601.07372 Sec 3.1-3.2, Fig 3 (derived arithmetic on their reported P_tot/P_act) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — novelty-check-has-any-2026-preprint-impl
> As of submission (July 2026) NO preprint keys conditional memory by morphological units. A terminology trap exists: every Engram-lineage paper says 'suffix n-gram', but 'suffix' means the trailing TOKEN IDs of the context sequence (last-k tokens, exact longest-match), NOT linguistic morphological suffixes. This is confirmed verbatim in Engram, Memory Grafting ('suffix n-grams ending at x_{b,t}', token-ID tuples), X-gram, and Tensorizing Engram ('suffix n-grams ending at the current token via token indices'). The morpheme-keyed contribution therefore remains genuinely unoccupied, but the naming collision is a reviewer landmine.
>
> **Numbers:** Engram arXiv 2601.07372; Memory Grafting 2605.20948; X-gram 2604.21724; Tensorizing Engram 2606.08347 — all use sequence-suffix token-ID keys, zero morphological segmentation
> **Relevance:** The paper's crux ('morpheme-keyed') survives, but the abstract/intro MUST explicitly disambiguate 'morphological-suffix keys' from the field's existing 'sequence-suffix n-grams' or reviewers will read the contribution as already-done.
> **Source:** arXiv 2601.07372 (Engram / Conditional Memory via Scalable Lookup); 2605.20948 (Memory Grafting); 2606.08347 (Tensorizing Engram) · **Sweep:** `slm-architecture-2026-07`

> [!warning] UNCERTAIN — post-hoc-attachment-of-engram-style-cond
> [transferable-untested] Gate math predicts the raw Engram attach is noisy but trainable: the Engram/Memory-Grafting gate alpha = sigmoid(<RMSNorm(K),RMSNorm(Q)>/sqrt(d)) is NOT zero at init — with random keys the pre-sigmoid argument is approximately zero-mean O(1), so alpha ~= 0.5 in expectation, injecting half-gated random values into the converged residual stream (consistent with the observed perplexity degradation in finding 3). Memory Grafting's Fig. 5 ablation shows the gate is essential when trained from scratch, but NO paper studies gate dynamics of a random memory over a converged backbone. Two published-adjacent safe-attach mechanisms: (a) additive learnable scalar alpha=0.01 validated at 0.5B (finding 2); (b) zero-initializing the Engram VALUE table makes the module output exactly 0 through Y=SiLU(Conv1D(RMSNorm(V~)))+V~ while value gradients remain nonzero — same principle as ControlNet zero-conv / LLaMA-Adapter zero-init attention, but never tested on Engram.
>
> **Numbers:** Expected init gate alpha ~= 0.5 (sigmoid of ~N(0, O(1))); validated attach scalar alpha_init = 0.01 at 0.5B; zero-init value table => exact 0 output at attach
> **Relevance:** Gives the two concrete init choices to A/B in the kill-switch ablation and the metric to log (mean gate alpha per layer, slot-usage entropy) as the 'suppression' detector — cheap to instrument on T4x2 fp16.
> **Source:** Derivation from Engram arXiv:2601.07372 gate equation + Memory Grafting arXiv:2605.20948 Fig. 5 + arXiv:2605.03229 additive-scalar result; zero-init lineage LLaMA-Adapter arXiv:2303.16199, ControlNet arXiv:2302.05543 · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[memory-grafting-scaling-language-model-pre-training-via-offline-conditional]], [[sparse-memory-finetuning-as-a-low-forgetting-alternative-to-lora-and-full]]

## Related
- [[physics-of-language-models-part-4-1-architecture-design-and-the-magic-of-canon|Physics of Language Models: Part 4.1, Architecture Design and the Magic of Canon Layers]] — Canon depthwise Conv1D functionally overlaps Engram's built-in Conv1D — competing local-mixing, not complementary
- [[ultramemv2-memory-networks-scaling-to-120b-parameters-with-superior-long|UltraMemV2: Memory Networks Scaling to 120B Parameters with Superior Long-Context Learning]] — Both scale static memory tables to huge param counts; UltraMemV2 is an alternate memory-network architecture reaching 120B
- [[a-collision-free-hot-tier-extension-for-engram-style-conditional-memory-a|A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Stud…]] — Direct Engram extension: collision-free hot-tier fixes the multiplicative-XOR hash collisions of this base design
- [[memory-grafting-scaling-language-model-pre-training-via-offline-conditional|Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory]] — Memory Grafting is Engram-lineage; slice cites its identical suffix-n-gram gate α=sigmoid(<RMSNorm K,Q>/√d)
- [[ggml-org-llama-cpp-howto-add-model-md-discussion-16770|ggml-org/llama.cpp HOWTO-add-model.md + Discussion #16770]] — Deployment tax: Engram conditional-lookup memory needs a full custom llm_arch + gguf-py C++ integration, not a drop-in

[[Home]]
