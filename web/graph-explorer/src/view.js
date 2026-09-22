import Sigma from "sigma";
import { TYPE_COLORS, TYPE_NAMES, DEFAULT_HIDDEN_TYPES, graphColor, escapeHtml, scoreNode } from "./config.js";

export function createView(model, state) {
  const $ = (id) => document.getElementById(id);
  const els = {
    container: $("sigma-container"), homeLink: $("homeLink"), focusInput: $("focusInput"), nodeList: $("nodeList"),
    focusBtn: $("focusBtn"), openBtn: $("openBtn"), resetCameraBtn: $("resetCameraBtn"), modeSwitch: $("modeSwitch"),
    modeHint: $("modeHint"), egoControls: $("egoControls"), hop1: $("hop1"), hop2: $("hop2"), typeFilters: $("typeFilters"),
    relationFilters: $("relationFilters"), allTypesBtn: $("allTypesBtn"), allRelationsBtn: $("allRelationsBtn"),
    communityList: $("communityList"), communityCount: $("communityCount"), selectionCard: $("selectionCard"),
    pathFrom: $("pathFrom"), pathTo: $("pathTo"), pathBtn: $("pathBtn"), clearPathBtn: $("clearPathBtn"),
    pathResult: $("pathResult"), stats: $("stats"), status: $("status"), legend: $("legend"),
  };
  els.homeLink.href = `${model.data.basePath || ""}/`;

  const cssVar = (name) => getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  const renderer = new Sigma(model.graph, els.container, {
    renderEdgeLabels: false, labelDensity: 0.08, labelGridCellSize: 82, labelRenderedSizeThreshold: 7,
    defaultEdgeColor: cssVar("--edge"), defaultNodeColor: TYPE_COLORS.other,
    zIndex: true, minCameraRatio: 0.025, maxCameraRatio: 8,
  });

  const edgeAllowed = (edge) => (edge.types?.length ? edge.types : ["wikilink"]).some((type) => state.enabledRelations.has(type));
  const nodeAllowed = (node) => Boolean(node) && state.enabledTypes.has(node.type || "other");

  function visibleEgoNodes() {
    if (!state.focus || !model.byId.has(state.focus)) return new Set();
    const levels = new Map([[state.focus, 0]]), queue = [state.focus];
    while (queue.length) {
      const current = queue.shift();
      const level = levels.get(current);
      if (level >= state.hops) continue;
      for (const item of model.adjacency.get(current) || []) {
        if (!edgeAllowed(item.edge) || !nodeAllowed(model.byId.get(item.id)) || levels.has(item.id)) continue;
        levels.set(item.id, level + 1);
        queue.push(item.id);
      }
    }
    let ids = [...levels].map(([id]) => id).filter((id) => id === state.focus || nodeAllowed(model.byId.get(id)));
    const cap = state.hops === 1 ? 100 : 260;
    if (ids.length > cap) ids = [state.focus, ...ids.filter((id) => id !== state.focus)
      .sort((a, b) => scoreNode(model.byId.get(b)) - scoreNode(model.byId.get(a))).slice(0, cap - 1)];
    return new Set(ids);
  }

  function renderGraph() {
    const visibleNodes = state.mode === "ego" ? visibleEgoNodes() : new Set(model.nodes.filter(nodeAllowed).map((n) => n.id));
    const visibleEdges = new Set();
    for (const [key, edge] of model.edgeByKey) {
      if (visibleNodes.has(edge.source) && visibleNodes.has(edge.target) && edgeAllowed(edge)) visibleEdges.add(key);
    }
    const pathMode = state.pathNodes.size > 0;
    renderer.setSetting("nodeReducer", (id, attrs) => {
      if (!visibleNodes.has(id)) return { ...attrs, hidden: true };
      const raw = model.byId.get(id);
      const inPath = state.pathNodes.has(id);
      const inCommunity = state.community == null || String(attrs.community) === String(state.community);
      const faded = (pathMode && !inPath) || (state.community != null && !inCommunity);
      const boosted = id === state.focus ? 1.75 : id === state.hovered ? 1.45 : inPath ? 1.32 : 1;
      return {
        ...attrs, hidden: false, color: faded ? "rgba(123,132,144,0.18)" : graphColor(raw), size: attrs.size * boosted,
        forceLabel: Boolean(id === state.focus || id === state.hovered || inPath || attrs.size >= 8.2),
        label: faded ? null : attrs.label, zIndex: id === state.focus ? 5 : id === state.hovered ? 4 : inPath ? 3 : 1,
      };
    });
    renderer.setSetting("edgeReducer", (key, attrs) => {
      if (!visibleEdges.has(key)) return { ...attrs, hidden: true };
      const edge = model.edgeByKey.get(key);
      const inPath = state.pathEdges.has(key);
      const sourceCommunity = String(model.graph.getNodeAttribute(edge.source, "community"));
      const targetCommunity = String(model.graph.getNodeAttribute(edge.target, "community"));
      const inCommunity = state.community == null || sourceCommunity === String(state.community) || targetCommunity === String(state.community);
      const faded = (state.pathEdges.size > 0 && !inPath) || (state.community != null && !inCommunity);
      const touchesFocus = edge.source === state.focus || edge.target === state.focus || edge.source === state.hovered || edge.target === state.hovered;
      const color = inPath
        ? cssVar("--path")
        : faded
          ? cssVar("--edge-faded")
          : touchesFocus
            ? cssVar("--edge-focus")
            : attrs.typed
              ? cssVar("--edge-typed")
              : cssVar("--edge");
      return {
        ...attrs, hidden: false, color,
        size: inPath ? 3.4 : touchesFocus ? 2.05 : attrs.typed ? 1.45 : 0.72,
        zIndex: inPath ? 5 : touchesFocus ? 3 : attrs.typed ? 1 : 0,
      };
    });
    renderer.refresh();
    els.stats.textContent = `${visibleNodes.size} nodes · ${visibleEdges.size} edges · ${model.communities.length} galaxies`;
    els.modeHint.textContent = state.mode === "galaxy" ? "全局生态" : `${state.hops}-hop 邻域`;
    els.status.textContent = state.mode === "galaxy"
      ? `Galaxy · Louvain 自动识别 ${model.communities.length} 个生态社区`
      : `Ego · ${model.byId.get(state.focus)?.name || "未选择"} · ${state.hops}-hop`;
  }

  function updateModeControls() {
    els.modeSwitch.querySelectorAll("button[data-mode]").forEach((button) => button.classList.toggle("active", button.dataset.mode === state.mode));
    els.egoControls.classList.toggle("hidden", state.mode !== "ego");
    els.hop1.classList.toggle("active", state.hops === 1);
    els.hop2.classList.toggle("active", state.hops === 2);
  }

  function renderSelection() {
    const node = model.byId.get(state.focus);
    if (!node) {
      els.selectionCard.className = "selection-card empty";
      els.selectionCard.textContent = "点击星系中的节点查看详情。";
      return;
    }
    const community = model.communityById.get(String(model.graph.getNodeAttribute(node.id, "community")));
    const tags = [...new Set([...(node.areas || []), ...(node.communities || []), node.layer].filter(Boolean))].slice(0, 7);
    els.selectionCard.className = "selection-card";
    els.selectionCard.innerHTML = `
      <div class="selection-title"><div><div class="selection-type">${escapeHtml(TYPE_NAMES[node.type] || node.type)}</div><h2>${escapeHtml(node.name)}</h2></div><span class="micro">${escapeHtml(community?.name || "Galaxy")}</span></div>
      <div class="selection-metrics"><div class="metric"><strong>${node.degree || 0}</strong><span>degree</span></div><div class="metric"><strong>${Number(node.bridgeScore || 0).toFixed(1)}</strong><span>bridge</span></div><div class="metric"><strong>${node.crossCategoryDegree || 0}</strong><span>cross</span></div></div>
      ${tags.length ? `<div class="tag-row">${tags.map((tag) => `<span class="tag">${escapeHtml(tag)}</span>`).join("")}</div>` : ""}`;
  }

  function renderCommunities(onClick) {
    els.communityCount.textContent = String(model.communities.length);
    els.communityList.innerHTML = model.communities.slice(0, 18).map((community) => {
      const anchor = model.byId.get(community.anchorId);
      return `<button class="community-item ${state.community === community.id ? "active" : ""}" data-community="${escapeHtml(community.id)}"><span class="community-orbit" style="background:${graphColor(anchor)}"></span><span class="community-copy"><strong>${escapeHtml(community.name)}</strong><span>${escapeHtml(community.subtitle)}</span></span><span class="community-count">${community.size}</span></button>`;
    }).join("");
    els.communityList.querySelectorAll("[data-community]").forEach((button) => button.addEventListener("click", () => onClick(button.dataset.community)));
  }

  function buildFilters(onChange) {
    els.typeFilters.innerHTML = "";
    for (const type of model.nodeTypes) {
      const button = document.createElement("button");
      button.className = `chip${state.enabledTypes.has(type) ? " active" : ""}`;
      button.textContent = TYPE_NAMES[type] || type;
      button.onclick = () => {
        state.enabledTypes.has(type) ? state.enabledTypes.delete(type) : state.enabledTypes.add(type);
        button.classList.toggle("active", state.enabledTypes.has(type)); onChange();
      };
      els.typeFilters.appendChild(button);
    }
    els.relationFilters.innerHTML = "";
    for (const type of model.relationTypes) {
      const button = document.createElement("button");
      button.className = `chip${state.enabledRelations.has(type) ? " active" : ""}`;
      button.textContent = type;
      button.onclick = () => {
        state.enabledRelations.has(type) ? state.enabledRelations.delete(type) : state.enabledRelations.add(type);
        button.classList.toggle("active", state.enabledRelations.has(type)); onChange();
      };
      els.relationFilters.appendChild(button);
    }
  }

  function fillNodeList() {
    const seen = new Set(), options = [];
    for (const node of model.nodes.slice().sort((a, b) => a.name.localeCompare(b.name))) {
      for (const label of [node.name, ...(node.aliases || [])]) {
        if (!label || seen.has(label)) continue;
        seen.add(label);
        options.push(`<option value="${escapeHtml(label)}">${escapeHtml(TYPE_NAMES[node.type] || node.type)} · ${escapeHtml(node.id)}</option>`);
      }
    }
    els.nodeList.innerHTML = options.join("");
    const important = model.nodeTypes.filter((type) => !DEFAULT_HIDDEN_TYPES.has(type)).slice(0, 9);
    els.legend.innerHTML = important.map((type) => `<span class="legend-item"><span class="legend-dot" style="background:${TYPE_COLORS[type] || TYPE_COLORS.other}"></span>${escapeHtml(TYPE_NAMES[type] || type)}</span>`).join("");
  }

  return { els, renderer, renderGraph, updateModeControls, renderSelection, renderCommunities, buildFilters, fillNodeList };
}
