// Build the citation graph for react-force-graph-2d from the scraped data.
// No layout here — the force simulation runs live on the client (that is what
// finally kills the hairball: physics + zoom + drag instead of a static dump).

import citationsRaw from "@/data/citations.json";
import papersRaw from "@/data/papers.json";
import type { CitationsFile, GraphData, GraphLink, GraphNode, Paper, PapersFile } from "./types";

/** Stable node id — MUST match canonical_id in the Python scrapers. */
function canonicalId(arxivId: string | null | undefined, doi: string | null | undefined, title: string): string {
  if (arxivId) return `arxiv:${arxivId}`;
  if (doi) return `doi:${doi.toLowerCase()}`;
  return "title:" + title.toLowerCase().replace(/[^a-z0-9]+/g, " ").trim();
}

let cached: GraphData | null = null;

export function buildGraph(): GraphData {
  if (cached) return cached;

  const papers: Paper[] = (papersRaw as unknown as PapersFile).papers;
  const cit = citationsRaw as unknown as CitationsFile;

  const pmap = new Map<string, Paper>();
  for (const p of papers) pmap.set(canonicalId(p.arxiv_id, p.doi, p.title), p);

  const indeg = new Map<string, number>();
  const appears = new Set<string>();
  for (const [a, b] of cit.edges) {
    appears.add(a);
    appears.add(b);
    indeg.set(b, (indeg.get(b) ?? 0) + 1);
  }

  const corpusIds = [...appears].filter((n) => !n.startsWith("global:") && pmap.has(n));
  const globalIds = Object.keys(cit.global_nodes).filter((g) => appears.has(g));
  const includedIds = new Set<string>([...corpusIds, ...globalIds]);

  const nodes: GraphNode[] = [];
  const nodeById = new Map<string, GraphNode>();

  for (const id of corpusIds) {
    const p = pmap.get(id);
    if (!p) continue;
    const ind = indeg.get(id) ?? 0;
    const c = cit.node_citations[id] ?? p.citation_count ?? 0;
    const node: GraphNode = {
      id, kind: "paper", cat: p.categories[0] ?? "other",
      title: p.title, year: p.year, citations: c || null, indeg: ind,
      url: p.url, val: Math.max(1, ind * 3 + c * 0.08), neighbors: [], links: [],
    };
    nodes.push(node);
    nodeById.set(id, node);
  }
  for (const id of globalIds) {
    const g = cit.global_nodes[id];
    const cb = indeg.get(id) ?? 0;
    const node: GraphNode = {
      id, kind: "global", cat: "global", label: g.label, title: g.label,
      year: g.year, citations: null, indeg: cb,
      url: `https://arxiv.org/abs/${g.arxiv}`, val: Math.max(3, cb * 1.6),
      neighbors: [], links: [],
    };
    nodes.push(node);
    nodeById.set(id, node);
  }

  // label the 12 most influential papers (every global already has a label)
  const ranked = nodes.filter((n) => n.kind === "paper").sort((a, b) => b.val - a.val);
  for (const n of ranked.slice(0, 12)) {
    n.label = n.title.length > 32 ? n.title.slice(0, 32) + "…" : n.title;
  }

  const links: GraphLink[] = [];
  for (const [a, b] of cit.edges) {
    if (!includedIds.has(a) || !includedIds.has(b)) continue;
    const sa = nodeById.get(a);
    const tb = nodeById.get(b);
    if (!sa || !tb) continue;
    const link: GraphLink = { source: a, target: b };
    links.push(link);
    sa.neighbors!.push(tb);
    tb.neighbors!.push(sa);
    sa.links!.push(link);
    tb.links!.push(link);
  }

  cached = {
    nodes, links, method: cit.method,
    shown: nodes.length, globals: globalIds.length,
    total: papers.length, edgeCount: links.length,
  };
  return cached;
}
