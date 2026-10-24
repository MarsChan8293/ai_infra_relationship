---
type: project
name: ds4
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/antirez/ds4
areas:
  - dedicated-inference-engine
  - llm-inference
  - cuda-kernel
  - ssd-streaming
  - dgx-spark
  - blackwell
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# ds4

## 项目简介
DwarfStar（ds4）是轻量 C/CUDA 专用推理引擎，面向 DeepSeek/GLM 等模型，减少通用 Serving 栈依赖并提供针对模型的执行与 SSD Streaming 路径。

## 硬件兼容性与证据层级
- **DGX Spark / GB10（SM121a）已明确支持**：官方 `make cuda-spark` 构建目标、`docs/DGX_SPARK.md` 和 GB10 实测/测试记录。
- **RTX PRO 6000（SM120）**：官方 Makefile 支持 `sm_120a` 构建，但本轮未发现 RTX PRO 6000 SKU 的独立验证，不标记为已实测。

## 核心技术与部署意义
- 使用原生 CUDA kernels，针对选择性模型执行。
- DeepSeek V4.1 Flash 可在单台 Spark 上通过本地 SSD Streaming 运行较大权重；双 Spark 提供网络 TP 实验与性能记录。
- 必须按模型、量化、单机/双机和上下文条件比较 TTFT/TPOT。

## 关系与对比
[[community/HawkBearPig/DGPP/DGPP|DGPP]]、[[community/sf-stav/veloGB10/veloGB10|veloGB10]] 是 GB10 专用路线对比；[[community/NVIDIA/Flare/Flare|Flare]] 是独立 NVIDIA 本地推理架构。

## 来源
- https://github.com/antirez/ds4
- https://github.com/antirez/ds4/blob/HEAD/README.md
