---
type: project
name: "SEIS"
layer: optimization
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/smth-fun/self-evolving-inference-system
docs: https://github.com/nehzux/SEIS
areas:
  - self-evolving-inference-system
  - agentic-code-evolution
  - kernel-runtime-cooptimization
  - frozen-benchmark
  - experiment-memory
hardware:
  - nvidia
last_verified: "2026-11"
---

# SEIS

## 项目简介

SEIS（Self-Evolving Inference Systems）使用 Coding Agent 跨轮修改 mini-SGLang 推理引擎源代码，优化范围涉及 Kernel、量化、CUDA Graph、Runtime 和调度，而不只限于单个算子。

## 核心机制

每轮启动新的 Claude Code Session，继承前轮源码与 `learning.md` 经验记录；冻结 Benchmark，要求输出正确性验证，并根据吞吐决定保留修改。实际可运行脚手架在 smth-fun/self-evolving-inference-system；nehzux/SEIS 主要是论文展示仓。

## 昇腾适配与限制

目前绑定 NVIDIA/CUDA/Triton；迁移昇腾时应借鉴连续代码演化和冻结评测，重做 CANN 编译、NPU Profiler、vLLM-Ascend 构建/重启与数值门禁。公开脚手架 RTX PRO 6000 上 512→1,016 tok/s 与论文 H100 3.27x 为不同实验，不能外推到 910C。

## 技术关系

[[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]；与 [[community/InferMatrixLab/InferRSI/InferRSI|InferRSI]] 的验证能力是架构互补，不表示已集成。

## 维护组织与来源

上游组织：`smth-fun`（以公开仓库治理与贡献证据为准，未确认个人维护者身份）。

- https://github.com/smth-fun/self-evolving-inference-system
- https://github.com/nehzux/SEIS
- https://arxiv.org/abs/2610.04646
