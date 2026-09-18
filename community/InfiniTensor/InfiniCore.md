---
type: project
name: InfiniCore
linked_people:
  - "community/InfiniTensor/GordonYang1"
  - "community/InfiniTensor/qinyiqun"
  - "community/InfiniTensor/wooway777"
  - "community/InfiniTensor/zhangyue207"
  - "university/启元实验室/潘泽众 Zezhong Pan"
  - "university/启元实验室/黄嘉成 Jiacheng Huang"
layer: heterogeneous-compute
open_source: true
repository: https://github.com/InfiniTensor/InfiniCore
areas: [heterogeneous-compute, runtime, operators, collective-communication, hardware-backend, llm-inference]
people:
  - "university/启元实验室/黄嘉成 Jiacheng Huang"
  - "university/启元实验室/潘泽众 Zezhong Pan"
  - "community/InfiniTensor/zhangyue207"
  - "community/InfiniTensor/qinyiqun"
  - "community/InfiniTensor/wooway777"
  - "community/InfiniTensor/GordonYang1"
last_verified: "2026-09"
linked_companies: []
---
# InfiniCore

InfiniCore 是九源生态的统一异构计算架构。2026-09-11 官方仓库完成一次关键重构：InfiniCore 收敛为顶层 integration repository / component manifest，底层能力明确拆成 [[InfiniRT]]、[[InfiniOps]]、[[InfiniCCL]]。

## 架构
- [[InfiniRT]]：device / memory / runtime services。
- [[InfiniOps]]：统一 operator API 与硬件特化实现。
- [[InfiniCCL]]：distributed collective communication。
- 上层由 [[InfiniLM]]、[[InfiniTrain]] 等应用/框架消费。

该结构把“统一接口”与 NVIDIA、Ascend、Cambricon、Kunlun、Moore Threads、MetaX、Hygon、Iluvatar 等平台的原生 SDK / optimized implementation 分离。

## 人物与工程边
- [[university/启元实验室/黄嘉成 Jiacheng Huang|黄嘉成（Jiacheng Huang / voltjia）]]：2026-09 主导将 InfiniCore 收敛成三组件 architecture 的公开 PR/commit 作者之一。
- [[university/启元实验室/潘泽众 Zezhong Pan|潘泽众（Zezhong Pan / PanZezhong1725）]]：持续贡献 MoE、paged cache、Kimi / Qwen 等 inference operators 与 InfiniCCL wrapper。
- [[zhangyue207]]、[[qinyiqun]]、[[wooway777]]、[[GordonYang1]]：分别覆盖国产后端、MoE/quant、multi-backend inference 与 CCL/operator integration。

## Sources
- https://github.com/InfiniTensor/InfiniCore
- https://github.com/InfiniTensor/InfiniCore/pull/1406
- https://github.com/InfiniTensor/InfiniCore/commit/26f7382d121380bb146e81dada08a8835bce5ad2

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/InfiniTensor/GordonYang1|GordonYang1]]：[[InfiniCore]]：NVIDIA operator integration / correctness 修复。
- [[community/InfiniTensor/qinyiqun|qinyiqun]]：[[InfiniCore]]：MoE runtime / operators、quantized GEMM、Marlin repack、async tensor copy。
- [[community/InfiniTensor/wooway777|wooway777]]：[[InfiniCore]]：Moore Threads / MetaX graph、Iluvatar / Ali Qwen operators 等多后端工程。
- [[community/InfiniTensor/zhangyue207|zhangyue207]]：[[InfiniCore]] / [[InfiniLM]]：同时参与 Kunlun / Hygon 等推理适配与 model execution 修复。
- [[university/启元实验室/潘泽众 Zezhong Pan|潘泽众（Zezhong Pan）]]：GitHub `PanZezhong1725` 在 [[community/InfiniTensor/InfiniCore|InfiniCore]] 持续推进 MoE / paged cache / Kimi Delta Attention / InfiniCCL wrapper 等，在 [[community/InfiniTensor/InfiniLM|InfiniLM]] 推进 Kimi-K3、Qwen3-next 与 cross-node PP + intra-n...
- [[university/启元实验室/黄嘉成 Jiacheng Huang|黄嘉成（Jiacheng Huang）]]：GitHub `voltjia` 的直接工程轨迹横跨 [[community/InfiniTensor/NineToothed|NineToothed]]、[[community/InfiniTensor/InfiniCore|InfiniCore]]、[[community/InfiniTensor/InfiniOps|InfiniOps]]、[[community/InfiniTensor/InfiniRT|InfiniRT]]、[[community/Infini...

<!-- END AUTO PROJECT PEOPLE -->
