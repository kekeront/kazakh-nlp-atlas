import { GAPS } from "@/lib/curated";

export function GapMap() {
  return (
    <div className="gaps">
      {GAPS.map((g, i) => (
        <div key={i} className={`gap ${g.yours ? "you" : ""}`}>
          <div className="mk">{g.yours ? "◆ ВЫ ЗДЕСЬ" : "○ открыто"}</div>
          <div className="body">
            <h3>{g.title}</h3>
            <p>{g.why}</p>
            <span className="eff">{g.effort}</span>
          </div>
        </div>
      ))}
    </div>
  );
}
