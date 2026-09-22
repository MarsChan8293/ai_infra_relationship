import { UndirectedGraph } from "graphology";
import louvain from "graphology-communities-louvain";
import forceAtlas2 from "graphology-layout-forceatlas2";
import { COMMUNITY_PRIORITY, hash01, scoreNode, nodeSize, graphColor } from "./config.js";

const GOLDEN_ANGLE = Math.PI * (3 - Math.sqrt(5));

export function createGraphModel(data) {
  const nodes = data.nodes ?? [];
  const edges = data.edges ?? [];
  const byId = new Map(nodes.map((node) => [node.id, node]));
  const edgeByKey = new Map();
  const adjacency = new Map(nodes.map((node) => [node.id, []]));
  const graph = new UndirectedGraph({ allowSelfLoops: false, multi: false });

  for (const node of nodes) {
    const angle = hash01(`${node.id}:angle`) * Math.PI * 2;
    const radius = 15 + hash01(`${node.id}:radius`) * 55;
    graph.addNode(node.id, {
      label: node.name, x: Math.cos(angle) * radius, y: Math.sin(angle) * radius,
      size: nodeSize(node), color: graphColor(node), nodeType: node.type || "other", raw: node,
    });
  }

  for (const [index, edge] of edges.entries()) {
    if (!graph.hasNode(edge.source) || !graph.hasNode(edge.target) || edge.source === edge.target) continue;
    if (graph.hasEdge(edge.source, edge.target)) continue;
    const key = edge.id || `e${index}`;
    graph.addEdgeWithKey(key, edge.source, edge.target, {
      size: edge.typed ? 1.15 : 0.55,
      color: edge.typed ? "rgba(112,132,153,0.46)" : "rgba(126,139,153,0.2)",
      typed: Boolean(edge.typed), relationTypes: edge.types?.length ? edge.types : ["wikilink"],
    });
    edgeByKey.set(key, edge);
    adjacency.get(edge.source)?.push({ id: edge.target, edge, key });
    adjacency.get(edge.target)?.push({ id: edge.source, edge, key });
  }

  assignGalaxyLayout(graph, byId);
  const communities = summarizeCommunities(graph, byId);
  const communityById = new Map(communities.map((item) => [item.id, item]));
  const nodeTypes = [...new Set(nodes.map((node) => node.type || "other"))].sort();
  const relationTypes = [...new Set(edges.flatMap((edge) => edge.types?.length ? edge.types : ["wikilink"]))]
    .sort((a, b) => a === "wikilink" ? 1 : b === "wikilink" ? -1 : a.localeCompare(b));

  return { data, nodes, edges, byId, edgeByKey, adjacency, graph, communities, communityById, nodeTypes, relationTypes };
}

function assignGalaxyLayout(graph, byId) {
  if (!graph.order) return;
  if (graph.size) louvain.assign(graph, { resolution: 1.08 });
  else graph.forEachNode((node) => graph.setNodeAttribute(node, "community", node));

  const groups = new Map();
  graph.forEachNode((node, attrs) => {
    const community = String(attrs.community ?? "0");
    if (!groups.has(community)) groups.set(community, []);
    groups.get(community).push(node);
  });
  const ordered = [...groups.entries()].sort((a, b) => {
    const sum = (ids) => ids.reduce((total, id) => total + scoreNode(byId.get(id)), 0);
    return b[1].length - a[1].length || sum(b[1]) - sum(a[1]);
  });

  ordered.forEach(([community, ids], index) => {
    const centerRadius = index === 0 ? 0 : 145 * Math.sqrt(index);
    const centerAngle = index * GOLDEN_ANGLE;
    const cx = Math.cos(centerAngle) * centerRadius;
    const cy = Math.sin(centerAngle) * centerRadius;
    const cloudRadius = 18 + Math.sqrt(ids.length) * 13;
    ids.forEach((id) => {
      const angle = hash01(`${id}:community-angle`) * Math.PI * 2;
      const radius = Math.sqrt(hash01(`${id}:community-radius`)) * cloudRadius;
      graph.mergeNodeAttributes(id, {
        x: cx + Math.cos(angle) * radius,
        y: cy + Math.sin(angle) * radius,
        community: String(community),
      });
    });
  });

  if (!graph.size) return;
  forceAtlas2.assign(graph, {
    iterations: graph.order > 1400 ? 70 : graph.order > 700 ? 100 : 140,
    settings: {
      ...forceAtlas2.inferSettings(graph), barnesHutOptimize: graph.order > 350,
      gravity: 0.75, scalingRatio: 13, slowDown: 8,
    },
  });
}

function summarizeCommunities(graph, byId) {
  const groups = new Map();
  graph.forEachNode((id, attrs) => {
    const community = String(attrs.community ?? "0");
    if (!groups.has(community)) groups.set(community, []);
    groups.get(community).push(byId.get(id));
  });
  return [...groups.entries()].map(([id, group]) => {
    const ranked = group.slice().sort((a, b) =>
      (COMMUNITY_PRIORITY.get(b.type) || 0) - (COMMUNITY_PRIORITY.get(a.type) || 0) || scoreNode(b) - scoreNode(a));
    const areaCounts = new Map();
    for (const node of group) {
      for (const area of node.areas || []) areaCounts.set(area, (areaCounts.get(area) || 0) + 1);
      if (node.layer) areaCounts.set(node.layer, (areaCounts.get(node.layer) || 0) + 1);
    }
    const topAreas = [...areaCounts].sort((a, b) => b[1] - a[1]).slice(0, 2).map(([area]) => area);
    const anchor = ranked[0];
    return {
      id, size: group.length, anchorId: anchor?.id, name: anchor?.name || `Cluster ${id}`,
      subtitle: topAreas.join(" · ") || anchor?.type || "生态社区",
      score: group.reduce((sum, node) => sum + scoreNode(node), 0),
    };
  }).sort((a, b) => b.size - a.size || b.score - a.score);
}

export function findNode(model, value) {
  const needle = String(value || "").trim().toLowerCase();
  if (!needle) return null;
  const keys = (node) => [node.name, node.id, ...(node.aliases || [])].filter(Boolean).map((v) => String(v).toLowerCase());
  const exact = model.nodes.filter((node) => keys(node).some((key) => key === needle));
  if (exact.length) return exact.sort((a, b) => scoreNode(b) - scoreNode(a))[0];
  return model.nodes.filter((node) => keys(node).some((key) => key.includes(needle)))
    .sort((a, b) => scoreNode(b) - scoreNode(a))[0] || null;
}

export function shortestPath(model, state, fromValue, toValue) {
  const start = findNode(model, fromValue);
  const goal = findNode(model, toValue);
  if (!start || !goal) return { error: "找不到起点或终点。" };
  const nodeAllowed = (node) => Boolean(node) && state.enabledTypes.has(node.type || "other");
  const edgeAllowed = (edge) => (edge.types?.length ? edge.types : ["wikilink"]).some((type) => state.enabledRelations.has(type));
  if (!nodeAllowed(start) || !nodeAllowed(goal)) return { error: "起点或终点被当前节点类型筛选隐藏。" };

  const queue = [start.id];
  const previous = new Map([[start.id, null]]);
  const via = new Map();
  while (queue.length) {
    const current = queue.shift();
    if (current === goal.id) break;
    for (const item of model.adjacency.get(current) || []) {
      if (!edgeAllowed(item.edge) || !nodeAllowed(model.byId.get(item.id)) || previous.has(item.id)) continue;
      previous.set(item.id, current);
      via.set(item.id, item);
      queue.push(item.id);
    }
  }
  if (!previous.has(goal.id)) return { error: "当前筛选条件下没有可达路径。" };
  const ids = [], edgeKeys = [];
  let current = goal.id;
  while (current) {
    ids.push(current);
    const item = via.get(current);
    if (item) edgeKeys.push(item.key);
    current = previous.get(current);
  }
  return { ids: ids.reverse(), edgeKeys: edgeKeys.reverse(), via };
}
