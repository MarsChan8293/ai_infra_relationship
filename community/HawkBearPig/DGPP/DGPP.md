---
type: project
name: DGPP
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/HawkBearPig/dgpp
areas:
  - dgx-spark
  - cpp-cuda-runtime
  - tensor-parallel
  - roce
  - nvfp4
  - prefix-cache
  - moe-inference
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# DGPP

## 项目简介
DGPP 是 GB10 专用 C++/CUDA 推理引擎，包含 CUDA Kernel、RDMA Collectives、Tokenizer、Jinja Template、Scheduler、Prefix Cache 和兼容 OpenAI 的 HTTP Serving。

## 硬件兼容性与证据层级
- **1/2/4 台 DGX Spark（GB10、SM121）**：README 明确提供不同模型的部署模板和测量结果，跨节点 TP 使用 RoCE。
- **RTX PRO 6000 / SM120**：目前未列为支持目标。

## 核心技术与部署意义
- 不同模型支持的 world size/quant 和 KV Pool 各异；不能将某模型 TP4 成功推导为所有模型均可 TP4。
- 重点研究原生 RDMA collective、TP 通信、prefix cache、KV 容量和故障行为。

## 关系与对比
[[community/sf-stav/veloGB10/veloGB10|veloGB10]]、[[community/kindlingai/gr8/gr8|gr8]] 和 [[community/antirez/ds4/ds4|ds4]] 是 GB10 比较对象。

## 来源
- https://github.com/HawkBearPig/dgpp
- https://github.com/HawkBearPig/dgpp/blob/HEAD/README.md
