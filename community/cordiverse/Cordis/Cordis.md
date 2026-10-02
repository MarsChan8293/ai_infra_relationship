---
type: project
name: Cordis
status: active
linked_people: []
repository: https://github.com/cordiverse/cordis
docs: https://deepseek-harness.github.io/deepseek-harness/reference/cordis-primer
last_verified: "2026-10"
layer: runtime
areas:
  - "plugin-meta-framework"
  - "spatiotemporal-composability"
  - "dependency-injection"
  - "typed-events"
  - "reversible-effects"
integrations: []
linked_companies: []
---
# Cordis

## 项目简介
Cordis 是 cordiverse 维护的 “Meta-Framework of Spatiotemporal Composability”。它提供以 context、service、typed event、effect lifecycle 为中心的插件组合模型，是 [[community/deepseek-ai/DeepSeek-Harness/DeepSeek-Harness|DeepSeek Harness]] 的底层 framework。

## 与 DeepSeek Harness 的关系
DSH 官方 architecture 文档明确写明“Cordis is the framework under dsh”。在 DSH 中，插件把 services、events 与 reversible effects 挂到共享 context，卸载插件时注册行为可随生命周期回滚；因此 Cordis 决定了 DSH “everything-is-a-plugin” 的核心组合语义。

Cordis 自身不是 DeepSeek inference engine，也不因为被 DSH 使用就归属深度求索；本图谱将其作为独立上游 runtime/framework 节点。

## Sources
- https://github.com/cordiverse/cordis
- https://arxiv.org/abs/2608.25512
- https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md
