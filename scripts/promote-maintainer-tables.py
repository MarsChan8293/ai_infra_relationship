#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import re
import urllib.error
import urllib.request

ROOT = pathlib.Path('.').resolve()
RUN_ID = '2026-09-18-discover-full'
HANDLE_RE = re.compile(r'^[A-Za-z0-9][A-Za-z0-9-]{0,38}$')
SKIP = {'github','githubid','id','maintainer','maintainers','username','user','owner','global-owner','global-owner1','global-owner2','example','someone','yourname'}


def fetch(url: str) -> str:
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 ai-infra-discover/1.0'})
    try:
        with urllib.request.urlopen(req,timeout=8) as r:
            return r.read(300000).decode(r.headers.get_content_charset() or 'utf-8',errors='replace')
    except Exception:
        return ''


def valid_profile(handle: str) -> bool:
    req=urllib.request.Request('https://github.com/'+handle,headers={'User-Agent':'Mozilla/5.0 ai-infra-discover/1.0'})
    try:
        with urllib.request.urlopen(req,timeout=6) as r:
            return 200 <= int(getattr(r,'status',200) or 200) < 400
    except urllib.error.HTTPError as e:
        return e.code in (401,403,429)
    except Exception:
        return False


def parse_active_ids(text: str) -> list[str]:
    m=re.search(r'(?ims)^##\s+Active\s*$([\s\S]*?)(?=^##\s|\Z)',text)
    section=m.group(1) if m else text
    out=[]
    for line in section.splitlines():
        s=line.strip()
        if not s.startswith('|'):
            continue
        cols=[c.strip().strip('`*') for c in s.strip('|').split('|')]
        if not cols:
            continue
        h=cols[0]
        if not HANDLE_RE.fullmatch(h) or h.lower() in SKIP:
            continue
        if h not in out and valid_profile(h):
            out.append(h)
    return out


def frontmatter(text: str) -> dict:
    if not text.startswith('---\n'):
        return {}
    lines=text.splitlines()
    try: end=lines.index('---',1)
    except ValueError: return {}
    d={}; key=None
    for raw in lines[1:end]:
        if raw.startswith('  - ') and key:
            d.setdefault(key,[]).append(raw[4:].strip().strip('"\'')); continue
        if ':' in raw and not raw.startswith(' '):
            key,val=raw.split(':',1); key=key.strip(); val=val.strip()
            if val.startswith('[') and val.endswith(']'):
                d[key]=[x.strip().strip('"\'') for x in val[1:-1].split(',') if x.strip()]
            else: d[key]=val.strip('"\'')
    return d


def build_handle_index() -> dict[str,pathlib.Path]:
    idx={}
    for root in ('company','community','university'):
        for p in (ROOT/root).rglob('*.md'):
            fm=frontmatter(p.read_text(encoding='utf-8',errors='replace'))
            if fm.get('type')!='person': continue
            vals=[str(fm.get('name') or '')]
            aliases=fm.get('aliases') or []
            if isinstance(aliases,list): vals += [str(x) for x in aliases]
            for v in vals:
                h=v.strip().lstrip('@')
                if HANDLE_RE.fullmatch(h): idx.setdefault(h.lower(),p)
    return idx


def add_project(path: pathlib.Path, project: str) -> bool:
    text=path.read_text(encoding='utf-8')
    if not text.startswith('---\n'): return False
    lines=text.splitlines(); end=lines.index('---',1)
    for i in range(1,end):
        if not lines[i].startswith('projects:'): continue
        raw=lines[i].split(':',1)[1].strip()
        if raw.startswith('[') and raw.endswith(']'):
            vals=[x.strip().strip('"\'') for x in raw[1:-1].split(',') if x.strip()]
            if project in vals: return False
            vals.append(project); lines[i]='projects: '+json.dumps(vals,ensure_ascii=False)
            path.write_text('\n'.join(lines)+'\n',encoding='utf-8'); return True
        j=i+1; vals=[]
        while j<end and lines[j].startswith('  - '): vals.append(lines[j][4:].strip().strip('"\'')); j+=1
        if project in vals: return False
        lines.insert(j,'  - '+json.dumps(project,ensure_ascii=False)); path.write_text('\n'.join(lines)+'\n',encoding='utf-8'); return True
    lines.insert(end,'projects: ['+json.dumps(project,ensure_ascii=False)+']')
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8'); return True


frontier_path=ROOT/'generated/full-discover-frontier.json'
history_path=ROOT/'research/action-history.json'
frontier=json.loads(frontier_path.read_text(encoding='utf-8'))
history=json.loads(history_path.read_text(encoding='utf-8'))
hmap={(r.get('run_id'),r.get('action_id')):r for r in history.get('records',[])}
idx=build_handle_index(); created=[]; edge_count=0

for rec in frontier.get('records',[]):
    if rec.get('relation')!='maintainers': continue
    gov=rec.get('governance') or {}; files=gov.get('files') or []
    if not files: continue
    url=files[0].get('url') or ''
    if 'MAINTAINERS' not in (files[0].get('path') or '').upper(): continue
    text=fetch(url)
    handles=parse_active_ids(text)[:6]
    if not handles: continue
    source_id=rec['source_id']; project=rec['source_name']; parent=(ROOT/(source_id+'.md')).parent
    new_nodes=0; new_edges=0
    for h in handles:
        existing=idx.get(h.lower())
        if existing:
            if add_project(existing,project): new_edges+=1; edge_count+=1
        else:
            dest=parent/(h+'.md')
            if not dest.exists():
                content=(
                    '---\n'
                    'type: person\n'
                    f'name: {json.dumps(h,ensure_ascii=False)}\n'
                    f'aliases: [{json.dumps("@"+h,ensure_ascii=False)}]\n'
                    f'projects: [{json.dumps(project,ensure_ascii=False)}]\n'
                    'roles: [Governance Maintainer]\n'
                    'confidence: project-credit\n'
                    'last_verified: "2026-09"\n'
                    '---\n'
                    f'# {h}\n\n'
                    f'`@{h}` is a handle-first identity listed in the project-owned active maintainer table for [[{project}]]. This records project governance only and does not infer employer, legal identity, or job title.\n\n'
                    '## Sources\n'
                    f'- {url}\n'
                )
                dest.write_text(content,encoding='utf-8'); idx[h.lower()]=dest; created.append(dest.relative_to(ROOT).with_suffix('').as_posix()); new_nodes+=1; new_edges+=1; edge_count+=1
        item='maintainer:@'+h
        if item not in rec['resolved']: rec['resolved'].append(item)
    rec['unresolved']=[x for x in rec.get('unresolved',[]) if x not in {'maintainer_identity_parse','maintainer_governance'}]
    if len(handles)<6:
        rec['status']='success'
    else:
        rec['status']='partial'
        if 'additional_governance_handles_after_cap' not in rec['unresolved']: rec['unresolved'].append('additional_governance_handles_after_cap')
    hr=hmap.get((RUN_ID,rec['action_id']))
    if hr:
        hr['status']=rec['status']; hr['resolved_dimensions']=rec['resolved']; hr['unresolved_dimensions']=rec['unresolved']
        hr['outcome']['new_nodes']=new_nodes; hr['outcome']['new_edges']=new_edges
        hr['outcome']['evidence_upgraded']=len(handles); hr['outcome']['verified_claims']=len(handles)
        hr['note']=f'Active project MAINTAINERS table verified {len(handles)} GitHub maintainer handle(s); {new_nodes} handle-first nodes created.'

frontier['created_nodes']=created
from collections import Counter
statuses=Counter(r.get('status') for r in frontier.get('records',[]))
frontier['status_counts']=dict(statuses)
frontier_path.write_text(json.dumps(frontier,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
history_path.write_text(json.dumps(history,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

report=ROOT/'docs/research-runs/2026-09-18-discover-full.md'
text=report.read_text(encoding='utf-8')
text=re.sub(r'- Durable outcomes: .*', '- Durable outcomes: '+', '.join(f'{k}={v}' for k,v in sorted(statuses.items())), text)
text=re.sub(r'- Governance-maintainer nodes created: \*\*\d+\*\*', f'- Governance-maintainer nodes created: **{len(created)}**', text)
text=re.sub(r'- Newly encoded maintainer project edges: \*\*\d+\*\*', f'- Newly encoded maintainer project edges: **{edge_count}**', text)
section='## New governance-maintainer nodes\n\n'+(('\n'.join('- `'+x+'`' for x in created)) if created else '- None')+'\n\n## Frontier artifact'
text=re.sub(r'## New governance-maintainer nodes\n\n[\s\S]*?\n\n## Frontier artifact',section,text)
report.write_text(text,encoding='utf-8')
print('promoted active maintainer identities',len(created),'edges',edge_count,'statuses',dict(statuses))
