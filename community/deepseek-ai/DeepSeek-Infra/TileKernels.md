---
type: project
name: TileKernels
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/Chenhao Xu"
  - "community/deepseek-ai/DeepSeek-Infra/Huanqi Cao"
  - "community/deepseek-ai/DeepSeek-Infra/Kuai Yu"
  - "community/deepseek-ai/DeepSeek-Infra/Rui Tian"
  - "community/deepseek-ai/DeepSeek-Infra/Weilin Zhao"
  - "community/deepseek-ai/DeepSeek-Infra/Xiangwen Wang"
  - "community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao"
linked_concepts:
  - "concept/kernel/optimization/Kernel Fusion"
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
linked_companies:
  - "company/深度求索/深度求索"
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

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/Chenhao Xu|Chenhao Xu]]：Project source / contributor context: https://github.com/deepseek-ai
- https://github.com/deepseek-ai/TileKernels/blob/main/pyproject.toml
- [[community/deepseek-ai/DeepSeek-Infra/Huanqi Cao|Huanqi Cao]]：[[TileKernels]]：官方 citation 与 package author。
- [[community/deepseek-ai/DeepSeek-Infra/Kuai Yu|Kuai Yu]]：Project source / contributor context: https://github.com/deepseek-ai
- https://github.com/deepseek-ai/TileKernels/blob/main/pyproject.toml
- [[community/deepseek-ai/DeepSeek-Infra/Rui Tian|Rui Tian]]：[[TileKernels]]：官方 citation / package author；GitHub `tianr22` 提交 Engram kernel revision，package metadata 同时公开 `tianr22@deepseek.com`，因此 handle ↔ 姓名映射可核验。
- [[community/deepseek-ai/DeepSeek-Infra/Weilin Zhao|Weilin Zhao]]：https://github.com/deepseek-ai/TileKernels/blob/main/README.md
- [[community/deepseek-ai/DeepSeek-Infra/Xiangwen Wang|Xiangwen Wang]]：https://github.com/deepseek-ai/TileKernels/blob/main/README.md
- [[community/deepseek-ai/DeepSeek-Infra/赵成钢 Chenggang Zhao|赵成钢（Chenggang Zhao）]]：[[DeepGEMM]]：2025 公开项目原始作者
- [[TileKernels]]：2026 官方 citation / package author，继续连接 MoE routing、quantization 与 TileLang-based kernel 路线

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Kernel Fusion|Kernel Fusion]]

<!-- END AUTO PROJECT CONCEPTS -->
