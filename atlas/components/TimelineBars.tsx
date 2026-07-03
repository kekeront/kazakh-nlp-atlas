import { PAPERS } from "@/lib/data";

export function TimelineBars() {
  const byYear: Record<number, number> = {};
  for (const p of PAPERS) if (p.year) byYear[p.year] = (byYear[p.year] ?? 0) + 1;
  const yrs = Object.keys(byYear).map(Number).sort((a, b) => a - b);
  const max = Math.max(...Object.values(byYear));

  return (
    <>
      <div className="timeline">
        {yrs.map((y) => {
          const c = byYear[y];
          const h = Math.max(3, (c / max) * 100);
          return (
            <div key={y} className={`tl-bar ${y >= 2024 ? "boom" : ""}`}>
              <span className="v">{c}</span>
              <div className="bar" style={{ height: `${h}%` }} title={`${y}: ${c}`} />
              <span className="y">{y}</span>
            </div>
          );
        })}
      </div>
      <div className="tl-note">▮ золотом — 2024–2026: эра LLM приходит в казахский</div>
    </>
  );
}
