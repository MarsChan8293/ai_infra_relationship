---
type: project
name: GPUStack Runner
linked_people:
  - "community/gpustack/GPUStack/thxCode"
layer: runtime
status: active
repository: https://github.com/gpustack/runner
areas: [inference-runtime, container-images, backend-packaging, heterogeneous-inference, vllm, sglang, mindie]
hardware: [nvidia, amd, ascend, hygon, metax, mthreads, t-head]
integrations: [GPUStack, vLLM, SGLang, MindIE-LLM]
companies: ["GPUStack"]
last_verified: "2026-09"
linked_companies:
  - "company/GPUStack/GPUStack"
---
# GPUStack Runner

GPUStack Runner 是 [[community/gpustack/GPUStack/GPUStack|GPUStack]] 的推理运行镜像与 backend 打包层。它维护不同 accelerator software stack 与 inference engine 组合的可运行镜像，把“某个引擎支持某张卡”推进到可部署、可复现的 production artifact。

## 支持矩阵

当前公开矩阵覆盖：

- Ascend CANN：[[community/vllm-project/vLLM/vLLM|vLLM]]、[[community/sgl-project/SGLang/SGLang|SGLang]]、[[community/Ascend/MindIE-LLM/MindIE-LLM|MindIE-LLM]]
- NVIDIA CUDA：vLLM、SGLang
- AMD ROCm：vLLM、SGLang
- Hygon DTK、T-Head、MetaX、Moore Threads 等国产 / 异构栈

因此 Runner 是 GPUStack 与上游 inference engine、芯片软件栈之间非常具体的工程交汇点。

## 人物

- [[community/gpustack/GPUStack/thxCode|thxCode]]：2026-09 仍持续维护 vLLM 镜像与补丁，包括 MooncakeConnector Prometheus 修复、Hygon/DTK 路径及 dependency packaging。

## Sources

- https://github.com/gpustack/runner
- https://github.com/gpustack/runner/commit/ecab5861cdd94434521ee679d0697675b3ff7c28
- https://github.com/gpustack/runner/commit/766ef2f498339f95a0dda247b123f019e85d5e60

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/gpustack/GPUStack/thxCode|thxCode]]：https://github.com/gpustack/runner/commit/766ef2f498339f95a0dda247b123f019e85d5e60

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/GPUStack/GPUStack|GPUStack]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
