---
type: project
name: Chord
status: active
repository: https://github.com/novitalabs/chord
docs: https://github.com/novitalabs/chord/tree/main/docs
last_verified: "2026-10"
companies: ["Novita AI"]
layer: kernel
areas: [gemm, moe-kernels, w4a16, int4, quantization, jit, expert-parallelism, tensor-parallelism]
hardware: [nvidia]
integrations: [vLLM, Humming, CUTLASS]
---
# Chord

Chord 是 Novita Labs 开源的 W4A16 MoE CUDA operator：BF16 activation、INT4 weight、group-32 scale，针对 Kimi K2.5/K2.6/K2.7 的 serving shape 做专门优化。

## 架构定位

Chord 属于推理 engine 下方的 MoE GEMM kernel 层，不是完整 serving engine。当前包含两条主要 kernel family：

- **indexed**：从 [[community/inclusionAI/humming/humming|Humming]] 演化而来，直接消费 vLLM 的 sorted_ids / expert_ids / num_tokens_padded 路由布局。
- **grouped_contiguous / grouped_masked**：基于 [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] 的 SM90 W4A16 grouped GEMM 路径，分别面向 prefill 与 decode。

## 硬件与并行形态

公开配置覆盖：

- H200 / SM90：EP8 prefill、EP8 decode、TP8 mixed serving。
- H200 / SM90 grouped：EP8 / EP16 / EP32 prefill 与 decode。
- B200 / B300：EP8 decode。

这意味着 Chord 的调优单位不是“一个通用 INT4 kernel”，而是结合 routed tokens per expert、prefill/decode phase、EP/TP shard shape 来选择 schedule。

## vLLM 集成

Chord 的 indexed 路径刻意暴露 Humming-compatible import root，因此在兼容版本中可通过 vLLM 现有 Humming backend 选择；grouped operator 向 Humming backend 的完整框架集成仍在推进中。

关系链可概括为：

[[company/月之暗面/Kimi-K2|Kimi K2.x]] → W4A16 / MoE serving shape → **Chord** → [[community/vllm-project/vLLM/vLLM|vLLM]]

同时存在两条源码谱系：

[[community/inclusionAI/humming/humming|Humming]] → Chord indexed

[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] → Chord grouped SM90

## 性能意义

Novita AI 与 vLLM 团队 2026-09-15 的公开结果显示，Chord 在 H200 多个 EP8/TP8 场景相对匹配的 public Humming 路径有约 1.1x–1.35x 的 kernel-level 提升；在 B300 EP8 decode 对未调优 Humming default 的比较中最高达到约 2.15x。该结果应理解为特定 shape/kernel 的测量，而不是所有端到端 workload 的统一加速比例。

## Sources

- https://github.com/novitalabs/chord
- https://vllm.ai/blog/2026-09-15-novita-chord-w4a16-moe
- https://github.com/novitalabs/chord/blob/main/docs/optimizations.md
- https://github.com/novitalabs/chord/blob/main/chord_kernels/operator/SOURCE.md
