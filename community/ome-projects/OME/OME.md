---
type: "project"
name: "OME"
linked_people: []
layer: "distributed-serving"
status: "unknown"
maturity: "unknown"
code_availability: "public"
repository: "https://github.com/ome-projects/ome"
last_verified: "2026-10"
areas: ["inference-serving"]
integrations: []
linked_companies: []
---

# OME

## 项目简介

OME（Open Model Engine）是面向大模型部署的 Kubernetes serving 项目，提供模型、运行时和 InferenceService 等资源管理。

## 图谱关系

[[LLM Autotuner]]：LLM Autotuner 的 Kubernetes 安装指南明确依赖 OME 的模型加载、服务部署与 benchmark 资源。

## Sources

- https://github.com/ome-projects/ome
- https://github.com/novitalabs/autotuner/blob/main/docs/user-guide/kubernetes.md
