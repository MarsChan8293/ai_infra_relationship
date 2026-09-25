---
type: project
name: llama.cpp
linked_concepts:
  - "concept/quantization/FP4 Quantization"
  - "concept/quantization/Quantization"
  - "concept/quantization/Weight-Only Quantization"
status: active
docs: https://github.com/ggml-org/llama.cpp
linked_people:
  - "community/ggml-org/llama.cpp/Georgi Gerganov"
companies: ["Hugging Face"]
company_relation: joined-hugging-face-maintainer-team
layer: inference-engine
repository: https://github.com/ggml-org/llama.cpp
areas:
  - "llm-inference"
  - "vlm-inference"
  - "local-inference"
  - "edge-inference"
  - "quantization"
  - "gguf"
  - "cpu-gpu-hybrid"
  - "multi-backend"
  - "c-cpp"
  - "openai-compatible-server"
hardware:
  - "cpu"
  - "nvidia gpu"
  - "amd gpu"
  - "apple silicon"
  - "ascend npu"
  - "intel gpu"
  - "intel npu"
  - "moore threads gpu"
  - "snapdragon"
  - "risc-v"
  - "webgpu"
  - "nvidia"
  - "amd"
  - "apple"
governance: ggml-org maintainer network; project remains open-source and technically autonomous after GGML/llama.cpp team joined Hugging Face in 2026
people:
  - "community/ggml-org/llama.cpp/Georgi Gerganov"
integrations: []
last_verified: "2026-09"
linked_companies:
  - "company/Hugging Face/Hugging Face"
---
# llama.cpp

## 项目定位

llama.cpp 是 ggml-org 的 C/C++ LLM / VLM inference engine，目标是以最少依赖在本地与云端广泛硬件上实现高性能推理。它是当前 Local AI / edge inference 生态的重要基础项目之一。

官方 README 当前强调：
- plain C/C++ implementation；
- Apple Silicon 作为 first-class citizen，使用 ARM NEON / Accelerate / Metal；
- x86 AVX / AVX2 / AVX512 / AMX；
- RISC-V 支持；
- 1.5–8 bit integer quantization；
- CUDA / HIP / MUSA / Vulkan / SYCL / CANN / OpenVINO / WebGPU 等 backend；
- CPU + GPU hybrid inference，可运行大于总 VRAM 的模型；
- `llama serve` 提供 OpenAI-compatible API server。

## ggml / GGUF

llama.cpp 官方 README 明确说明项目构建在 [[community/ggml-org/ggml/ggml|ggml]] tensor library 之上。GGUF、量化 tensor 与 ggml backend 生态共同构成 llama.cpp 的本地推理基础。

这里把技术链明确建为：

`ggml tensor runtime → GGUF / quantization → llama.cpp inference engine`

## 多硬件后端

截至 2026-09，官方 README 列出的 backend 包括：
- CANN：Ascend NPU；
- CUDA：NVIDIA GPU；
- HIP：AMD GPU；
- Metal：Apple Silicon；
- MUSA：Moore Threads GPU；
- OpenCL：Adreno GPU；
- OpenVINO：Intel CPU / GPU / NPU（README 标注 In Progress）；
- SYCL：Intel GPU；
- Vulkan / WebGPU / RPC 等。

因此 llama.cpp 在本图谱中不仅是“桌面聊天工具”，而是一条覆盖 **CPU / GPU / NPU / edge device** 的异构 inference runtime 主线。

## 治理 / 维护网络

官方 README 直接提供 `maintainer PRs` 查询并说明：maintainers 可以向 llama.cpp 分支 push、merge PR 到 `master`。该查询当前包含 `ggerganov` 等维护者账号，因此人物治理边应优先依据该一手列表，而不是按 commit 数量推断。

当前先建立最核心节点：
- [[community/ggml-org/llama.cpp/Georgi Gerganov|Georgi Gerganov]]：llama.cpp Maintainer、ggml Founder。

其他维护者可在后续 BFS 中按 backend / module ownership 分层加入，例如 CUDA、Metal、Vulkan、SYCL、server、quantization / GGUF 等方向。

## Hugging Face 关系

2026-02-20，Hugging Face 官方宣布 **GGML and llama.cpp join Hugging Face**。Georgi Gerganov 与团队加入 Hugging Face，但官方同时说明：
- llama.cpp 仍保持开源；
- 社区治理与技术方向保持连续；
- Georgi 和团队继续全职维护 llama.cpp，并保持技术/社区领导自主权。

因此这里把 Hugging Face 记录为强组织关联，但不把项目来源改写成“HF 发起”。

## 与现有图谱项目的关系

- **FreeToken**：[[community/FlashML-org/FreeToken/FreeToken|FreeToken]] 官方 README 将 llama.cpp 列为设计/代码学习来源之一；两者都关注 consumer hardware 上的大模型推理，但 FreeToken 更偏 edge-native MoE CPU↔GPU expert execution，llama.cpp 更偏通用 local inference runtime + GGUF / quantization / broad backend。
- **vLLM / SGLang**：同属 inference engine，但 llama.cpp 的核心优势更偏本地、跨平台、低依赖与量化部署；不因功能相似自动建立 maintainer 人际关系。
- **KTransformers**：都涉及大于显存容量模型与 CPU/GPU 协同，但技术实现、治理社区独立。
- **Ascend**：llama.cpp 官方支持 CANN backend，可与现有 Ascend 图谱形成硬件 backend 邻接；只有在找到具体共同 PR / maintainer 证据后再建立人物强边。

## Sources
- https://github.com/ggml-org/llama.cpp
- https://github.com/ggml-org/llama.cpp/blob/master/README.md
- https://github.com/ggml-org/llama.cpp/blob/master/AUTHORS
- https://github.com/ggml-org/ggml
- https://ggml.ai/
- https://huggingface.co/blog/ggml-joins-hf

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/ggml-org/llama.cpp/Georgi Gerganov|Georgi Gerganov]]：llama.cpp 官方 README 当前维护的 `maintainer PRs` 查询明确包含 `ggerganov`，因此这里把其角色记录为 llama.cpp Maintainer，而不是仅凭历史提交数量推断治理身份。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Hugging Face/Hugging Face|Hugging Face]]：公司页与社区/项目页均有显式记录；关系：`joined-hugging-face-maintainer-team`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/quantization/FP4 Quantization|FP4 Quantization]]
- [[concept/quantization/Quantization|Quantization]]
- [[concept/quantization/Weight-Only Quantization|Weight-Only Quantization]]

<!-- END AUTO PROJECT CONCEPTS -->
