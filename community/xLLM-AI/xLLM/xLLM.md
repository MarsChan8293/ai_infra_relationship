---
type: project
name: xLLM
status: active
repository: https://github.com/xLLM-AI/xllm
docs: https://docs.xllm-ai.com/
last_verified: "2026-09"
layer: inference-engine
areas:
  - "llm-inference"
  - "heterogeneous-inference"
  - "chinese-ai-accelerators"
  - "service-engine-decoupling"
  - "kv-cache"
  - "enterprise-serving"
hardware:
  - "ascend"
  - "cambricon"
  - "moore-threads"
  - "hygon-dcu"
  - "metax"
  - "iluvatar-corex"
integrations:
  - "Mooncake"
  - "xLLM-service"
---
# xLLM

## 项目简介
xLLM 是面向国产 / 中国 AI 加速器深度优化的高性能 LLM inference framework。项目采用 service-engine decoupled architecture：engine 负责模型计算，service 层负责调度与可用性，并强调低延迟、高吞吐和企业级部署。

截至 2026-09，官方公开支持 Ascend NPU、Cambricon MLU、Moore Threads MUSA、Hygon DCU、MetaX MACA 与 Iluvatar CoreX 等多类加速器。项目在 2026-07 宣布捐赠给开放原子开源基金会。

## GitHub
https://github.com/xLLM-AI/xllm

## 官方文档
https://docs.xllm-ai.com/

## 主要维护者 / 组织
由 xLLM 社区维护。项目 README 说明其来源于京东大规模线上业务实践，并在 2026 年进入开放原子开源基金会。这里记录项目和组织级事实，不因 repository contributor 列表自动建立人物雇佣关系。

## 核心能力
- 面向多种国产 AI accelerator 的统一高性能 LLM inference engine。
- service / engine 解耦，便于将执行引擎与集群调度服务分开演进。
- 支持多种主流大模型和国产模型的快速适配。
- 基于 [[Mooncake]] 构建 hybrid KV cache management，支持 global KV 管理、offload 与 prefetch。
- 与独立的 [[xLLM-service]] 共同形成 execution engine + cluster service 的两层架构。

## 生态关系
- [[Mooncake]]：xLLM 官方明确使用 Mooncake 构建 hybrid KV cache management。
- [[xLLM-service]]：独立的集群服务层，负责资源池、请求调度、PD/EPD 角色和容错。
- [[vLLM]] / [[SGLang]]：属于同一 inference-engine 大类，但 xLLM 的核心差异是对国产加速器的专门优化；这里属于技术定位比较，不标记为直接 integration。
- [[vLLM-Ascend]] / [[MindIE-LLM]]：在 Ascend 推理生态中属于可比较的不同执行路径。

## Sources
- https://github.com/xLLM-AI/xllm
- https://docs.xllm-ai.com/
