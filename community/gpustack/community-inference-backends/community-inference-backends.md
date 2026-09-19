---
type: project
name: GPUStack Community Inference Backends
linked_people:
  - "company/GPUStack/Yinlin Li"
layer: ecosystem
status: active
repository: https://github.com/gpustack/community-inference-backends
areas: [inference-backend, backend-marketplace, model-serving, extensibility, heterogeneous-inference]
integrations: [GPUStack, llama.cpp, TensorRT-LLM, TokenSpeed]
companies: ["GPUStack"]
last_verified: "2026-09"
linked_companies:
  - "company/GPUStack/GPUStack"
---
# GPUStack Community Inference Backends

这是 [[community/gpustack/GPUStack/GPUStack|GPUStack]] 的社区 inference backend 扩展目录。其目的不是把所有引擎都塞进 GPUStack core，而是用标准化 spec 让 inference engine 开发者和高级用户独立接入 backend。

## 当前生态

公开目录已包含：

- LLM：[[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]]、[[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]]、[[community/lightseekorg/TokenSpeed/TokenSpeed|TokenSpeed]]
- Vision / OCR：MinerU、PaddleX-GenAI-Server
- Embedding / Reranker：Text-Embeddings-Inference、mis-tei
- Audio：Kokoro-FastAPI

项目明确区分 built-in backend 与 community backend：前者由 GPUStack core 维护，后者由社区 / upstream 负责，并可以随着真实使用与集成成熟度晋升为 built-in。

## 人物

- [[company/GPUStack/Yinlin Li|Yinlin Li / linyinli]]：2026-01 初始化该 community backend catalog，之后继续更新说明。

## Sources

- https://github.com/gpustack/community-inference-backends
- https://github.com/gpustack/community-inference-backends/commit/e314e1bb0152d806a3e35ef49e63729344fffe60
- https://github.com/gpustack/community-inference-backends/commit/6669659af1de493f92a3eefabd93112e9d1a544c

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/GPUStack/Yinlin Li|Yinlin Li]]：2026-01 初始化 [[community/gpustack/community-inference-backends/community-inference-backends|GPUStack Community Inference Backends]] catalog，形成 GPUStack core 与社区 inference engine 之间的扩展边界。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/GPUStack/GPUStack|GPUStack]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
