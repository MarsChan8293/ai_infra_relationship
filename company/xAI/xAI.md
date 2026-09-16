---
type: company
name: xAI
projects: [Grok-1]
linked_people: []
linked_projects: []
last_verified: "2026-09"
---
# xAI

## 公司简介
xAI 是 frontier-model lab 与 AI infrastructure operator，研发 Grok 系列模型，并建设大规模 GPU 训练/推理集群。它在 AI Infra 图谱中的意义主要是超大规模算力集群、模型训练系统与 production inference 的结合，而非当前仓库已有的某个单一开源 serving 社区。

## 公开项目
- [[company/xAI/Grok-1|Grok-1]]：xAI 官方公开的 314B MoE 模型与 JAX reference implementation。官方 README 明确说明参考 MoE 实现并非高效 production inference stack，因此本图谱把它作为模型/参考执行节点，而不是内部 serving 系统的替身。
- xAI 官方 GitHub 还公开 SDK、protobuf、Grok Build 等项目；这些项目分别偏 API 接入、接口定义与 coding-agent tooling，本轮不机械扩成推理优化节点。

## 图谱中的连接
与 [[NVIDIA]] GPU/CUDA 生态、大规模 networking/storage、模型 serving 系统存在直接基础设施关系。只有出现公开作者、maintainer 或任职证据时才建立到具体 vLLM/SGLang 等人物的强关系边。

## Sources
- https://github.com/xai-org
- https://github.com/xai-org/grok-1
- https://x.ai/
