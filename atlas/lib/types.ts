// Shared types for the Kazakh-NLP atlas. Strong typing throughout — the data
// shapes mirror the scraper output (papers.json) and citation graph (citations.json).

export interface Paper {
  title: string;
  authors: string[];
  year: number | null;
  date: string | null;
  url: string;
  venue: string | null;
  citation_count: number | null;
  categories: string[];
  abstract: string;
  arxiv_id?: string | null;
  doi?: string | null;
}

export interface PapersFile {
  meta: {
    count: number;
    source_breakdown: Record<string, number>;
    category_breakdown: Record<string, number>;
    [k: string]: unknown;
  };
  papers: Paper[];
}

export interface CitationsFile {
  method: string;
  stats: Record<string, number | string>;
  edges: Array<[string, string]>;
  node_citations: Record<string, number>;
  global_nodes: Record<string, { label: string; year: number; arxiv: string }>;
}

export interface Milestone {
  year: number;
  scope: "global" | "kazakh";
  label: string;
  what: string;
  url: string | null;
}

export interface FlagshipModel {
  name: string;
  org: string;
  year: string;
  params: string;
  base: string;
  vocab: string;
  tokenizer: string;
  morphClaim: string;
  benchmarks: string;
  highlight: boolean;
  note: string;
  url: string;
}

export interface Gap {
  title: string;
  yours: boolean;
  why: string;
  effort: string;
}

export interface CategoryMeta {
  label: string;
  icon: string;
  frontier?: string;
}

// ----- citation graph (consumed by react-force-graph-2d) ----- //

export interface GraphNode {
  id: string;
  kind: "paper" | "global";
  cat: string;
  /** always-on label for hubs + global breakthroughs; undefined for the long tail */
  label?: string;
  /** full title (paper) or breakthrough name (global) — used in the tooltip */
  title: string;
  year: number | null;
  citations: number | null;
  indeg: number;
  url: string;
  /** size driver for nodeVal */
  val: number;
  // mutated in at build time (highlight pattern); also x/y/vx/vy added by the sim
  neighbors?: GraphNode[];
  links?: GraphLink[];
  x?: number;
  y?: number;
}

export interface GraphLink {
  source: string | GraphNode;
  target: string | GraphNode;
}

export interface GraphData {
  nodes: GraphNode[];
  links: GraphLink[];
  method: string;
  shown: number;
  globals: number;
  total: number;
  edgeCount: number;
}

// ----- "Что делать сейчас": open problems for first-time contributors ----- //

export type Difficulty = "low" | "medium" | "high";

export interface Citation {
  title: string;
  url: string;
  arxiv: string | null;
}

export interface PainPoint {
  title: string;
  detail: string;
  category: string;
  difficulty: Difficulty;
  firstStep: string;
  citations: Citation[];
}

export interface Hypothesis {
  claim: string;
  status: "unverified" | "contested" | "assumed";
  detail: string;
  howToTest: string;
  difficulty: Difficulty;
  citations: Citation[];
}
