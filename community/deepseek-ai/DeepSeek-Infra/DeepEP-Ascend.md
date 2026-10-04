---
type: project
name: DeepEP-Ascend
parent: DeepSeek-Infra
linked_concepts:
  - "concept/communication/collectives/All-to-All"
  - "concept/communication/collectives/Collective Communication"
  - "concept/inference/parallelism/Expert Parallelism"
  - "concept/kernel/programming/JIT Kernel Compilation"
status: active
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/Chenhao Xu"
  - "community/deepseek-ai/DeepSeek-Infra/Chenqi Zhao"
  - "community/deepseek-ai/DeepSeek-Infra/Kuai Yu"
  - "community/deepseek-ai/DeepSeek-Infra/Rui Tian"
  - "community/deepseek-ai/DeepSeek-Infra/Shangyan Zhou"
  - "community/deepseek-ai/DeepSeek-Infra/Yizhi Wang"
  - "community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou"
  - "community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao"
repository: https://github.com/deepseek-ai/DeepEP-Ascend
docs: https://github.com/deepseek-ai/DeepEP-Ascend
last_verified: "2026-10"
companies: ["深度求索"]
layer: communication
areas:
  - "expert-parallel"
  - "all-to-all"
  - "moe-dispatch"
  - "moe-combine"
  - "pipeline-communication"
  - "bucket-collectives"
  - "remote-memory"
hardware:
  - "ascend"
integrations:
  - "DeepEP"
  - "DeepJIT"
  - "CANN"
  - "clangd-ascend"
linked_companies:
  - "company/深度求索/深度求索"
code_availability: public
---
# DeepEP-Ascend

## 项目简介
DeepEP-Ascend 是 DeepSeek 面向 Huawei Ascend NPU 的高性能训练/推理通信库，是 [[DeepEP]] 的 Ascend 对应实现。公开 EPBuffer API 与 NVIDIA 版 DeepEP 对齐，核心对象是 MoE Expert Parallel 的 dispatch/combine all-to-all；同时暴露 PPBuffer、BucketBuffer 与 EngramBuffer 等通信/远端内存接口。

## 核心数据面
- Ascend C kernel 使用 HCCL/HCOMM、UBMEM 与 URMA。
- device kernel 通过 [[DeepJIT]] 在运行时编译。
- EP 支持 BF16 / FP8 dispatch、BF16 combine、cached handles、deterministic layouts、expert padding 与 deferred epilogues。
- PPBuffer 提供相邻 pipeline rank send/receive。
- BucketBuffer 面向普通 tensor 的 batched all-gather 等集合通信。
- EngramBuffer 面向 NPU-backed table / per-layer fetch，承接 Engram 风格的远端 memory access。

## 当前能力边界
官方 README 将 PP、Engram 和 Bucket 标记为 experimental / ongoing；Bucket reduce-scatter 与 all-reduce、expert load-balancing communication kernels 等仍在开发。Hybrid communication、CPU-backed Engram storage、graph capture 当前也被明确列为 unsupported。不能把“接口已暴露”写成“完整生产能力已完成”。

## 性能证据与部署限制
2026-09-30 README 在 Ascend 950DT、CANN 9.2.0、EP8–EP128 上公开 dispatch/combine 带宽。官方同时明确：这些结果使用 DeepSeek 获得的 PoC HDK 与额外手工配置，并非公开商用 baseline；Huawei 当时计划约在 2026-10-15 发布带相关配置的 Atlas 850E Q3 commercial HDK。因此当前性能数字应视为特定 PoC 软件/固件环境下的可复现实验，而不是普通公开环境的默认表现。

## 公开作者
官方 citation：[[赵成钢 Chenggang Zhao|Chenggang Zhao]]、[[Shangyan Zhou]]、[[周可行 Kexing Zhou|Kexing Zhou]]、[[Rui Tian]]、[[Chenqi Zhao]]、[[Chenhao Xu]]、[[Yizhi Wang]]、[[Kuai Yu]]。这里记录 citation 作者关系，不把作者身份自动提升为 maintainer 或当前雇佣证明。

## 生态关系
[[DeepEP]] · [[DeepJIT]] · [[DeepGEMM-Ascend]] · [[FlashMLA]] · [[community/Ascend/Ascend/Ascend|Ascend]] · [[community/Ascend/CANN/CANN|CANN]] · [[clangd-ascend]]

## Sources
- https://github.com/deepseek-ai/DeepEP-Ascend
- https://github.com/deepseek-ai/DeepEP
- https://github.com/deepseek-ai/DeepJIT

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/Chenhao Xu|Chenhao Xu]]：[[DeepEP-Ascend]]：2026 official citation author。
- [[community/deepseek-ai/DeepSeek-Infra/Chenqi Zhao|Chenqi Zhao]]：https://github.com/deepseek-ai/DeepEP-Ascend
- [[community/deepseek-ai/DeepSeek-Infra/Kuai Yu|Kuai Yu]]：[[DeepEP-Ascend]]：2026 official citation author。
- [[community/deepseek-ai/DeepSeek-Infra/Rui Tian|Rui Tian]]：[[DeepEP-Ascend]]：2026 official citation author。
- [[community/deepseek-ai/DeepSeek-Infra/Shangyan Zhou|Shangyan Zhou]]：[[DeepEP-Ascend]]：2026 official citation author。
- [[community/deepseek-ai/DeepSeek-Infra/Yizhi Wang|Yizhi Wang]]：https://github.com/deepseek-ai/DeepEP-Ascend
- [[community/deepseek-ai/DeepSeek-Infra/周可行 Kexing Zhou|周可行（Kexing Zhou）]]：[[DeepEP-Ascend]]：2026 official citation author。
- [[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢（Chenggang Zhao）]]：[[DeepEP-Ascend]]：2026 official citation first author。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/communication/collectives/All-to-All|All-to-All]]
- [[concept/communication/collectives/Collective Communication|Collective Communication]]
- [[concept/inference/parallelism/Expert Parallelism|Expert Parallelism]]
- [[concept/kernel/programming/JIT Kernel Compilation|JIT Kernel Compilation]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
