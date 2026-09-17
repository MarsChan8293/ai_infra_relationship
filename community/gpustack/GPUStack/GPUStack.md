---
type: project
name: GPUStack
organization: gpustack
linked_people:
  - "company/GPUStack/秦小康"
layer: inference-orchestration
open_source: true
linked_companies:
  - "company/GPUStack/GPUStack"
companies: ["GPUStack"]
---
# GPUStack

GPUStack 是面向生产环境的开源 GPU / accelerator 集群管理与 AI model serving 平台，位于底层硬件与 [[vLLM]]、[[SGLang]]、TensorRT-LLM 等推理引擎之间的编排层。

## AI Infra 位置
- 多集群 GPU / NPU 资源管理与调度
- vLLM、SGLang、TensorRT-LLM 等可插拔 inference backend
- 模型服务、负载均衡、高可用、监控与统一 API gateway
- 覆盖 NVIDIA、AMD、Ascend、海光、摩尔线程、沐曦、寒武纪、天数智芯、平头哥等异构加速器
- 2025–2026 持续加入 speculative decoding、KV cache 扩展、自动 engine selection / 参数优化等 production inference 能力

## 人物
- [[company/GPUStack/秦小康|秦小康]]：AICC2026 官方议程列为 GPUStack CEO，分享国产 GPU 在 Token 工厂 / AI Infra 中的规模化使用。

## Sources
- https://github.com/gpustack/gpustack
- https://gpustack.ai/
- https://gpustack.ai/blog/introducing-gpustack/
- https://www.aicconf.net/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/GPUStack/秦小康|秦小康]]：[[community/gpustack/GPUStack/GPUStack|GPUStack]]：公司 / 开源项目核心组织关系；项目本身是 GPU / NPU 集群管理与高性能模型 serving 编排层。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/GPUStack/GPUStack|GPUStack]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
