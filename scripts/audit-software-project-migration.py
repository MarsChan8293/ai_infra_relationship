#!/usr/bin/env python3
import argparse,json,pathlib,re,sys
from collections import defaultdict
from urllib.parse import urlsplit, urlunsplit

ROOTS=("company","community","university")
LAYERS={"inference-engine","distributed-serving","gateway","kv-cache","storage","communication","runtime","kernel","compiler","training","scheduler","device-resource","benchmark","ecosystem","optimization","other"}
STATUS={"active","maintenance","deprecated","archived","unknown"}
LEGACY={"object_type","schema_version","category","repo","capabilities","backends","snapshot","updated","upstream_org"}
MONTH=re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")

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

def lst(v):
    if v in (None,""):return []
    return v if isinstance(v,list) else [str(v)]

def fold(s):return re.sub(r"\s+"," ",s.strip()).casefold()

def canonical_repository_url(value):
    if not isinstance(value,str) or not value.strip():
        return None
    raw=value.strip()
    parsed=urlsplit(raw)
    if parsed.scheme not in {"http","https"} or not parsed.netloc:
        return None
    host=parsed.netloc.casefold()
    if host.startswith("www."):
        host=host[4:]
    path=parsed.path.rstrip("/")
    if path.endswith(".git"):
        path=path[:-4]
    # Repository field must identify a repository/org root, not a deep page.
    if host in {"github.com","gitcode.com","gitee.com"}:
        parts=[part for part in path.split("/") if part]
        if host=="github.com" and len(parts)>2:
            return "__deep__"
        if host in {"gitcode.com","gitee.com"} and len(parts)>2:
            return "__deep__"
    return urlunsplit(("https",host,path,"",""))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root",default="."); ap.add_argument("--generated",default="generated")
    a=ap.parse_args(); root=pathlib.Path(a.root).resolve(); gen=root/a.generated; gen.mkdir(parents=True,exist_ok=True)
    m=json.loads((root/"research/software-project-migration.json").read_text(encoding="utf-8")); items=m["projects"]
    errors=[]; projects=[]; infra=[]
    for r in ROOTS:
        b=root/r
        if not b.exists():continue
        for p in b.rglob("*.md"):
            f=fm(p.read_text(encoding="utf-8")); t=f.get("type"); rel=p.relative_to(root).as_posix()
            if t=="infra-project":infra.append(rel)
            if t=="project":
                repo_raw=f.get("repository")
                projects.append({
                    "path":rel,
                    "name":str(f.get("name") or p.stem),
                    "repo":repo_raw,
                    "repo_canonical":canonical_repository_url(repo_raw),
                    "parent":f.get("parent"),
                    "fm":f
                })
    for p in infra:errors.append({"kind":"infra-project","path":p,"detail":"migrate to project"})
    names=defaultdict(list); repos=defaultdict(list)
    for p in projects:
        names[fold(p["name"])].append(p)
        if p.get("repo_canonical") and p["repo_canonical"]!="__deep__":
            repos[p["repo_canonical"]].append(p)
    seen=set()
    for it in items:
        path=it["canonical_path"]; target=root/path
        if path in seen:errors.append({"kind":"duplicate-map","path":path,"detail":it["name"]})
        seen.add(path)
        if not target.exists():errors.append({"kind":"missing","path":path,"detail":it["name"]}); continue
        f=fm(target.read_text(encoding="utf-8"))
        if f.get("type")!="project":errors.append({"kind":"type","path":path,"detail":repr(f.get("type"))})
        if f.get("name")!=it["name"]:errors.append({"kind":"name","path":path,"detail":repr(f.get("name"))})
        ms=names.get(fold(it["name"]),[])
        if len(ms)!=1 or ms[0]["path"]!=path:errors.append({"kind":"non-unique-name","path":path,"detail":str([x["path"] for x in ms])})
        if f.get("layer") not in LAYERS:errors.append({"kind":"layer","path":path,"detail":repr(f.get("layer"))})
        if f.get("status") not in STATUS:errors.append({"kind":"status","path":path,"detail":repr(f.get("status"))})
        repo_raw=f.get("repository")
        repo_canonical=canonical_repository_url(repo_raw)
        if repo_raw not in (None,""):
            if repo_canonical is None:
                errors.append({"kind":"repository-url-invalid","path":path,"detail":repr(repo_raw)})
            elif repo_canonical=="__deep__":
                errors.append({"kind":"repository-url-not-root","path":path,"detail":repr(repo_raw)})
            elif repo_raw!=repo_canonical:
                errors.append({"kind":"repository-url-noncanonical","path":path,"detail":f"{repo_raw!r} -> {repo_canonical!r}"})
        docs_raw=f.get("docs")
        if docs_raw not in (None,""):
            parsed_docs=urlsplit(str(docs_raw))
            if parsed_docs.scheme not in {"http","https"} or not parsed_docs.netloc:
                errors.append({"kind":"docs-url-invalid","path":path,"detail":repr(docs_raw)})
        lv=f.get("last_verified")
        if not isinstance(lv,str) or not MONTH.match(lv):errors.append({"kind":"last_verified","path":path,"detail":repr(lv)})
        for k in LEGACY:
            if k in f:errors.append({"kind":"legacy-field","path":path,"detail":k})
        for x in lst(f.get("integrations")):
            ms=names.get(fold(x),[])
            if len(ms)!=1:errors.append({"kind":"integration","path":path,"detail":f"{x}: {[q['path'] for q in ms]}"})
    mapped_paths={it["canonical_path"] for it in items}
    for repo,rows in repos.items():
        scoped=[x for x in rows if x["path"] in mapped_paths]
        if len(scoped)<2:continue
        nm={fold(x["name"]) for x in scoped}; bad=[]
        for x in scoped:
            par=fold(str(x.get("parent") or ""))
            child_of_peer=bool(par and par in nm)
            parent_of_peer=any(fold(str(y.get("parent") or ""))==fold(x["name"]) for y in scoped)
            if not (child_of_peer or parent_of_peer):bad.append(x)
        if bad:errors.append({"kind":"duplicate-repository","path":bad[0]["path"],"detail":repo+" :: "+", ".join(x["name"] for x in scoped)})
    out={"format":"software-project-migration-audit-v1","mapped":len(items),"projects":len(projects),"infra_projects":len(infra),"errors":errors,"status":"pass" if not errors else "fail"}
    (gen/"software-project-migration-audit.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    md=["# Software Project Migration Audit","",f"- Status: **{out['status'].upper()}**",f"- Mapped: {len(items)} / 59",f"- Project nodes: {len(projects)}",f"- infra-project nodes: {len(infra)}",f"- Errors: {len(errors)}","","## Errors",""]
    md += ["- None."] if not errors else [f"- `{e['kind']}`: `{e['path']}` - {e['detail']}" for e in errors]
    (gen/"software-project-migration-audit.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(f"software migration audit: {out['status']}; mapped={len(items)} errors={len(errors)}")
    for e in errors:print("ERROR",e["kind"],e["path"],e["detail"])
    return 1 if errors else 0
if __name__=="__main__":sys.exit(main())
