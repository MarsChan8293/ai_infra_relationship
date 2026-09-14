---
type: project
name: NIXL
governance: company-led
company: NVIDIA
companies: [NVIDIA]
company_relation: company-led
layer: inference-data-movement
open_source: true
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
