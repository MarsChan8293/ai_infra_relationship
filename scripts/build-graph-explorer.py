#!/usr/bin/env python3
"""Build a lightweight, dependency-free relationship explorer for Quartz output."""

from __future__ import annotations

import argparse
import json
import pathlib
from urllib.parse import quote


def load_json(path: pathlib.Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def node_href(node_id: str, base_path: str) -> str:
    parts = [quote(part) for part in node_id.split("/")]
    return f"{base_path.rstrip('/')}/{'/'.join(parts)}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--generated", default="generated")
    parser.add_argument("--output", required=True)
    parser.add_argument("--base-path", default="/ai_infra_relationship")
    args = parser.parse_args()

    generated = pathlib.Path(args.generated)
    output = pathlib.Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    nodes = load_json(generated / "nodes.json", [])
    wiki_edges = load_json(generated / "edges.json", [])
    typed_edges = load_json(generated / "typed-edges.json", [])
    metrics = load_json(generated / "metrics.json", {})

    if not nodes:
        raise SystemExit("nodes.json is empty; run audit-graph.py first")

    node_map = {node["id"]: node for node in nodes}
    payload_nodes = []
    for node in nodes:
        frontmatter = node.get("frontmatter") or {}
        payload_nodes.append(
            {
                "id": node["id"],
                "name": node.get("name") or node["id"].split("/")[-1],
                "type": node.get("type") or "note",
                "category": node.get("category") or "other",
                "areas": frontmatter.get("areas") if isinstance(frontmatter.get("areas"), list) else [],
                "communities": frontmatter.get("communities") if isinstance(frontmatter.get("communities"), list) else [],
                "degree": (metrics.get(node["id"]) or {}).get("degree", 0),
                "bridgeScore": (metrics.get(node["id"]) or {}).get("bridge_score", 0),
                "href": node_href(node["id"], args.base_path),
            }
        )

    # Merge ordinary wikilinks and typed relations by pair. Typed relation types are
    # preserved as first-class filters while ordinary links remain available as a
    # broad fallback relation.
    merged: dict[tuple[str, str], dict] = {}
    for edge in wiki_edges:
        source, target = edge.get("source"), edge.get("target")
        if source not in node_map or target not in node_map or source == target:
            continue
        key = tuple(sorted((source, target)))
        item = merged.setdefault(key, {"source": key[0], "target": key[1], "types": set(), "typed": False})
        item["types"].add("wikilink")

    for edge in typed_edges:
        source, target = edge.get("source"), edge.get("target")
        if source not in node_map or target not in node_map or source == target:
            continue
        key = tuple(sorted((source, target)))
        item = merged.setdefault(key, {"source": key[0], "target": key[1], "types": set(), "typed": False})
        item["typed"] = True
        for relation_type in edge.get("relation_types") or []:
            item["types"].add(relation_type)

    payload_edges = [
        {
            "source": item["source"],
            "target": item["target"],
            "types": sorted(item["types"]),
            "typed": item["typed"],
        }
        for item in merged.values()
    ]

    data = {"nodes": payload_nodes, "edges": payload_edges, "basePath": args.base_path.rstrip("/")}
    (output / "data.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    html = r'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>AI Infra Relationship · Graph Explorer</title>
<style>
:root{color-scheme:light dark;--bg:#fbfbfd;--panel:#fff;--text:#202124;--muted:#6b7280;--line:#d7dce3;--accent:#315a78;--accent2:#7b8da1;--chip:#eef3f7;--shadow:0 10px 32px rgba(0,0,0,.08)}
@media(prefers-color-scheme:dark){:root{--bg:#161618;--panel:#202024;--text:#ebebec;--muted:#aaa7ad;--line:#3c3c42;--accent:#8ab4ce;--accent2:#8497aa;--chip:#292c31;--shadow:0 10px 30px rgba(0,0,0,.3)}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:14px/1.45 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.shell{max-width:1500px;margin:auto;padding:20px}.top{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:14px}.title{font-size:22px;font-weight:760}.sub{color:var(--muted);font-size:12px}.home{color:var(--accent);text-decoration:none}.grid{display:grid;grid-template-columns:minmax(260px,330px) minmax(0,1fr);gap:14px}@media(max-width:900px){.grid{grid-template-columns:1fr}.canvas-wrap{min-height:58vh}}.panel,.canvas-wrap{background:var(--panel);border:1px solid var(--line);border-radius:14px;box-shadow:var(--shadow)}.panel{padding:14px;max-height:calc(100vh - 90px);overflow:auto}.section{padding:10px 0;border-bottom:1px solid var(--line)}.section:last-child{border-bottom:0}.section h3{font-size:13px;margin:0 0 8px}.row{display:flex;gap:7px;align-items:center;flex-wrap:wrap}input,select,button{font:inherit}input[type=text]{width:100%;padding:9px 10px;border:1px solid var(--line);border-radius:9px;background:var(--bg);color:var(--text)}button,.chip{border:1px solid var(--line);background:var(--chip);color:var(--text);padding:6px 9px;border-radius:999px;cursor:pointer}.chip.active,button.active{border-color:var(--accent);background:color-mix(in srgb,var(--accent) 16%,var(--panel));color:var(--accent)}button.primary{border-color:var(--accent);background:var(--accent);color:white}.small{font-size:12px;color:var(--muted)}.filter-list{display:flex;gap:6px;flex-wrap:wrap}.canvas-wrap{position:relative;min-height:760px;overflow:hidden}.toolbar{position:absolute;z-index:3;left:12px;top:12px;display:flex;gap:6px;flex-wrap:wrap}.stats{position:absolute;z-index:3;right:12px;top:12px;color:var(--muted);background:color-mix(in srgb,var(--panel) 92%,transparent);border:1px solid var(--line);padding:6px 9px;border-radius:999px}.status{position:absolute;left:12px;bottom:10px;color:var(--muted);background:color-mix(in srgb,var(--panel) 92%,transparent);padding:5px 8px;border-radius:8px;z-index:3}.path-result{margin-top:8px;padding:8px;border-radius:9px;background:var(--chip);min-height:38px}.path-node{color:var(--accent);cursor:pointer;text-decoration:none}.path-node:hover{text-decoration:underline}svg{width:100%;height:100%;min-height:760px;display:block}.edge{stroke:var(--line);stroke-width:1;opacity:.52}.edge.typed{stroke:var(--accent2);stroke-width:1.6;opacity:.78}.node{cursor:pointer}.node circle{stroke:var(--panel);stroke-width:2}.node text{fill:var(--text);font-size:11px;paint-order:stroke;stroke:var(--panel);stroke-width:3px;stroke-linejoin:round}.node.focus text{font-weight:700;font-size:13px}.legend{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:4px 8px;font-size:12px}.dot{width:9px;height:9px;border-radius:50%;display:inline-block;margin-right:5px}.empty{display:flex;align-items:center;justify-content:center;height:100%;min-height:700px;color:var(--muted)}
</style>
</head>
<body>
<div class="shell">
  <div class="top"><div><div class="title">AI Infra Relationship · 关系探索器</div><div class="sub">默认 1-hop，按需展开 2-hop；筛人、筛关系、找路径，不再看毛线球。</div></div><a class="home" id="homeLink" href="#">返回知识库</a></div>
  <div class="grid">
    <aside class="panel">
      <div class="section"><h3>焦点人物 / 节点</h3><input id="focusInput" type="text" list="nodeList" placeholder="输入 游凯超 / vLLM / Inferact…"/><datalist id="nodeList"></datalist><div class="row" style="margin-top:7px"><button id="focusBtn" class="primary">聚焦</button><button id="openBtn">打开页面</button></div></div>
      <div class="section"><h3>节点类型</h3><div id="typeFilters" class="filter-list"></div></div>
      <div class="section"><h3>关系类型</h3><div id="relationFilters" class="filter-list"></div><div class="small" style="margin-top:6px">typed relation 会优先高亮；wikilink 是普通知识库链接。</div></div>
      <div class="section"><h3>Path Finder</h3><input id="pathFrom" type="text" list="nodeList" placeholder="起点"/><input id="pathTo" type="text" list="nodeList" placeholder="终点" style="margin-top:6px"/><button id="pathBtn" class="primary" style="margin-top:7px">寻找最短路径</button><div id="pathResult" class="path-result small">输入两个人或节点。</div></div>
      <div class="section"><h3>说明</h3><div class="small">点击节点：重新聚焦。双击节点：打开页面。1-hop / 2-hop 只渲染局部邻域。2-hop 过大时会优先保留 bridge score / degree 高的节点。</div></div>
      <div class="section"><h3>节点图例</h3><div id="legend" class="legend"></div></div>
    </aside>
    <main class="canvas-wrap">
      <div class="toolbar"><button id="hop1" class="active">1-hop</button><button id="hop2">2-hop</button><button id="resetBtn">重置筛选</button></div>
      <div id="stats" class="stats"></div>
      <svg id="graph" viewBox="0 0 1100 760" role="img" aria-label="Relationship graph"></svg>
      <div id="status" class="status"></div>
    </main>
  </div>
</div>
<script>
(async()=>{
const data=await fetch('./data.json').then(r=>r.json());
const nodes=data.nodes,edges=data.edges,byId=new Map(nodes.map(n=>[n.id,n]));
const adj=new Map(nodes.map(n=>[n.id,[]]));
for(const e of edges){adj.get(e.source)?.push({id:e.target,edge:e});adj.get(e.target)?.push({id:e.source,edge:e});}
const colors={person:'#4f7da5',company:'#a36b47',project:'#5f8b62',university:'#8a6faf','person-link':'#7f8c8d',index:'#999',note:'#999',other:'#999'};
const typeNames={person:'人物',company:'公司',project:'项目',university:'高校/研究机构','person-link':'人物镜像',index:'索引',note:'笔记',other:'其他'};
const nodeTypes=[...new Set(nodes.map(n=>n.type||'other'))].sort();
const relationTypes=[...new Set(edges.flatMap(e=>e.types||['wikilink']))].sort((a,b)=>a==='wikilink'?1:b==='wikilink'?-1:a.localeCompare(b));
let enabledTypes=new Set(nodeTypes), enabledRelations=new Set(relationTypes), hops=1;
let focus=pickInitial();
const svg=document.getElementById('graph'),focusInput=document.getElementById('focusInput'),nodeList=document.getElementById('nodeList');
const status=document.getElementById('status'),stats=document.getElementById('stats');
document.getElementById('homeLink').href=data.basePath+'/';

function pickInitial(){const q=new URLSearchParams(location.search).get('focus');if(q){const hit=findNode(q);if(hit)return hit.id;}return [...nodes].filter(n=>n.type==='person').sort((a,b)=>(b.bridgeScore||0)-(a.bridgeScore||0)||(b.degree||0)-(a.degree||0))[0]?.id||nodes[0].id}
function findNode(value){if(!value)return null;const v=value.trim().toLowerCase();return byId.get(value)||nodes.find(n=>n.name.toLowerCase()===v)||nodes.find(n=>n.id.toLowerCase()===v)||nodes.find(n=>n.name.toLowerCase().includes(v))||null}
function esc(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function edgeAllowed(e){return (e.types||[]).some(t=>enabledRelations.has(t))}
function nodeAllowed(n){return enabledTypes.has(n.type||'other')}
function filteredNeighbors(id){return (adj.get(id)||[]).filter(x=>edgeAllowed(x.edge)&&nodeAllowed(byId.get(x.id)))}
function scoreNode(id){const n=byId.get(id);return (n?.bridgeScore||0)*4+(n?.degree||0)}
function collect(){const levels=new Map([[focus,0]]),queue=[focus];while(queue.length){const cur=queue.shift(),level=levels.get(cur);if(level>=hops)continue;for(const item of filteredNeighbors(cur)){if(!levels.has(item.id)){levels.set(item.id,level+1);queue.push(item.id)}}}
  let ids=[...levels.keys()].filter(id=>id===focus||nodeAllowed(byId.get(id)));
  const cap=hops===1?90:180;if(ids.length>cap){const keep=new Set([focus]);for(const level of [1,2]){const part=ids.filter(id=>levels.get(id)===level).sort((a,b)=>scoreNode(b)-scoreNode(a));const allowance=level===1?Math.min(part.length,70):Math.max(0,cap-keep.size);part.slice(0,allowance).forEach(id=>keep.add(id))}ids=[...keep];status.textContent=`2-hop 邻域较大，已优先显示 ${ids.length} 个高桥梁度节点。`;}else status.textContent=`当前焦点：${byId.get(focus)?.name||focus}`;
  const set=new Set(ids);const es=edges.filter(e=>set.has(e.source)&&set.has(e.target)&&edgeAllowed(e));return{ids,levels,edges:es}}
function positions(ids,levels){const p=new Map(),cx=550,cy=385;p.set(focus,{x:cx,y:cy});for(const level of [1,2]){const ring=ids.filter(id=>levels.get(id)===level).sort((a,b)=>scoreNode(b)-scoreNode(a));const radius=level===1?220:345;ring.forEach((id,i)=>{const angle=-Math.PI/2+(Math.PI*2*i/Math.max(1,ring.length));p.set(id,{x:cx+Math.cos(angle)*radius,y:cy+Math.sin(angle)*radius})})}return p}
function render(){const {ids,levels,edges:visibleEdges}=collect(),pos=positions(ids,levels);svg.innerHTML='';
  const edgeLayer=document.createElementNS('http://www.w3.org/2000/svg','g');for(const e of visibleEdges){const a=pos.get(e.source),b=pos.get(e.target);if(!a||!b)continue;const line=document.createElementNS('http://www.w3.org/2000/svg','line');line.setAttribute('x1',a.x);line.setAttribute('y1',a.y);line.setAttribute('x2',b.x);line.setAttribute('y2',b.y);line.setAttribute('class','edge '+(e.typed?'typed':''));const tt=document.createElementNS('http://www.w3.org/2000/svg','title');tt.textContent=(e.types||[]).join(', ');line.appendChild(tt);edgeLayer.appendChild(line)}svg.appendChild(edgeLayer);
  const nodeLayer=document.createElementNS('http://www.w3.org/2000/svg','g');for(const id of ids){const n=byId.get(id),p=pos.get(id);if(!n||!p)continue;const g=document.createElementNS('http://www.w3.org/2000/svg','g');g.setAttribute('class','node '+(id===focus?'focus':''));g.setAttribute('transform',`translate(${p.x},${p.y})`);const c=document.createElementNS('http://www.w3.org/2000/svg','circle');const r=id===focus?12:Math.max(5,Math.min(9,5+Math.log2((n.degree||0)+1)));c.setAttribute('r',r);c.setAttribute('fill',colors[n.type]||colors.other);g.appendChild(c);const t=document.createElementNS('http://www.w3.org/2000/svg','text');t.setAttribute('x',r+5);t.setAttribute('y','4');t.textContent=n.name.length>24?n.name.slice(0,23)+'…':n.name;g.appendChild(t);const tt=document.createElementNS('http://www.w3.org/2000/svg','title');tt.textContent=`${n.name}\n${n.type} · degree ${n.degree||0} · bridge ${n.bridgeScore||0}`;g.appendChild(tt);g.onclick=()=>setFocus(id);g.ondblclick=()=>location.href=n.href;nodeLayer.appendChild(g)}svg.appendChild(nodeLayer);stats.textContent=`${ids.length} nodes · ${visibleEdges.length} edges · ${hops}-hop`;focusInput.value=byId.get(focus)?.name||focus;history.replaceState(null,'','?focus='+encodeURIComponent(focus));}
function setFocus(id){if(!byId.has(id))return;focus=id;render()}
function buildFilters(){const typeBox=document.getElementById('typeFilters');typeBox.innerHTML='';for(const type of nodeTypes){const b=document.createElement('button');b.className='chip active';b.textContent=typeNames[type]||type;b.onclick=()=>{enabledTypes.has(type)?enabledTypes.delete(type):enabledTypes.add(type);b.classList.toggle('active',enabledTypes.has(type));render()};typeBox.appendChild(b)}const relBox=document.getElementById('relationFilters');relBox.innerHTML='';for(const type of relationTypes){const b=document.createElement('button');b.className='chip active';b.textContent=type;b.onclick=()=>{enabledRelations.has(type)?enabledRelations.delete(type):enabledRelations.add(type);b.classList.toggle('active',enabledRelations.has(type));render()};relBox.appendChild(b)}}
function fillNodeList(){nodeList.innerHTML=nodes.slice().sort((a,b)=>a.name.localeCompare(b.name)).map(n=>`<option value="${esc(n.name)}">${esc(n.type)} · ${esc(n.id)}</option>`).join('')}
function setHop(value){hops=value;document.getElementById('hop1').classList.toggle('active',value===1);document.getElementById('hop2').classList.toggle('active',value===2);render()}
function bfs(from,to){const start=findNode(from),goal=findNode(to);if(!start||!goal)return{error:'找不到起点或终点。'};const q=[start.id],prev=new Map([[start.id,null]]),via=new Map();while(q.length){const cur=q.shift();if(cur===goal.id)break;for(const item of filteredNeighbors(cur)){if(prev.has(item.id))continue;prev.set(item.id,cur);via.set(item.id,item.edge);q.push(item.id)}}if(!prev.has(goal.id))return{error:'当前筛选条件下没有可达路径。'};const ids=[];let cur=goal.id;while(cur){ids.push(cur);cur=prev.get(cur)}ids.reverse();return{ids,via}}
function showPath(){const result=bfs(document.getElementById('pathFrom').value,document.getElementById('pathTo').value),box=document.getElementById('pathResult');if(result.error){box.textContent=result.error;return}box.innerHTML='';result.ids.forEach((id,i)=>{if(i){const e=result.via.get(id),sep=document.createElement('span');sep.textContent='  → '+((e?.types||[]).filter(t=>t!=='wikilink').join('/')||'link')+' →  ';box.appendChild(sep)}const a=document.createElement('a');a.className='path-node';a.textContent=byId.get(id)?.name||id;a.onclick=ev=>{ev.preventDefault();setFocus(id)};a.href='#';box.appendChild(a)})}
function reset(){enabledTypes=new Set(nodeTypes);enabledRelations=new Set(relationTypes);buildFilters();render()}
fillNodeList();buildFilters();document.getElementById('legend').innerHTML=nodeTypes.map(t=>`<div><span class="dot" style="background:${colors[t]||colors.other}"></span>${esc(typeNames[t]||t)}</div>`).join('');
document.getElementById('focusBtn').onclick=()=>{const n=findNode(focusInput.value);if(n)setFocus(n.id)};focusInput.onkeydown=e=>{if(e.key==='Enter')document.getElementById('focusBtn').click()};document.getElementById('openBtn').onclick=()=>{const n=byId.get(focus);if(n)location.href=n.href};document.getElementById('hop1').onclick=()=>setHop(1);document.getElementById('hop2').onclick=()=>setHop(2);document.getElementById('resetBtn').onclick=reset;document.getElementById('pathBtn').onclick=showPath;render();
})().catch(err=>{document.body.innerHTML='<pre style="padding:24px">Graph Explorer failed: '+String(err)+'</pre>'})
</script>
</body></html>'''
    (output / "index.html").write_text(html, encoding="utf-8")
    print(f"Graph explorer: {len(payload_nodes)} nodes, {len(payload_edges)} merged edges -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
