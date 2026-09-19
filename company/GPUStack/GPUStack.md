---
type: company
name: GPUStack
aliases: ["GPUStack.ai"]
areas: [ai-infrastructure, gpu-cluster, model-serving, heterogeneous-compute, distributed-inference, gpu-resource-management, maas, gpuaas]
projects:
  - GPUStack
  - GPUStack Runtime
  - GPUStack Runner
  - GPUStack Operator
  - GPUStack Community Inference Backends
  - GGUF Parser
people:
  - "company/GPUStack/秦小康"
  - "company/GPUStack/Yinlin Li"
founded: "2022"
headquarters: "Shenzhen, Guangdong, China"
last_verified: "2026-09"
---
# GPUStack

GPUStack.ai 是围绕开源 [[community/gpustack/GPUStack/GPUStack|GPUStack]] 构建 AI infrastructure 的公司 / 团队。公开公司资料显示其 2022 年成立于深圳，核心团队具有 Rancher Labs / cloud-native infrastructure 背景。

从 2026 年的公开代码结构看，GPUStack 已经不是单一 model-serving 工具，而是拆成了一组互相咬合的基础设施组件：

- [[community/gpustack/GPUStack/GPUStack|GPUStack]]：主 control plane，负责多集群 GPU 管理、模型部署、scheduler、gateway、可观测性与 API。
- [[community/gpustack/runtime/runtime|GPUStack Runtime]]：异构 GPU / NPU 探测与 workload runtime。
- [[community/gpustack/runner/runner|GPUStack Runner]]：vLLM / SGLang / MindIE 等推理引擎的多硬件镜像供应链。
- [[community/gpustack/gpustack-operator/gpustack-operator|GPUStack Operator]]：Kubernetes accelerator device-resource / scheduling control plane。
- [[community/gpustack/community-inference-backends/community-inference-backends|GPUStack Community Inference Backends]]：社区 backend marketplace / extension boundary。
- [[community/gpustack/gguf-parser-go/gguf-parser-go|GGUF Parser]]：GGUF memory / throughput / placement 评估工具。

## AI Infra 方向

- 多集群 GPU / NPU 管理与资源编排
- [[community/vllm-project/vLLM/vLLM|vLLM]] / [[community/sgl-project/SGLang/SGLang|SGLang]] / [[community/NVIDIA/TensorRT-LLM/TensorRT-LLM|TensorRT-LLM]] 等推理引擎统一管理
- MaaS / GPUaaS、OpenAI-compatible model serving、模型网关、高可用和可观测性
- [[community/LMCache/LMCache/LMCache|LMCache]] / shared KV cache、speculative decoding 等 production inference 能力
- NVIDIA、AMD、Ascend、Hygon、MetaX、Moore Threads、Iluvatar、Cambricon、T-Head 等异构 accelerator 适配

## 核心人物与工程节点

- [[company/GPUStack/秦小康|秦小康]]：CEO；AICC2026 Token 工厂论坛嘉宾。
- [[company/GPUStack/Yinlin Li|Yinlin Li / linyinli]]：公开资料列为 Solutions Architect；持续参与 Kubernetes、Ascend、community backend 与文档 / solution engineering。
- [[community/gpustack/GPUStack/thxCode|thxCode]]：跨 Runtime / Runner / Operator 的高密度核心工程贡献者；当前公开证据不足以仅凭贡献推断公司雇佣关系。
- [[community/gpustack/GPUStack/gitlawr|gitlawr]]：GPUStack Collaborator，近期集中在 shared KV cache 与 control-plane。
- [[community/gpustack/GPUStack/yxf0314|yxf0314]]：distributed serving / vLLM load balancing / Ascend / worker lifecycle 方向活跃贡献者。

## Rancher → GPUStack 线索

GPUStack.ai 的公开公司介绍明确写到核心团队成员包括 former Rancher Labs founders and lead employees。这个背景与 gitlawr 等人的历史 Rancher OSS 轨迹相互呼应，因此 Rancher / SUSE → GPUStack 是值得后续单独 BFS 的人才迁移路径。

这里暂不把“Rancher 开源贡献”自动升级成“Rancher 雇佣经历”，也不从共同公司 / 项目推断 coworker 或汇报线。

## Sources

- https://gpustack.ai/
- https://github.com/gpustack/gpustack
- https://www.linkedin.com/company/gpustack-ai/
- https://github.com/gpustack/runtime
- https://github.com/gpustack/runner
- https://github.com/gpustack/gpustack-operator
- https://github.com/gpustack/community-inference-backends
- https://www.aicconf.net/
