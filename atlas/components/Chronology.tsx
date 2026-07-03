import { MILESTONES } from "@/lib/curated";

export function Chronology() {
  return (
    <>
      <div className="chrono-key">
        <span><b style={{ color: "var(--sky)" }}>🌍 Мир</b></span>
        <span><b style={{ color: "var(--gold)" }}>🇰🇿 Казахстан</b></span>
      </div>
      <div className="chrono">
        {MILESTONES.map((m, i) => {
          const inner = (
            <>
              <div className="sc">{m.scope === "kazakh" ? "🇰🇿 Казахстан" : "🌍 Мир"}</div>
              <h4>{m.label}</h4>
              <p>{m.what}</p>
            </>
          );
          return (
            <div key={`${m.year}-${i}`} className={`mile ${m.scope}`}>
              <div className="yr"><span>{m.year}</span></div>
              {m.url ? (
                <a className="mE" href={m.url} target="_blank" rel="noopener noreferrer">{inner}</a>
              ) : (
                <div className="mE">{inner}</div>
              )}
            </div>
          );
        })}
      </div>
    </>
  );
}
