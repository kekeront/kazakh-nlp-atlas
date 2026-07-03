import papersRaw from "@/data/papers.json";
import type { Paper, PapersFile } from "./types";

export const PAPERS: Paper[] = (papersRaw as unknown as PapersFile).papers;

/** Count papers per category (a paper can carry several tags). */
export function categoryCounts(): Record<string, number> {
  const counts: Record<string, number> = {};
  for (const p of PAPERS) {
    for (const c of p.categories) counts[c] = (counts[c] ?? 0) + 1;
  }
  return counts;
}
