---
type: project
name: DeepEP-Ascend
parent: DeepSeek-Infra
status: active
linked_people: []
repository: https://github.com/deepseek-ai/DeepEP-Ascend
docs: https://github.com/deepseek-ai/DeepEP-Ascend
last_verified: "2026-10"
companies: ["深度求索"]
company_relation: company-led
layer: communication
areas:
  - "expert-parallel"
  - "all-to-all"
  - "moe-dispatch"
  - "moe-combine"
  - "remote-memory"
hardware:
  - "ascend"
integrations:
  - "HCCL"
  - "HCOMM"
  - "UBMEM"
  - "URMA"
  - "DeepJIT"
linked_companies:
  - "company/深度求索/深度求索"
---
# DeepEP-Ascend

## 项目简介
DeepEP-Ascend 是 DeepSeek 面向 Huawei Ascend NPU 的高性能训练/推理通信库，是 [[DeepEP]] 的 Ascend 对应实现。公开 buffer API 与 NVIDIA 版 DeepEP 对齐，核心目标是 MoE Expert Parallel 的 dispatch/combine 与低延迟 all-to-all。

## GitHub
https://github.com/deepseek-ai/DeepEP-Ascend

## 关键技术
- Ascend C kernel 基于 HCCL/HCOMM、UBMEM、URMA，并通过 [[DeepJIT]] 运行时编译。
- 支持 FP8 dispatch 与 deferred epilogue。
- PP、CP/DP Bucket collective 与 Engram 远端内存访问属于公开路线中的进行中能力。
- 官方 2026-09-30 README 给出 Ascend 950DT / 128-rank EP 测试数据，并明确指出部分满带宽结果依赖当时的 PoC HDK 配置。

## 生态关系
[[DeepEP]] · [[DeepJIT]] · [[DeepGEMM-Ascend]] · [[FlashMLA]] · [[community/Ascend/Ascend/Ascend|Ascend]] · HCCL/HCOMM · UBMEM · URMA

## 公开贡献者
官方 citation 作者包括 [[赵成钢 Chenggang Zhao]]、[[Shangyan Zhou]]、[[周可行 Kexing Zhou]]、[[Rui Tian]]、Chenqi Zhao、[[Chenhao Xu]]、Yizhi Wang、[[Kuai Yu]]。

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
