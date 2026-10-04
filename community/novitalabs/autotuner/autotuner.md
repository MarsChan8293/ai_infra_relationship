---
type: project
name: LLM Autotuner
linked_concepts:
  - "concept/compiler/Autotuning"
  - "concept/quantization/Quantization"
status: active
linked_people: []
repository: https://github.com/novitalabs/autotuner
docs: https://novitalabs.github.io/autotuner/
last_verified: "2026-10"
companies: ["Novita AI"]
layer: optimization
areas: [autotuning, inference-optimization, configuration-management, slo, benchmarking, quantization, agentic-optimization]
hardware: [nvidia]
integrations: [vLLM, SGLang, OME, genai-bench]
linked_companies:
  - "company/Novita AI/Novita AI"
---
# LLM Autotuner

Novita AI 的 LLM Autotuner 用于自动搜索 vLLM / SGLang 的推理参数组合，在 SLO 与硬件约束下优化吞吐和延迟。

## 架构定位

它与推理引擎不是竞争关系，而是位于 engine 配置与 benchmark loop 上方的 optimization/control layer：

模型 + 硬件 + engine/version + workload/SLO → 参数搜索 → 部署实验 → benchmark → scoring → 最优配置

这一定位与你仓库里 M-H-E（Model-Hardware-Engine）配置管理问题直接相关：同一个模型在不同 GPU、engine 与版本上需要重新搜索 serving 参数，而不能把一套启动参数当成静态模板长期复用。

## 能力

- vLLM / SGLang 参数自动调优。
- Grid search 与 Bayesian optimization。
- SLO-aware scoring。
- Docker、Local GPU、OME/Kubernetes 部署模式。
- Web UI、CLI 与 Agent mode。
- 量化参数、GPU tracking、parallel experiment execution。
- 通过 task / experiment 记录形成可复现的参数与结果集合。

## 图谱关系

[[community/vllm-project/vLLM/vLLM|vLLM]] / [[community/sgl-project/SGLang/SGLang|SGLang]] → LLM Autotuner

它适合作为“推理配置管理”与“自动 benchmark/tuning”之间的桥梁节点，而不是 kernel autotuner。

## Sources

- https://github.com/novitalabs/autotuner
- https://novitalabs.github.io/autotuner/

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/compiler/Autotuning|Autotuning]]
- [[concept/quantization/Quantization|Quantization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Novita AI/Novita AI|Novita AI]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
