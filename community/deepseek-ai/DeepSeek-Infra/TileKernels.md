---
type: project
name: TileKernels
companies: ["深度求索"]
company_relation: company-led
layer: gpu-kernels
open_source: true
repository: https://github.com/deepseek-ai/TileKernels
areas: [gpu-kernels, tilelang, moe, quantization, fp8, fp4, routing, engram]
people:
  - "community/deepseek-ai/DeepSeek-Infra/Chenhao Xu"
  - "community/deepseek-ai/DeepSeek-Infra/Xiangwen Wang"
  - "community/deepseek-ai/DeepSeek-Infra/Huanqi Cao"
  - "community/deepseek-ai/DeepSeek-Infra/Rui Tian"
  - "community/deepseek-ai/DeepSeek-Infra/Weilin Zhao"
  - "community/deepseek-ai/DeepSeek-Infra/Kuai Yu"
  - "community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao"
last_verified: "2026-09"
---
# TileKernels

TileKernels 是 DeepSeek 基于 [[community/tile-ai/TileLang/TileLang|TileLang]] 开源的高性能 LLM GPU kernel 集合。官方 README 明确写明部分 kernel 已用于 DeepSeek 内部 training / inference 场景。

## 覆盖能力
- MoE gating / routing：Top-k expert selection、token-to-expert mapping、fused expansion / reduction。
- Quantization：per-token / per-block / per-channel FP8、FP4、E5M6，以及 fused SwiGLU + quantization。
- Engram：gating、RMSNorm、forward / backward 与 weight-gradient reduction。
- mHC / modeling：Manifold HyperConnection kernels 与上层 autograd wrappers。

## TileLang 桥
`北京大学 / Tile-AI → TileLang → TileKernels → DeepSeek production training / inference`

该边来自项目 README 的明确依赖与致谢，不表示 TileLang 社区对 DeepSeek 项目拥有治理关系。

## 作者网络
官方 README 与 `pyproject.toml` 一致列出 Xiangwen Wang、Chenhao Xu、Huanqi Cao、Rui Tian、Weilin Zhao、Kuai Yu、Chenggang Zhao，并公开七人的 `@deepseek.com` 专业邮箱。

## Sources
- https://github.com/deepseek-ai/TileKernels
- https://github.com/deepseek-ai/TileKernels/blob/main/README.md
- https://github.com/deepseek-ai/TileKernels/blob/main/pyproject.toml
