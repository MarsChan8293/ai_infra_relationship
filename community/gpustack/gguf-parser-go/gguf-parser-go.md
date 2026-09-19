---
type: project
name: GGUF Parser
linked_people:
  - "community/gpustack/GPUStack/thxCode"
layer: benchmark
status: active
repository: https://github.com/gpustack/gguf-parser-go
areas: [gguf, memory-estimation, throughput-estimation, model-profiling, resource-planning, placement]
integrations: [GPUStack, llama.cpp]
companies: ["GPUStack"]
last_verified: "2026-09"
linked_companies:
  - "company/GPUStack/GPUStack"
---
# GGUF Parser

GGUF Parser 是 GPUStack 生态里的模型资源评估工具，用于读取 GGUF metadata，并在不完整下载模型的情况下估算内存占用、device placement 与最大 tokens per second。

它和 [[community/gpustack/GPUStack/GPUStack|GPUStack]] 的 scheduler / deployment evaluation 关系紧密：主仓库中存在直接的 GGUF parser 参数与 resource-fit 调度逻辑，且 2026-09 仍持续更新 pinned parser 版本。

## AI Infra 价值

- 远程 chunk reading，避免为评估先下载完整 GGUF。
- 按多 GPU / RPC / tensor split 估计 RAM、VRAM 与 offload placement。
- 可基于 device metric 做最大 TPS 的实验性估算。
- 对 [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] / GGUF 推理生态形成 resource planning 前置层。

## 人物

- [[community/gpustack/GPUStack/thxCode|thxCode]]：GPUStack 主仓库的 scheduler 与 parser 调用路径中存在其长期工程痕迹，并持续更新 parser 版本。

## Sources

- https://github.com/gpustack/gguf-parser-go
- https://github.com/gpustack/gpustack/commit/731b4fc9365f2acd47c004f7b0993a93c2ec14a6

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/gpustack/GPUStack/thxCode|thxCode]]：项目关联；人物页已明确记录该项目。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/GPUStack/GPUStack|GPUStack]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
