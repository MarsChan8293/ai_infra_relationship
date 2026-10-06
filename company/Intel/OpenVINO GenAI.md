---
type: project
name: OpenVINO GenAI
organization: OpenVINO Toolkit / Intel
linked_people: []
linked_concepts:
  - "concept/inference/decoding/Speculative Decoding"
companies: ["Intel"]
company_relation: company-led
layer: inference-engine
open_source: true
repository: https://github.com/openvinotoolkit/openvino.genai
areas: ["llm-inference", "genai", "continuous-batching", "kv-cache", "speculative-decoding", "sparse-attention", "cpu", "gpu", "npu", "genai-inference-library"]
last_verified: "2026-09"
linked_companies:
  - "company/Intel/Intel"
linked_projects:
  - "company/Intel/OpenVINO"
code_availability: public
---
# OpenVINO GenAI

OpenVINO GenAI 是构建在 OpenVINO Runtime 之上的生成式 AI inference library，为 LLM、VLM、Diffusion、Whisper 等 workload 提供 C++ / Python / Node.js pipeline。

## 推理优化
- LLM pipeline 支持 CPU / GPU / NPU。
- continuous batching，用于 LLM serving 场景。
- prefix caching / KV cache 管理。
- speculative decoding。
- KV-cache token eviction 与 sparse attention / prefill 优化。
- LoRA adapter 加载与多 adapter 组合。

这些能力使它比通用 OpenVINO runtime 更接近本图谱关注的 LLM serving / inference optimization 热路径。

## Intel 关系
Intel 官方 OpenVINO 支持资料把 **OpenVINO GenAI** 明确列为“运行和部署 generative AI models”的主要工具之一；代码由 `openvinotoolkit/openvino.genai` 持续发布，2026 年仍有 release。

## Sources
- https://github.com/openvinotoolkit/openvino.genai
- https://www.intel.com/content/www/us/en/support/articles/000056468/software/development-software.html
- https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Intel/Intel|Intel]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/decoding/Speculative Decoding|Speculative Decoding]]

<!-- END AUTO PROJECT CONCEPTS -->
