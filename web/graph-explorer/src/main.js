import "./styles.css";
import { DEFAULT_HIDDEN_TYPES } from "./config.js";
import { createGraphModel, findNode, shortestPath } from "./graph-model.js";
import { createView } from "./view.js";

const data = await fetch("./data.json").then((response) => {
  if (!response.ok) throw new Error(`data.json ${response.status}`);
  return response.json();
});
const model = createGraphModel(data);
const state = {
  mode: "galaxy", hops: 1, focus: null, hovered: null, community: null,
  enabledTypes: new Set(model.nodeTypes.filter((type) => !DEFAULT_HIDDEN_TYPES.has(type))),
  enabledRelations: new Set(model.relationTypes), pathNodes: new Set(), pathEdges: new Set(),
};
const view = createView(model, state);
const { els, renderer } = view;

function initialFocus() {
  const requested = findNode(model, new URLSearchParams(location.search).get("focus"));
  if (requested) return requested.id;
  return model.nodes.filter((node) => node.type === "person").sort((a, b) => (b.bridgeScore || 0) - (a.bridgeScore || 0))[0]?.id || model.nodes[0]?.id || null;
}
state.focus = initialFocus();

function clearPath(render = true) {
  state.pathNodes.clear(); state.pathEdges.clear();
  els.pathResult.textContent = "路径计算遵守当前节点与关系筛选。";
  if (render) view.renderGraph();
}

function focusNode(id, switchToEgo = false) {
  if (!id || !model.graph.hasNode(id)) return;
  state.focus = id; state.community = null;
  if (switchToEgo) state.mode = "ego";
  els.focusInput.value = model.byId.get(id)?.name || id;
  view.updateModeControls(); view.renderSelection(); renderCommunities(); view.renderGraph();
  const display = renderer.getNodeDisplayData(id);
  if (display) renderer.getCamera().animate({ x: display.x, y: display.y, ratio: 0.32 }, { duration: 420 });
  const url = new URL(location.href); url.searchParams.set("focus", id); history.replaceState(null, "", url);
}

function focusCommunity(id) {
  const community = model.communityById.get(String(id));
  if (!community) return;
  state.mode = "galaxy"; state.community = String(id); state.focus = community.anchorId || state.focus;
  view.updateModeControls(); view.renderSelection(); renderCommunities(); view.renderGraph();
  const display = community.anchorId ? renderer.getNodeDisplayData(community.anchorId) : null;
  if (display) renderer.getCamera().animate({ x: display.x, y: display.y, ratio: 0.55 }, { duration: 450 });
}

function renderCommunities() { view.renderCommunities(focusCommunity); }
function filtersChanged() { clearPath(false); view.renderGraph(); }

function showPath() {
  const result = shortestPath(model, state, els.pathFrom.value, els.pathTo.value);
  if (result.error) { clearPath(false); els.pathResult.textContent = result.error; return; }
  state.pathNodes = new Set(result.ids); state.pathEdges = new Set(result.edgeKeys);
  state.mode = "galaxy"; state.community = null; view.updateModeControls(); renderCommunities(); view.renderGraph();
  els.pathResult.innerHTML = "";
  result.ids.forEach((id, index) => {
    if (index) {
      const item = result.via.get(id), separator = document.createElement("span");
      separator.className = "path-separator";
      separator.textContent = ` → ${(item?.edge.types || ["link"]).join("/")} → `;
      els.pathResult.appendChild(separator);
    }
    const link = document.createElement("a");
    link.href = "#"; link.className = "path-node"; link.textContent = model.byId.get(id)?.name || id;
    link.onclick = (event) => { event.preventDefault(); focusNode(id); };
    els.pathResult.appendChild(link);
  });
}

renderer.on("enterNode", ({ node }) => { state.hovered = node; view.renderGraph(); });
renderer.on("leaveNode", () => { state.hovered = null; view.renderGraph(); });
renderer.on("clickNode", ({ node }) => focusNode(node));
renderer.on("doubleClickNode", ({ node }) => { const target = model.byId.get(node); if (target?.href) location.href = target.href; });
renderer.on("clickStage", () => { state.community = null; renderCommunities(); view.renderGraph(); });

els.modeSwitch.onclick = (event) => {
  const button = event.target.closest("button[data-mode]");
  if (!button) return;
  state.mode = button.dataset.mode; state.community = null; view.updateModeControls(); renderCommunities(); view.renderGraph();
};
els.hop1.onclick = () => { state.hops = 1; view.updateModeControls(); view.renderGraph(); };
els.hop2.onclick = () => { state.hops = 2; view.updateModeControls(); view.renderGraph(); };
els.focusBtn.onclick = () => { const node = findNode(model, els.focusInput.value); if (node) focusNode(node.id); };
els.focusInput.onkeydown = (event) => { if (event.key === "Enter") els.focusBtn.click(); };
els.openBtn.onclick = () => { const node = model.byId.get(state.focus); if (node?.href) location.href = node.href; };
els.resetCameraBtn.onclick = () => { state.community = null; renderCommunities(); view.renderGraph(); renderer.getCamera().animatedReset({ duration: 500 }); };
els.allTypesBtn.onclick = () => { state.enabledTypes = new Set(model.nodeTypes); view.buildFilters(filtersChanged); view.renderGraph(); };
els.allRelationsBtn.onclick = () => { state.enabledRelations = new Set(model.relationTypes); view.buildFilters(filtersChanged); view.renderGraph(); };
els.pathBtn.onclick = showPath;
els.clearPathBtn.onclick = () => clearPath(true);

view.fillNodeList(); view.buildFilters(filtersChanged); renderCommunities(); view.updateModeControls(); view.renderSelection(); view.renderGraph();
if (state.focus) els.focusInput.value = model.byId.get(state.focus)?.name || state.focus;

window.addEventListener("keydown", (event) => {
  if (event.key !== "Escape") return;
  clearPath(false); state.community = null; renderCommunities(); view.renderGraph();
});
