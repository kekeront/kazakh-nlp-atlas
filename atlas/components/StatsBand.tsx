import { PAPERS } from "@/lib/data";

export function StatsBand() {
  const years = PAPERS.map((p) => p.year).filter((y): y is number => !!y);
  const yMin = Math.min(...years);
  const yMax = Math.max(...years);
  const recent = PAPERS.filter((p) => (p.year ?? 0) >= 2024).length;
  const pct = Math.round((recent / PAPERS.length) * 100);
  const tok = PAPERS.filter((p) => p.categories.includes("tokenization")).length;

  const stats: Array<[string | number, string]> = [
    [PAPERS.length, "работ в корпусе"],
    [`${yMin}–${yMax}`, "годы"],
    [`${pct}%`, "за 2024–2026"],
    [tok, "про токенизацию"],
  ];

  return (
    <div className="stats">
      {stats.map(([n, l]) => (
        <div className="stat" key={l}>
          <div className="num">{n}</div>
          <div className="lab">{l}</div>
        </div>
      ))}
    </div>
  );
}
