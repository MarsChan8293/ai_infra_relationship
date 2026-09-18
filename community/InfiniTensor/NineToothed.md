---
type: project
name: NineToothed
layer: compiler
open_source: true
repository: https://github.com/InfiniTensor/ninetoothed
areas: [compiler, kernel-dsl, triton, tilelang, gpu-kernels, tensor-oriented-metaprogramming, heterogeneous-compute]
people:
  - "university/启元实验室/王豪杰 Haojie Wang"
  - "university/启元实验室/黄嘉成 Jiacheng Huang"
last_verified: "2026-09"
---
# NineToothed

NineToothed（九齿）是 Triton-based DSL / compiler，通过 **tensor-oriented meta-programming（TOM）** 和 arrange-and-apply 抽象降低高性能 GPU kernel 开发门槛。

## 2026 演进
项目已经从“更高层 Triton DSL”推进到更完整的 compiler pipeline：
- SSA compiler pipeline；
- pass / backend registry；
- executable multi-backend support；
- Triton、CUDA、TileLang 等 backend 路线；
- architecture-aware caching / AOT / autotuning。

[[university/启元实验室/王豪杰 Haojie Wang|王豪杰（whjthu）]]与 [[university/启元实验室/黄嘉成 Jiacheng Huang|黄嘉成（voltjia）]]均有持续直接代码贡献。

## 与 TileLang / DeepSeek 的桥
NineToothed 的 TileLang backend 与你图中已有 [[community/tile-ai/TileLang/TileLang|TileLang]] 构成直接 compiler/backend 邻接；TileLang 又被 [[community/deepseek-ai/DeepSeek-Infra/TileKernels|DeepSeek TileKernels]] 采用。

因此可形成：

`启元实验室 / NineToothed ↔ TileLang → DeepSeek TileKernels`

这里只记录 backend integration / 技术生态邻接，不推断人员合作或共同治理。

## Sources
- https://github.com/InfiniTensor/ninetoothed
- https://github.com/InfiniTensor/ninetoothed/pull/164
- https://github.com/InfiniTensor/ninetoothed/pull/213
- https://github.com/InfiniTensor/ninetoothed/pull/218
