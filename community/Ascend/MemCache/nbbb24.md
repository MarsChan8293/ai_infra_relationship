---
type: person
name: nbbb24
aliases: ["@nbbb24"]
projects: [MemCache, SGLang]
roles: [Ascend MemCache HiCache Integration Author]
areas: [kv-cache, hicache, prefix-cache, zero-copy, distributed-storage, ascend]
confidence: project-credit
last_verified: "2026-09"
---
# nbbb24

项目：[[MemCache]] · [[SGLang]]

## SGLang × MemCache
- 2026 年提交 SGLang PR #26043，将 Ascend MemCache 接入 HiCache 作为新的 L3 external storage backend。
- 实现 `AscendMemcacheStore`，基于 `memcache_hybrid.DistributedObjectStore` 提供 `batch_get` / `batch_set` / `batch_exists` 等 zero-copy page I/O，并将 `ascend_memcache` 注册进 HiCache storage backend factory。
- 目标是让 Ascend HiCache 从 HBM + host 两层扩展到 distributed L3 storage，实现跨节点 prefix cache sharing / reuse，服务长上下文与多轮场景。

截至 2026-09 核验时，该 PR 仍处于 open 状态，因此这里记录为 **integration author / ongoing contribution**，不写成已合入能力或 maintainer。

## Sources
- https://github.com/sgl-project/sglang/pull/26043
- https://gitcode.com/Ascend/memcache
