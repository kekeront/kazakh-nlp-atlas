"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export function Nav() {
  const path = usePathname();
  return (
    <nav className="nav">
      <div className="nav-in">
        <Link href="/" className={path === "/" ? "on" : ""}>Атлас казахского NLP</Link>
        <Link href="/contribute" className={path === "/contribute" ? "on" : ""}>
          Что делать сейчас →
        </Link>
      </div>
    </nav>
  );
}
