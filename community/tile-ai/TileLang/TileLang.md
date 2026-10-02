---
type: project
name: TileLang
linked_people:
  - "university/北京大学/Lei Wang"
  - "university/北京大学/Yining Shi"
  - "university/北京大学/吴童 Tong Wu"
  - "university/北京大学/程羽 Yu Cheng"
linked_concepts:
  - "concept/compiler/Autotuning"
  - "concept/compiler/Backend Code Generation"
  - "concept/compiler/Compiler Lowering"
  - "concept/kernel/gemm/GEMM"
  - "concept/kernel/programming/JIT Kernel Compilation"
  - "concept/compiler/Kernel Compiler Pipeline"
  - "concept/kernel/programming/Kernel DSL"
  - "concept/compiler/Layout Optimization"
layer: compiler
status: active
repository: https://github.com/tile-ai/tilelang
last_verified: "2026-10"
companies: []
company_relation: academic-research-led
areas:
  - "kernel-dsl"
  - "kernel-generation"
  - "multi-backend"
  - "ascend-950"
hardware:
  - "gpu"
  - "cpu"
  - "ascend"
integrations:
  - "TileLang-Ascend"
  - "TileLang-MLIR-Ascend"
  - "DeepGEMM-Ascend"
linked_companies: []
---
# TileLang

## 项目简介
TileLang（Tile Language）是面向 AI workload 高性能 kernel 开发的领域专用语言与编译系统。它以 Pythonic DSL 描述 tile 级数据流，在 TVM 编译基础设施之上提供更显式的 memory placement、data movement、layout、thread binding 与 software pipelining 控制，目标是在保持可编程性的同时接近手写 GPU kernel 的性能。

当前官方示例覆盖 GEMM、Dequant GEMM、FlashAttention、LinearAttention、MLA decoding 等典型训练/推理 kernel，并面向 NVIDIA、AMD、Huawei Ascend、Apple Metal 与 CPU 等多种后端。它在图谱中的定位不是 serving engine，而是连接模型算子与硬件执行层的 **AI compiler / kernel DSL**。

## 主要贡献公司
TileLang 的强起源边是北京大学学术团队与 Microsoft Research Asia 的研究/实习协作，但当前没有证据支持把项目归为某一家公司的主导开源项目，因此 `companies` 保持为空。作者后来进入 NVIDIA、ByteDance 等公司属于人才迁移，不反向改写项目归属。

## GitHub
- https://github.com/tile-ai/tilelang
- Organization: https://github.com/tile-ai

## 北大 / MSRA 起源
官方仓库明确记录：TileLang 初始版本主要由 [[Lei Wang]]、[[程羽 Yu Cheng]]、[[Yining Shi]] 开发，由北京大学 [[杨智 Zhi Yang]] 指导；部分工作发生在 Microsoft Research 实习期间，Lingxiao Ma、Yuqing Xia、Jilong Xue、Fan Yang 提供指导和支持。

ICLR 2026 论文《TileLang: Bridge Programmability and Performance in Modern Neural Kernels》作者包括 Lei Wang、Yu Cheng、Yining Shi、Zhiwen Mo、Zhengju Tang、Wenhao Xie、[[吴童 Tong Wu]]、[[马凌霄 Lingxiao Ma]]、Yuqing Xia、Jilong Xue、Fan Yang、[[杨智 Zhi Yang]]，并被接收为 Oral。

## 技术谱系
TileLang 并非从零出现。它可以放在北大/微软 AI compiler 长链中理解：

[[杨智 Zhi Yang]] → [[马凌霄 Lingxiao Ma]] / Rammer → Welder（[[Yining Shi]] 第一作者）→ TileLang → GPU/AI kernel DSL。

- **Rammer（OSDI 2020）**：在编译期统一考虑算子内/算子间并行调度。
- **Welder（OSDI 2023）**：用 tile-graph 从 memory-access 角度联合优化算子融合与数据复用。
- **TileLang**：进一步把 tile 级编程模型暴露给 kernel 开发者，直接服务于现代 attention、GEMM、quantized kernel 等场景。
- **PipeThreader（OSDI 2025）**：[[程羽 Yu Cheng]]、Lei Wang、Yining Shi 等延续 software-defined pipelining 路线，代码开源于 TileLang 生态。

## Ascend 路线（2026-09-30）

TileLang 当前存在三条需要区分的 Ascend 路径：

1. **TileLang 主仓内置 Ascend 950 backend**：2026-09-30 官方加入 `target="ascend"`，在共享 TileLang frontend 下提供 Ascend-specific lowering、自动 scheduling / synchronization、Cube + Vector code generation、SIMT/SIMD 编程、L1 / UB / L0 memory primitives，并以 CANN + `torch_npu` 作为运行环境。官方示例包括 GEMM、FP8 quantization、FlashAttention 与 DeepGEMM 风格 kernel。
2. **[[community/tile-ai/TileLang/TileLang-Ascend|TileLang-Ascend]]**：独立 ecosystem adapter，面向 Ascend A2/A3，包含 Ascend C & PTO 与 AscendNPU IR 技术路线，覆盖 GEMM、FlashAttention、Sparse FlashAttention、dispatch/combine、Lightning Indexer、TopK Selector 等。
3. **[[community/tile-ai/TileLang/TileLang-MLIR-Ascend|TileLang-MLIR-Ascend]]**：独立 MLIR-based Ascend adapter，以 AscendNPU IR 为主要 lowering / codegen 路径，面向 A2/A3，并提供 DeepSeek V4 mHC、GEMM、FlashAttention 等示例。

主仓 Ascend 950 backend 属于 TileLang release/source tree 内的正式 supported backend；A2/A3 的 `ascendc` / `pto` / `npuir` 则由独立 ecosystem adapters 承担，不能简单合并成一个“TileLang 支持 Ascend”标签。

### DeepSeek × TileLang × Ascend 950

TileLang 官方 Ascend 950 backend 文档明确写明，其初始版本主要由 `silentCoder-dev`、`Elevator14B`、`Denverjin`、`AutumnKite`、`SiriusNEO`、`timetraveler314`、`liguanglin`、`Achazwl`、`bucket-xv` 等 DeepSeek AI 开发者完成，并感谢 TileLang 社区和 Huawei 团队的协作。因此这里记录的是有官方证据的直接实现/协作关系，而不只是技术邻接。

这也解释了 [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM-Ascend|DeepGEMM-Ascend]] 中 TileLang 的角色：DeepSeek Ascend kernel 栈与 TileLang Ascend 950 backend 在底层 kernel / compiler 能力上直接交汇。

## 主要人物
- [[杨智 Zhi Yang]]：北京大学计算机学院，AI computing systems / distributed systems；TileLang 指导者，也是 Rammer、Welder 技术谱系的重要学术节点。
- [[Lei Wang]]：TileLang ICLR 2026 第一作者、官方仓库列出的初版主要开发者之一；GitHub `LeiWang1999`。
- [[程羽 Yu Cheng]]：北京大学杨智组研究生、TileLang core developer；同时在 MSRA Systems Research Group 实习，研究 deep learning compilation optimization；还参与 [[TileScale]]。
- [[Yining Shi]]：Welder OSDI 2023 第一作者、TileLang 初版主要开发者/ICLR 2026 作者；公开资料显示后进入 NVIDIA。
- [[吴童 Tong Wu]]：北大 EECS、杨智指导；Tile-AI 成员，贡献 TileLang、TileScale、TileOps，并有 ByteDance 实习经历。
- [[马凌霄 Lingxiao Ma]]：北大博士、杨智/代亚非指导；后任 MSRA researcher，Rammer/Roller/Welder 等系统核心作者，也是 TileLang 的产业研究指导桥梁。

## 生态关系
- [[北京大学]]：TileLang 的主要学术源头，也是 Rammer/Welder/TileLang 连续 compiler genealogy 的核心节点。
- **Microsoft Research Asia**：从 Rammer、Welder 到 TileLang 均存在紧密的共同研究与实习指导关系。
- **TVM**：TileLang 官方明确感谢 TVM 社区，当前编译基础设施建立在 TVM 之上。
- [[NVIDIA]]：[[Yining Shi]] 的后续去向，把北大 compiler 人才链连接到 GPU 平台侧。
- [[字节跳动]]：[[吴童 Tong Wu]] 的公开实习去向，是年轻 TileLang/LLM systems 人才向产业扩散的一个桥。
- [[community/deepseek-ai/DeepSeek-Infra/TileKernels|TileKernels]]：DeepSeek 2026 开源的 TileLang-based LLM GPU kernel 集合，形成 `TileLang → DeepSeek production kernels` 的直接技术采用边。
- [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM-Ascend|DeepGEMM-Ascend]]：Ascend 950 kernel 路径直接采用 TileLang；HC prenorm 等实现与 TileLang Ascend backend 形成直接交汇。
- [[community/tile-ai/TileLang/TileLang-Ascend|TileLang-Ascend]] / [[community/tile-ai/TileLang/TileLang-MLIR-Ascend|TileLang-MLIR-Ascend]]：A2/A3 ecosystem adapters，与主仓 Ascend 950 supported backend 分开维护。
- BitBLAS / AttentionEngine：TileLang 官方仓库列出的采用项目，可作为后续继续扩图的节点。

## 图谱洞察
北大 TileLang 系最值得保留的不是“某个 DSL 项目”，而是连续十余年的系统抽象迁移：从 Rammer 的 holistic scheduling，到 Welder 的 tile-level memory optimization，再到 TileLang 把 tile 变成开发者可直接编程的 AI kernel abstraction。它与 [[FlashInfer]]、DeepGEMM、Triton 一类项目处在相邻技术层，未来很可能通过 attention/GEMM/MLA kernel 与 [[vLLM]]、[[SGLang]] 等 serving runtime 形成更多直接连接。

## Sources
- https://github.com/tile-ai/tilelang
- https://proceedings.iclr.cc/paper_files/paper/2026/hash/76fb92288bf90360c527efb0d1c2aba6-Abstract-Conference.html
- https://ir.pku.edu.cn/handle/20.500.11897/751298
- https://www.usenix.org/conference/osdi25/presentation/cheng
- https://www.usenix.org/conference/osdi23/presentation/shi
- https://www.usenix.org/conference/osdi20/presentation/ma\n- https://github.com/deepseek-ai/TileKernels
- https://github.com/tile-ai/tilelang/blob/main/tilelang/ascend/README.md
- https://github.com/tile-ai/tilelang-ascend
- https://github.com/tile-ai/tilelang-mlir-ascend

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[university/北京大学/Lei Wang|Lei Wang]]：TileLang ICLR 2026 第一作者。
- [[university/北京大学/Yining Shi|Yining Shi]]：**Welder（OSDI 2023）**：第一作者。Welder 用 tile-graph 对深度学习执行的 memory access、operator fusion 与 data reuse 进行联合优化，是从 Rammer 走向 TileLang 的关键中间节点。
- [[university/北京大学/吴童 Tong Wu|Tong Wu]]：[[TileLang]]：活跃贡献者，ICLR 2026 Oral 作者。
- [[university/北京大学/程羽 Yu Cheng|Yu Cheng]]：[[TileLang]] core developer、初版主要开发者之一。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/compiler/Autotuning|Autotuning]]
- [[concept/compiler/Backend Code Generation|Backend Code Generation]]
- [[concept/compiler/Compiler Lowering|Compiler Lowering]]
- [[concept/kernel/gemm/GEMM|GEMM]]
- [[concept/kernel/programming/JIT Kernel Compilation|JIT Kernel Compilation]]
- [[concept/compiler/Kernel Compiler Pipeline|Kernel Compiler Pipeline]]
- [[concept/kernel/programming/Kernel DSL|Kernel DSL]]
- [[concept/compiler/Layout Optimization|Layout Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->
