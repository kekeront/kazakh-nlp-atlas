"use client";

import { useMemo, useState } from "react";
import { CATEGORY_META, CATEGORY_ORDER } from "@/lib/curated";
import { categoryCounts, PAPERS } from "@/lib/data";

type SortMode = "date" | "cit" | "old";

const trunc = (s: string, n: number) => (s.length > n ? s.slice(0, n - 1) + "…" : s);

export function PaperExplorer() {
  const [q, setQ] = useState("");
  const [cat, setCat] = useState<string | null>(null);
  const [sort, setSort] = useState<SortMode>("date");
  const counts = useMemo(() => categoryCounts(), []);

  const rows = useMemo(() => {
    const filtered = PAPERS.filter((p) => {
      if (cat && !p.categories.includes(cat)) return false;
      if (q) {
        const blob = `${p.title} ${p.authors.join(" ")}`.toLowerCase();
        if (!blob.includes(q)) return false;
      }
      return true;
    });
    return filtered.sort((a, b) => {
      if (sort === "cit") return (b.citation_count ?? 0) - (a.citation_count ?? 0);
      if (sort === "old") return (a.date ?? "9999").localeCompare(b.date ?? "9999");
      return (b.date ?? "0").localeCompare(a.date ?? "0");
    });
  }, [q, cat, sort]);

  const chips = CATEGORY_ORDER.filter((c) => (counts[c] ?? 0) > 0);

  return (
    <>
      <div className="controls">
        <input
          value={q}
          onChange={(e) => setQ(e.target.value.toLowerCase().trim())}
          placeholder="Поиск по названию или автору…"
        />
        <select value={sort} onChange={(e) => setSort(e.target.value as SortMode)}>
          <option value="date">↓ новее</option>
          <option value="cit">↓ цитирования</option>
          <option value="old">↑ старше</option>
        </select>
      </div>
      <div className="chips">
        <button className={`chip ${cat === null ? "on" : ""}`} onClick={() => setCat(null)}>
          все · {PAPERS.length}
        </button>
        {chips.map((c) => (
          <button key={c} className={`chip ${cat === c ? "on" : ""}`} onClick={() => setCat(c)}>
            {CATEGORY_META[c]?.label ?? c} · {counts[c]}
          </button>
        ))}
      </div>
      <p className="count">{rows.length} работ показано</p>
      <div className="plist">
        {rows.map((p, i) => {
          const au = p.authors.slice(0, 3).join(", ") + (p.authors.length > 3 ? " et al." : "");
          return (
            <a
              key={`${p.arxiv_id || p.doi || p.title}-${i}`}
              className="paper"
              href={p.url}
              target="_blank"
              rel="noopener noreferrer"
            >
              <div className="pt">{p.title}</div>
              <div className="meta">
                <span>{p.year ?? "—"}</span>
                <span>{au}</span>
                {p.citation_count != null && <span className="cit">↑{p.citation_count}</span>}
                {p.venue && <span>{p.venue}</span>}
              </div>
              <div className="ab">{trunc(p.abstract, 260)}</div>
              <div className="tags">
                {p.categories.map((c) => (
                  <span className="tg" key={c}>{CATEGORY_META[c]?.label ?? c}</span>
                ))}
              </div>
            </a>
          );
        })}
      </div>
    </>
  );
}
