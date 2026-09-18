---
type: project
name: InfiniTensor
organization: InfiniTensor
linked_people:
  - "community/InfiniTensor/baominghelly"
  - "community/InfiniTensor/GordonYang1"
  - "community/InfiniTensor/qinyiqun"
  - "community/InfiniTensor/wooway777"
  - "community/InfiniTensor/zhangyue207"
  - "company/字节跳动/郑立言 Liyan Zheng"
  - "university/启元实验室/王豪杰 Haojie Wang"
layer: inference-engine
open_source: true
repository: https://github.com/InfiniTensor/InfiniTensor
areas: [inference-engine, tensor-compiler, hardware-backend, heterogeneous-compute, cuda-graph, dynamic-shape]
people:
  - "university/启元实验室/王豪杰 Haojie Wang"
  - "company/字节跳动/郑立言 Liyan Zheng"
  - "company/清程极智/翟季冬 Jidong Zhai"
last_verified: "2026-09"
linked_companies: []
---
# InfiniTensor

## 项目定位
InfiniTensor 是 InfiniTensor / 九源生态中的**原始高性能推理引擎与系统研究验证仓库**，支持 NVIDIA GPU、寒武纪 MLU、昆仑芯 XPU、昇腾 NPU、Intel CPU 等异构硬件。

到 2026 年，它已经不再适合作为整个 GitHub organization 的唯一代表节点。生态主干已分化为：

- [[community/InfiniTensor/InfiniCore|InfiniCore]]：统一异构计算架构顶层集成，2026-09 重构为 InfiniRT / InfiniOps / InfiniCCL 的 component manifest。
- [[community/InfiniTensor/InfiniRT|InfiniRT]]：runtime 与 device abstraction。
- [[community/InfiniTensor/InfiniOps|InfiniOps]]：高性能算子与 backend-specific kernels。
- [[community/InfiniTensor/InfiniCCL|InfiniCCL]]：collective communication。
- [[community/InfiniTensor/InfiniLM|InfiniLM]]：现代大模型推理框架。
- [[community/InfiniTensor/InfiniTrain|InfiniTrain]]：多维并行大模型训练框架。
- [[community/InfiniTensor/NineToothed|NineToothed]]：Triton-based tensor-oriented DSL / compiler。
- [[community/InfiniTensor/ntops|ntops]]：NineToothed 的 LLM operators。

因此本页保留“原始推理引擎 + 学术技术谱系”语义，而把当前生产型训推 / runtime / operator / communication 能力拆到独立节点。

## 仍在活跃的原始引擎
2026-07 至 08，[[university/启元实验室/王豪杰 Haojie Wang|王豪杰（Haojie Wang / whjthu）]]仍直接推进该仓库，包括 dynamic CUDA Graph recapture/cache、dynamic-shape memory reuse、ONNX frontend correctness 等，因此不能把它简单标成 abandoned legacy。

## PET / EinNet 技术谱系
InfiniTensor 与 PACMAN 的 tensor-program optimization 研究有直接技术谱系。官方 README 将 PET / EinNet 作为重要研究基础。

EinNet 是 OSDI 2023 derivation-based tensor program optimizer，由 [[company/字节跳动/郑立言 Liyan Zheng|郑立言（Liyan Zheng）]]、[[university/启元实验室/王豪杰 Haojie Wang|王豪杰（Haojie Wang）]]、[[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]] 等共同完成。

## 图谱意义
当前更合理的可遍历结构是：

`清华 HPC / PACMAN → PET / EinNet → InfiniTensor`

再向工程化九源栈扩展：

`启元实验室 → InfiniCore → InfiniRT / InfiniOps / InfiniCCL → InfiniLM / InfiniTrain`

同时 compiler / kernel 线为：

`NineToothed ↔ Triton / TileLang backend → ntops / InfiniOps`

## Sources
- https://github.com/InfiniTensor
- https://github.com/InfiniTensor/InfiniTensor
- https://github.com/InfiniTensor/InfiniTensor/pull/314
- https://github.com/InfiniTensor/InfiniTensor/pull/311
- https://github.com/InfiniTensor/InfiniTensor/pull/309
- https://www.cs.tsinghua.edu.cn/info/1257/5770.htm
- https://cccf.hrbeu.edu.cn/cn/article/id/5aa85132-b8db-4152-99d8-7b3cab286df2
- https://www.usenix.org/conference/osdi23/presentation/zheng

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/InfiniTensor/baominghelly|baominghelly]]：https://github.com/InfiniTensor/InfiniOps/pull/977
- [[community/InfiniTensor/GordonYang1|GordonYang1]]：https://github.com/InfiniTensor/InfiniCCL/pull/60
- [[community/InfiniTensor/qinyiqun|qinyiqun]]：https://github.com/InfiniTensor/InfiniLM/pull/444
- [[community/InfiniTensor/wooway777|wooway777]]：https://github.com/InfiniTensor/InfiniLM/pull/574
- [[community/InfiniTensor/zhangyue207|zhangyue207]]：https://github.com/InfiniTensor/InfiniOps/pull/783
- [[company/字节跳动/郑立言 Liyan Zheng|郑立言（Liyan Zheng）]]：[[community/InfiniTensor/InfiniTensor|InfiniTensor]]：公开个人主页列为其核心项目；项目由 EinNet 等 tensor-program optimization 研究线演化而来，当前定位为面向 GPU / AI accelerators 的高性能推理引擎。
- [[university/启元实验室/王豪杰 Haojie Wang|王豪杰（Haojie Wang）]]：[[community/InfiniTensor/InfiniTensor|InfiniTensor]]：清华大学计算机系个人主页明确写明“目前在主持开源项目 InfiniTensor 的开发工作”；2026 仍直接贡献 dynamic CUDA Graph recapture/cache、dynamic-shape memory reuse 与 ONNX frontend。

<!-- END AUTO PROJECT PEOPLE -->
