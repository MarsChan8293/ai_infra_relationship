#!/usr/bin/env python3
from __future__ import annotations

import concurrent.futures
import datetime as dt
import json
import pathlib
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict

ROOT = pathlib.Path('.').resolve()
AS_OF = '2026-09-18'
RUN_ID = '2026-09-18-discover-full'
NODE_ROOTS = ('company', 'community', 'university')
URL_RE = re.compile(r'https?://[^\s<>()\]"\']+')
GH_REPO_RE = re.compile(r'https?://(?:www\.)?github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)', re.I)
HANDLE_RE = re.compile(r'@([A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))(?!/)')
PROFILE_RE = re.compile(r'https?://(?:www\.)?github\.com/([A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))(?:[\s)#>,]|$)', re.I)
WIKILINK_RE = re.compile(r'(?<!!)\[\[([^\]\n]+)\]\]')
GOV_FILES = ('MAINTAINERS.md','MAINTAINERS','.github/MAINTAINERS.md','CODEOWNERS','.github/CODEOWNERS','OWNERS','OWNERS.md','GOVERNANCE.md')
BOT_HANDLES = {'github-actions','dependabot','renovate','codecov','all-contributors','pre-commit-ci'}


def parse_scalar(raw: str):
    value = raw.strip()
    if not value:
        return ''
    if value == '[]':
        return []
    if value.startswith('[') and value.endswith(']'):
        body = value[1:-1].strip()
        if not body:
            return []
        return [x.strip().strip('"\'') for x in body.split(',') if x.strip()]
    low = value.lower()
    if low == 'true': return True
    if low == 'false': return False
    if low in {'null','none','~'}: return None
    return value.strip('"\'')


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith('---\n'):
        return {}, text
    lines = text.splitlines()
    try:
        end = lines.index('---', 1)
    except ValueError:
        return {}, text
    data = {}
    current = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith('#'):
            continue
        if raw.startswith('  - ') and current:
            items = data.setdefault(current, [])
            if isinstance(items, list): items.append(parse_scalar(raw[4:]))
            continue
        if raw.startswith('-') or ':' not in raw:
            continue
        key, value = raw.split(':',1)
        key = key.strip()
        data[key] = parse_scalar(value)
        current = key
    return data, '\n'.join(lines[end+1:])


def clean_url(u: str) -> str:
    return u.rstrip('.,;:!?`})]')


def github_repo_urls(text: str) -> list[str]:
    out=[]
    for m in GH_REPO_RE.finditer(text):
        owner, repo = m.group(1), m.group(2).removesuffix('.git')
        if repo.lower() in {'issues','pulls','commit','commits','tree','blob'}: continue
        url=f'https://github.com/{owner}/{repo}'
        if url not in out: out.append(url)
    return out


def node_id(path: pathlib.Path) -> str:
    return path.relative_to(ROOT).with_suffix('').as_posix()


def add_frontmatter_list_item(path: pathlib.Path, key: str, item: str) -> bool:
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        return False
    lines = text.splitlines()
    try:
        end = lines.index('---',1)
    except ValueError:
        return False
    q = json.dumps(item, ensure_ascii=False)
    for i in range(1,end):
        if not lines[i].startswith(key + ':'):
            continue
        raw = lines[i].split(':',1)[1].strip()
        if raw.startswith('[') and raw.endswith(']'):
            vals = parse_scalar(raw)
            if isinstance(vals,list) and item in vals: return False
            vals = vals if isinstance(vals,list) else []
            vals.append(item)
            lines[i] = f'{key}: ' + json.dumps(vals, ensure_ascii=False)
            path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
            return True
        j=i+1; existing=[]
        while j<end and lines[j].startswith('  - '):
            existing.append(str(parse_scalar(lines[j][4:])))
            j+=1
        if item in existing: return False
        if raw:
            old=str(parse_scalar(raw)); lines[i]=f'{key}:'; lines.insert(i+1,f'  - {json.dumps(old,ensure_ascii=False)}'); end+=1; j=i+2
        lines.insert(j,f'  - {q}')
        path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
        return True
    lines.insert(end, f'{key}:')
    lines.insert(end+1, f'  - {q}')
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return True


def fetch_text(url: str, timeout: int = 6) -> tuple[str, str, int | None]:
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 ai-infra-discover/1.0','Accept':'text/html,text/plain,*/*'})
    try:
        with urllib.request.urlopen(req,timeout=timeout) as r:
            data=r.read(250000)
            enc=r.headers.get_content_charset() or 'utf-8'
            return data.decode(enc,errors='replace'), r.geturl(), int(getattr(r,'status',200) or 200)
    except urllib.error.HTTPError as e:
        if e.code in (401,403,405,429): return '', url, int(e.code)
        return '', url, int(e.code)
    except Exception:
        return '', url, None


def governance_probe(repo_url: str):
    m=GH_REPO_RE.match(repo_url)
    if not m: return {'repo':repo_url,'files':[],'handles':[]}
    owner,repo=m.group(1),m.group(2).removesuffix('.git')
    files=[]; handles=[]
    for branch in ('main','master'):
        found_this_branch=False
        for rel in GOV_FILES:
            raw=f'https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{rel}'
            text,final,code=fetch_text(raw,5)
            if code == 200 and text:
                found_this_branch=True
                hs=[]
                for h in HANDLE_RE.findall(text):
                    if h.lower() not in BOT_HANDLES and h not in hs: hs.append(h)
                for h in PROFILE_RE.findall(text):
                    if h.lower() not in BOT_HANDLES and h not in hs: hs.append(h)
                files.append({'url':raw,'path':rel,'handles':hs})
                for h in hs:
                    if h not in handles: handles.append(h)
        if found_this_branch: break
    return {'repo':repo_url,'files':files,'handles':handles}


subprocess.run(['python3','scripts/plan-research-v3.py','--operator','discover','--budget','2000','--limit','2000','--as-of',AS_OF],check=True)
payload=json.loads((ROOT/'generated/research-actions.json').read_text(encoding='utf-8'))
actions=payload.get('selected_actions',[])

# Index nodes, people handles and repositories.
nodes={}; handle_to_path={}; repo_to_node={}
for root in NODE_ROOTS:
    for path in (ROOT/root).rglob('*.md'):
        text=path.read_text(encoding='utf-8',errors='replace')
        fm,body=parse_frontmatter(text)
        nid=node_id(path)
        nodes[nid]={'path':path,'fm':fm,'body':body,'text':text,'type':fm.get('type'),'name':str(fm.get('name') or path.stem)}
        if fm.get('type') == 'person':
            vals=[str(fm.get('name') or '')]
            aliases=fm.get('aliases') or []
            if isinstance(aliases,list): vals += [str(x) for x in aliases]
            for v in vals:
                h=v.strip().lstrip('@')
                if re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]{0,38}',h): handle_to_path.setdefault(h.lower(),path)
        repos=github_repo_urls(text)
        for r in repos[:2]: repo_to_node.setdefault(r.lower(),nid)

# Probe up to two source URLs per action, deduplicated across the portfolio.
action_urls={}; unique_urls=[]
for a in actions:
    src=nodes.get(a['source']['id'])
    text=src['text'] if src else ''
    urls=[]
    for u in URL_RE.findall(text):
        u=clean_url(u)
        if u not in urls: urls.append(u)
    urls=urls[:2]
    action_urls[a['action_id']]=urls
    for u in urls:
        if u not in unique_urls: unique_urls.append(u)

probe_results={}
def probe(u):
    text,final,code=fetch_text(u)
    return u, {'live': code is not None and (200 <= code < 400 or code in (401,403,405,429)), 'code':code, 'final':final, 'repos':github_repo_urls(text)[:20]}
with concurrent.futures.ThreadPoolExecutor(max_workers=28) as ex:
    for u,res in ex.map(probe,unique_urls): probe_results[u]=res

# Governance probes for maintainer actions.
maintainer_jobs={}
for a in actions:
    if a.get('relation')!='maintainers': continue
    src=nodes.get(a['source']['id']); text=src['text'] if src else ''
    repos=github_repo_urls(text)
    if repos: maintainer_jobs[a['action_id']]=repos[0]
gov_results={}
with concurrent.futures.ThreadPoolExecutor(max_workers=18) as ex:
    futs={ex.submit(governance_probe,r):(aid,r) for aid,r in maintainer_jobs.items()}
    for fut in concurrent.futures.as_completed(futs):
        aid,_=futs[fut]
        try: gov_results[aid]=fut.result()
        except Exception: gov_results[aid]={'files':[],'handles':[]}

history_path=ROOT/'research/action-history.json'
history=json.loads(history_path.read_text(encoding='utf-8'))
records=history.setdefault('records',[])
records=[r for r in records if r.get('run_id')!=RUN_ID]
history['records']=records
frontier=[]; status_counts=Counter(); relation_counts=Counter(); created_nodes=[]; upgraded_edges=0

for a in actions:
    aid=a['action_id']; rel=a.get('relation',''); src=a['source']; source_id=src['id']; source_name=src['name']
    n=nodes.get(source_id); text=n['text'] if n else ''
    resolved=[]; unresolved=[]; new_nodes=0; new_edges=0; verified=0; rejected=0
    urls=action_urls.get(aid,[]); live=[probe_results[u] for u in urls if probe_results.get(u,{}).get('live')]
    discovered_repos=[]
    for r in live:
        for repo in r.get('repos',[]):
            if repo.lower() not in discovered_repos: discovered_repos.append(repo.lower())
    local_repos=[x.lower() for x in github_repo_urls(text)]
    discovered_repos=[r for r in discovered_repos if r not in local_repos]
    internal=[x.split('|',1)[0].split('#',1)[0].strip() for x in WIKILINK_RE.findall(text)]

    status='unresolved'
    note=''
    if rel=='maintainers':
        g=gov_results.get(aid,{}); handles=list(dict.fromkeys(g.get('handles') or []))
        files=g.get('files') or []
        if files:
            resolved.append('governance_file:'+files[0]['path'])
        if handles:
            cap=handles[:6]
            for h in cap:
                existing=handle_to_path.get(h.lower())
                project_name=source_name
                if existing:
                    if add_frontmatter_list_item(existing,'projects',project_name): new_edges+=1; upgraded_edges+=1
                    resolved.append('maintainer:@'+h)
                    continue
                parent=(ROOT/(source_id+'.md')).parent
                dest=parent/(h+'.md')
                if dest.exists():
                    resolved.append('maintainer:@'+h); continue
                areas=(n['fm'].get('areas') if n else []) or []
                if not isinstance(areas,list): areas=[]
                src_url=files[0]['url'] if files else (maintainer_jobs.get(aid) or '')
                content='---\n'
                content+='type: person\n'
                content+=f'name: {json.dumps(h,ensure_ascii=False)}\n'
                content+=f'aliases: [{json.dumps("@"+h,ensure_ascii=False)}]\n'
                content+=f'projects: [{json.dumps(project_name,ensure_ascii=False)}]\n'
                content+='roles: [Governance Maintainer]\n'
                if areas: content+='areas: '+json.dumps(areas,ensure_ascii=False)+'\n'
                content+='confidence: project-credit\nlast_verified: "2026-09"\n---\n'
                content+=f'# {h}\n\n'
                content+=f'`@{h}` is recorded as a handle-first maintainer identity for [[{project_name}]]. The project governance file explicitly names this GitHub handle; this node does not infer employer, legal identity, or job title beyond that governance role.\n\n## Sources\n- {src_url}\n'
                dest.write_text(content,encoding='utf-8')
                handle_to_path[h.lower()]=dest
                new_nodes+=1; new_edges+=1; created_nodes.append(node_id(dest)); resolved.append('maintainer:@'+h)
            verified=len(cap)
            if len(handles)>6:
                status='partial'; unresolved.append('additional_governance_handles_after_cap')
            else:
                status='success'
            note=f'Governance evidence yielded {len(handles)} maintainer handle(s); {new_nodes} handle-first nodes created.'
        elif files:
            status='partial'; unresolved.append('maintainer_identity_parse'); note='Governance file found but no stable individual GitHub handles were parsed.'
        elif maintainer_jobs.get(aid):
            status='partial'; unresolved.append('maintainer_governance'); note='Repository probed, but common governance files did not yield stable maintainer identities.'
        else:
            status='unresolved'; unresolved.append('canonical_repository'); unresolved.append('maintainers'); note='No canonical GitHub repository was available for a governance-file probe.'
    else:
        # Full-portfolio frontier crawl. A reachable first-party/source page is an attempted discovery,
        # not enough to declare the semantic relation solved.
        if local_repos:
            resolved.append('repository_context:'+local_repos[0])
        if discovered_repos:
            for r in discovered_repos[:5]: resolved.append('frontier_repo:'+r)
        if internal:
            resolved.append(f'internal_graph_links:{len(internal)}')
        if live:
            resolved.append(f'reachable_sources:{len(live)}')
        if rel=='originating_org' and local_repos:
            m=GH_REPO_RE.match(local_repos[0])
            if m: resolved.append('repository_namespace:'+m.group(1)); unresolved.append('originating_org_semantics')
        elif rel=='affiliation':
            unresolved.append('current_affiliation')
        elif rel=='project_contribution':
            unresolved.append('contribution_role_strength')
        elif rel in {'projects','related_projects'}:
            unresolved.append('project_relevance_and_direct_relation')
        elif rel in {'labs_or_groups','key_people','core_people','member_orgs','academic_links','parent_or_partner_org','spinouts','technical_collaborator'}:
            unresolved.append(rel+'_semantic_confirmation')
        else:
            unresolved.append(rel or 'semantic_relation')
        if live or discovered_repos or internal or local_repos:
            status='partial'; note='Full DISCOVER frontier probe completed; candidate context retained without promoting weak signals to a strong graph edge.'
        else:
            status='unresolved'; note='No stable first-party/source frontier signal was available in the automated full-portfolio pass.'

    frontier.append({'action_id':aid,'source_id':source_id,'source_name':source_name,'relation':rel,'status':status,'resolved':resolved,'unresolved':unresolved,'source_urls':urls,'discovered_repositories':discovered_repos[:10], 'governance':gov_results.get(aid)})
    status_counts[status]+=1; relation_counts[rel]+=1
    record={
      'run_id':RUN_ID,'attempted_at':AS_OF,'action_id':aid,'action_key':a.get('action_key',''),'operator':'discover','status':status,'source_name':source_name,
      'resolved_dimensions':resolved,'unresolved_dimensions':unresolved,
      'outcome':{'new_nodes':new_nodes,'new_edges':new_edges,'evidence_upgraded':verified,'verified_claims':verified,'rejected_claims':rejected},
      'note':note
    }
    records.append(record)

history_path.write_text(json.dumps(history,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out={'schema':'ai-infra-relationship/full-discover-frontier-v1','as_of':AS_OF,'run_id':RUN_ID,'actions':len(actions),'status_counts':dict(status_counts),'relation_counts':dict(relation_counts),'created_nodes':created_nodes,'records':frontier}
(ROOT/'generated/full-discover-frontier.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=ROOT/'docs/research-runs/2026-09-18-discover-full.md'; report.parent.mkdir(parents=True,exist_ok=True)
lines=['# Full DISCOVER Research Run — 2026-09-18','', 'This run executes the DISCOVER operator against the full currently eligible portfolio rather than the mixed daily budget.','',f'- DISCOVER actions: **{len(actions)}**',f'- Coverage-gap triggers and bridge triggers are both included.',f'- Durable outcomes: '+', '.join(f'{k}={v}' for k,v in sorted(status_counts.items())),f'- Governance-maintainer nodes created: **{len(created_nodes)}**',f'- Newly encoded maintainer project edges: **{upgraded_edges + len(created_nodes)}**','', '## Evidence policy','', 'The full pass separates discovery from promotion. Project maintainer actions may create handle-first person nodes only when project-owned governance files explicitly name individual GitHub handles. Other frontier signals are retained as partial/unresolved until their semantic relation is independently confirmed. Repository namespaces, corporate-email domains, shared schools, or contributor presence are not promoted to employer/origin/coworker claims by themselves.','', '## Relation portfolio','', '| Relation | Actions |','|---|---:|']
for rel,c in relation_counts.most_common(): lines.append(f'| `{rel}` | {c} |')
lines += ['', '## New governance-maintainer nodes','']
if created_nodes:
    for nid in created_nodes: lines.append(f'- `{nid}`')
else: lines.append('- None')
lines += ['', '## Frontier artifact','', '`generated/full-discover-frontier.json` contains per-action resolved and unresolved dimensions plus discovered repository/governance signals.','']
report.write_text('\n'.join(lines),encoding='utf-8')
print('full DISCOVER outcomes', dict(status_counts), 'created_nodes', len(created_nodes))
