import fs from "node:fs"
import path from "node:path"

const contentRoot = path.resolve(process.argv[2] ?? "")
if (!contentRoot || !fs.existsSync(contentRoot)) {
  console.error(`Content root does not exist: ${contentRoot}`)
  process.exit(2)
}

const failOnAmbiguous = process.env.WIKILINK_FAIL_ON_AMBIGUOUS === "1"
const failOnMissing = process.env.WIKILINK_FAIL_ON_MISSING === "1"

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

function quartzSafeStem(stem) {
  return stem
    .replace(/\.(?=\s)/g, "")
    .replace(/\./g, "-")
    .replace(/-{2,}/g, "-")
}

// Quartz v5 currently treats dots inside Markdown basenames differently while
// slugifying output files vs. wikilink targets. Rename only the staged build
// copies, never repository source Markdown, and keep the old names as aliases.
const originalAliasByCanonical = new Map()
const stagedRenames = []
for (const file of walk(contentRoot)) {
  const ext = path.extname(file)
  const stem = path.basename(file, ext)
  const safeStem = quartzSafeStem(stem)
  if (safeStem === stem) continue

  const destination = path.join(path.dirname(file), `${safeStem}${ext}`)
  if (fs.existsSync(destination)) {
    throw new Error(`Cannot normalize dotted filename because destination exists: ${destination}`)
  }

  const originalRelNoExt = stripMd(toPosix(path.relative(contentRoot, file)))
  fs.renameSync(file, destination)
  const canonicalRelNoExt = stripMd(toPosix(path.relative(contentRoot, destination)))
  originalAliasByCanonical.set(canonicalRelNoExt, originalRelNoExt)
  stagedRenames.push({ from: originalRelNoExt, to: canonicalRelNoExt })
}

const files = walk(contentRoot)
const records = files.map((file) => {
  const rel = toPosix(path.relative(contentRoot, file))
  const relNoExt = stripMd(rel)
  const originalRelNoExt = originalAliasByCanonical.get(relNoExt) ?? relNoExt
  return {
    file,
    rel,
    relNoExt,
    originalRelNoExt,
    dir: path.posix.dirname(relNoExt),
    originalDir: path.posix.dirname(originalRelNoExt),
    base: path.posix.basename(relNoExt),
    originalBase: path.posix.basename(originalRelNoExt),
  }
})

const byRel = new Map()
const byRelLower = new Map()
const byBase = new Map()
const byBaseLower = new Map()

function addIndex(map, key, record) {
  if (!key) return
  const items = map.get(key) ?? []
  if (!items.includes(record)) items.push(record)
  map.set(key, items)
}

for (const record of records) {
  const relAliases = new Set([record.relNoExt, record.originalRelNoExt])
  for (const relAlias of relAliases) {
    addIndex(byRel, relAlias, record)
    addIndex(byRelLower, relAlias.toLowerCase(), record)
  }

  const baseAliases = new Set([record.base, record.originalBase])
  for (const baseAlias of baseAliases) {
    addIndex(byBase, baseAlias, record)
    addIndex(byBaseLower, baseAlias.toLowerCase(), record)
  }
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
  const exact = byRel.get(target) ?? []
  if (exact.length === 1) return exact[0]
  const caseInsensitive = byRelLower.get(target.toLowerCase()) ?? []
  return caseInsensitive.length === 1 ? caseInsensitive[0] : null
}

function resolveTarget(targetRaw, source) {
  const target = normalizeTarget(targetRaw)
  if (!target) return { record: null, reason: "empty" }

  const exact = exactRecord(target)
  if (exact) return { record: exact, reason: "exact" }

  const relativeCandidates = new Set([
    normalizeTarget(path.posix.join(source.dir, target)),
    normalizeTarget(path.posix.join(source.originalDir, target)),
  ])
  for (const relative of relativeCandidates) {
    const relativeExact = exactRecord(relative)
    if (relativeExact) return { record: relativeExact, reason: "relative" }
  }

  const base = path.posix.basename(target)
  let candidates = byBase.get(base) ?? []
  if (candidates.length === 0) candidates = byBaseLower.get(base.toLowerCase()) ?? []

  if (candidates.length === 1) return { record: candidates[0], reason: "unique-basename" }

  if (candidates.length > 1) {
    const sameDir = candidates.filter(
      (candidate) => candidate.dir === source.dir || candidate.originalDir === source.originalDir,
    )
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
      const display = explicitAlias || path.posix.basename(normalizeTarget(targetRaw)) || resolved.record.originalBase
      return `[[${resolved.record.relNoExt}${anchor}\\|${display}]]`
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

const unresolvedByReason = unresolved.reduce((acc, item) => {
  acc[item.reason] = (acc[item.reason] ?? 0) + 1
  return acc
}, {})

const report = {
  markdownFiles: records.length,
  stagedRenames,
  totalLinks,
  resolvedLinks,
  unresolvedLinks,
  unresolvedByReason,
  samePageLinks,
  policy: {
    failOnAmbiguous,
    failOnMissing,
  },
  unresolved,
}

const reportPath = path.join(contentRoot, ".wikilink-audit.json")
fs.writeFileSync(reportPath, `${JSON.stringify(report, null, 2)}\n`)

console.log(`Wikilink audit: ${records.length} Markdown files, ${totalLinks} links, ${resolvedLinks} resolved, ${unresolvedLinks} unresolved, ${samePageLinks} same-page links.`)
console.log(`Unresolved by reason: ${JSON.stringify(unresolvedByReason)}`)
if (stagedRenames.length > 0) {
  console.log(`Normalized ${stagedRenames.length} dotted Markdown filenames in the staged build copy:`)
  for (const item of stagedRenames) console.log(`- ${item.from} -> ${item.to}`)
}
if (unresolved.length > 0) {
  console.log("Unresolved/ambiguous wikilinks are rendered as plain text to prevent 404s, but are preserved in the audit artifact:")
  for (const item of unresolved.slice(0, 200)) {
    const suffix = item.candidates.length ? ` candidates=${item.candidates.join(", ")}` : ""
    console.log(`- ${item.source}: [[${item.target}]] (${item.reason})${suffix}`)
  }
  if (unresolved.length > 200) console.log(`... plus ${unresolved.length - 200} more; see ${reportPath}`)
}

const ambiguousCount = unresolvedByReason.ambiguous ?? 0
const missingCount = unresolvedByReason.missing ?? 0
if ((failOnAmbiguous && ambiguousCount > 0) || (failOnMissing && missingCount > 0)) {
  console.error(
    `Wikilink policy failed: ambiguous=${ambiguousCount} (fail=${failOnAmbiguous}), missing=${missingCount} (fail=${failOnMissing}).`,
  )
  process.exit(1)
}
