// Kazakh koshkar-muyiz (ram's horn) motif — a quiet section divider.

export function Ornament({ color = "#e9b949" }: { color?: string }) {
  return (
    <div className="orn">
      <span className="ln" />
      <svg width="64" height="22" viewBox="0 0 64 22" fill="none" stroke={color} strokeWidth="1.4">
        <path d="M32 3v16M32 11c-6 0-9-4-9-7 0-2 1.5-3 3-3 2 0 3 2 2.5 4M32 11c6 0 9-4 9-7 0-2-1.5-3-3-3-2 0-3 2-2.5 4" />
        <circle cx="32" cy="11" r="2.3" fill={color} stroke="none" />
        <path d="M14 11h6M44 11h6" />
      </svg>
      <span className="ln" />
    </div>
  );
}
