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

它对本图谱的重要性在于：这是昇腾侧少数直接落在 **KV Cache 池化 / Prefix Cache / 分离式推理数据面** 的开源项目，位置介于 serving engine、调度层与硬件数据传输层之间。

## GitCode
https://gitcode.com/Ascend/memcache

## GitHub 镜像
https://github.com/Ascend/memcache

## 推理优化主线
- **多级 KV Cache 池**：支持 HBM / DDR / SSD 等多层缓存池，以及冷热数据淘汰、预取。
- **OneCopy 数据路径**：底层依赖 [[MemFabric]]，在不同 Ascend 硬件上利用 device RDMA / SDMA、host RDMA、URMA、UBOE 等路径完成跨节点与跨介质访问。
- **Prefix Cache / KV Event**：除数据存储外，还通过 KvEvent 将 key store/remove/clear 等状态发布给上层调度系统，为 cache-aware routing 提供信号。
- **高可用与解耦部署**：仓库持续出现 MetaService HA、分离部署、地址导出、KV offload 等工程改动。

## 人物网络

### 1. MemCache / MemFabric 核心数据面
- [[yrewzjsx]]：MemCache 与 MemFabric 两个仓库中的高频 merge gatekeeper / core contributor，覆盖存储、配置、可靠性、benchmark 与多条接口路径。当前不因 merge 权限自动写成 maintainer。
- [[chenyz6]]：另一个跨双仓的稳定 merge / review 入口，同时直接处理 MemFabric Device URMA / BatchDataCopy 等数据移动路径。
- [[j00808874]]：连接 MemCache 服务面与 MemFabric HOST_SHM / fault-injection，覆盖 MetaService HA、REST、metrics、共享内存数据操作等。
- [[shilinlee]]：连接 setup config、Python/wheel/CI 与 56-bit GVA、AICPU kernel packaging、NUMA scan 等“可交付性 + 大容量池化”工程。
- [[彭海清 Haiqing Peng|彭海清（Haiqing Peng）]]：`p3rry`，负责 MemFabric 接口解耦、ABI / stream 适配、56-bit GVA 等，并提供 MemCache KvEvent 的前置框架。
- [[Zixi Qu]]：推进 KvEvent 广播、ZMQ / security / IPv6，并把 MemCache 事件流接向 PyMotor 的 prefill affinity / cache-aware scheduling。
- [[gcw_qYJeyWK4]]：与 Zixi Qu 共同推进 key eviction / prefetch，直接负责 DRAM ↔ SSD 分层 KV cache 冷热迁移路径。

### 2. vLLM-Ascend：Layerwise KV Pool
- [[DreamerLeader]]：2026 Q1 RFC 将 MemCache 纳入 AscendStore KV Pool backend，并推动 connector / backend 抽象。
- [[tyy0829]]：layerwise KV Pool + MemCache backend 的关键实现者，推进 request-level key、GVA、`batch_copy`、lease 生命周期与按层 save/load。
- [[ader47]]：与 tyy0829 共同署名 v0.23.0 layerwise MemCache backport，是该实现的直接共同贡献者。
- [[Pz1116]]：继续把路线扩展到 DeepSeek V4 多 KV group，处理 per-group GVA 与 multi-group layerwise callbacks，同时公开维护 KV Pool roadmap / known issues。

### 3. MindIE / SGLang：调度与 serving 集成
- [[吕有辉]]（`codeDogPro`）：在 MindIE-PyMotor / [[MindIE-Motor]] 侧接入 MemCache KvEvent，通过 kv-conductor 做缓存感知路由，使请求优先落到已经拥有共享前缀 KV 的节点。
- [[nbbb24]]：在 [[SGLang]] PR #26043 中实现 `AscendMemcacheStore`，尝试把 MemCache 作为 HiCache L3 distributed storage backend；截至 2026-09 该 PR 仍为 open，因此记录为 ongoing integration，而不是已合入维护角色。

## 已验证的人物协作链
- [[彭海清 Haiqing Peng|彭海清]] → [[Zixi Qu]]：KvEvent 前置框架到 PyMotor affinity 所需事件广播，PR 描述有明确继承式工程证据。
- [[Zixi Qu]] ↔ [[gcw_qYJeyWK4]]：共同实现 key eviction / prefetch，覆盖 DRAM 与 SSD 之间的 KV 数据迁移。
- [[tyy0829]] ↔ [[ader47]]：vLLM-Ascend PR #11585 明确共同署名 layerwise MemCache backend。
- [[tyy0829]] → [[Pz1116]]：Pz1116 的 DeepSeek V4 multi-group 实现明确基于 tyy0829 的原始 layerwise 工作。
- [[Zixi Qu]] → [[吕有辉]]：MemCache 侧 KvEvent 发布与 MindIE-Motor 侧 KvEvent 消费形成明确的跨项目上下游集成链。

## Serving / KV 生态关系
- [[MemFabric]]：**强依赖 / 数据传输底座**。MemCache 官方安装与 README 均明确依赖 MemFabric。
- [[vLLM-Ascend]]：**已验证 KV Pool backend**，并已继续演进到 layerwise / multi-group KV Pool。
- [[MindIE-Motor]] / MindIE-PyMotor：已出现 MemCache pool 与 KvEvent 驱动的 cache-aware scheduling 实际工程集成。
- [[SGLang]]：HiCache L3 MemCache backend 已有完整公开 PR 与性能验证，但截至本轮仍未合入。
- [[Mooncake]]：同一 KV cache / data movement 邻域；MemCache 提交存在 API 对齐工作，但不因接口相似自动推断治理或人物关系。

## BFS 下一跳
1. `yrewzjsx / chenyz6 -> governance`：继续寻找 MAINTAINERS / CODEOWNERS / release owner 等正式治理证据，决定是否可从 gatekeeper 升级到 maintainer。
2. `tyy0829 / Pz1116 -> vLLM-Ascend reviewer network`：追 weijinqian0、Wang Xiyuan、Yikun、MengqingCao 等 reviewer 与 MemCache KV Pool 的 pair-specific review / code ownership 证据。
3. `吕有辉 -> MindIE-Motor / PyMotor`：继续追 kv-conductor、KV affinity、offload event 的共同作者，补齐 control-plane 人物网络。
4. `nbbb24 -> SGLang HiCache`：观察 PR #26043 是否合入、谁完成关键 review，以及是否进入 HiCache CODEOWNERS / oncall 网络。
5. `MemCache -> Mooncake / LMCache`：只比较工程边界、API 对齐与直接共同 PR，不因功能竞争/互补自动建立人物边。

## Sources
- https://gitcode.com/Ascend/memcache/tree/develop
- https://gitcode.com/Ascend/memfabric_hybrid/tree/master
- https://gitcode.com/Ascend/MindIE-Motor/tree/master/examples/deployer/startup/roles
- https://github.com/vllm-project/vllm-ascend/issues/6410
- https://github.com/vllm-project/vllm-ascend/pull/11444
- https://github.com/vllm-project/vllm-ascend/pull/11585
- https://github.com/vllm-project/vllm-ascend/pull/12083
- https://github.com/sgl-project/sglang/pull/26043

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
