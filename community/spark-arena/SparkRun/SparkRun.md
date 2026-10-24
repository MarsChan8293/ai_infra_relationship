---
type: project
name: "SparkRun"
layer: distributed-serving
status: active
code_availability: public
repository: https://github.com/spark-arena/sparkrun
areas:
  - dgx-spark
  - deployment
  - multi-node-inference
  - recipe-management
  - cluster-management
  - model-serving
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# SparkRun

## 项目简介
SparkRun 是用于一台或多台 DGX Spark 的 LLM 推理工作负载启动与管理工具，不是计算 Token 的独立推理 Kernel/Runtime。

## 硬件兼容性与证据层级
- **DGX Spark / GB10：明确主要支持硬件**，提供 SSH mesh、ConnectX-7 检测、容器与模型 Recipe 管理、跨多 Spark TP 启动流程。
- **RTX PRO 6000（SM120）**：该项目目前主要面向 DGX Spark 的部署运维，未确认 6000 原生管理能力。

## 核心技术与部署意义
- 提供运行/日志/停止、模型显存估计和 Recipe Registry，统一执行其他真正的推理引擎。
- 不应拿 SparkRun 与 vLLM/SGLang 的 Token/s 当作同级引擎性能对比。
- README 提到匿名遥测，离线/敏感部署需显式关闭。

## 关系与对比
可编排 [[vLLM]]、[[SGLang]]、[[llama.cpp]] 等模型服务；与 [[community/HawkBearPig/DGPP/DGPP|DGPP]] 不构成引擎实现同义关系。

## 来源
- https://github.com/spark-arena/sparkrun
- https://github.com/spark-arena/sparkrun/blob/HEAD/README.md
