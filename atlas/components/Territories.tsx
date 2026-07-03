import { CATEGORY_META, CATEGORY_ORDER } from "@/lib/curated";
import { categoryCounts } from "@/lib/data";

export function Territories() {
  const counts = categoryCounts();
  const max = Math.max(...Object.values(counts));

  return (
    <div className="terr">
      {CATEGORY_ORDER.filter((c) => (counts[c] ?? 0) > 0).map((c) => {
        const m = CATEGORY_META[c];
        const n = counts[c];
        const front = !!m?.frontier;
        return (
          <div key={c} className={`card ${front ? "front" : ""}`}>
            <div className="top">
              <span className="ico">{m?.icon ?? "·"}</span>
              <span className="nm">{m?.label ?? c}</span>
              <span className="ct">{n}</span>
            </div>
            <div className="dens">
              <i style={{ width: `${Math.max(6, (n / max) * 100)}%` }} />
            </div>
            {front ? (
              <div className="frontier-note">{m!.frontier}</div>
            ) : (
              <div>
                <span className="dense-tag">{n >= max * 0.6 ? "плотно" : "есть карта"}</span>
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
