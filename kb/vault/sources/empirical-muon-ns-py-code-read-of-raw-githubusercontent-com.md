---
kb_id: "title:empirical muon ns code read of raw githubusercontent com kellerjordan muon master muon py"
type: "source"
title: "Empirical: muon_ns.py + code read of raw.githubusercontent.com/KellerJ…"
doi: null
hf_repo: null
year: null
topics: ["hardware-gate"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:empirical muon ns code read of raw githubusercontent com kellerjordan muon master muon py"]
tags: ["source", "topic/hardware-gate"]
---
# Empirical: muon_ns.py + code read of raw.githubusercontent.com/KellerJ…

**Topics:** [[hardware-gate]]

## Source URLs
- Empirical: muon_ns.py + code read of raw.githubusercontent.com/KellerJordan/Muon/master/muon.py

## Findings

> [!note] CLAIM — hardware-gate
> Muon IS usable on T4, but the official implementation contains a 6.6x SM75 performance trap: KellerJordan/Muon's zeropower_via_newtonschulz5 hard-casts to bfloat16 ('X = G.bfloat16()', 5 iterations, coefficients a,b,c = 3.4445, -4.7750, 2.0315), and bf16 matmul on SM75 is software-emulated. NS5 in fp16 is numerically equivalent (input is norm-normalized to ~[0,1] first, so fp16 range is safe) and runs on tensor cores. One-line patch (.bfloat16() -> .half()) makes Muon fast on T4. Optimizer state is a single momentum buffer per param (state['momentum_buffer'] = torch.zeros_like(p)) — the ~50% optimizer-VRAM saving vs AdamW's two moments is structurally confirmed. Flag: transferable-untested (never run on a Kazakh model).
>
> **Numbers:** NS5 on a 2048x5632 matrix (600M-class FFN weight), SM75: bf16 189.6 ms, fp32 120.4 ms, fp16 28.9 ms per matrix; orthogonalization quality identical — singular values of output in [0.673,1.137] (bf16), [0.682,1.135] (fp16), [0.682,1.134] (fp32), all finite
> **Relevance:** Muon's ~2x data-efficiency claim (Moonlight, arXiv 2502.02982) is reachable on free T4 compute for the from-scratch v2 track, but ONLY with the fp16 patch; unpatched Muon would burn ~6.6x optimizer wall-clock in NS.
> **Source:** Empirical: muon_ns.py + code read of raw.githubusercontent.com/KellerJordan/Muon/master/muon.py · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[muon-is-scalable-for-llm-training|Muon is Scalable for LLM Training]] — Empirical SM75 6.6x bf16 trap in KellerJordan Muon; this paper argues Muon scales but is silent on Turing/fp16 NS5 path
- [[lab-measurement-peak-vram-standard-adam-state-arithmetic-2|Lab measurement (peak VRAM) + standard Adam state arithmetic (2+2+4+4+…]] — Muon's single momentum buffer confirms the ~50% optimizer-VRAM saving vs the AdamW 2+2+4+4+4 arithmetic in that node

[[Home]]
