---
type: project
name: xLLM-service
parent: xLLM
status: active
repository: https://github.com/xLLM-AI/xllm-service
last_verified: "2026-09"
layer: distributed-serving
areas:
  - "cluster-serving"
  - "request-scheduling"
  - "pd-disaggregation"
  - "epd-disaggregation"
  - "online-offline-scheduling"
  - "fault-tolerance"
integrations:
  - "xLLM"
---
# xLLM-service

## 项目简介
xLLM-service 是建立在 [[xLLM]] inference engine 之上的独立服务层框架，目标是为集群部署提供高效、容错、灵活的 LLM serving。它不是单机执行引擎，而是负责资源池管理、请求调度、角色分配和故障恢复，因此在图谱层级上更接近 distributed-serving/control-plane。

## GitHub
https://github.com/xLLM-AI/xllm-service

## 主要维护者 / 组织
由 xLLM 社区维护。官方 README 明确说明该项目基于 xLLM inference engine，并注明 xLLM 来源于 JD.com。人物关系仍需以明确的 governance / maintainer / affiliation 证据单独建模。

## 核心能力
- 在线 / 离线请求统一调度，支持在线请求抢占与离线 best-effort 执行。
- 根据实际请求负载动态调整 P/D 比例，并支持实例 P/D 角色切换。
- 面向多模态请求提供 E/P/D 三阶段 disaggregation。
- 监控计算实例状态，在实例故障后重新调度中断请求。
- 与 [[xLLM]] engine 解耦，使 serving control plane 与模型执行层可以独立演进。

## 生态关系
- [[xLLM]]：直接的 inference engine 依赖。
- [[llm-d]] / [[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] / [[MindIE-Motor]]：在 PD 分离、集群调度与容错方向存在明显技术邻接，但当前不把“同类定位”写成 direct integration。
- [[AIBrix]]：同样覆盖 distributed inference / scheduling 的相邻方案，但治理和技术栈不同。

## Sources
- https://github.com/xLLM-AI/xllm-service
