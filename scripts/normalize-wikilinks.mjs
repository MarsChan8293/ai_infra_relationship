import fs from "node:fs"
import path from "node:path"

const contentRoot = path.resolve(process.argv[2] ?? "")
if (!contentRoot || !fs.existsSync(contentRoot)) {
  console.error(`Content root does not exist: ${contentRoot}`)
  process.exit(2)
}

const toPosix = (value) => value.split(path.sep).join("/")
const stripMd = (value) => value.replace(/\.md$/i, "")

function walk(dir) {
  const result = []
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) result.push(...walk(full))
    else if (entry.isFile() && entry.name.toLowerCase().endsWith(".md")) result.push(full)
  }
  return result
}

const files = walk(contentRoot)
const records = files.map((file) => {
  const rel = toPosix(path.relative(contentRoot, file))
  const relNoExt = stripMd(rel)
  return {
    file,
    rel,
    relNoExt,
    dir: path.posix.dirname(relNoExt),
    base: path.posix.basename(relNoExt),
  }
})

const byRel = new Map(records.map((r) => [r.relNoExt, r]))
const byRelLower = new Map()
const byBase = new Map()
const byBaseLower = new Map()

for (const record of records) {
  const relLower = record.relNoExt.toLowerCase()
  const relItems = byRelLower.get(relLower) ?? []
  relItems.push(record)
  byRelLower.set(relLower, relItems)

  const baseItems = byBase.get(record.base) ?? []
  baseItems.push(record)
  byBase.set(record.base, baseItems)

  const baseLower = record.base.toLowerCase()
  const lowerItems = byBaseLower.get(baseLower) ?? []
  lowerItems.push(record)
  byBaseLower.set(baseLower, lowerItems)
}

function safeDecode(value) {
  try {
    return decodeURIComponent(value)
  } catch {
    return value
  }
}

function normalizeTarget(value) {
  let target = safeDecode(value.trim()).replace(/\\/g, "/")
  target = target.replace(/\.md$/i, "")
  target = target.replace(/^\/+/, "")
  target = path.posix.normalize(target)
  if (target === ".") return ""
  return target
}

function exactRecord(target) {
  if (!target) return null
  if (byRel.has(target)) return byRel.get(target)
  const caseInsensitive = byRelLower.get(target.toLowerCase()) ?? []
  return caseInsensitive.length === 1 ? caseInsensitive[0] : null
}

function resolveTarget(targetRaw, source) {
  const target = normalizeTarget(targetRaw)
  if (!target) return { record: null, reason: "empty" }

  const exact = exactRecord(target)
  if (exact) return { record: exact, reason: "exact" }

  const relative = normalizeTarget(path.posix.join(source.dir, target))
  const relativeExact = exactRecord(relative)
  if (relativeExact) return { record: relativeExact, reason: "relative" }

  const base = path.posix.basename(target)
  let candidates = byBase.get(base) ?? []
  if (candidates.length === 0) candidates = byBaseLower.get(base.toLowerCase()) ?? []

  if (candidates.length === 1) return { record: candidates[0], reason: "unique-basename" }

  if (candidates.length > 1) {
    const sameDir = candidates.filter((candidate) => candidate.dir === source.dir)
    if (sameDir.length === 1) return { record: sameDir[0], reason: "same-directory" }
    return {
      record: null,
      reason: "ambiguous",
      candidates: candidates.map((candidate) => candidate.relNoExt),
    }
  }

  return { record: null, reason: "missing" }
}

let totalLinks = 0
let resolvedLinks = 0
let unresolvedLinks = 0
let samePageLinks = 0
const unresolved = []

for (const source of records) {
  const original = fs.readFileSync(source.file, "utf8")
  const rewritten = original.replace(/(?<!!)\[\[([^\]\n]+)\]\]/g, (full, inner) => {
    totalLinks += 1

    const pipeAt = inner.indexOf("|")
    const targetAndAnchor = (pipeAt >= 0 ? inner.slice(0, pipeAt) : inner).trim()
    const explicitAlias = pipeAt >= 0 ? inner.slice(pipeAt + 1).trim() : ""

    if (!targetAndAnchor || targetAndAnchor.startsWith("#") || targetAndAnchor.startsWith("^")) {
      samePageLinks += 1
      return full
    }

    const hashAt = targetAndAnchor.indexOf("#")
    const targetRaw = hashAt >= 0 ? targetAndAnchor.slice(0, hashAt).trim() : targetAndAnchor
    const anchor = hashAt >= 0 ? targetAndAnchor.slice(hashAt) : ""

    const resolved = resolveTarget(targetRaw, source)
    if (resolved.record) {
      resolvedLinks += 1
      const display = explicitAlias || path.posix.basename(normalizeTarget(targetRaw)) || resolved.record.base
      return `[[${resolved.record.relNoExt}${anchor}|${display}]]`
    }

    unresolvedLinks += 1
    const display = explicitAlias || path.posix.basename(normalizeTarget(targetRaw)) || targetRaw
    unresolved.push({
      source: source.rel,
      target: targetRaw,
      reason: resolved.reason,
      candidates: resolved.candidates ?? [],
    })
    return display
  })

  if (rewritten !== original) fs.writeFileSync(source.file, rewritten)
}

const report = {
  markdownFiles: records.length,
  totalLinks,
  resolvedLinks,
  unresolvedLinks,
  samePageLinks,
  unresolved,
}

const reportPath = path.join(contentRoot, ".wikilink-audit.json")
fs.writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`)

console.log(`Wikilink audit: ${records.length} Markdown files, ${totalLinks} links, ${resolvedLinks} resolved, ${unresolvedLinks} unresolved, ${samePageLinks} same-page links.`)
if (unresolved.length > 0) {
  console.log("Unresolved/ambiguous wikilinks were rendered as plain text to prevent 404s:")
  for (const item of unresolved.slice(0, 200)) {
    const suffix = item.candidates.length ? ` candidates=${item.candidates.join(", ")}` : ""
    console.log(`- ${item.source}: [[${item.target}]] (${item.reason})${suffix}`)
  }
  if (unresolved.length > 200) console.log(`... plus ${unresolved.length - 200} more; see ${reportPath}`)
}
