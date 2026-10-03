---
type: project
name: TritonAscendBench
layer: benchmark
status: active
repository: https://github.com/Gxj230958/TritonAscendBench
docs: https://github.com/Gxj230958/TritonAscendBench/tree/main/docs
areas:
  - "kernel-migration"
  - "triton-ascend"
  - "ascend-910b"
  - "correctness"
  - "performance"
  - "production-kernels"
  - "reward-hacking-defense"
hardware:
  - "nvidia"
  - "ascend"
last_verified: "2026-10"
---
# TritonAscendBench
## 项目定位

TritonAscendBench（TAB）不是从 PyTorch op 生成新 kernel 的 benchmark，而是专门测 **生产 GPU Triton kernel 能否迁移到 Ascend 910B / triton-ascend，同时保持 correctness 与 performance**。

## 任务设计

当前公开 101 个任务，源自 vLLM / SGLang inference path：

- L1：单算子、elementwise、reduce、quant、sampling；
- L2：fusion、Cube matmul、LoRA、MoE EP、Mamba step；
- L3：Flash Attention、Fused MoE、Mamba chunk pipeline。

runtime 默认不 import vLLM / SGLang；二者是 provenance / upstream reference，而不是运行时 integration。因此这里不把它们写入 Project v3 的 `integrations` 字段。

## Correctness 与性能边界

correctness 以 PyTorch oracle + tolerance contract 为当前 live scored axis；Ascend 910B performance path 需要真实 NPU，README 当前仍标记为 research preview，完整 verified runner 在 roadmap 中。官方还提供 process isolation、AST denylist、submission validation 等 reward-hacking defense。

## 图谱意义

TAB 把 [[community/triton-lang/Triton/Triton|Triton]]、vLLM/SGLang production kernel 与 Ascend migration 连接起来，适合作为 CANNBot-DSL、triton-ascend、kernel agent 体系的迁移 correctness gate，而不是把“能生成 kernel”与“能迁移生产 kernel”混为一谈。

## Sources

- https://github.com/Gxj230958/TritonAscendBench
