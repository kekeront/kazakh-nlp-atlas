"use client";

import dynamic from "next/dynamic";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { ForwardRefExoticComponent, RefAttributes } from "react";
import type {
  ForceGraphMethods,
  ForceGraphProps,
  LinkObject,
  NodeObject,
} from "react-force-graph-2d";
import { CATEGORY_COLORS, CATEGORY_META } from "@/lib/curated";
import { buildGraph } from "@/lib/graph";
import type { GraphLink, GraphNode } from "@/lib/types";

// react-force-graph-2d paints to <canvas> and touches `window`, so it must be
// client-only. next/dynamic strips its ref typing, so we re-assert it here —
// the single library boundary. All graph logic is fully typed.
const ForceGraph2D = dynamic(() => import("react-force-graph-2d"), {
  ssr: false,
}) as unknown as ForwardRefExoticComponent<ForceGraphProps & RefAttributes<ForceGraphMethods>>;

function radius(n: GraphNode): number {
  return Math.sqrt(Math.max(1, n.val)) * (n.kind === "global" ? 1.6 : 1.1) + 2;
}

export function CitationGraph() {
  const data = useMemo(() => buildGraph(), []);
  const fgRef = useRef<ForceGraphMethods | null>(null);
  const wrapRef = useRef<HTMLDivElement>(null);
  const [dims, setDims] = useState({ w: 1000, h: 640 });
  const [hoverNode, setHoverNode] = useState<GraphNode | null>(null);
  const [hlNodes, setHlNodes] = useState<Set<GraphNode>>(new Set());
  const [hlLinks, setHlLinks] = useState<Set<GraphLink>>(new Set());

  useEffect(() => {
    const el = wrapRef.current;
    if (!el) return;
    const apply = () => setDims({ w: el.clientWidth, h: el.clientHeight });
    apply();
    const ro = new ResizeObserver(apply);
    ro.observe(el);
    return () => ro.disconnect();
  }, []);

  const onHover = useCallback((node: NodeObject | null) => {
    const n = node as GraphNode | null;
    const nn = new Set<GraphNode>();
    const nl = new Set<GraphLink>();
    if (n) {
      nn.add(n);
      n.neighbors?.forEach((x) => nn.add(x));
      n.links?.forEach((l) => nl.add(l));
    }
    setHlNodes(nn);
    setHlLinks(nl);
    setHoverNode(n);
  }, []);

  // De-cluster the dense core: stronger repulsion + longer links than the
  // d3 defaults (charge ~-30, link ~30), so 119 nodes spread instead of piling.
  const configureForces = useCallback((fg: ForceGraphMethods | null) => {
    fgRef.current = fg;
    if (!fg) return;
    // d3-force objects carry .strength()/.distance() at runtime, but the lib
    // types them only as the callable ForceFn — cast through unknown to reach them.
    const charge = fg.d3Force("charge");
    if (charge) (charge as unknown as { strength: (s: number) => void }).strength(-145);
    const link = fg.d3Force("link");
    if (link) (link as unknown as { distance: (d: number) => void }).distance(46);
    fg.d3ReheatSimulation();
  }, []);

  const dimmed = hoverNode != null;

  const paintNode = useCallback(
    (obj: NodeObject, ctx: CanvasRenderingContext2D, scale: number) => {
      const n = obj as GraphNode;
      const r = radius(n);
      const active = !dimmed || hlNodes.has(n);
      const x = n.x ?? 0;
      const y = n.y ?? 0;
      ctx.globalAlpha = active ? 1 : 0.12;
      ctx.fillStyle = CATEGORY_COLORS[n.cat] ?? "#888";
      if (n.kind === "global") {
        ctx.save();
        ctx.translate(x, y);
        ctx.rotate(Math.PI / 4);
        ctx.fillRect(-r, -r, r * 2, r * 2);
        ctx.restore();
      } else {
        ctx.beginPath();
        ctx.arc(x, y, r, 0, 2 * Math.PI);
        ctx.fill();
      }
      const showLabel = (n.label || n === hoverNode || hlNodes.has(n)) && active;
      if (showLabel && scale > 0.45) {
        const label = n.label ?? n.title.slice(0, 28);
        const fs = Math.max(8.5, (n.kind === "global" ? 11 : 9) / scale);
        ctx.font = `${fs}px ui-monospace, monospace`;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillStyle = n.kind === "global" ? "#f8d986" : "#cfc6ac";
        ctx.globalAlpha = active ? 0.95 : 0.1;
        ctx.fillText(label, x, y - r - fs * 0.7);
      }
      ctx.globalAlpha = 1;
    },
    [dimmed, hlNodes, hoverNode],
  );

  const cats = useMemo(
    () => [...new Set(data.nodes.filter((n) => n.kind === "paper").map((n) => n.cat))],
    [data],
  );
  const corpusShown = data.shown - data.globals;

  return (
    <>
      <div className="graph-wrap" ref={wrapRef}>
        <div className="graph-hint">наведи на узел · колесо = зум · тащи фон / узлы</div>
        {dims.w > 0 && (
          <ForceGraph2D
            ref={configureForces}
            width={dims.w}
            height={dims.h}
            graphData={{ nodes: data.nodes, links: data.links }}
            backgroundColor="rgba(0,0,0,0)"
            nodeRelSize={1}
            nodeVal={(n: NodeObject) => Math.max(1, (n as GraphNode).val)}
            nodeLabel={(n: NodeObject) => {
              const g = n as GraphNode;
              return g.kind === "global"
                ? `${g.label} — цитируется ${g.indeg} каз. работами`
                : `${g.title} · ${g.year ?? ""} · ↑${g.citations ?? 0} · in-corpus ${g.indeg}`;
            }}
            nodeCanvasObject={paintNode}
            nodePointerAreaPaint={(obj: NodeObject, color: string, ctx: CanvasRenderingContext2D) => {
              const n = obj as GraphNode;
              const r = radius(n);
              ctx.fillStyle = color;
              ctx.beginPath();
              ctx.arc(n.x ?? 0, n.y ?? 0, r + 2, 0, 2 * Math.PI);
              ctx.fill();
            }}
            linkColor={(l: LinkObject) => (hlLinks.has(l as GraphLink) ? "#f8d986" : "rgba(236,225,200,0.10)")}
            linkWidth={(l: LinkObject) => (hlLinks.has(l as GraphLink) ? 1.8 : 0.6)}
            onNodeHover={onHover}
            onNodeClick={(n: NodeObject) => {
              const url = (n as GraphNode).url;
              if (url) window.open(url, "_blank", "noopener");
            }}
            d3VelocityDecay={0.32}
            warmupTicks={100}
            cooldownTicks={220}
            onEngineStop={() => fgRef.current?.zoomToFit(500, 60)}
            autoPauseRedraw={false}
          />
        )}
      </div>

      <div className="glegend">
        <span><i style={{ background: CATEGORY_COLORS.global }} />мировой breakthrough</span>
        {cats.map((c) => (
          <span key={c}>
            <i style={{ background: CATEGORY_COLORS[c] ?? "#888" }} />
            {CATEGORY_META[c]?.label ?? c}
          </span>
        ))}
      </div>
      <div className="gnote">
        {corpusShown} связанных работ + {data.globals} мировых хабов · {data.edgeCount} рёбер
        цитирования · метод: {data.method}. Ещё {data.total - corpusShown} работ без рёбер — в
        списке ниже.
      </div>
    </>
  );
}
