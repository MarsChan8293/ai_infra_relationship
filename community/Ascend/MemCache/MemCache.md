---
type: project
name: MemCache
linked_people:
  - "community/Ascend/MemCache/ader47"
  - "community/Ascend/MemCache/chenyz6"
  - "community/Ascend/MemCache/DreamerLeader"
  - "community/Ascend/MemCache/gcw_qYJeyWK4"
  - "community/Ascend/MemCache/j00808874"
  - "community/Ascend/MemCache/nbbb24"
  - "community/Ascend/MemCache/Pz1116"
  - "community/Ascend/MemCache/shilinlee"
  - "community/Ascend/MemCache/tyy0829"
  - "community/Ascend/MemCache/yrewzjsx"
  - "community/Ascend/MemCache/Zixi Qu"
  - "community/Ascend/MemCache/吕有辉"
  - "community/Ascend/MemCache/彭海清 Haiqing Peng"
companies: ["华为"]
company_relation: company-led
layer: kv-cache
hardware: [Ascend]
open_source: true
repository: https://gitcode.com/Ascend/memcache
areas: [kv-cache, distributed-storage, prefix-cache, memory-pooling, disaggregated-serving, ascend]
last_verified: "2026-09"
linked_companies:
  - "company/华为/华为"
---
# MemCache

## 项目简介
MemCache 是 Ascend 生态面向 AI / LLM 推理的高性能分布式 KV Cache 存储引擎。它把 HBM、DDR、SSD 等多级介质组织成缓存池，并通过 [[MemFabric]] 提供的跨机、跨介质直接访问能力降低 KV 数据搬运开销。

它对本图谱的重要性在于：这是昇腾侧少数直接落在 **KV Cache 池化 / Prefix Cache / 分离式推理数据面** 的开源项目，位置介于 serving engine 与硬件数据传输层之间。

## GitCode
https://gitcode.com/Ascend/memcache

## GitHub 镜像
https://github.com/Ascend/memcache

## 推理优化主线
- **多级 KV Cache 池**：支持 HBM / DDR / SSD 等多层缓存池，以及冷热数据淘汰、预取。
- **OneCopy 数据路径**：底层依赖 [[MemFabric]]，在不同 Ascend 硬件上利用 device RDMA / SDMA、host RDMA、URMA、UBOE 等路径完成跨节点与跨介质访问。
- **Prefix Cache**：官方 2026-06 动态明确给出 MemCache 使能推理 PrefixCache 的案例。
- **高可用与解耦部署**：仓库持续出现 MetaService HA、分离部署、地址导出、KV offload 等工程改动。

## Serving / KV 生态关系
- [[MemFabric]]：**强依赖 / 数据传输底座**。MemCache 官方安装与 README 均明确依赖 MemFabric。
- [[vLLM-Ascend]]：**已验证 KV Pool backend**。vLLM-Ascend 官方 KV Pool 文档提供以 MemCache 作为 backend 的部署流程。
- [[SGLang]]：MemCache 官方 README 明确列为已对接的开源推理框架之一；后续 BFS 继续核验具体 connector / adapter 路径与负责人。
- [[MindIE-LLM]]：MemCache 官方 README 明确列为已对接的昇腾推理框架之一；后续继续追具体集成边。
- [[Mooncake]]：属于同一 KV cache / data movement 邻域。MemCache 2026 年提交中出现与 Mooncake API 对齐的改动，但这里暂不写成直接治理或共同维护关系。

## 第一轮人物探索候选
当前仓库 merge metadata 中反复出现 `yrewzjsx`、`chenyz6`、`shilinlee_com` / `shilinlee`、`p3rry`、`j00808874` 等 handle，分别覆盖 merge、核心 API、MemFabric 解耦、HA / REST、构建与性能路径。

这些信号足以进入下一轮人物调查，但**本轮不直接把它们标成 maintainer**：目前尚未找到稳定的 MAINTAINERS / CODEOWNERS / governance 文件来证明正式治理角色，也不根据邮箱或 handle 猜实名与职级。

## BFS 下一跳
1. `MemCache -> maintainers / core reviewers`：优先找 governance、长期 merge 权限与 release 责任人。
2. `MemCache -> MemFabric -> maintainers`：识别 KV 存储层与数据移动层是否由同一批核心工程师连接。
3. `MemCache -> vLLM-Ascend`：追具体 KV connector / backend PR 与两侧直接协作者。
4. `MemCache -> SGLang / MindIE-LLM`：确认实际 adapter、接口 owner 和性能优化贡献者。
5. `MemCache -> Mooncake / LMCache`：只比较工程边界、API 对齐和竞争/互补关系，不因功能相似自动建立人物关系。

## Sources
- https://gitcode.com/Ascend/memcache/tree/develop
- https://gitcode.com/Ascend/memcache/blob/develop/README.md
- https://github.com/Ascend/memcache
- https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/kv_pool.html

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/Ascend/MemCache/ader47|ader47]]：是 2026 年 layerwise KV Pool + MemCache backend 实现的直接共同贡献者。
- [[community/Ascend/MemCache/chenyz6|chenyz6]]：长期出现在 MemCache 的 `Merged-by` 记录中，覆盖 MetaService、MemFabric 接口、KV Event、测试与构建等关键路径。
- [[community/Ascend/MemCache/DreamerLeader|DreamerLeader]]：2026-01 发起 vLLM-Ascend RFC #6410，明确提出把 MemCache 纳入 KV Pool storage backend，并将原有 MooncakeStoreConnector 抽象为统一的 AscendStoreConnector + Backend 接口。
- [[community/Ascend/MemCache/gcw_qYJeyWK4|gcw_qYJeyWK4]]：还涉及 async flush、rewarm 等 storage tier / reliability 工作，是当前 MemCache 分层存储方向非常值得继续追的人物。
- [[community/Ascend/MemCache/j00808874|j00808874]]：早期到中期多次提交覆盖服务面与工程基础设施，是 MemCache 从“KV 存储库”走向可部署系统的重要贡献者之一。
- [[community/Ascend/MemCache/nbbb24|nbbb24]]：2026 年提交 SGLang PR #26043，将 Ascend MemCache 接入 HiCache 作为新的 L3 external storage backend。
- [[community/Ascend/MemCache/Pz1116|Pz1116]]：2026 Q2 KV Cache Pool roadmap 的主要公开推动者之一，明确把 MemCache、Mooncake、YuanRong 等列为 AscendStore backend。
- [[community/Ascend/MemCache/shilinlee|shilinlee]]：https://gitcode.com/Ascend/memcache/tree/develop
- [[community/Ascend/MemCache/tyy0829|tyy0829]]：2026 年直接推进 vLLM-Ascend 的 **layerwise KV Pool + MemCache backend**：减少 per-layer key / MetaServer lookup 开销，把 GVA 分配移动到 worker，并使用 MemCache `batch_copy` / lease 生命周期管理完成按层 KV save/load。
- [[community/Ascend/MemCache/yrewzjsx|yrewzjsx]]：在 MemCache 的大量 MR 中持续出现 `Merged-by: yrewzjsx`，覆盖配置、存储层、KV Event、CI、文档、可靠性等多个子系统，是当前最明显的代码入口 / 合并把关者之一。
- [[community/Ascend/MemCache/Zixi Qu|Zixi Qu]]：https://gitcode.com/Ascend/memcache/tree/develop/3rdparty
- [[community/Ascend/MemCache/吕有辉|吕有辉]]：在 MindIE-PyMotor 推进多 KV 池化后端支持，使 MemCache MetaService / LocalService 能适配 A2 / A3 / A5 等部署路径。
- [[community/Ascend/MemCache/彭海清 Haiqing Peng|彭海清（Haiqing Peng）]]：其贡献同时触及 MemFabric 自身和 MemCache 对 MemFabric 的接口边界，是这条数据面链路中很值得继续追的核心工程人物。

<!-- END AUTO PROJECT PEOPLE -->
