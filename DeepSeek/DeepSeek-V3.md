---
type: model-project
company: DeepSeek
model: DeepSeek-V3
areas: [moe, mla, multi-token-prediction]
---
# DeepSeek-V3

671B 总参数、37B 激活参数的 MoE 模型。技术报告强调 [[DeepSeekMoE]]、MLA、auxiliary-loss-free load balancing 与 multi-token prediction。

## 图谱中的核心人物
[[DeepSeek/梁文锋 Liang Wenfeng|梁文锋（Liang Wenfeng）]] · [[DeepSeek/陈德里 Deli Chen|陈德里（Deli Chen）]] · [[DeepSeek/郭达雅 Daya Guo|郭达雅（Daya Guo）]] · [[DeepSeek/邵智宏 Zhihong Shao|邵智宏（Zhihong Shao）]] · [[Jiashi Li]]

## 下沉到 Infra 的技术
- MLA → [[FlashMLA]]
- MoE all-to-all / expert parallel → [[DeepEP]]
- GEMM kernels → [[DeepGEMM]]
- Serving → [[vLLM]] / [[SGLang]] / [[TensorRT-LLM]]

## Source
https://arxiv.org/abs/2412.19437
