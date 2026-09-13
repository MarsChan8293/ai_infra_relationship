---
type: model-project
company: DeepSeek
model: DeepSeek-V3
areas: [moe, mla, multi-token-prediction]
---
# DeepSeek-V3

671B 总参数、37B 激活参数的 MoE 模型。技术报告强调 [[DeepSeekMoE]]、MLA、auxiliary-loss-free load balancing 与 multi-token prediction。

## 图谱中的核心人物
[[梁文锋]] · [[陈德里]] · [[郭达雅]] · [[邵智宏]] · [[Jiashi Li]]

## 下沉到 Infra 的技术
- MLA → [[FlashMLA]]
- MoE all-to-all / expert parallel → [[DeepEP]]
- GEMM kernels → [[DeepGEMM]]
- Serving → [[vLLM]] / [[SGLang]] / [[TensorRT-LLM]]

## Source
https://arxiv.org/abs/2412.19437
