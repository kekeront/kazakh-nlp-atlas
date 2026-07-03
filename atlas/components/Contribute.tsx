import { CATEGORY_COLORS, CATEGORY_META } from "@/lib/curated";
import { HYPOTHESES, PAIN_POINTS } from "@/lib/openProblems";
import type { Citation } from "@/lib/types";

const DIFF: Record<string, string> = { low: "лёгкий старт", medium: "средне", high: "амбициозно" };
const STATUS: Record<string, string> = {
  unverified: "не проверено",
  contested: "оспаривается",
  assumed: "допущение",
};

function Cites({ items }: { items: Citation[] }) {
  if (!items.length) return null;
  return (
    <div className="cites">
      {items.map((c, i) => (
        <a key={i} className="cite" href={c.url} target="_blank" rel="noopener noreferrer" title={c.title}>
          {c.arxiv ? `arXiv:${c.arxiv}` : "источник"} ↗
        </a>
      ))}
    </div>
  );
}

export function PainPointList() {
  return (
    <div className="pp-grid">
      {PAIN_POINTS.map((p, i) => {
        const color = CATEGORY_COLORS[p.category] ?? "#54b9d8";
        return (
          <div key={i} className="pp" style={{ borderTopColor: color }}>
            <div className="pp-top">
              <span className="pp-cat">{CATEGORY_META[p.category]?.label ?? p.category}</span>
              <span className={`diff ${p.difficulty}`}>{DIFF[p.difficulty]}</span>
            </div>
            <h3>{p.title}</h3>
            <p className="det">{p.detail}</p>
            <div className="step"><b>Первый шаг</b>{p.firstStep}</div>
            <Cites items={p.citations} />
          </div>
        );
      })}
    </div>
  );
}

export function HypothesisList() {
  return (
    <div className="hyps">
      {HYPOTHESES.map((h, i) => (
        <div key={i} className="hyp">
          <div className="hyp-top">
            <span className={`status ${h.status}`}>{STATUS[h.status]}</span>
            <span className={`diff ${h.difficulty}`} style={{ marginLeft: "auto" }}>{DIFF[h.difficulty]}</span>
          </div>
          <h3>{h.claim}</h3>
          <p className="det">{h.detail}</p>
          <div className="test"><b>Как проверить</b>{h.howToTest}</div>
          <Cites items={h.citations} />
        </div>
      ))}
    </div>
  );
}
