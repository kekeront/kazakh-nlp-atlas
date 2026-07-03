# Paper Directory

The week-1 arXiv paper lives here. Read the three docs in order:

1. **[TOPIC.md](TOPIC.md)** — what we're writing and why.
2. **[SPRINT_PLAN.md](SPRINT_PLAN.md)** — day-by-day deliverables (Day 1–7).
3. **main.tex** — the actual draft. It grows every day. Currently a skeleton with TODOs.

## Build the PDF
```bash
# install minimal TeX:    sudo apt install texlive-latex-recommended texlive-bibtex-extra
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
The first compile will have undefined references — that's fine, the final two passes resolve them.

## Layout

```
paper/
├── arxiv.sty              # standard arxiv preprint style
├── main.tex               # the draft (writing prompts inline as \textsc{TODO})
├── references.bib         # bibliography, pre-seeded with canonical cites
├── TOPIC.md               # paper topic + rationale + research questions
├── SPRINT_PLAN.md         # 7-day day-by-day plan
├── figures/               # save publication-ready plots here as .pdf
└── experiments/           # raw experimental outputs (csv, json) — git-tracked
```

## The Daily Rule

**At the end of every day, the PDF must compile to a slightly more complete draft.**
No exceptions. Even if all you added is one bullet, you compile and commit.

This is the single most underrated research habit. Most people write the whole paper in the last 48 hours
and it shows. We grow it daily, so the last 48 hours are about polish, not panic.
