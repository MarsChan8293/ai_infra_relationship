---
type: project
name: InfiniTensor
organization: InfiniTensor
layer: inference-engine
open_source: true
repository: https://github.com/InfiniTensor/InfiniTensor
areas: [inference-engine, tensor-compiler, hardware-backend, heterogeneous-compute]
people:
  - "company/字节跳动/郑立言 Liyan Zheng"
  - "company/清程极智/翟季冬 Jidong Zhai"
last_verified: "2026-09"
---
# InfiniTensor

## 项目简介
InfiniTensor 是面向 GPU 与多类 AI accelerators 的高性能推理引擎，强调模型部署和系统研究验证，并支持 NVIDIA GPU、寒武纪 MLU、昆仑芯 XPU、昇腾 NPU、Intel CPU 等硬件后端。

项目技术谱系与 PACMAN 的 tensor-program optimization 工作紧密相关。官方仓库将 [[#EinNet|EinNet]] 列为重要研究基础，并计划将 EinNet 能力合入新的框架演进路线。

## EinNet
EinNet 是 OSDI 2023 的 derivation-based tensor program optimizer，由 [[company/字节跳动/郑立言 Liyan Zheng|郑立言（Liyan Zheng）]]、[[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]] 等共同完成。它通过一般 tensor algebra expression 间的推导变换扩大优化搜索空间，并可自动生成变换所需的新算子。

## 图谱意义
InfiniTensor 把 PACMAN 的 compiler / tensor optimization 研究线继续延伸到现代 inference engine 与多硬件 backend 层，是连接 `翟季冬 → 郑立言 → ByteDance Seed` 之外另一条“学术系统技术 → 开源推理基础设施”的边。

## Sources
- https://github.com/InfiniTensor/InfiniTensor
- https://www.usenix.org/conference/osdi23/presentation/zheng
- https://pacman.cs.tsinghua.edu.cn/~zjd/projects/einnet/
- https://wintersurf.github.io/
