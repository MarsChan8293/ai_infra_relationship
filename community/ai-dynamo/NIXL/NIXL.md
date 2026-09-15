---
type: project
name: NIXL
linked_people:
  - "community/ai-dynamo/NIXL/Adit Ranadive"
  - "community/ai-dynamo/NIXL/Efraim Eygin"
  - "community/ai-dynamo/NIXL/Ilia Yastrebov"
  - "community/ai-dynamo/NIXL/James Thomas"
  - "community/ai-dynamo/NIXL/Matvei Pashkovskii"
  - "community/ai-dynamo/NIXL/Mikhail Brinskiy"
  - "community/ai-dynamo/NIXL/Rongbing Zhou"
  - "community/ai-dynamo/NIXL/Ryan Hankins"
  - "community/ai-dynamo/NIXL/Tomer Davidor"
governance: company-led
companies: ["NVIDIA"]
company_relation: company-led
layer: inference-data-movement
open_source: true
linked_companies:
  - "company/NVIDIA/NVIDIA"
---
# NIXL

## 项目简介
NIXL（NVIDIA Inference Xfer Library）是推理数据传输与内存抽象层，为 GPU、CPU、storage 和网络后端提供统一的数据移动接口。它尤其适合 disaggregated serving、远程 KV transfer、storage offload 与 elastic expert parallel 等需要跨节点/跨介质搬运大块模型状态的场景。

## GitHub
https://github.com/ai-dynamo/nixl

## 主要贡献公司
- [[company/NVIDIA/NVIDIA|NVIDIA]]：项目发起与主要工程组织；在 ai-dynamo 组织下开放开发。

## 主要维护者 / 组织
由 NVIDIA 发起并在 ai-dynamo 组织下开放开发，连接 UCX、libfabric、GPU Direct 等底层传输生态。

## 生态关系
[[Dynamo]] · [[vLLM]] · [[LMCache]] · [[Mooncake]] · [[AMD]] · [[Amazon]] · [[HPE]] · [[Databricks]]。NIXL 位于 engine 与具体传输/storage backend 之间，是数据面而非调度器。

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/ai-dynamo/NIXL/Adit Ranadive|Adit Ranadive]]：Project source / contributor context: https://github.com/ai-dynamo/nixl
- [[community/ai-dynamo/NIXL/Efraim Eygin|Efraim Eygin]]：[[NIXL]]：core / tracing 方向活跃贡献者
- [[community/ai-dynamo/NIXL/Ilia Yastrebov|Ilia Yastrebov]]：[[NIXL]]：core API / Python bindings 活跃贡献者
- [[community/ai-dynamo/NIXL/James Thomas|James Thomas]]：[[NIXL]]：remote registration / core transfer lifecycle 贡献者
- [[community/ai-dynamo/NIXL/Matvei Pashkovskii|Matvei Pashkovskii]]：[[NIXL]]：AMD/ROCm/libfabric 支持贡献者
- [[community/ai-dynamo/NIXL/Mikhail Brinskiy|Mikhail Brinskiy]]：Project source / contributor context: https://github.com/ai-dynamo/nixl
- [[community/ai-dynamo/NIXL/Rongbing Zhou|Rongbing Zhou]]：[[NIXL]]：libfabric / AWS EFA / Neuron 方向贡献者
- [[community/ai-dynamo/NIXL/Ryan Hankins|Ryan Hankins]]：[[NIXL]]：libfabric / CXI 方向贡献者
- [[community/ai-dynamo/NIXL/Tomer Davidor|Tomer Davidor]]：[[NIXL]]：GPU Device API / UCX 方向贡献者

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/NVIDIA/NVIDIA|NVIDIA]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
