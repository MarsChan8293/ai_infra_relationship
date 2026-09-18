---
type: project
name: InfiniCore
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
