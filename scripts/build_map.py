"""Render the Kazakh-NLP research atlas to a self-contained HTML file.

Reads the scraped corpus (paper/survey/papers.json) and overlays a curated
editorial layer -- the flagship-model comparison and the "uncharted" gap map --
that turns a pile of papers into an argument: where the field is dense, where it
is thin, and where a contribution is open.

The output is a single file with all data inlined, so it opens straight from
file:// with no server and no CORS friction.

Separation of concerns (deliberate):
  * scrape_papers.py  -> reproducible scraped FACTS (papers.json)
  * build_map.py      -> human CURATION + analysis + presentation

Usage:
    python code/build_map.py [--data paper/survey/papers.json]
                             [--out  paper/survey/index.html]
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------------- #
# Curated editorial layer  (hand-verified from primary sources, June 2026)
# --------------------------------------------------------------------------- #

# Display labels for the auto-tagged categories from the scraper.
CATEGORY_META: dict[str, dict[str, str]] = {
    "language-model": {"label": "Языковые модели / LLM", "icon": "◈"},
    "tokenization": {"label": "Токенизация", "icon": "◇",
                     "frontier": "Тонкая граница. Почти всё — за 2024–2026. Независимого аудита морфем-выравнивания нет."},
    "morphology": {"label": "Морфология / сегментация", "icon": "❖",
                   "frontier": "Строят новые сегментаторы, но не аудируют, что делают существующие токенайзеры."},
    "machine-translation": {"label": "Машинный перевод", "icon": "⇄"},
    "speech": {"label": "Речь (ASR / TTS)", "icon": "◉"},
    "ner-ie": {"label": "NER / извлечение", "icon": "◎"},
    "dataset-corpus": {"label": "Датасеты / корпуса", "icon": "▤"},
    "evaluation": {"label": "Оценка / бенчмарки", "icon": "▣",
                   "frontier": "Бенчмарков мало, и они разрозненны. Til-Core вышел с НУЛЁМ опубликованных метрик."},
    "classification": {"label": "Классификация / сентимент", "icon": "◐"},
    "embeddings": {"label": "Эмбеддинги", "icon": "✶"},
    "other": {"label": "Прочее", "icon": "·"},
}

# Order territories from frontier (thin, high-opportunity) to dense.
CATEGORY_ORDER = [
    "tokenization", "morphology", "language-model", "evaluation",
    "embeddings", "classification", "ner-ie", "machine-translation",
    "speech", "dataset-corpus", "other",
]

# Flagship deployed models. `verified` facts come from config.json / paper /
# model card; `claim` columns report what the authors assert, not ground truth.
FLAGSHIP_MODELS: list[dict] = [
    {
        "name": "Til-Core-0.5B",
        "org": "Тіл Қазына (гос.)",
        "year": "2025",
        "params": "497M",
        "base": "Qwen2",
        "vocab": "256 000",
        "tokenizer": "morphBPE — BPE с запретом слияний через морфемные границы (сегментатор BiLSTM)",
        "morph_claim": "ДА — но сегментатор не выложен",
        "benchmarks": "НЕТ — ноль",
        "highlight": True,
        "note": "Громкий claim про морфологию + ноль опубликованных бенчмарков. Никто не проверял независимо.",
        "url": "https://huggingface.co/TilQazyna/Til-Core-0.5B",
    },
    {
        "name": "Sherkala-Chat-8B",
        "org": "Inception / MBZUAI",
        "year": "2025",
        "params": "8B",
        "base": "Llama-3.1",
        "vocab": "159 766",
        "tokenizer": "расширенный BPE (+25% к Llama-3.1)",
        "morph_claim": "нет (fertility-driven)",
        "benchmarks": "да",
        "highlight": False,
        "note": "Fertility казахского 4.73 → 2.04. Морфем-выравнивание не обсуждается.",
        "url": "https://arxiv.org/abs/2503.01493",
    },
    {
        "name": "SozKZ (50M–600M)",
        "org": "S. Tukenov",
        "year": "2026",
        "params": "50–600M",
        "base": "Llama-arch",
        "vocab": "50 000",
        "tokenizer": "ByteLevel BPE с нуля на казахском",
        "morph_claim": "нет",
        "benchmarks": "частично",
        "highlight": False,
        "note": "Аргумент через fertility, не через морфемные границы.",
        "url": "https://arxiv.org/abs/2603.20854",
    },
    {
        "name": "KazByte",
        "org": "R. Akylzhanov",
        "year": "2026",
        "params": "adapter→Qwen2.5-7B",
        "base": "Qwen2.5",
        "vocab": "— (byte-level)",
        "tokenizer": "обходит токенайзер целиком (байтовый адаптер)",
        "morph_claim": "n/a — нет токенайзера",
        "benchmarks": "да",
        "highlight": False,
        "note": "Контрапункт всему полю: «tokenizer tax» решают, убирая токенайзер.",
        "url": "https://arxiv.org/abs/2603.27859",
    },
    {
        "name": "KazLLM (8B / 70B)",
        "org": "ISSAI / NU",
        "year": "2024",
        "params": "8B, 70B",
        "base": "Llama-3.1",
        "vocab": "128 256 (Llama-3.1)",
        "tokenizer": "наследует Llama-3.1, расширение не документировано",
        "morph_claim": "нет",
        "benchmarks": "да (task-perf)",
        "highlight": False,
        "note": "150B+ токенов, 4 языка. Нет отдельной токенайзер-работы.",
        "url": "https://issai.nu.edu.kz/kazllm/",
    },
    {
        "name": "KazRoBERTa",
        "org": "ISSAI / NU",
        "year": "2022",
        "params": "~125M",
        "base": "RoBERTa",
        "vocab": "32 000",
        "tokenizer": "BPE только на казахском",
        "morph_claim": "нет",
        "benchmarks": "частично",
        "highlight": False,
        "note": "Старый baseline. Используется в гибридных морфо-анализаторах.",
        "url": "https://huggingface.co/issai",
    },
]

# The uncharted territory: what nobody has shipped. Ordered by how open it is.
GAPS: list[dict] = [
    {
        "title": "Независимый аудит морфем-выравнивания казахских токенайзеров",
        "yours": True,
        "why": "Никто не сравнивал несколько КАЗАХСКИХ токенайзеров (KazRoBERTa, SozKZ, Sherkala, Til-Core) по морфемным границам на едином gold-стандарте. Arnett 2025 берёт казахский как 1 из 70 языков и только дженерик-токенайзеры; Duisenova 2026 строит новый, но не аудирует существующие.",
        "effort": "ШИПАБЕЛЬНО на этой неделе",
    },
    {
        "title": "Эмпирическая проверка claim Til-Core про морфологию",
        "yours": True,
        "why": "Til-Core вышел с НУЛЁМ опубликованных бенчмарков и громким заявлением «поддержка казахской морфологии». Стань первым, кто измерил это независимо.",
        "effort": "входит в аудит",
    },
    {
        "title": "Precision-метрика морфем-выравнивания (не только recall)",
        "yours": True,
        "why": "Опубликованный MorphScore меряет RECALL морфемных границ. Precision (сколько границ токенайзера реальны) и F1 для казахского никто не считал. Чистая дифференциация от Arnett & Bergen.",
        "effort": "малая добавка к аудиту",
    },
    {
        "title": "Совместная таблица fertility × morpheme-alignment",
        "yours": False,
        "why": "Sherkala репортит fertility, MorphScore-работа репортит alignment — но никто не свёл обе оси для казахских токенайзеров в одну таблицу.",
        "effort": "средняя",
    },
    {
        "title": "Usage-vs-morphology divergence (что носители реально говорят)",
        "yours": True,
        "why": "Морфологически правильная форма ≠ форма, которую носитель употребляет (напр. «біздің кітаптар» вместо «кітаптарымыз», «неге» как монолит). Это методологически не покрыто ни одной работой. Опрос носителей → новый угол.",
        "effort": "мини-опрос, 30–50 ответов",
    },
]

THESIS = (
    "Казахский NLP пережил взрыв в 2024–2026 — но рост сконцентрирован в "
    "речи и машинном переводе. Токенизация и морфология остаются тонкой, "
    "недокартированной границей. Именно там открыты контрибьюшены."
)

# Linear chronology of groundbreaking work: global canon vs Kazakh adoption.
# The story is the LAG -- Transformer (2017) -> first big Kazakh LLM (2024).
MILESTONES: list[dict] = [
    {"year": 2013, "scope": "global", "label": "word2vec", "what": "Плотные векторные представления слов.", "url": "https://arxiv.org/abs/1301.3781"},
    {"year": 2014, "scope": "global", "label": "seq2seq", "what": "Encoder-decoder: перевод как генерация.", "url": "https://arxiv.org/abs/1409.3215"},
    {"year": 2014, "scope": "global", "label": "Attention (Bahdanau)", "what": "Выравнивание — конец bottleneck'а.", "url": "https://arxiv.org/abs/1409.0473"},
    {"year": 2016, "scope": "global", "label": "BPE для NMT (Sennrich)", "what": "Subword-юниты → редкие слова и морфология становятся подъёмны.", "url": "https://arxiv.org/abs/1508.07909"},
    {"year": 2017, "scope": "global", "label": "Transformer", "what": "«Attention is All You Need» — архитектура всей эпохи.", "url": "https://arxiv.org/abs/1706.03762"},
    {"year": 2018, "scope": "global", "label": "BERT", "what": "Двунаправленный pretraining, перенос на задачи.", "url": "https://arxiv.org/abs/1810.04805"},
    {"year": 2019, "scope": "kazakh", "label": "Первые continuous ASR / NMT", "what": "Казахская речь и перевод заходят в нейросети.", "url": None},
    {"year": 2019, "scope": "global", "label": "XLM-R", "what": "Мультиязычный pretraining на 100 языках — казахский внутри.", "url": "https://arxiv.org/abs/1911.02116"},
    {"year": 2020, "scope": "kazakh", "label": "Kazakh Speech Corpus (KSC)", "what": "Фундаментальный датасет — хаб №1 в графе цитирований.", "url": "https://arxiv.org/abs/2009.10334"},
    {"year": 2020, "scope": "global", "label": "GPT-3", "what": "In-context learning: масштаб как способность.", "url": "https://arxiv.org/abs/2005.14165"},
    {"year": 2021, "scope": "kazakh", "label": "KazNERD + KazakhTTS", "what": "Первые открытые NER и TTS ресурсы для казахского.", "url": "https://arxiv.org/abs/2111.13419"},
    {"year": 2021, "scope": "global", "label": "How Good is Your Tokenizer", "what": "Fertility: цена токенайзера для не-английского.", "url": "https://arxiv.org/abs/2012.15613"},
    {"year": 2022, "scope": "kazakh", "label": "KazRoBERTa", "what": "Первая казахская предобученная языковая модель (BPE 32k).", "url": None},
    {"year": 2022, "scope": "global", "label": "Chinchilla", "what": "Compute-optimal: данных важнее, чем размера.", "url": "https://arxiv.org/abs/2203.15556"},
    {"year": 2023, "scope": "global", "label": "LLaMA + Tokenizer Unfairness", "what": "Открытые веса → волна локальных адаптаций; токен-налог low-resource измерен.", "url": "https://arxiv.org/abs/2305.15425"},
    {"year": 2024, "scope": "kazakh", "label": "KazLLM (ISSAI)", "what": "Первый крупный казахский LLM (8B/70B, 150B+ токенов).", "url": "https://issai.nu.edu.kz/kazllm/"},
    {"year": 2024, "scope": "kazakh", "label": "«Do LLMs Speak Kazakh?»", "what": "Первая системная оценка казахского у 7 моделей.", "url": None},
    {"year": 2024, "scope": "global", "label": "MorphScore", "what": "Метрика морфем-выравнивания токенайзеров.", "url": "https://arxiv.org/abs/2411.14198"},
    {"year": 2025, "scope": "kazakh", "label": "Sherkala-Chat", "what": "SOTA казахский чат, vocab 159k, fertility 4.73→2.04.", "url": "https://arxiv.org/abs/2503.01493"},
    {"year": 2025, "scope": "kazakh", "label": "Til-Core (гос.)", "what": "morphBPE 256k, громкий claim про морфологию, 0 опубликованных бенчмарков.", "url": "https://huggingface.co/TilQazyna/Til-Core-0.5B"},
    {"year": 2026, "scope": "kazakh", "label": "SozKZ + KazByte", "what": "From-scratch SLM (50k BPE) и tokenizer-free (байтовый адаптер).", "url": "https://arxiv.org/abs/2603.20854"},
]

# Node colours for the citation graph, by category (+ the global-hub colour).
CATEGORY_COLORS: dict[str, str] = {
    "tokenization": "#e08a4a", "morphology": "#f0a35a", "language-model": "#e9b949",
    "evaluation": "#d4b483", "machine-translation": "#54b9d8", "speech": "#4a90b8",
    "ner-ie": "#6fc0a8", "dataset-corpus": "#7d9bc4", "classification": "#b88fc0",
    "embeddings": "#8fbf9f", "other": "#6f7d82", "global": "#f8d986",
}


def canonical_id(arxiv_id: str | None, doi: str | None, title: str) -> str:
    """Stable node id; MUST match the same function in scrape_citations.py."""
    if arxiv_id:
        return f"arxiv:{arxiv_id}"
    if doi:
        return f"doi:{doi.lower()}"
    return "title:" + re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def compute_graph(papers: list[dict], cit: dict) -> dict | None:
    """Force-directed layout (Fruchterman-Reingold) over the citation graph.

    Shows the SIGNAL: only nodes that participate in >=1 citation edge, plus the
    global breakthrough hubs they cite. Node radius scales with influence
    (in-corpus in-degree + global citations); colour encodes topic.
    """
    import numpy as np

    edges_raw = cit.get("edges", [])
    global_nodes = cit.get("global_nodes", {})
    node_cit = cit.get("node_citations", {})
    if not edges_raw:
        return None

    pmap = {
        canonical_id(p.get("arxiv_id"), p.get("doi"), p.get("title", "")): p
        for p in papers
    }
    indeg: dict[str, int] = {}
    appears: set[str] = set()
    for a, b in edges_raw:
        appears.add(a)
        appears.add(b)
        indeg[b] = indeg.get(b, 0) + 1

    corpus_ids = [n for n in appears if not n.startswith("global:") and n in pmap]
    global_ids = [g for g in global_nodes if g in appears]
    all_ids = corpus_ids + global_ids
    if len(all_ids) < 2:
        return None
    idx = {nid: i for i, nid in enumerate(all_ids)}
    E = [(idx[a], idx[b]) for a, b in edges_raw if a in idx and b in idx]

    n = len(all_ids)
    rng = np.random.default_rng(42)
    pos = rng.standard_normal((n, 2))
    ea = np.array([e[0] for e in E]) if E else np.array([], dtype=int)
    eb = np.array([e[1] for e in E]) if E else np.array([], dtype=int)
    k = 1.0 / math.sqrt(n)
    temp = 0.12
    for _ in range(420):
        delta = pos[:, None, :] - pos[None, :, :]
        dist = np.sqrt((delta ** 2).sum(2)) + 1e-9
        rep = (k * k) / dist
        disp = (delta / dist[:, :, None] * rep[:, :, None]).sum(1)
        if E:
            d = pos[ea] - pos[eb]
            dd = np.sqrt((d ** 2).sum(1)) + 1e-9
            att = (dd * dd) / k
            f = (d / dd[:, None]) * att[:, None]
            np.add.at(disp, ea, -f)
            np.add.at(disp, eb, f)
        dl = np.sqrt((disp ** 2).sum(1)) + 1e-9
        pos += (disp / dl[:, None]) * np.minimum(dl, temp)[:, None]
        temp *= 0.985

    mn, mx = pos.min(0), pos.max(0)
    span = mx - mn
    span[span == 0] = 1.0
    pad, W, H = 70, 1000, 680
    norm = (pos - mn) / span
    xs = pad + norm[:, 0] * (W - 2 * pad)
    ys = pad + norm[:, 1] * (H - 2 * pad)

    nodes: list[dict] = []
    for nid in all_ids:
        i = idx[nid]
        if nid.startswith("global:"):
            gd = global_nodes[nid]
            cb = indeg.get(nid, 0)
            nodes.append({
                "x": round(float(xs[i]), 1), "y": round(float(ys[i]), 1),
                "r": round(9 + 1.8 * math.sqrt(cb), 1), "kind": "global",
                "label": gd.get("label"), "year": gd.get("year"), "cit": None,
                "indeg": cb, "cat": "global",
                "url": f"https://arxiv.org/abs/{gd.get('arxiv')}",
            })
        else:
            p = pmap[nid]
            ind = indeg.get(nid, 0)
            c = node_cit.get(nid) or p.get("citation_count") or 0
            r = min(4 + 1.9 * math.sqrt(ind * 3 + c * 0.08), 24)
            nodes.append({
                "x": round(float(xs[i]), 1), "y": round(float(ys[i]), 1),
                "r": round(r, 1), "kind": "paper", "label": None,
                "title": p.get("title"), "year": p.get("year"),
                "cit": c or None, "indeg": ind, "cat": (p.get("categories") or ["other"])[0],
                "url": p.get("url"),
            })

    # label the 12 most influential papers + every global hub
    ranked = sorted(
        (i for i, nd in enumerate(nodes) if nd["kind"] == "paper"),
        key=lambda i: -(nodes[i]["indeg"] * 3 + (nodes[i]["cit"] or 0) * 0.08),
    )
    for i in ranked[:12]:
        t = nodes[i]["title"] or ""
        nodes[i]["label"] = (t[:32] + "…") if len(t) > 32 else t

    return {
        "method": cit.get("method"),
        "nodes": nodes,
        "edges": [[a, b] for a, b in E],
        "shown": n,
        "globals": len(global_ids),
        "total": len(papers),
        "edge_count": len(E),
    }


# --------------------------------------------------------------------------- #
# HTML template  (data injected at __DATA_JSON__; no f-strings to dodge braces)
# --------------------------------------------------------------------------- #

TEMPLATE = r"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Атлас казахского NLP · State of Kazakh NLP Research</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..900;1,9..144,400..600&family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#0a1822; --bg2:#0d2030; --panel:#10283a; --panel2:#14314699;
  --ink:#ece1c8; --ink-dim:#a9a487; --ink-faint:#6f7d82;
  --gold:#e9b949; --gold-hi:#f8d986; --sky:#54b9d8; --sky-dim:#2c6f88;
  --frontier:#e08a4a; --frontier-hi:#f4a766;
  --line:rgba(233,185,73,.16); --line-soft:rgba(236,225,200,.09);
  --serif:"Newsreader",Georgia,serif; --disp:"Fraunces",Georgia,serif;
  --mono:"IBM Plex Mono",ui-monospace,monospace;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:var(--serif); font-size:17px; line-height:1.6;
  -webkit-font-smoothing:antialiased;
  background-image:
    radial-gradient(1200px 600px at 75% -10%, rgba(84,185,216,.10), transparent 60%),
    radial-gradient(900px 500px at 10% 8%, rgba(233,185,73,.07), transparent 55%);
  background-attachment:fixed;
}
/* faint topographic grain */
body::before{
  content:""; position:fixed; inset:0; pointer-events:none; z-index:0; opacity:.5;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix type='saturate' values='0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='.03'/></svg>");
}
.wrap{position:relative; z-index:1; max-width:1180px; margin:0 auto; padding:0 28px}
a{color:var(--sky); text-decoration:none}
a:hover{color:var(--gold-hi)}

/* ---- ornament divider ---- */
.orn{display:flex; align-items:center; justify-content:center; gap:18px; margin:56px 0 40px; opacity:.85}
.orn .ln{height:1px; flex:1; max-width:280px; background:linear-gradient(90deg,transparent,var(--line),transparent)}
.orn svg{flex:none}

/* ---- masthead ---- */
header.mast{padding:72px 0 8px; text-align:center}
.kicker{font-family:var(--mono); font-size:12.5px; letter-spacing:.34em; text-transform:uppercase;
  color:var(--gold); margin-bottom:26px}
h1{font-family:var(--disp); font-weight:600; font-size:clamp(38px,6.4vw,76px); line-height:1.02;
  margin:0 0 6px; letter-spacing:-.015em; font-optical-sizing:auto;
  background:linear-gradient(180deg,#fff6e2,#e9b949 130%); -webkit-background-clip:text; background-clip:text; color:transparent}
.sub-en{font-family:var(--disp); font-style:italic; font-weight:400; font-size:clamp(17px,2.4vw,25px);
  color:var(--ink-dim); margin:2px 0 30px}
.thesis{max-width:730px; margin:0 auto; font-size:19px; color:var(--ink); line-height:1.66}
.thesis b{color:var(--gold-hi); font-weight:600}

/* ---- stat band ---- */
.stats{display:grid; grid-template-columns:repeat(4,1fr); gap:1px; margin:46px 0 8px;
  background:var(--line-soft); border:1px solid var(--line); border-radius:14px; overflow:hidden}
.stat{background:var(--panel); padding:22px 18px; text-align:center}
.stat .num{font-family:var(--disp); font-weight:600; font-size:clamp(30px,4.6vw,46px); color:var(--gold-hi); line-height:1}
.stat .lab{font-family:var(--mono); font-size:11px; letter-spacing:.13em; text-transform:uppercase;
  color:var(--ink-dim); margin-top:9px}
@media(max-width:680px){.stats{grid-template-columns:repeat(2,1fr)}}

/* ---- section frame ---- */
section{margin:18px 0}
.sec-head{display:flex; align-items:baseline; gap:14px; margin:0 0 22px}
.sec-head h2{font-family:var(--disp); font-weight:600; font-size:clamp(24px,3.4vw,36px); margin:0; letter-spacing:-.01em}
.sec-head .idx{font-family:var(--mono); font-size:13px; color:var(--gold); letter-spacing:.1em}
.sec-head .sub{font-family:var(--mono); font-size:12px; color:var(--ink-faint); margin-left:auto; letter-spacing:.05em}

/* ---- timeline ---- */
.timeline{display:flex; align-items:flex-end; gap:8px; height:230px; padding:16px 6px 0;
  border-bottom:1px solid var(--line); margin-bottom:10px}
.tl-bar{flex:1; display:flex; flex-direction:column; align-items:center; justify-content:flex-end; height:100%}
.tl-bar .bar{width:100%; max-width:56px; border-radius:5px 5px 0 0; background:linear-gradient(180deg,var(--sky-dim),#13384a);
  position:relative; transition:filter .2s; min-height:3px}
.tl-bar.boom .bar{background:linear-gradient(180deg,var(--gold-hi),var(--gold) 70%,#9d7a23)}
.tl-bar .bar:hover{filter:brightness(1.25)}
.tl-bar .v{font-family:var(--mono); font-size:12px; color:var(--ink); margin-bottom:6px}
.tl-bar .y{font-family:var(--mono); font-size:11px; color:var(--ink-dim); margin-top:8px; transform:rotate(-42deg); transform-origin:center; white-space:nowrap}
.tl-note{font-family:var(--mono); font-size:12px; color:var(--frontier-hi); text-align:right; margin-top:24px}

/* ---- territory grid ---- */
.terr{display:grid; grid-template-columns:repeat(2,1fr); gap:14px}
@media(max-width:760px){.terr{grid-template-columns:1fr}}
.card{background:var(--panel); border:1px solid var(--line); border-radius:13px; padding:20px 22px;
  position:relative; overflow:hidden}
.card.front{border-color:var(--frontier); background:linear-gradient(180deg,#1a2a2c,#10283a)}
.card .top{display:flex; align-items:center; gap:12px; margin-bottom:13px}
.card .ico{font-size:21px; color:var(--sky)}
.card.front .ico{color:var(--frontier-hi)}
.card .nm{font-family:var(--disp); font-weight:600; font-size:20px; flex:1}
.card .ct{font-family:var(--mono); font-size:22px; font-weight:600; color:var(--gold-hi)}
.dens{height:7px; border-radius:4px; background:#0c1b27; overflow:hidden; margin:4px 0 12px}
.dens i{display:block; height:100%; border-radius:4px; background:linear-gradient(90deg,var(--sky-dim),var(--sky))}
.card.front .dens i{background:linear-gradient(90deg,#9d6a30,var(--frontier-hi))}
.frontier-note{font-size:14.5px; color:var(--frontier-hi); line-height:1.5}
.frontier-tag{font-family:var(--mono); font-size:10px; letter-spacing:.18em; text-transform:uppercase;
  color:var(--bg); background:var(--frontier-hi); padding:2px 8px; border-radius:20px; font-weight:600}
.dense-tag{font-family:var(--mono); font-size:10px; letter-spacing:.16em; text-transform:uppercase; color:var(--sky)}

/* ---- flagship table ---- */
.tbl-scroll{overflow-x:auto; border:1px solid var(--line); border-radius:13px}
table{border-collapse:collapse; width:100%; min-width:760px; font-size:14.5px}
th,td{text-align:left; padding:13px 15px; border-bottom:1px solid var(--line-soft); vertical-align:top}
th{font-family:var(--mono); font-size:10.5px; letter-spacing:.13em; text-transform:uppercase; color:var(--gold);
  background:var(--bg2); position:sticky; top:0}
td .mdl{font-family:var(--disp); font-weight:600; font-size:16px; color:var(--ink)}
td .org{font-family:var(--mono); font-size:11px; color:var(--ink-faint)}
tr.hl{background:linear-gradient(90deg,rgba(224,138,74,.13),transparent)}
tr.hl td:first-child{box-shadow:inset 3px 0 0 var(--frontier-hi)}
.yes{color:#7fc98a} .no{color:var(--frontier-hi); font-weight:600} .mono{font-family:var(--mono); font-size:12.5px}
.rownote{font-size:12.5px; color:var(--ink-dim); font-style:italic; line-height:1.45}

/* ---- gap map ---- */
.gaps{display:flex; flex-direction:column; gap:13px}
.gap{display:flex; gap:18px; background:var(--panel); border:1px solid var(--line); border-radius:13px; padding:18px 22px}
.gap.you{border-color:var(--frontier); background:linear-gradient(110deg,rgba(224,138,74,.12),var(--panel) 60%)}
.gap .mk{font-family:var(--mono); font-size:11px; font-weight:600; letter-spacing:.1em; flex:none; width:118px; padding-top:3px}
.gap.you .mk{color:var(--frontier-hi)} .gap .mk{color:var(--ink-faint)}
.gap .body h3{font-family:var(--disp); font-weight:600; font-size:18.5px; margin:0 0 6px}
.gap .body p{margin:0; font-size:14.5px; color:var(--ink-dim); line-height:1.55}
.gap .eff{display:inline-block; margin-top:9px; font-family:var(--mono); font-size:10.5px; letter-spacing:.1em;
  text-transform:uppercase; color:var(--gold); border:1px solid var(--line); padding:3px 9px; border-radius:20px}
.gap.you .eff{color:var(--frontier-hi); border-color:var(--frontier)}
@media(max-width:680px){.gap{flex-direction:column; gap:8px} .gap .mk{width:auto}}

/* ---- explorer ---- */
.controls{display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin-bottom:20px}
#q{flex:1; min-width:220px; background:var(--panel); border:1px solid var(--line); color:var(--ink);
  font-family:var(--serif); font-size:15px; padding:11px 15px; border-radius:10px}
#q:focus{outline:none; border-color:var(--sky)}
#q::placeholder{color:var(--ink-faint)}
select{background:var(--panel); border:1px solid var(--line); color:var(--ink); font-family:var(--mono);
  font-size:12.5px; padding:11px 13px; border-radius:10px}
.chips{display:flex; flex-wrap:wrap; gap:7px; margin-bottom:18px}
.chip{font-family:var(--mono); font-size:11.5px; letter-spacing:.04em; color:var(--ink-dim); cursor:pointer;
  border:1px solid var(--line); padding:6px 12px; border-radius:20px; background:transparent; transition:all .15s}
.chip:hover{color:var(--ink)}
.chip.on{background:var(--gold); color:var(--bg); border-color:var(--gold); font-weight:600}
.plist{display:grid; grid-template-columns:repeat(2,1fr); gap:13px}
@media(max-width:760px){.plist{grid-template-columns:1fr}}
.paper{background:var(--panel); border:1px solid var(--line-soft); border-radius:12px; padding:17px 19px;
  display:flex; flex-direction:column; transition:border-color .15s, transform .15s}
.paper:hover{border-color:var(--sky); transform:translateY(-2px)}
.paper .pt{font-family:var(--disp); font-weight:600; font-size:16.5px; line-height:1.28; margin:0 0 7px}
.paper .meta{font-family:var(--mono); font-size:11px; color:var(--ink-faint); margin-bottom:9px; display:flex; gap:10px; flex-wrap:wrap}
.paper .meta .cit{color:var(--gold)}
.paper .ab{font-size:13.5px; color:var(--ink-dim); line-height:1.5; flex:1}
.paper .tags{display:flex; flex-wrap:wrap; gap:5px; margin-top:11px}
.paper .tg{font-family:var(--mono); font-size:9.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--sky-dim);
  border:1px solid var(--line-soft); padding:2px 7px; border-radius:14px}
.count{font-family:var(--mono); font-size:12px; color:var(--ink-faint); margin:0 0 14px}

/* ---- chronology (breakthroughs) ---- */
.chrono-key{display:flex; gap:30px; justify-content:center; font-family:var(--mono); font-size:13px; margin-bottom:26px}
.chrono{position:relative}
.chrono::before{content:""; position:absolute; left:50%; top:6px; bottom:6px; width:2px; transform:translateX(-50%);
  background:linear-gradient(180deg,transparent,var(--line) 5%,var(--line) 95%,transparent)}
.mile{position:relative; display:grid; grid-template-columns:1fr 84px 1fr; align-items:center; margin:0 0 13px}
.mile .yr{grid-column:2; text-align:center; z-index:2}
.mile .yr span{font-family:var(--mono); font-size:13px; color:var(--gold); font-weight:600; background:var(--bg); padding:5px 4px; border-radius:20px; display:inline-block; min-width:54px}
.mE{display:block; color:inherit; text-decoration:none; background:var(--panel); border:1px solid var(--line); border-radius:11px; padding:12px 15px; transition:border-color .15s, transform .15s}
a.mE:hover{transform:translateY(-2px)}
.mE h4{font-family:var(--disp); font-weight:600; font-size:16px; margin:0 0 3px}
.mE p{margin:0; font-size:13px; color:var(--ink-dim); line-height:1.45}
.mE .sc{font-family:var(--mono); font-size:9.5px; letter-spacing:.14em; text-transform:uppercase; margin-bottom:5px}
.mile.global .mE{grid-column:1; margin-right:20px; border-left:3px solid var(--sky)}
.mile.global .mE:hover{border-color:var(--sky)} .mile.global .sc{color:var(--sky)}
.mile.kazakh .mE{grid-column:3; margin-left:20px; border-left:3px solid var(--gold)}
.mile.kazakh .mE:hover{border-color:var(--gold)} .mile.kazakh .sc{color:var(--gold)}
@media(max-width:680px){
  .chrono::before{left:16px}
  .mile{grid-template-columns:32px 1fr}
  .mile .yr{grid-column:1; text-align:left} .mile .yr span{min-width:0; font-size:11px; padding:3px}
  .mile.global .mE,.mile.kazakh .mE{grid-column:2; margin:0 0 0 12px}
}

/* ---- citation graph ---- */
.graph-wrap{border:1px solid var(--line); border-radius:14px; overflow:hidden;
  background:radial-gradient(720px 420px at 50% 42%, rgba(84,185,216,.07), var(--bg2))}
#graph{width:100%; height:auto; display:block}
#graph .edge{stroke:rgba(236,225,200,.10); stroke-width:1}
#graph .node{cursor:pointer; transition:opacity .15s}
#graph .node circle,#graph .node rect{stroke:var(--bg); stroke-width:1.2}
#graph .glabel{font-family:var(--mono); font-size:10px; fill:var(--gold-hi); pointer-events:none}
#graph .hub-label{font-family:var(--mono); font-size:9.5px; fill:var(--ink-dim); pointer-events:none}
#graph.dim .node{opacity:.13} #graph.dim .edge{opacity:.035}
#graph .node.lit{opacity:1} #graph .edge.lit{stroke:var(--gold-hi); opacity:.75; stroke-width:1.7}
.glegend{display:flex; flex-wrap:wrap; gap:13px; justify-content:center; margin-top:16px; font-family:var(--mono); font-size:11px; color:var(--ink-dim)}
.glegend i{display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:5px; vertical-align:middle}
.gnote{font-family:var(--mono); font-size:12px; color:var(--ink-faint); text-align:center; margin-top:12px; line-height:1.5}

/* ---- footer ---- */
footer{margin:70px 0 60px; padding-top:30px; border-top:1px solid var(--line); font-size:13.5px; color:var(--ink-dim)}
footer h4{font-family:var(--mono); font-size:11px; letter-spacing:.16em; text-transform:uppercase; color:var(--gold); margin:0 0 12px}
footer code{font-family:var(--mono); font-size:12px; color:var(--sky); background:var(--panel); padding:2px 6px; border-radius:5px}
footer .cav{color:var(--frontier-hi)}
footer ul{margin:8px 0; padding-left:20px} footer li{margin:4px 0}
</style>
</head>
<body>
<div class="wrap">

  <header class="mast">
    <div class="kicker">Картография исследований · 2013 – 2026</div>
    <h1>Атлас казахского&nbsp;NLP</h1>
    <div class="sub-en">The State of Kazakh NLP Research</div>
    <p class="thesis" id="thesis"></p>
  </header>

  <div class="stats" id="stats"></div>

  <div class="orn"><span class="ln"></span><svg width="64" height="22" viewBox="0 0 64 22" fill="none" stroke="#e9b949" stroke-width="1.4"><path d="M32 3v16M32 11c-6 0-9-4-9-7 0-2 1.5-3 3-3 2 0 3 2 2.5 4M32 11c6 0 9-4 9-7 0-2-1.5-3-3-3-2 0-3 2-2.5 4"/><circle cx="32" cy="11" r="2.3" fill="#e9b949" stroke="none"/><path d="M14 11h6M44 11h6"/></svg><span class="ln"></span></div>

  <section>
    <div class="sec-head"><span class="idx">01</span><h2>Хронология поля</h2><span class="sub" id="boom-sub"></span></div>
    <div class="timeline" id="timeline"></div>
    <div class="tl-note">▮ золотом — 2024–2026: эра LLM приходит в казахский</div>
  </section>

  <div class="orn"><span class="ln"></span><svg width="64" height="22" viewBox="0 0 64 22" fill="none" stroke="#e9b949" stroke-width="1.4"><path d="M32 3v16M32 11c-6 0-9-4-9-7 0-2 1.5-3 3-3 2 0 3 2 2.5 4M32 11c6 0 9-4 9-7 0-2-1.5-3-3-3-2 0-3 2-2.5 4"/><circle cx="32" cy="11" r="2.3" fill="#e9b949" stroke="none"/><path d="M14 11h6M44 11h6"/></svg><span class="ln"></span></div>

  <section>
    <div class="sec-head"><span class="idx">02</span><h2>Линия прорывов</h2><span class="sub">мир ⟷ казахский · виден лаг</span></div>
    <div class="chrono-key"><span><b style="color:var(--sky)">🌍 Мир</b></span><span><b style="color:var(--gold)">🇰🇿 Казахстан</b></span></div>
    <div class="chrono" id="chrono"></div>
  </section>

  <div class="orn"><span class="ln"></span><svg width="64" height="22" viewBox="0 0 64 22" fill="none" stroke="#e9b949" stroke-width="1.4"><path d="M32 3v16M32 11c-6 0-9-4-9-7 0-2 1.5-3 3-3 2 0 3 2 2.5 4M32 11c6 0 9-4 9-7 0-2-1.5-3-3-3-2 0-3 2-2.5 4"/><circle cx="32" cy="11" r="2.3" fill="#e9b949" stroke="none"/><path d="M14 11h6M44 11h6"/></svg><span class="ln"></span></div>

  <section>
    <div class="sec-head"><span class="idx">03</span><h2>Территории</h2><span class="sub">по убыванию открытости</span></div>
    <div class="terr" id="territories"></div>
  </section>

  <div class="orn"><span class="ln"></span><svg width="64" height="22" viewBox="0 0 64 22" fill="none" stroke="#e9b949" stroke-width="1.4"><path d="M32 3v16M32 11c-6 0-9-4-9-7 0-2 1.5-3 3-3 2 0 3 2 2.5 4M32 11c6 0 9-4 9-7 0-2-1.5-3-3-3-2 0-3 2-2.5 4"/><circle cx="32" cy="11" r="2.3" fill="#e9b949" stroke="none"/><path d="M14 11h6M44 11h6"/></svg><span class="ln"></span></div>

  <section>
    <div class="sec-head"><span class="idx">04</span><h2>Граф цитирований</h2><span class="sub">размер = влияние · цвет = тема</span></div>
    <div class="graph-wrap"><svg id="graph" xmlns="http://www.w3.org/2000/svg"></svg></div>
    <div class="glegend" id="glegend"></div>
    <div class="gnote" id="gnote"></div>
  </section>

  <div class="orn"><span class="ln"></span><svg width="64" height="22" viewBox="0 0 64 22" fill="none" stroke="#e9b949" stroke-width="1.4"><path d="M32 3v16M32 11c-6 0-9-4-9-7 0-2 1.5-3 3-3 2 0 3 2 2.5 4M32 11c6 0 9-4 9-7 0-2-1.5-3-3-3-2 0-3 2-2.5 4"/><circle cx="32" cy="11" r="2.3" fill="#e9b949" stroke="none"/><path d="M14 11h6M44 11h6"/></svg><span class="ln"></span></div>

  <section>
    <div class="sec-head"><span class="idx">05</span><h2>Флагманские модели</h2><span class="sub">claim ≠ проверено</span></div>
    <div class="tbl-scroll"><table id="flagship"></table></div>
  </section>

  <div class="orn"><span class="ln"></span><svg width="64" height="22" viewBox="0 0 64 22" fill="none" stroke="#e08a4a" stroke-width="1.4"><path d="M32 3v16M32 11c-6 0-9-4-9-7 0-2 1.5-3 3-3 2 0 3 2 2.5 4M32 11c6 0 9-4 9-7 0-2-1.5-3-3-3-2 0-3 2-2.5 4"/><circle cx="32" cy="11" r="2.3" fill="#e08a4a" stroke="none"/><path d="M14 11h6M44 11h6"/></svg><span class="ln"></span></div>

  <section>
    <div class="sec-head"><span class="idx">06</span><h2>Незанятые земли</h2><span class="sub">где открыт контрибьюшен</span></div>
    <div class="gaps" id="gaps"></div>
  </section>

  <div class="orn"><span class="ln"></span><svg width="64" height="22" viewBox="0 0 64 22" fill="none" stroke="#e9b949" stroke-width="1.4"><path d="M32 3v16M32 11c-6 0-9-4-9-7 0-2 1.5-3 3-3 2 0 3 2 2.5 4M32 11c6 0 9-4 9-7 0-2-1.5-3-3-3-2 0-3 2-2.5 4"/><circle cx="32" cy="11" r="2.3" fill="#e9b949" stroke="none"/><path d="M14 11h6M44 11h6"/></svg><span class="ln"></span></div>

  <section>
    <div class="sec-head"><span class="idx">07</span><h2>Корпус работ</h2><span class="sub" id="corpus-sub"></span></div>
    <div class="controls">
      <input id="q" type="text" placeholder="Поиск по названию или автору…" autocomplete="off">
      <select id="sort">
        <option value="date">↓ новее</option>
        <option value="cit">↓ цитирования</option>
        <option value="old">↑ старше</option>
      </select>
    </div>
    <div class="chips" id="chips"></div>
    <p class="count" id="count"></p>
    <div class="plist" id="plist"></div>
  </section>

  <footer id="footer"></footer>
</div>

<script id="atlas-data" type="application/json">__DATA_JSON__</script>
<script>
const DATA = JSON.parse(document.getElementById('atlas-data').textContent);
const P = DATA.papers, META = DATA.category_meta, ORDER = DATA.category_order;
const esc = s => (s||'').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

/* thesis */
document.getElementById('thesis').innerHTML = DATA.thesis
  .replace('речи и машинном переводе','<b>речи и машинном переводе</b>')
  .replace('Токенизация и морфология','<b>Токенизация и морфология</b>');

/* stats */
const years = P.map(p=>p.year).filter(Boolean);
const yMin = Math.min(...years), yMax = Math.max(...years);
const recent = P.filter(p=>p.year>=2024).length;
const pct = Math.round(recent/P.length*100);
const tokN = P.filter(p=>p.categories.includes('tokenization')).length;
const stats = [
  [P.length,'работ в корпусе'],
  [yMin+'–'+yMax,'годы'],
  [pct+'%','за 2024–2026'],
  [tokN,'про токенизацию'],
];
document.getElementById('stats').innerHTML = stats.map(([n,l])=>
  `<div class="stat"><div class="num">${n}</div><div class="lab">${l}</div></div>`).join('');
document.getElementById('boom-sub').textContent = recent+' из '+P.length+' работ — за последние 3 года';

/* timeline */
const byYear = {};
P.forEach(p=>{ if(p.year) byYear[p.year]=(byYear[p.year]||0)+1; });
const yrs = Object.keys(byYear).map(Number).sort((a,b)=>a-b);
const maxY = Math.max(...Object.values(byYear));
document.getElementById('timeline').innerHTML = yrs.map(y=>{
  const c = byYear[y], h = Math.max(3, c/maxY*100), boom = y>=2024;
  return `<div class="tl-bar ${boom?'boom':''}"><span class="v">${c}</span>`
       + `<div class="bar" style="height:${h}%" title="${y}: ${c}"></div>`
       + `<span class="y">${y}</span></div>`;
}).join('');

/* territories */
const catN = {}; ORDER.forEach(c=>catN[c]=0);
P.forEach(p=>p.categories.forEach(c=>{ if(c in catN) catN[c]++; }));
const maxC = Math.max(...Object.values(catN));
document.getElementById('territories').innerHTML = ORDER.filter(c=>catN[c]>0).map(c=>{
  const m = META[c]||{}, n = catN[c], front = !!m.frontier;
  const tag = front
    ? `<span class="frontier-tag">граница</span>`
    : `<span class="dense-tag">${n>=maxC*0.6?'плотно':'есть карта'}</span>`;
  return `<div class="card ${front?'front':''}">
    <div class="top"><span class="ico">${m.icon||'·'}</span><span class="nm">${esc(m.label||c)}</span><span class="ct">${n}</span></div>
    <div class="dens"><i style="width:${Math.max(6,n/maxC*100)}%"></i></div>
    ${front ? `<div class="frontier-note">${esc(m.frontier)}</div>` : `<div>${tag}</div>`}
  </div>`;
}).join('');

/* chronology of breakthroughs */
const MS = DATA.milestones || [];
document.getElementById('chrono').innerHTML = MS.map(m=>{
  const side = m.scope==='kazakh' ? 'kazakh' : 'global';
  const sc = m.scope==='kazakh' ? '🇰🇿 Казахстан' : '🌍 Мир';
  const tag = m.url ? 'a' : 'div';
  const href = m.url ? ` href="${esc(m.url)}" target="_blank" rel="noopener"` : '';
  return `<div class="mile ${side}"><div class="yr"><span>${m.year}</span></div>`
       + `<${tag} class="mE"${href}><div class="sc">${sc}</div><h4>${esc(m.label)}</h4><p>${esc(m.what)}</p></${tag}></div>`;
}).join('');

/* citation graph */
const G = DATA.graph, COL = DATA.category_colors || {};
const graphSvg = document.getElementById('graph');
if(G && G.nodes && G.nodes.length){
  graphSvg.setAttribute('viewBox','0 0 1000 680');
  const parts = [];
  G.edges.forEach(([a,b])=>{
    const na=G.nodes[a], nb=G.nodes[b];
    parts.push(`<line class="edge" data-a="${a}" data-b="${b}" x1="${na.x}" y1="${na.y}" x2="${nb.x}" y2="${nb.y}"/>`);
  });
  G.nodes.forEach((nd,i)=>{
    const col = COL[nd.cat] || '#888';
    const tip = nd.kind==='global'
      ? `${nd.label} (${nd.year}) — цитируется ${nd.indeg} каз. работами`
      : `${nd.title||''} · ${nd.year||''} · ↑${nd.cit||0} цит · in-corpus ${nd.indeg}`;
    const shape = nd.kind==='global'
      ? `<rect x="${nd.x-nd.r}" y="${nd.y-nd.r}" width="${nd.r*2}" height="${nd.r*2}" transform="rotate(45 ${nd.x} ${nd.y})" fill="${col}"/>`
      : `<circle cx="${nd.x}" cy="${nd.y}" r="${nd.r}" fill="${col}"/>`;
    const lab = nd.label
      ? `<text class="${nd.kind==='global'?'glabel':'hub-label'}" x="${nd.x}" y="${nd.y-nd.r-4}" text-anchor="middle">${esc(nd.label)}</text>`
      : '';
    parts.push(`<g class="node" data-i="${i}" data-url="${esc(nd.url||'')}"><title>${esc(tip)}</title>${shape}${lab}</g>`);
  });
  graphSvg.innerHTML = parts.join('');

  const adj = {};
  G.edges.forEach(([a,b])=>{(adj[a]=adj[a]||new Set()).add(b);(adj[b]=adj[b]||new Set()).add(a);});
  const nodeEls=[...graphSvg.querySelectorAll('.node')], edgeEls=[...graphSvg.querySelectorAll('.edge')];
  const lit = i=>{
    graphSvg.classList.add('dim');
    const keep = adj[i] ? new Set(adj[i]) : new Set(); keep.add(i);
    nodeEls.forEach(el=>el.classList.toggle('lit', keep.has(+el.dataset.i)));
    edgeEls.forEach(el=>el.classList.toggle('lit', +el.dataset.a===i || +el.dataset.b===i));
  };
  const clr = ()=>{ graphSvg.classList.remove('dim');
    nodeEls.forEach(e=>e.classList.remove('lit')); edgeEls.forEach(e=>e.classList.remove('lit')); };
  nodeEls.forEach(el=>{
    el.addEventListener('mouseenter', ()=>lit(+el.dataset.i));
    el.addEventListener('mouseleave', clr);
    el.addEventListener('click', ()=>{ const u=el.dataset.url; if(u) window.open(u,'_blank','noopener'); });
  });

  const cats=[...new Set(G.nodes.filter(n=>n.kind==='paper').map(n=>n.cat))];
  document.getElementById('glegend').innerHTML =
    `<span><i style="background:${COL.global||'#f8d986'}"></i>мировой breakthrough</span>`
    + cats.map(c=>`<span><i style="background:${COL[c]||'#888'}"></i>${esc((META[c]||{}).label||c)}</span>`).join('');
  const corpusShown = G.shown - G.globals, hidden = G.total - corpusShown;
  document.getElementById('gnote').textContent =
    `${corpusShown} связанных работ + ${G.globals} мировых хабов · ${G.edge_count} рёбер цитирования · метод: ${G.method}. `
    + `Ещё ${hidden} работ без рёбер — в списке ниже.`;
} else if(graphSvg){
  const sec = graphSvg.closest('section'); if(sec) sec.style.display='none';
}

/* flagship table */
const F = DATA.flagship_models;
let th = `<thead><tr><th>Модель</th><th>Год</th><th>Параметры</th><th>База</th><th>Vocab</th><th>Токенайзер</th><th>Морфология?</th><th>Бенчмарки?</th></tr></thead>`;
let tb = '<tbody>'+F.map(m=>{
  const bench = /нет|ноль/i.test(m.benchmarks) ? `<span class="no">${esc(m.benchmarks)}</span>` : `<span class="yes">${esc(m.benchmarks)}</span>`;
  const morph = /^да/i.test(m.morph_claim) ? `<span class="yes">${esc(m.morph_claim)}</span>` : `<span class="mono">${esc(m.morph_claim)}</span>`;
  return `<tr class="${m.highlight?'hl':''}">
    <td><a href="${esc(m.url)}" target="_blank" rel="noopener"><span class="mdl">${esc(m.name)}</span></a>
        <div class="org">${esc(m.org)}</div>
        <div class="rownote">${esc(m.note)}</div></td>
    <td class="mono">${esc(m.year)}</td><td class="mono">${esc(m.params)}</td><td class="mono">${esc(m.base)}</td>
    <td class="mono">${esc(m.vocab)}</td><td>${esc(m.tokenizer)}</td><td>${morph}</td><td>${bench}</td>
  </tr>`;
}).join('')+'</tbody>';
document.getElementById('flagship').innerHTML = th+tb;

/* gaps */
document.getElementById('gaps').innerHTML = DATA.gaps.map(g=>`
  <div class="gap ${g.yours?'you':''}">
    <div class="mk">${g.yours?'◆ ВЫ ЗДЕСЬ':'○ открыто'}</div>
    <div class="body"><h3>${esc(g.title)}</h3><p>${esc(g.why)}</p><span class="eff">${esc(g.effort)}</span></div>
  </div>`).join('');

/* explorer */
let activeCat = null, qStr = '', sortMode = 'date';
const chipDefs = ORDER.filter(c=>catN[c]>0).map(c=>[c, (META[c]||{}).label||c, catN[c]]);
document.getElementById('chips').innerHTML =
  `<button class="chip on" data-c="">все · ${P.length}</button>` +
  chipDefs.map(([c,l,n])=>`<button class="chip" data-c="${c}">${esc(l)} · ${n}</button>`).join('');
document.getElementById('corpus-sub').textContent = 'arXiv + Semantic Scholar · '+P.length+' работ';

function render(){
  let rows = P.filter(p=>{
    if(activeCat && !p.categories.includes(activeCat)) return false;
    if(qStr){
      const blob = (p.title+' '+(p.authors||[]).join(' ')).toLowerCase();
      if(!blob.includes(qStr)) return false;
    }
    return true;
  });
  rows.sort((a,b)=>{
    if(sortMode==='cit') return (b.citation_count||0)-(a.citation_count||0);
    if(sortMode==='old') return (a.date||'9999').localeCompare(b.date||'9999');
    return (b.date||'0').localeCompare(a.date||'0');
  });
  document.getElementById('count').textContent = rows.length+' работ показано';
  document.getElementById('plist').innerHTML = rows.map(p=>{
    const cit = (p.citation_count!=null) ? `<span class="cit">↑${p.citation_count}</span>` : '';
    const au = (p.authors||[]).slice(0,3).join(', ') + ((p.authors||[]).length>3?' et al.':'');
    const tags = (p.categories||[]).map(c=>`<span class="tg">${esc((META[c]||{}).label||c)}</span>`).join('');
    return `<a class="paper" href="${esc(p.url)}" target="_blank" rel="noopener">
      <div class="pt">${esc(p.title)}</div>
      <div class="meta"><span>${p.year||'—'}</span><span>${esc(au)}</span>${cit}<span>${esc(p.venue||'')}</span></div>
      <div class="ab">${esc(p.abstract||'')}</div>
      <div class="tags">${tags}</div>
    </a>`;
  }).join('');
}
document.getElementById('chips').addEventListener('click', e=>{
  const b = e.target.closest('.chip'); if(!b) return;
  document.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));
  b.classList.add('on'); activeCat = b.dataset.c||null; render();
});
document.getElementById('q').addEventListener('input', e=>{ qStr=e.target.value.toLowerCase().trim(); render(); });
document.getElementById('sort').addEventListener('change', e=>{ sortMode=e.target.value; render(); });
render();

/* footer */
document.getElementById('footer').innerHTML = `
  <h4>Как построен этот атлас</h4>
  <p>Корпус собран скриптом <code>scrape_papers.py</code> из двух источников: arXiv API и Semantic Scholar Graph API.
  Scope — только казахский язык (фильтр: упоминание Kazakh/Qazaq + NLP/ML-релевантность). Дедуп по arXiv-id / DOI / названию,
  авто-тэггинг по ключевым словам. Редакторский слой (флагманы, незанятые земли) — ручная верификация по первоисточникам
  (config.json, model cards, paper'ы), <code>build_map.py</code>.</p>
  <p class="cav">⚠ Ограничения честно: Semantic Scholar частично отдал HTTP 429 (rate-limit) — non-arXiv покрытие в
  категориях tokenization/LLM/morphology/NER неполное. Авто-тэги — эвристика по абстракту, не ручная разметка.
  Флагманский claim-столбец отражает заявления авторов, не проверенную истину. Скрипт идемпотентный — дозапуск пополнит корпус.</p>
  <p>Источники сырых данных: <a href="http://export.arxiv.org/api/query" target="_blank" rel="noopener">arXiv API</a> ·
  <a href="https://api.semanticscholar.org" target="_blank" rel="noopener">Semantic Scholar</a> ·
  gold-стандарт морфологии: <a href="https://github.com/UniversalDependencies/UD_Kazakh-KTB" target="_blank" rel="noopener">UD_Kazakh-KTB</a>,
  <a href="https://wiki.apertium.org/wiki/Apertium-kaz" target="_blank" rel="noopener">apertium-kaz</a>.</p>
`;
</script>
</body>
</html>
"""


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #


def trim_paper(p: dict) -> dict:
    """Keep only what the UI renders; cap abstract to keep the file lean."""
    abstract = (p.get("abstract") or "").strip()
    if len(abstract) > 300:
        abstract = abstract[:297].rstrip() + "…"
    return {
        "title": p.get("title", ""),
        "authors": (p.get("authors") or [])[:5],
        "year": p.get("year"),
        "date": p.get("date"),
        "url": p.get("url", ""),
        "venue": p.get("venue") or "",
        "citation_count": p.get("citation_count"),
        "categories": p.get("categories") or [],
        "abstract": abstract,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Render the Kazakh-NLP research atlas.")
    parser.add_argument("--data", type=Path, default=Path("paper/survey/papers.json"))
    parser.add_argument("--out", type=Path, default=Path("paper/survey/index.html"))
    args = parser.parse_args()

    if not args.data.exists():
        raise SystemExit(f"missing corpus: {args.data} (run scrape_papers.py first)")

    raw = json.loads(args.data.read_text(encoding="utf-8"))
    papers = [trim_paper(p) for p in raw.get("papers", [])]

    # optional citation graph (built by scrape_citations.py)
    graph = None
    cit_path = args.data.parent / "citations.json"
    if cit_path.exists():
        try:
            cit = json.loads(cit_path.read_text(encoding="utf-8"))
            graph = compute_graph(raw.get("papers", []), cit)
            if graph:
                print(f"[graph] {graph['shown']} nodes, {graph['edge_count']} edges "
                      f"(method={graph['method']})", file=sys.stderr)
        except (ImportError, KeyError, ValueError, TypeError) as exc:
            print(f"[warn] graph build skipped: {exc}", file=sys.stderr)
    else:
        print("[graph] no citations.json -> graph section disabled", file=sys.stderr)

    bundle = {
        "papers": papers,
        "category_meta": CATEGORY_META,
        "category_order": CATEGORY_ORDER,
        "category_colors": CATEGORY_COLORS,
        "flagship_models": FLAGSHIP_MODELS,
        "gaps": GAPS,
        "milestones": MILESTONES,
        "graph": graph,
        "thesis": THESIS,
        "meta": raw.get("meta", {}),
    }

    data_json = json.dumps(bundle, ensure_ascii=False)
    # safe-embed inside <script>: neutralise any literal </script> in abstracts
    data_json = data_json.replace("</", "<\\/")

    html = TEMPLATE.replace("__DATA_JSON__", data_json)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(html, encoding="utf-8")
    kb = len(html.encode("utf-8")) / 1024
    print(f"[done] {len(papers)} papers -> {args.out}  ({kb:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
