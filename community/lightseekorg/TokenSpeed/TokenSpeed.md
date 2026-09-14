---
type: project
name: TokenSpeed
governance: foundation-led
organization: LightSeek Foundation
companies: ["NVIDIA","AMD","Together AI","阿里巴巴"]
company_relation: cross-company-co-creation
layer: agentic-llm-inference-engine
open_source: true
---
# TokenSpeed

## 项目简介
TokenSpeed 是 LightSeek Foundation 于 2026 年公开的 LLM inference engine，针对长上下文、多轮、持续生成的 agentic workloads 重新设计 serving runtime。核心方向包括 compiler-backed parallelism、C++ scheduler / Python execution plane、KV resource ownership / reuse、pluggable kernel layer 与异构 accelerator 支持。

开发于 2026-03 中旬启动，并在 2026-05-06 对外发布。到 2026-09，项目已继续推进 Kimi K3、Qwen3.8 等模型的 day-0 / production-oriented 优化，因此是当前推理优化人才图谱中需要单独建模的新节点，而不应只视为 SGLang 或 TensorRT-LLM 的旁支。

## GitHub
https://github.com/lightseekorg/tokenspeed

## 主要贡献公司
TokenSpeed 由 LightSeek Foundation 治理，不属于单一公司。公开 co-creation / collaboration 网络中，公司级强连接包括：
- [[company/NVIDIA/NVIDIA|NVIDIA]]：DevTech / Dynamo 等工程协作与 day-0 backend 支持。
- [[company/AMD/AMD|AMD]]：Triton / accelerator 侧共同开发网络。
- [[company/Together AI/Together AI|Together AI]]：inference 团队参与共同创建；[[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]] 同时是明确的人才桥。
- [[company/阿里巴巴/阿里巴巴|阿里巴巴]]：通过 Qwen Inference 团队参与共同创建/优化网络。

## 主要维护者 / 组织
由 LightSeek Foundation 社区维护。[[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]] 于 2026-03 共同创建 TokenSpeed；其个人主页同时列其为 LightSeek Foundation governing board 成员。项目官方发布说明其开发汇集了多家 AI Infra 团队与开源维护者。

## 技术关系
- [[vLLM]]：TokenSpeed 官方发布称 TokenSpeed MLA 已被 vLLM 采用，属于具体 kernel 技术回流关系，不等同于两个项目团队合并。
- [[Dynamo]]：NVIDIA Dynamo 在 2026-05-06 提供 TokenSpeed day-0 backend support。
- [[TensorRT-LLM]]：官方说明将其作为性能基线/重要技术参照，并明确感谢 TensorRT-LLM maintainers；属于技术影响关系。
- [[SGLang]]、[[FlashInfer]]、[[Mooncake]]：官方发布将这些项目列入 broader inference ecosystem / collaboration network；其中 Yineng Zhang 本人此前又直接参与 SGLang、FlashInfer、Mooncake，形成明确的人才桥。
- [[Together AI]]：官方发布把 Together AI 列为协作方；Yineng Zhang 同时领导 Together AI inference 团队。

## 2026 进展
- 2026-05-06：TokenSpeed 首次公开发布；NVIDIA Dynamo 同日提供 backend 支持。
- 2026-08-12：LightSeek 发布 Qwen3.8 day-0 inference 优化。
- 2026-08-26：LightSeek 官方记录 TokenSpeed 与 SMG 进入 PyTorch Ecosystem。
- 2026-09-08：发布 Kimi K3 on GB300 长上下文、多轮 agentic serving 优化。

## Sources
- https://github.com/lightseekorg/tokenspeed
- https://lightseek.org/blog/lightseek-tokenspeed.html
- https://lightseek.org/blog/
- https://docs.nvidia.com/dynamo/v1.1.1/digest/tokenspeed-day-0
- https://zhyncs.com/
