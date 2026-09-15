---
type: project
name: InfiniTensor
organization: InfiniTensor
linked_people:
  - "company/字节跳动/郑立言 Liyan Zheng"
  - "university/启元实验室/王豪杰 Haojie Wang"
layer: inference-engine
open_source: true
repository: https://github.com/InfiniTensor/InfiniTensor
areas: [inference-engine, tensor-compiler, hardware-backend, heterogeneous-compute]
people:
  - "university/启元实验室/王豪杰 Haojie Wang"
  - "company/字节跳动/郑立言 Liyan Zheng"
  - "company/清程极智/翟季冬 Jidong Zhai"
last_verified: "2026-09"
linked_companies: []
---
# InfiniTensor

## 项目简介
InfiniTensor 是面向 GPU 与多类 AI accelerators 的高性能推理引擎，强调模型部署和系统研究验证，并支持 NVIDIA GPU、寒武纪 MLU、昆仑芯 XPU、昇腾 NPU、Intel CPU 等硬件后端。

[[university/启元实验室/启元实验室|启元实验室]]是这一生态的重要机构支持方。InfiniTensor 官方 GitHub organization 明确写明由 Qiyuan Lab、Tsinghua University 等支持；2025 年启元实验室团队公开的“九源统一智能计算架构”进一步把统一算子/通信/运行时、领域编程语言、训练与推理框架组织成面向国产异构芯片的基础软件栈。

## 九源 / InfiniTensor 生态

- **InfiniCore**：统一算子、通信与运行时能力。
- **InfiniLM**：大模型推理框架。
- **InfiniTrain**：大模型训练框架。
- **NineToothed（九齿）**：基于 Triton 思路、提供更高层抽象的领域编程语言。
- **InfiniTensor**：当前官方仓库定位为面向 GPU / AI accelerators 的高性能推理引擎，兼具部署与系统研究验证价值。

[[university/启元实验室/王豪杰 Haojie Wang|王豪杰（Haojie Wang）]]是这里的关键桥梁人物。清华大学计算机系个人主页明确写明其“目前在主持开源项目 InfiniTensor 的开发工作”，同时 2025 年 CCF 资料将其 affiliation 写为启元实验室智能计算系统研究中心 / 清华大学计算机系。

项目技术谱系与 PACMAN 的 tensor-program optimization 工作紧密相关。官方仓库将 [[#EinNet|EinNet]] 列为重要研究基础，并计划将 EinNet 能力合入新的框架演进路线。

## EinNet
EinNet 是 OSDI 2023 的 derivation-based tensor program optimizer，由 [[company/字节跳动/郑立言 Liyan Zheng|郑立言（Liyan Zheng）]]、[[university/启元实验室/王豪杰 Haojie Wang|王豪杰（Haojie Wang）]]、[[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]] 等共同完成。它通过一般 tensor algebra expression 间的推导变换扩大优化搜索空间，并可自动生成变换所需的新算子。

## 图谱意义
InfiniTensor 现在同时连接三条线：
1. `清华 HPC / PACMAN → PET / EinNet → tensor program optimization`；
2. `启元实验室 → 九源统一智能计算架构 → 国产异构芯片软件栈`；
3. `InfiniTensor / InfiniCore / InfiniLM / InfiniTrain → 现代大模型训推基础设施`。

这使它成为连接清华系统研究、启元实验室、国产芯片软件生态与现代 inference engine 的高价值桥节点。

## Sources
- https://github.com/InfiniTensor
- https://github.com/InfiniTensor/InfiniTensor
- https://www.cs.tsinghua.edu.cn/info/1257/5770.htm
- https://cccf.hrbeu.edu.cn/cn/article/id/5aa85132-b8db-4152-99d8-7b3cab286df2
- https://www.infinitensor.com/
- https://www.usenix.org/conference/osdi23/presentation/zheng
- https://pacman.cs.tsinghua.edu.cn/~zjd/projects/einnet/
- https://wintersurf.github.io/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/字节跳动/郑立言 Liyan Zheng|郑立言（Liyan Zheng）]]：[[community/InfiniTensor/InfiniTensor|InfiniTensor]]：公开个人主页列为其核心项目；项目由 EinNet 等 tensor-program optimization 研究线演化而来，当前定位为面向 GPU / AI accelerators 的高性能推理引擎。
- [[university/启元实验室/王豪杰 Haojie Wang|王豪杰（Haojie Wang）]]：[[community/InfiniTensor/InfiniTensor|InfiniTensor]]：清华大学计算机系个人主页明确写明“目前在主持开源项目 InfiniTensor 的开发工作”。

<!-- END AUTO PROJECT PEOPLE -->
