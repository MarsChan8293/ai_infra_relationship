---
type: project
name: gr8
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/kindlingai/gr8
areas:
  - dgx-spark
  - native-cuda
  - roce
  - tensor-parallel
  - glm
  - mla
  - speculative-decoding
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# gr8

## 项目简介
gr8 是面向 GLM 5.3 的从零实现 CUDA 推理引擎，在线 Serving 不依赖 vLLM、PyTorch 或 NCCL，节点经 RoCE v2 verbs 传输并暴露 OpenAI 兼容服务。

## 硬件兼容性与证据层级
- **3/4/6 台 DGX Spark 或 GB10 OEM（SM121a）**：作者给出 TP3/TP4/TP6、性能和构建要求，当前为 Beta。
- **RTX PRO 6000 / SM120**：不属于当前服务部署矩阵。

## 核心技术与部署意义
- 聚焦 GLM 5.3 MoE、MLA、稀疏 indexer 和 MTP/DFlash2。
- 用原生 RoCE、精简 CUDA 运行时验证多机 TP 与模型专用化，适合与 DGPP/veloGB10 同条件比较。

## 关系与对比
[[community/HawkBearPig/DGPP/DGPP|DGPP]]、[[community/sf-stav/veloGB10/veloGB10|veloGB10]]。

## 来源
- https://github.com/kindlingai/gr8
- https://github.com/kindlingai/gr8/blob/HEAD/README.md
