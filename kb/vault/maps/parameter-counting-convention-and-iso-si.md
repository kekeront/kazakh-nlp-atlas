---
type: "moc"
topic: "parameter-counting-convention-and-iso-si"
nodes: 3
papers: 3
sources: 0
uncertain_claims: 4
tags: ["moc"]
---
# Topic: parameter-counting-convention-and-iso-si

The frontier here is a single load-bearing accounting question for QymyzLM: does a ~500M-active dense backbone plus a ~512M Engram lookup table belong to the ≤600M size class, or does the field re-bracket it as a ~1B-total model? The KB answer is CONFIRMED and cuts against the ≤600M framing: the sparse-model convention (Mixtral 8x7B = "47B/13B active"; DeepSeek-V3 = "the 671B model", 5.5% activation) size-classes by TOTAL params, crediting capacity to total and only compute to active. Engram's own Section 3.1 defines P_tot ⊇ the memory table and its headline is explicitly iso-TOTAL-param AND iso-FLOP (5.7B/568M-active, 9.9B/993M-active), so invoking Engram to beat a smaller-total model contradicts the source. All three Kazakh peers (Qwen3-0.6B 32.8%, SozKZ-600M ~30%, Gemma3-270M) are DENSE — total==active — so at ~1B total the honest peer bar rises to Llama-3.2-1B/Gemma3-1B/Qwen2.5-1.5B (34.3%), and "beats every 500M SLM" becomes a category error. Two axes stay separable: the model is genuinely competitive on the active/FLOP axis, but on the footprint axis (512M table ≈1GB fp16, offloaded to host/NVMe) it is 1.7–3.7x its named peers. The only flagged-uncertain thread is whether Engram's U-shaped ρ≈75–80% allocation law transfers to a dense backbone with P_sparse≈0, where adding the table is pure addition rather than reallocation.

## Frontier highlights
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Languag…]] — Engram Sec 3.1 defines P_tot ⊇ memory table; headline is iso-TOTAL-param AND iso-FLOP — no smaller-class claim
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — Dense Kazakh peers have total==active; at ~1B total the bar rises to Qwen2.5-1.5B 34.3%, re-bracketing the model
- [[mixtral-of-experts|Mixtral of Experts]] — MoE convention size-classes by TOTAL: Mixtral=47B(13B active), DeepSeek-V3=671B — capacity credited to total

## Papers (3)
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models]] (2026) — deepseek-tech
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[mixtral-of-experts|Mixtral of Experts]] (2024) — parameter-counting-convention-and-iso-si

## Related topics
- [[kazakh-turkic-nlp]] — 2 shared nodes
- [[novelty-check]] — 2 shared nodes

[[Home]]
