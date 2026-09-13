---
type: project
name: Triton Inference Server
company: NVIDIA
layer: production-inference-server
open_source: true
---
# Triton Inference Server

## 项目简介
Triton Inference Server 是 NVIDIA 的通用 production inference server，支持多种 framework/backend、动态 batching、并发模型执行、metrics 与 cloud/datacenter/edge 部署。它早于当前 LLM-specialized serving 热潮，是 NVIDIA production inference 栈的重要基础层。

## GitHub
https://github.com/triton-inference-server/server

## 主要维护者 / 组织
由 [[NVIDIA]] / Triton Inference Server 社区维护，具体 backend 通常分布在多个仓库与子项目中。

## 生态关系
[[TensorRT-LLM]] · [[Dynamo]] · [[NVIDIA]]。在本图谱中它代表较通用的模型服务器层，TensorRT-LLM 代表 LLM runtime，Dynamo 代表数据中心级 orchestration。
