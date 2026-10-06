---
type: project
name: "CANNBot-DSL"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
  - "concept/compiler/Kernel Compiler Pipeline"
  - "concept/kernel/programming/Kernel DSL"
layer: compiler
status: active
repository: https://gitcode.com/cann/cannbot-dsl
docs: https://cannbot-dsl.gitcode.com/api/
areas: ["kernel-dsl", "agentic-kernel-optimization", "ascend-npu", "ascend-950", "kernel-codegen", "aot-compilation", "native-operator-package", "attention", "sparse-attention", "matmul", "deepseek-v4.1"]
hardware: ["ascend"]
integrations: ["CANNBot"]
companies: ["华为"]
last_verified: "2026-10"
linked_companies:
  - "company/华为/华为"
code_availability: public
---

# CANNBot-DSL

CANNBot-DSL 是 CANNBot 仓群中的 **DSL / compiler 层**，目标是为 Ascend NPU 提供更适合 Agent 生成、修改、调试和验证复杂算子的编程范式。它不是单独的 autonomous Agent；上层 Agent / Harness 主要由 [[community/Ascend/CANNBot/CANNBot|CANNBot]] 与其 skills/plugin 负责，CANNBot-DSL 提供可被这些 Agent 操作的 kernel programming interface 与 compiler backend。

## 当前公开能力

截至 2026-09-30，公开版本为 CANNBot-DSL 0.7.0，可通过 `pip install cannbot-dsl` 安装；compiler backend 随 wheel 提供。官方配套口径面向 Ascend 950PR / 950DT（NPU ARCH 3510），并提供 Host、Kernel、AI CPU API、AOT 编译以及 Native 算子包发布能力。

仓库公开的 kernel / operator 样例已经覆盖：

- MatMul / BatchMatMul / GroupedMatMul 与 MXFP8 / MXFP4 量化矩阵乘；
- Flash Attention、FP8 Full-Quant Attention、Sparse Flash Attention；
- Qwen Sparse Attention、Flash MLA、量化块稀疏 Attention；
- Kimi Delta Attention；
- DeepSeek V4.1 的 indexer / attention prologue / sparse MLA / KV compression 等路径；
- RMSNorm、PointNet、VoxelConv 等。

README 明确说明这些样例由 CANNBot 基于 CANNBot-DSL 生成，因此它是 Ascend **Agentic Kernel Optimization** 中“Agent ↔ Kernel DSL ↔ Compiler ↔ NPU”链路的重要底层接口。

## DeepSeek V4.1

2026-09-30 更新明确增加 DeepSeek V4.1 相关算子，包括 `indexer_prologue_qw`、`indexer_prologue_k`、`attn_prologue`、`quant_lightning_indexer_dsl`、`quant_sparse_lightning_indexer_dsl` 与 `mixed_quant_sparse_flash_mla`。这使其不仅是通用 DSL，也直接进入 sparse attention / indexer / quantized KV 等新一代推理 kernel 路径。

## 与 CANNBot 的关系

[[community/Ascend/CANNBot/CANNBot|CANNBot]] 负责 Agent、plugin、workflow / harness 与端到端优化编排；CANNBot-DSL 提供 Agent 亲和的算子表达、编译与运行接口。两者组合后形成：

```text
Agent / Skill / Harness
        ↓
      CANNBot
        ↓
   CANNBot-DSL
        ↓
Compiler Backend / AOT / Native Package
        ↓
 Ascend 950 NPU Kernel
```

## Sources

- https://gitcode.com/cann/cannbot-dsl
- https://cannbot-dsl.gitcode.com/api/
- https://gitcode.com/cann/community/tree/master/CANN/sigs/cannbot

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]
- [[concept/compiler/Kernel Compiler Pipeline|Kernel Compiler Pipeline]]
- [[concept/kernel/programming/Kernel DSL|Kernel DSL]]

<!-- END AUTO PROJECT CONCEPTS -->
