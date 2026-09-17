---
type: project
name: OpenVINO
organization: OpenVINO Toolkit / Intel
linked_people: []
companies: ["Intel"]
company_relation: company-led
layer: inference-runtime-toolkit
open_source: true
repository: https://github.com/openvinotoolkit/openvino
areas: [inference-runtime, llm-inference, genai, cpu, gpu, npu, model-optimization]
last_verified: "2026-09"
linked_companies:
  - "company/Intel/Intel"
linked_projects:
  - "company/Intel/OpenVINO GenAI"
---
# OpenVINO

OpenVINO 是面向 AI inference 的开源 toolkit / runtime。Intel 官方把它作为跨 CPU、GPU、NPU 的 inference 部署与优化软件栈持续发布，2026.x 版本继续增加 Generative AI、LLM 与多模态能力。

## AI Infra 位置
- 模型转换、图优化与 runtime execution。
- CPU / GPU / NPU 多硬件部署。
- 面向 LLM / GenAI 的推理优化，并通过 [[company/Intel/OpenVINO GenAI|OpenVINO GenAI]] 提供更高层生成式 AI pipeline。
- Intel 官方 2026 年资料继续把 OpenVINO 作为 inference / GenAI 工具链发布，因此属于当前项目而非历史兼容关系。

## Intel 关系
Intel 官方开发者站点直接提供 OpenVINO Toolkit 的版本、下载、GenAI / LLM 能力和 Intel hardware 部署说明；开源代码由 `openvinotoolkit` GitHub organization 承载。这里记录的是官方产品 / 开源项目级关联，而不是因为第三方项目“支持 OpenVINO”反推 Intel ownership。

## Sources
- https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html
- https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/whats-new.html
- https://github.com/openvinotoolkit/openvino
