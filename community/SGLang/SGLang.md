---
type: project
name: SGLang
layer: llm-serving-engine
open_source: true
---
# SGLang

## 项目简介
SGLang 是面向大语言模型与多模态模型的高性能 serving framework，从 RadixAttention / prefix reuse 出发，逐步扩展到 continuous batching、speculative decoding、structured generation、distributed serving、MoE 与多模态执行。它与 vLLM 一起构成当前开源 LLM serving engine 的核心路线。

## GitHub
https://github.com/sgl-project/sglang

## 主要维护者 / 组织
由 sgl-project 社区维护，起源与 UC Berkeley Sky Computing Lab 高度相关，并形成 [[RadixArk]] 等产业化节点。核心人物包括 [[郑连民 Lianmin Zheng]]、[[盛颖 Ying Sheng]]、[[尹良升 Liangsheng Yin]]、[[谢志强 Zhiqiang Xie]]，以及 RadixArk/SGLang 社区的 Cheng Wan、Qiaolin Yu、Baizhou Zhang 等。

历史核心维护者中，[[community/SGLang/Yineng Zhang|Yineng Zhang]] 在 2024–2025 担任 SGLang core maintainer，并参与 DeepSeek-V3 day-0 support 与性能优化；2025-07 后进入 [[Together AI]] inference 团队，2026-03 又共同创建 [[TokenSpeed]]。这里按时间写为“历史 core maintainer”，不把其 2024–2025 身份误写成当前治理角色。

## 跨项目人才桥
- [[community/SGLang/Shenggui Li|Shenggui Li]]：当前 SGLang Core Dev、SpecForge Project Lead；此前处于 [[Colossal-AI]] / HPC-AI 早期核心系统网络，形成 distributed training → serving / speculative decoding 的人才迁移桥。
- [[community/SGLang/Yineng Zhang|Yineng Zhang]]：2024–2025 SGLang core maintainer；同时是 [[FlashInfer]]、[[Mooncake]] 作者网络成员，2025-07 加入 [[Together AI]]，2026-03 co-create [[TokenSpeed]]。这是 SGLang → production inference → 新 serving engine 的直接人才迁移边。

## 生态关系
[[vLLM]] · [[FlashInfer]] · [[Mooncake]] · [[DeepSeek-Infra]] · [[Dynamo]] · [[TokenSpeed]] · [[RadixArk]] · [[Colossal-AI]] · [[UC Berkeley]]。项目社区协作不能自动推断为公司同事。

## Sources
- https://github.com/sgl-project/sglang
- https://zhyncs.com/
