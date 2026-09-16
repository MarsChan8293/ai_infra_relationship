---
type: community
name: LightSeek Foundation
aliases: ["LightSeek", "LightSeek Foundation"]
linked_people:
  - "community/sgl-project/SGLang/Yineng Zhang"
category: open-source-inference-foundation
areas: [llm-inference, agentic-inference, speculative-decoding, serving-systems]
governance: foundation-led
website: https://lightseek.org/
last_verified: "2026-09"
linked_companies: []
---
# LightSeek Foundation

## 社区定位
LightSeek Foundation 是围绕开放 LLM inference 基础设施与工程协作形成的 foundation/community 节点。2026 年持续发布并协作推进 [[TokenSpeed]]、[[community/lightseekorg/TorchSpec/TorchSpec|TorchSpec]]、SMG 等推理系统工作，重点覆盖 agentic inference、speculative decoding、kernel/runtime 与 serving frontend。

## AI Infra 主线
- [[TokenSpeed]]：面向 agentic workloads 的高性能 LLM inference engine。
- [[community/lightseekorg/TorchSpec/TorchSpec|TorchSpec]]：面向 speculative decoding 的分布式训练框架；其 inference ↔ training hidden-state 数据平面直接使用 [[community/kvcache-ai/Mooncake/Mooncake|Mooncake Store]]。
- SMG：将 CPU-bound serving frontend 与 GPU inference engine 解耦的 gateway/runtime 路线。

## 关系边界
Foundation 成员或治理关系不自动等同于雇佣关系。人物与项目的具体贡献、公司身份与合作关系仍以人物页和公开项目来源为准。

## Sources
- https://lightseek.org/
- https://lightseek.org/blog/
- https://github.com/lightseekorg/TorchSpec
- https://lightseek.org/blog/lightseek-tokenspeed.html

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]]：[[community/lightseekorg/LightSeek-Foundation/LightSeek-Foundation|LightSeek Foundation]]：governing board 成员；2026-03 共同创建 [[TokenSpeed]]。

<!-- END AUTO PROJECT PEOPLE -->
