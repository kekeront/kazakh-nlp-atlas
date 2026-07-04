---
type: "moc"
topic: "kaggle-t4x2-compute-vram-budget-for-the"
nodes: 8
papers: 1
sources: 7
uncertain_claims: 2
tags: ["moc"]
---
# Topic: kaggle-t4x2-compute-vram-budget-for-the

The lab has empirically pinned the Kaggle-free-tier CPT envelope for Qwen3-0.6B-Base (596M params) on T4x2 (2x16GB, sm_75, no NVLink), and the load-bearing verdict is that VRAM is NOT the binding constraint — throughput and quota are. Measured fwd+bwd peak is only 2.73 GiB at 4K ctx; full-FT totals ~12.3GB (fp32 Adam) or ~7GB (8-bit Adam), so ZeRO/FSDP is unnecessary, plain DDP is preferred, and QLoRA has no memory rationale at this scale (NF4 saves <0.9GB while blocking full-param gains). The hard wall is tokens/wall-time: measured 1,584–2,049 tok/s/GPU (~15–20% MFU) → ~0.31–0.53B tokens/week under the ~30h/week (T4x2 counts 1x → effective ~60 GPU-h) quota, making the literature-recommended 20–25B-token CPT dead on arrival (38–81 weeks); the feasible 12-week campaign is ~3.8–6.4B tokens-seen. Two engineering landmines are confirmed: sm_75 has NO FlashAttention and the mem-efficient SDPA kernel rejects Qwen3's 16-vs-8 GQA head mismatch, silently falling to the O(s²) MATH backend (reproduced OOM) unless a repeat_kv patch expands KV heads; and fp16 CPT of the bf16-native checkpoint is the one UNCERTAIN item — no published success/failure exists, with adjacent evidence pointing both ways (Qwen fp16 NaN reports vs arXiv:2510.26788 arguing bf16 rounding, not fp16 range, is the real instability). Open questions: whether fp16 CPT is stable at lr~1e-4 on this checkpoint, and whether 2048-ctx + late-4K-annealing (to reclaim ~23% throughput) holds for Kazakh long-context.

## Frontier highlights
- [[derived-from-lab-measurement-t4bench2-py-t4bench3-py-kaggle|Derived from lab measurement (t4bench2.py/t4bench3.py) + Kaggle quota…]] — Verdict: 20-25B-token CPT is DOA on Kaggle (38-81 wk); feasible envelope ~3.8-6.4B tok / 12-wk campaign
- [[lab-measurement-peak-vram-standard-adam-state-arithmetic-2|Lab measurement (peak VRAM) + standard Adam state arithmetic (2+2+4+4+…]] — VRAM not binding: full-FT fits one 16GB T4 (~12.3GB/~7GB); QLoRA and ZeRO/FSDP have no rationale at 0.6B
- [[lab-probe-2026-07-04-torch-nn-attention-sdpa-kernel|Lab probe 2026-07-04 (torch.nn.attention.sdpa_kernel warnings verbatim…]] — sm_75 has no FlashAttention; GQA 16-vs-8 forces MATH backend OOM unless repeat_kv patch expands KV heads
- [[lab-measurement-2026-07-04-torch-2-11-0-cu130-transformers|Lab measurement 2026-07-04, torch 2.11.0+cu130, transformers 5.5.2, HF…]] — Throughput anchor: 1,584 tok/s @4K, 2,049 @bs4x2048, ~15-20% MFU on Turing sm_75 (closest T4 proxy)
- [[defeating-the-training-inference-mismatch-via-fp16|Defeating the Training-Inference Mismatch via FP16]] — Only UNCERTAIN item: fp16 CPT of bf16-native ckpt untested; paper argues bf16 rounding not fp16 range is instability
- [[kaggle-product-feedback-announcement-notebooks-update-new|Kaggle product-feedback announcement   ([Notebooks update] New GPU (T4…]] — Hardware envelope: ~30 GPU-h/week, 12h sessions, T4x2 at 1x quota = effective ~60 GPU-h/week

## Papers (1)
- [[defeating-the-training-inference-mismatch-via-fp16|Defeating the Training-Inference Mismatch via FP16]] (2025) — kaggle-t4x2-compute-vram-budget-for-the

## Sources & findings (7)
- [[derived-from-lab-measurement-t4bench2-py-t4bench3-py-kaggle|Derived from lab measurement (t4bench2.py/t4bench3.py) + Kaggle quota…]] — [verdict] The recommended 20-25B tokens-seen CPT does NOT fit the Kaggle quota — dead on arrival. At the measured 1.5-2.…
- [[kaggle-product-feedback-announcement-notebooks-update-new|Kaggle product-feedback announcement   ([Notebooks update] New GPU (T4…]] — [transferable-untested; hardware fact] Kaggle free-tier quota confirmed: ~30 GPU-hours/week, 12h max session, and the T4…
- [[lab-measurement-2026-07-04-torch-2-11-0-cu130-transformers|Lab measurement 2026-07-04, torch 2.11.0+cu130, transformers 5.5.2, HF…]] — [measured-in-lab on the target checkpoint; language-agnostic] Direct fp16 training microbenchmark of Qwen/Qwen3-0.6B-Bas…
- [[lab-measurement-peak-vram-standard-adam-state-arithmetic-2|Lab measurement (peak VRAM) + standard Adam state arithmetic (2+2+4+4+…]] — [measured + derived] VRAM is NOT the binding constraint and the asserted ZeRO-2/FSDP requirement is unnecessary: full-FT…
- [[lab-measurement-t4bench2-py-t4bench3-py|Lab measurement t4bench2.py/t4bench3.py]] — [measured; recipe lever] Context length 4096 costs ~23% throughput vs 2048 at this scale (1,584 vs 1,948-2,049 tok/s mea…
- [[lab-probe-2026-07-04-torch-nn-attention-sdpa-kernel|Lab probe 2026-07-04 (torch.nn.attention.sdpa_kernel warnings verbatim…]] — [measured; engineering landmine] On sm_75 (Kaggle T4 and lab 2070), PyTorch 2.11 has NO FlashAttention (kernel explicitl…
- [[state-size-arithmetic-from-measured-596-0m-params|State-size arithmetic from measured 596.0M params]] — [derived; transferable-untested] Checkpoint/restart overhead across 12h session boundaries is manageable but disk-bound:…

[[Home]]
