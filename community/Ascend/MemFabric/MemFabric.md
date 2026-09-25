---
type: project
name: MemFabric
linked_people:
  - "community/Ascend/MemCache/chenyz6"
  - "community/Ascend/MemCache/j00808874"
  - "community/Ascend/MemCache/shilinlee"
  - "community/Ascend/MemCache/yrewzjsx"
  - "community/Ascend/MemCache/Zixi Qu"
  - "community/Ascend/MemCache/彭海清 Haiqing Peng"
linked_concepts:
  - "concept/communication/data-movement/Data Movement"
  - "concept/memory/HBM"
  - "concept/memory/Host Memory"
  - "concept/memory/Memory Hierarchy"
  - "concept/memory/Memory Pooling"
  - "concept/communication/data-movement/Point-to-Point Transfer"
  - "concept/communication/data-movement/RDMA"
companies: ["华为"]
company_relation: company-led
layer: communication
hardware: [Ascend]
open_source: true
repository: https://gitcode.com/Ascend/memfabric_hybrid
areas: [memory-pooling, data-movement, disaggregated-serving, kv-cache, rdma, ascend]
last_verified: "2026-09"
linked_companies:
  - "company/华为/华为"
---
# MemFabric

## 项目简介
MemFabric 是 Ascend 生态的开源内存池化与高性能数据移动底座，将多节点 DRAM / HBM 等异构内存统一池化，并提供接近内存语义的跨机直接访问接口。

对 AI Infra 图谱而言，它更接近 **KV Cache / PD 分离背后的 data plane**，而不是 serving engine：上层系统可以把 KV、模型参数或训练/推理中间数据放在统一内存池中，再利用 Ascend 的 Device RoCE、SDMA、UB / URMA 等链路进行高速搬运。

## GitCode
https://gitcode.com/Ascend/memfabric_hybrid

## 推理优化主线
- **DRAM + HBM 混合池化**：把多机多层内存抽象为统一的全局内存空间。
- **跨机直接访问**：覆盖 H2D、D2H、D2RH、RH2D、D2D 等数据路径，减少传统中转拷贝。
- **Ascend A2 / A3 / A5 数据通路**：官方文档持续扩展 Device RoCE、SDMA、URMA、UBOE 等后端。
- **LLM 数据面**：官方列出的应用包括 KV cache、PD 传输、模型参数缓存、参数 reshard 等。

## 生态关系
- [[MemCache]]：**强依赖关系**。MemCache 以 MemFabric 作为多级内存和异构网络传输底座。
- [[vLLM-Ascend]]：官方资料明确给出 MemFabric + MemCache 作为 vLLM-Ascend backend 使能推理加速的路径。
- [[Mooncake]]：MemFabric 官方性能测试直接对接 Mooncake Transfer Engine，说明两者在 data movement 接口层存在真实工程邻接；后续应继续核验对应集成代码与贡献者。

## 第一轮人物探索候选
MemFabric 与 MemCache 的提交/合并记录中出现明显重叠的 handle，例如 `yrewzjsx`、`chenyz6`、`shilinlee_com` / `shilinlee`、`p3rry` 等。这种跨两个仓库的重复工程活动是很强的 BFS 线索，但仍需 governance、review ownership 或 release 责任证据后再升级为 maintainer / core reviewer 节点。

## BFS 下一跳
1. `MemFabric -> maintainers / reviewers`：寻找稳定治理角色与 release owner。
2. `MemFabric -> MemCache`：识别跨仓库核心工程师和接口 owner。
3. `MemFabric -> Mooncake Transfer Engine`：确认适配代码、性能测试负责人和接口边界。
4. `MemFabric -> vLLM-Ascend`：追 backend 集成 PR、KV connector 和数据搬运路径。

## Sources
- https://gitcode.com/Ascend/memfabric_hybrid/tree/master
- https://gitcode.com/Ascend/memfabric_hybrid/blob/develop/README.md
- https://gitcode.com/Ascend/memfabric_hybrid/tree/master/benchmark

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/Ascend/MemCache/chenyz6|chenyz6]]：长期出现在 MemCache 的 `Merged-by` 记录中，覆盖 MetaService、MemFabric 接口、KV Event、测试与构建等关键路径。
- [[community/Ascend/MemCache/j00808874|j00808874]]：HOST_SHM 改动同时触及 `hybm` / `smem`，使其成为 MemCache 与 MemFabric 共享内存 / 数据面路径上的高价值桥梁人物。
- [[community/Ascend/MemCache/shilinlee|shilinlee]]：https://gitcode.com/Ascend/memfabric_hybrid/tree/master/script
- [[community/Ascend/MemCache/yrewzjsx|yrewzjsx]]：在 MemFabric / memfabric_hybrid 的 develop、release 分支同样持续参与 merge，并与 [[chenyz6]] 形成跨仓库重复 review / merge 邻接。
- [[community/Ascend/MemCache/Zixi Qu|Zixi Qu]]：在 memfabric_hybrid 中参与 examples / naming 等改动，说明其活动跨越存储上层与内存池化底座。
- [[community/Ascend/MemCache/彭海清 Haiqing Peng|彭海清（Haiqing Peng）]]：负责或参与 MemFabric C API / 动态加载解耦、ABI 对齐、stream 字段适配等底层接口工作。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/communication/data-movement/Data Movement|Data Movement]]
- [[concept/memory/HBM|HBM]]
- [[concept/memory/Host Memory|Host Memory]]
- [[concept/memory/Memory Hierarchy|Memory Hierarchy]]
- [[concept/memory/Memory Pooling|Memory Pooling]]
- [[concept/communication/data-movement/Point-to-Point Transfer|Point-to-Point Transfer]]
- [[concept/communication/data-movement/RDMA|RDMA]]

<!-- END AUTO PROJECT CONCEPTS -->
