---
type: person
name: Dongjoo Seo
aliases: ["DongDongJu", "@DongDongJu"]
current_affiliations: ["Samsung"]
public_email: dongjoo.seo1@samsung.com
communities: [LMCache]
roles: [LMCache Committer, Component Owner]
areas: [kv-cache, multiprocess, distributed-kv-cache, memory-management, storage-backend, dax, cxl, sglang-integration, c-extensions, rust, operator]
confidence: verified
last_verified: "2026-09"
---
# Dongjoo Seo（DongDongJu）

LMCache 官方 `MAINTAINERS.md` 将 Dongjoo Seo 列为 Samsung Committer。2026 年公开提交持续使用 `dongjoo.seo1@samsung.com`。

## LMCache 角色
当前 `CODEOWNERS` 覆盖 multiprocess、distributed/L2、memory management、storage backend、SGLang integration、C extensions、operator、Rust，以及 CXL / Maru / DAX 路径。

2026 年其工程主线尤其集中在 **Device-DAX / CXL 作为 KV cache 层级**：包括 DAX hotplug、hybrid L1 overflow、allocator 拆分，以及 DAX L2 load batching/并行 copy 优化。

此外，其 #4130 直接加入 **SGLang ↔ vLLM KV cache sharing** 示例，是一个少见的跨 serving-engine cache-sharing 桥节点。

## Sources
- https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://github.com/LMCache/LMCache/commit/f09885bf10546d1d8e11939052660069a24502d1
- https://github.com/LMCache/LMCache/commit/a2bb21d1c160e80e64389fed0d7213d5b9e0d84b
- https://github.com/LMCache/LMCache/commit/e38ee4157a11703b07845f45fd98e714b25c13cd
