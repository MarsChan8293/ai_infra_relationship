---
type: person
name: Aoi
aliases: ["Aionw", "@Aionw"]
communities: [Mooncake]
projects: [Mooncake]
roles: [Mooncake Store HA Codeowner, Mooncake CI Codeowner, Mooncake Contributor]
areas: [distributed-storage, kv-cache, high-availability, storage-architecture, nvme, observability, llm-inference]
confidence: verified
last_verified: "2026-09"
---
# Aoi（@Aionw）

公开 GitHub 资料目前只稳定确认公开名 **Aoi**、账号 `@Aionw` 与北京所在地；没有足够证据确认法定姓名或当前雇主，因此不做身份猜测。

## Mooncake 角色
Mooncake 当前 `CODEOWNERS` 把 `@Aionw` 放在 `.github` / CI 路径以及 `mooncake-store/*/ha/` 的 codeowner 集合中。2026 年其持续发起和实现多项 Store 架构 RFC，因此应视为当前 Mooncake Store / HA 工程网络中的重要维护节点，而不只是偶发 contributor。

## 代表性工作
- **SegmentPool 重构**：提出以 SegmentPool 统一 Memory / CXL / NoF 可分配 region，以 LocalSsdManager 单独管理 client-local SSD 的 Store 架构重构。
- **Store domain state / metrics 解耦**：推动 eviction、promotion、replica placement 等业务状态不再依赖 metrics 反向读取。
- **AcceleratorDevice abstraction**：降低 Mooncake Store 本地 accelerator memory 代码对具体 vendor SDK 的耦合。
- **MasterAdminServer / mooncake-cli**：持续整理 Store 管理、运维和可观测接口。
- **CI / docs / build**：同时承担项目级 CI、文档和构建维护，是少数跨 Store 核心与 repo operations 的节点。

## 人物关系
- [[community/kvcache-ai/Mooncake/Ke Yang|Ke Yang]]：Mooncake Store 的顶层 Codeowner；Aionw 则在 Store HA 与 repo/CI 层承担具体 codeownership，构成 Store 治理的不同层级。
- [[community/kvcache-ai/Mooncake/Xuchun Shang|Xuchun Shang]]、[[community/kvcache-ai/Mooncake/Xinpeng Zhao|Xinpeng Zhao]]：同处 Mooncake Store / integration 工程网络，但公开资料不足以推断当前公司或直属团队关系。

## Sources
- https://github.com/Aionw
- https://github.com/kvcache-ai/Mooncake/blob/main/.github/CODEOWNERS
- https://github.com/kvcache-ai/Mooncake/issues/3360
- https://github.com/kvcache-ai/Mooncake/issues/3158
- https://github.com/kvcache-ai/Mooncake/issues/2582
- https://github.com/kvcache-ai/Mooncake/issues/2400
- https://github.com/kvcache-ai/Mooncake/issues/2406
