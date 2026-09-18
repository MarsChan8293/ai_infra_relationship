---
type: project
name: InfiniOps
layer: gpu-kernels
open_source: true
repository: https://github.com/InfiniTensor/InfiniOps
areas: [operator-library, gpu-kernels, attention, kv-cache, quantization, heterogeneous-compute, ascend]
people:
  - "university/启元实验室/黄嘉成 Jiacheng Huang"
  - "community/InfiniTensor/zhangyue207"
  - "community/InfiniTensor/baominghelly"
  - "community/InfiniTensor/wooway777"
last_verified: "2026-09"
---
# InfiniOps

InfiniOps 是 [[InfiniCore]] 的高性能 operator 层，在统一算子接口下提供不同硬件 backend 的优化实现。它是九源生态里最贴近 kernel / attention / KV-cache 热路径的节点。

## 昇腾主线
2026 年公开 PR 显示：
- [[zhangyue207]]：连续贡献 Ascend `flash_attention`、`reshape_and_cache`、RMSNorm、RoPE、TopK/TopP sampler、custom kernel build 等。
- [[baominghelly]]：持续处理 Ascend paged FlashAttention layout、variable-length FlashAttention、KV-cache provider、Ascend CI / SoC detection 等。

因此图谱可形成：

`InfiniOps → Ascend attention / KV-cache kernels → InfiniLM`

这里记录直接代码贡献，不由贡献自动推断启元实验室任职或项目治理权限。

## 其他生态
InfiniOps 同时覆盖 NVIDIA、Cambricon、Kunlun、Moore Threads、MetaX、Hygon、Iluvatar、Ali PPU 等 heterogeneous backends，并支持 linked providers，例如 FlashInfer sampling provider。

## Sources
- https://github.com/InfiniTensor/InfiniOps
- https://github.com/InfiniTensor/InfiniOps/pull/783
- https://github.com/InfiniTensor/InfiniOps/pull/782
- https://github.com/InfiniTensor/InfiniOps/pull/977
- https://github.com/InfiniTensor/InfiniOps/pull/976
- https://github.com/InfiniTensor/InfiniOps/pull/930
