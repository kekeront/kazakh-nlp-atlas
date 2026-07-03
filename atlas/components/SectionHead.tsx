export function SectionHead({ idx, title, sub }: { idx: string; title: string; sub?: string }) {
  return (
    <div className="sec-head">
      <span className="idx">{idx}</span>
      <h2>{title}</h2>
      {sub && <span className="sub">{sub}</span>}
    </div>
  );
}
