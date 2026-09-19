#!/usr/bin/env python3
import argparse,json,pathlib,sys
from collections import defaultdict

ORDER=["inference-engine","distributed-serving","gateway","kv-cache","storage","communication","runtime","kernel","compiler","training","scheduler","device-resource","benchmark","ecosystem","optimization","other"]

def scalar(v):
    v=v.strip()
    if not v:return ""
    if v=="[]":return []
    if v.startswith("[") and v.endswith("]"):
        return [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
    if v.lower() in {"null","none","~"}:return None
    return v.strip("\"'")

def fm(text):
    if not text.startswith("---\n"):return {}
    lines=text.splitlines()
    try:end=lines.index("---",1)
    except ValueError:return {}
    d={}; cur=None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):continue
        if raw.startswith("  - ") and cur:
            d.setdefault(cur,[]).append(scalar(raw[4:])); continue
        if raw.startswith((" ","-")) or ":" not in raw:continue
        k,v=raw.split(":",1); cur=k.strip(); d[cur]=scalar(v)
    return d

def vals(v):
    if v in (None,""):return []
    return v if isinstance(v,list) else [str(v)]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root",default="."); ap.add_argument("--output",default="generated/software-project-index.md")
    a=ap.parse_args(); root=pathlib.Path(a.root).resolve()
    m=json.loads((root/"research/software-project-migration.json").read_text(encoding="utf-8"))
    groups=defaultdict(list)
    for item in m["projects"]:
        p=root/item["canonical_path"]
        if not p.exists():raise SystemExit(f"missing canonical project: {item['canonical_path']}")
        f=fm(p.read_text(encoding="utf-8"))
        groups[str(f.get("layer") or "other")].append({
            "name":item["name"],"path":item["canonical_path"][:-3],
            "status":str(f.get("status") or ""),"areas":vals(f.get("areas")),
            "integrations":vals(f.get("integrations")),"action":item["action"]
        })
    lines=["# Software Project Index","",
           "Generated from research/software-project-migration.json and canonical Project v3 frontmatter.","",
           f"- Projects: {len(m['projects'])}","- Concepts: not included; they remain in ai_infra_docs/software/concepts.",""]
    for layer in ORDER:
        rows=sorted(groups.get(layer,[]),key=lambda x:x["name"].casefold())
        if not rows:continue
        lines += [f"## {layer}","", "| Project | Status | Areas | Integrations |", "| --- | --- | --- | ---: |"]
        for r in rows:
            areas=", ".join(r["areas"][:5])
            lines.append(f"| [[{r['path']}|{r['name']}]] | {r['status']} | {areas} | {len(r['integrations'])} |")
        lines.append("")
    unknown=sorted(set(groups)-set(ORDER))
    if unknown:
        raise SystemExit("unknown layers: "+", ".join(unknown))
    out=root/a.output; out.parent.mkdir(parents=True,exist_ok=True); out.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(f"software project index: {len(m['projects'])} projects -> {out.relative_to(root)}")
    return 0

if __name__=="__main__":sys.exit(main())
