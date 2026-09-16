#!/usr/bin/env python3
"""Synchronize company/project/community -> person reverse relationships.

Person Markdown remains the source of truth for human-authored facts:
- `current_affiliations:` -> company association when the affiliation resolves to a company.
- `public_email:` -> `email_affiliations:` only when its domain matches the conservative
  allowlist in `schema/email-domain-company.json`.
- `email_affiliations:` proves an organization association from a public professional
  email domain; it does NOT by itself prove current employment or a job title.
- `linked_companies:` is the generated canonical union of company associations from
  `current_affiliations:` and `email_affiliations:`.
- school/research/model-team affiliations are valid but handled by their own entity layers.
- `projects:` / `project:` / `communities:` / `community:` -> project/community `linked_people:`.

Existing hand-written narrative and curated `people:` fields are preserved. Only
explicitly generated frontmatter fields and marked body sections are replaced.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import defaultdict

NODE_ROOTS = ("company", "community", "university")
PROJECT_TYPES = {"project", "community", "infra-project", "project-collection"}
NON_COMPANY_AFFILIATION_TYPES = {"school", "research-institution", "model-team"}
COMPANY_START = "<!-- BEGIN AUTO COMPANY PEOPLE -->"
COMPANY_END = "<!-- END AUTO COMPANY PEOPLE -->"
PROJECT_START = "<!-- BEGIN AUTO PROJECT PEOPLE -->"
PROJECT_END = "<!-- END AUTO PROJECT PEOPLE -->"
PERSON_COMPANY_START = "<!-- BEGIN AUTO PERSON COMPANIES -->"
PERSON_COMPANY_END = "<!-- END AUTO PERSON COMPANIES -->"
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")
EMAIL_RE = re.compile(r"^[^@\s<>]+@([^@\s<>]+)$")

COMMON_ALIASES = {
    "清华大学": ["Tsinghua University"],
    "北京大学": ["Peking University", "PKU"],
    "上海交通大学": ["Shanghai Jiao Tong University", "SJTU"],
    "浙江大学": ["Zhejiang University", "ZJU"],
    "UC Berkeley": ["University of California, Berkeley", "Berkeley"],
    "北京智源人工智能研究院": ["BAAI", "Beijing Academy of Artificial Intelligence"],
}


def norm(value: str) -> str:
    return value.replace("\\", "/").strip().strip("/").removesuffix(".md")


def fold(value: str) -> str:
    return re.sub(r"\s+", " ", norm(value)).casefold()


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return [], text
    lines = text.splitlines()
    try:
        end = lines.index("---", 1)
    except ValueError:
        return [], text
    tail = "\n" if text.endswith("\n") else ""
    return lines[1:end], "\n".join(lines[end + 1 :]) + tail


def join_frontmatter(lines: list[str], body: str) -> str:
    return "---\n" + "\n".join(lines).rstrip() + "\n---\n" + body


def key_of(line: str):
    if line.startswith((" ", "\t", "-")) or ":" not in line:
        return None
    return line.split(":", 1)[0].strip() or None


def blocks(lines: list[str]):
    result, i = [], 0
    while i < len(lines):
        key = key_of(lines[i])
        if not key:
            result.append((None, [lines[i]]))
            i += 1
            continue
        j = i + 1
        while j < len(lines) and key_of(lines[j]) is None:
            j += 1
        result.append((key, lines[i:j]))
        i = j
    return result


def parse_inline_list(body: str) -> list[str]:
    if not body.strip():
        return []
    parts, buf, quote = [], [], None
    for ch in body:
        if ch in "\"'":
            if quote == ch:
                quote = None
            elif quote is None:
                quote = ch
            buf.append(ch)
        elif ch == "," and quote is None:
            parts.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf).strip())
    return [part.strip().strip("\"'") for part in parts if part.strip()]


def get_block(lines: list[str], wanted: str):
    return next((block for key, block in blocks(lines) if key == wanted), None)


def get_values(lines: list[str], wanted: str) -> list[str]:
    block = get_block(lines, wanted)
    if not block:
        return []
    value = block[0].split(":", 1)[1].strip()
    if not value:
        return [line[4:].strip().strip("\"'") for line in block[1:] if line.startswith("  - ") and line[4:].strip()]
    if value.startswith("[") and value.endswith("]"):
        return parse_inline_list(value[1:-1])
    return [value.strip("\"'")]


def get_scalar(lines: list[str], wanted: str):
    block = get_block(lines, wanted)
    if not block:
        return None
    value = block[0].split(":", 1)[1].strip()
    return value.strip("\"'") if value else None


def set_block_list(lines: list[str], key: str, values: list[str]) -> list[str]:
    values = list(dict.fromkeys(v for v in values if v))
    replacement = [f"{key}: []"] if not values else [f"{key}:"] + [f"  - {json.dumps(v, ensure_ascii=False)}" for v in values]
    out, inserted = [], False
    for existing, block in blocks(lines):
        if existing == key:
            if not inserted:
                out.extend(replacement)
                inserted = True
            continue
        if not inserted and existing in {
            "areas", "projects", "companies", "company_relation", "category", "layer",
            "open_source", "repository", "governance", "confidence", "last_verified",
        }:
            out.extend(replacement)
            inserted = True
        out.extend(block)
    if not inserted:
        out.extend(replacement)
    return out


def set_optional_block_list(lines: list[str], key: str, values: list[str]) -> list[str]:
    if values or get_block(lines, key):
        return set_block_list(lines, key, values)
    return lines


def all_markdown(root: pathlib.Path):
    for dirname in NODE_ROOTS:
        base = root / dirname
        if base.exists():
            yield from sorted(base.rglob("*.md"))


def load_records(root: pathlib.Path):
    rows = []
    for path in all_markdown(root):
        text = path.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if not fm:
            continue
        rel = path.relative_to(root).as_posix()
        rows.append({
            "path": path,
            "rel": rel,
            "id": rel[:-3],
            "text": text,
            "fm": fm,
            "body": body,
            "type": get_scalar(fm, "type") or "",
            "name": get_scalar(fm, "name") or path.stem,
            "english_name": get_scalar(fm, "english_name") or "",
        })
    return rows


def aliases_for(record: dict) -> list[str]:
    values = [record["name"], pathlib.PurePosixPath(record["id"]).name, *get_values(record["fm"], "aliases")]
    values.extend(COMMON_ALIASES.get(record["name"], []))
    return list(dict.fromkeys(v for v in values if v))


def build_index(records: list[dict], allowed_types: set[str]):
    selected = [r for r in records if r["type"] in allowed_types]
    aliases: dict[str, list[dict]] = defaultdict(list)
    ids = {}
    for record in selected:
        ids[fold(record["id"])] = record
        seen = set()
        for value in aliases_for(record):
            token = fold(value)
            if token and token not in seen:
                seen.add(token)
                aliases[token].append(record)
    return selected, aliases, ids


def resolve(value: str, aliases, ids):
    value = norm(value)
    direct = ids.get(fold(value))
    if direct:
        return direct
    for candidate in (value, pathlib.PurePosixPath(value).name):
        unique = {r["id"]: r for r in aliases.get(fold(candidate), [])}
        if len(unique) == 1:
            return next(iter(unique.values()))
    return None


def link_target(inner: str) -> str:
    return norm(inner.split("|", 1)[0].split("#", 1)[0].strip())


def display_name(person: dict) -> str:
    name, english = person["name"], person["english_name"]
    return f"{name}（{english}）" if english and fold(name) != fold(english) else name


def load_email_domain_policy(root: pathlib.Path) -> tuple[dict[str, str], set[str], pathlib.Path]:
    path = root / "schema/email-domain-company.json"
    if not path.exists():
        raise SystemExit(f"Missing email-domain policy: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    rules: dict[str, str] = {}
    for item in payload.get("rules", []):
        domain = str(item.get("domain") or "").strip().strip(".").casefold()
        company = str(item.get("company") or "").strip()
        if not domain or not company:
            continue
        if domain in rules and rules[domain] != company:
            raise SystemExit(f"Conflicting email-domain rule for {domain}: {rules[domain]} vs {company}")
        rules[domain] = company
    ignored = {
        str(value).strip().strip(".").casefold()
        for value in payload.get("ignored_domains", [])
        if str(value).strip()
    }
    return rules, ignored, path


def extract_email_domain(value: str | None) -> str | None:
    if not value:
        return None
    match = EMAIL_RE.match(value.strip())
    return match.group(1).strip(".").casefold() if match else None


def suffix_matches(domain: str, candidate: str) -> bool:
    return domain == candidate or domain.endswith("." + candidate)


def infer_email_company(public_email: str | None, rules: dict[str, str], ignored: set[str]):
    domain = extract_email_domain(public_email)
    if not domain:
        return None, None, "invalid" if public_email else None
    if any(suffix_matches(domain, ignored_domain) for ignored_domain in ignored):
        return None, domain, "ignored"
    matches = [(len(rule_domain), rule_domain, company) for rule_domain, company in rules.items() if suffix_matches(domain, rule_domain)]
    if not matches:
        return None, domain, "unmapped"
    _, matched_domain, company = max(matches)
    return company, domain, matched_domain


def body_detail(person: dict, target: dict, aliases, ids, preferred_tokens: tuple[str, ...], strict_preferred: bool = False) -> str | None:
    active_heading, fallback = "", None
    for raw in person["body"].splitlines():
        stripped = raw.strip()
        if stripped.startswith("## "):
            active_heading = stripped[3:].strip().casefold()
            continue
        if not stripped.startswith("-"):
            continue
        matched = False
        for match in WIKILINK_RE.finditer(stripped):
            resolved = resolve(link_target(match.group(1)), aliases, ids)
            if resolved and resolved["id"] == target["id"]:
                matched = True
                break
        if not matched:
            folded = fold(stripped)
            matched = any(fold(alias) in folded for alias in aliases_for(target))
        if not matched:
            continue
        detail = stripped.lstrip("- ").strip()
        if len(detail) > 240:
            detail = detail[:237].rstrip() + "..."
        if any(token in active_heading for token in preferred_tokens):
            return detail
        if not strict_preferred:
            fallback = fallback or detail
    return fallback


def replace_auto_section(body: str, start: str, end: str, section: str | None) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), flags=re.DOTALL)
    if section is None:
        updated = pattern.sub("", body, count=1)
        return re.sub(r"\n{3,}", "\n\n", updated).rstrip() + "\n"
    if pattern.search(body):
        updated = pattern.sub(section, body, count=1)
        return updated if updated.endswith("\n") else updated + "\n"
    return body.rstrip() + "\n\n" + section + "\n"


def company_source_label(sources: set[str]) -> str:
    if sources == {"current_affiliation", "email_domain"}:
        return "当前 affiliation + 公开职业邮箱域名双重证据"
    if "current_affiliation" in sources:
        return "人物页 `current_affiliations:` 明确记录"
    if "email_domain" in sources:
        return "公开职业邮箱域名证据；表示组织关联，不单独证明当前任职"
    return "人物页公开组织关联"


def person_company_section(person: dict, companies: list[dict], source_fields: dict[str, set[str]]) -> str | None:
    if not companies:
        return None
    lines = [
        PERSON_COMPANY_START,
        "## 关联公司（自动汇总）",
        "",
        "以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。"
        "邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。",
        "",
    ]
    for company in companies:
        label = company_source_label(source_fields.get(company["id"], set()))
        lines.append(f"- [[{company['id']}|{company['name']}]]：{label}。")
    lines.extend(["", PERSON_COMPANY_END])
    return "\n".join(lines)


def company_section(company: dict, people: list[dict], source_fields: dict[str, set[str]], aliases, ids) -> str | None:
    if not people:
        return None
    lines = [
        COMPANY_START,
        "## 关联人物（自动汇总）",
        "",
        "以下人物由其 `current_affiliations:` 与/或 `public_email` 企业域名规则反向汇总。"
        "邮箱域名证据表示可核验的组织关联，但不会单独推断当前任职、职级、直属汇报或团队归属。",
        "",
    ]
    for person in people:
        detail = body_detail(person, company, aliases, ids, ("当前", "工作", "经历", "简介"), strict_preferred=True)
        label = company_source_label(source_fields.get(person["id"], set()))
        description = f"{label}；{detail}" if detail else f"{label}。"
        lines.append(f"- [[{person['id']}|{display_name(person)}]]：{description}")
    lines.extend(["", COMPANY_END])
    return "\n".join(lines)


def project_section(target: dict, people: list[dict], source_fields: dict[str, set[str]], aliases, ids) -> str | None:
    if not people:
        return None
    lines = [PROJECT_START, "## 关联人物（自动汇总）", "", "以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。", ""]
    for person in people:
        detail = body_detail(person, target, aliases, ids, ("项目", "社区", "贡献", "当前", "核心", "技术"))
        fields = source_fields.get(person["id"], set())
        if detail:
            description = detail
        elif "projects" in fields or "project" in fields:
            description = "项目关联；人物页已明确记录该项目。"
        else:
            description = "社区贡献关联；人物页已明确记录该社区。"
        lines.append(f"- [[{person['id']}|{display_name(person)}]]：{description}")
    lines.extend(["", PROJECT_END])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()

    rules, ignored_domains, policy_path = load_email_domain_policy(root)
    records = load_records(root)
    companies, company_aliases, company_ids = build_index(records, {"company"})
    noncompanies, noncompany_aliases, noncompany_ids = build_index(records, NON_COMPANY_AFFILIATION_TYPES)
    project_nodes, project_aliases, project_ids = build_index(records, PROJECT_TYPES)
    people = [r for r in records if r["type"] == "person"]

    company_reverse: dict[str, list[dict]] = defaultdict(list)
    company_sources: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    project_reverse: dict[str, list[dict]] = defaultdict(list)
    project_sources: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    unresolved = []
    unmapped_email_domains = defaultdict(list)
    ignored_email_domains = defaultdict(int)
    inferred_email_links = 0
    person_touched = []

    for person in people:
        person_company_ids: dict[str, dict] = {}
        inferred_email_affiliations: list[str] = []

        for value in get_values(person["fm"], "current_affiliations"):
            target = resolve(value, company_aliases, company_ids)
            if not target:
                if resolve(value, noncompany_aliases, noncompany_ids):
                    continue
                unresolved.append({"kind": "affiliation", "person": person["rel"], "value": value})
                continue
            person_company_ids[target["id"]] = target
            company_sources[target["id"]][person["id"]].add("current_affiliation")

        public_email = get_scalar(person["fm"], "public_email")
        inferred_company_name, email_domain, email_status = infer_email_company(public_email, rules, ignored_domains)
        if inferred_company_name:
            target = resolve(inferred_company_name, company_aliases, company_ids)
            if not target:
                unresolved.append({
                    "kind": "email-domain-company",
                    "person": person["rel"],
                    "value": inferred_company_name,
                    "domain": email_domain,
                })
            else:
                inferred_email_affiliations.append(target["name"])
                person_company_ids[target["id"]] = target
                company_sources[target["id"]][person["id"]].add("email_domain")
                inferred_email_links += 1
        elif email_status == "unmapped" and email_domain:
            unmapped_email_domains[email_domain].append(person["rel"])
        elif email_status == "ignored" and email_domain:
            ignored_email_domains[email_domain] += 1
        elif email_status == "invalid":
            unresolved.append({"kind": "invalid-public-email", "person": person["rel"], "value": public_email})

        for target in person_company_ids.values():
            company_reverse[target["id"]].append(person)

        updated_fm = set_optional_block_list(person["fm"], "email_affiliations", inferred_email_affiliations)
        linked_company_ids = sorted(person_company_ids, key=str.casefold)
        updated_fm = set_optional_block_list(updated_fm, "linked_companies", linked_company_ids)
        linked_company_records = [person_company_ids[company_id] for company_id in linked_company_ids]
        person_source_fields = {
            company_id: company_sources[company_id].get(person["id"], set())
            for company_id in linked_company_ids
        }
        updated_body = replace_auto_section(
            person["body"],
            PERSON_COMPANY_START,
            PERSON_COMPANY_END,
            person_company_section(person, linked_company_records, person_source_fields),
        )
        updated_person = join_frontmatter(updated_fm, updated_body)
        if updated_person != person["text"]:
            person["path"].write_text(updated_person, encoding="utf-8")
            person["text"] = updated_person
            person["fm"] = updated_fm
            person["body"] = updated_body
            person_touched.append(person["rel"])

        seen_projects = set()
        for field in ("projects", "project", "communities", "community"):
            for value in get_values(person["fm"], field):
                target = resolve(value, project_aliases, project_ids)
                if not target:
                    unresolved.append({"kind": field, "person": person["rel"], "value": value})
                    continue
                project_sources[target["id"]][person["id"]].add(field)
                if target["id"] not in seen_projects:
                    project_reverse[target["id"]].append(person)
                    seen_projects.add(target["id"])

    touched = list(person_touched)
    company_associations, project_associations = 0, 0
    for company in companies:
        unique_people = {p["id"]: p for p in company_reverse.get(company["id"], [])}
        linked = sorted(unique_people.values(), key=lambda r: r["id"].casefold())
        company_associations += len(linked)
        updated_fm = set_block_list(company["fm"], "linked_people", [p["id"] for p in linked])
        updated_body = replace_auto_section(
            company["body"],
            COMPANY_START,
            COMPANY_END,
            company_section(company, linked, company_sources.get(company["id"], {}), company_aliases, company_ids),
        )
        updated = join_frontmatter(updated_fm, updated_body)
        if updated != company["text"]:
            company["path"].write_text(updated, encoding="utf-8")
            touched.append(company["rel"])

    for target in project_nodes:
        linked = sorted(project_reverse.get(target["id"], []), key=lambda r: r["id"].casefold())
        project_associations += len(linked)
        updated_fm = set_block_list(target["fm"], "linked_people", [p["id"] for p in linked])
        updated_body = replace_auto_section(target["body"], PROJECT_START, PROJECT_END, project_section(target, linked, project_sources.get(target["id"], {}), project_aliases, project_ids))
        updated = join_frontmatter(updated_fm, updated_body)
        if updated != target["text"]:
            target["path"].write_text(updated, encoding="utf-8")
            touched.append(target["rel"])

    generated_person_company_files = sum(
        1 for person in people if get_values(person["fm"], "linked_companies")
    )

    print(
        f"Entity reverse sync: {len(companies)} companies / {company_associations} company-person links "
        f"({inferred_email_links} supported by mapped public-email domains); "
        f"{generated_person_company_files} person nodes with linked_companies; "
        f"{len(project_nodes)} project-community nodes / {project_associations} contribution links; "
        f"{len(touched)} files updated ({len(person_touched)} person nodes); {len(unresolved)} unresolved source values; "
        f"{len(noncompanies)} non-company affiliation targets recognized; policy={policy_path.relative_to(root)}."
    )
    for domain, person_paths in sorted(unmapped_email_domains.items()):
        print(f"UNMAPPED EMAIL DOMAIN {domain}: {len(person_paths)} person(s), e.g. {person_paths[0]}")
    for domain, count in sorted(ignored_email_domains.items()):
        print(f"IGNORED EMAIL DOMAIN {domain}: {count}")
    for rel in touched[:120]:
        print("UPDATE:", rel)
    if len(touched) > 120:
        print(f"... plus {len(touched) - 120} more updated files")
    for item in unresolved[:120]:
        print("UNRESOLVED:", item)
    if len(unresolved) > 120:
        print(f"... plus {len(unresolved) - 120} more unresolved values")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
