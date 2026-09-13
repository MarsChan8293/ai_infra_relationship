---
type: model-project
company: DeepSeek
model: DeepSeek-V3
areas: [moe, mla, multi-token-prediction]
public_repo: true
---
# DeepSeek-V3

## 项目简介
DeepSeek-V3 是 DeepSeek 的 MoE foundation model，671B 总参数、37B 激活参数。技术路线结合 DeepSeekMoE、Multi-head Latent Attention（MLA）、auxiliary-loss-free load balancing 与 multi-token prediction。对 AI Infra 图谱尤其重要的是，它的模型结构直接催生了 attention、expert-parallel communication 与 GEMM 等系统优化项目。

## GitHub
https://github.com/deepseek-ai/DeepSeek-V3

## 主要维护者 / 组织
由 [[DeepSeek]] / deepseek-ai 公开维护；模型作者、系统作者与仓库贡献者需按各自公开证据区分，不把同属 DeepSeek 自动写成同一模块团队。

## 图谱中的核心人物
[[梁文锋 Liang Wenfeng]] · [[陈德里 Deli Chen]] · [[郭达雅 Daya Guo]] · [[邵智宏 Zhihong Shao]] · [[Jiashi Li]]

## 下沉到 Infra 的技术
- MLA → [[FlashMLA]]
- MoE all-to-all / expert parallel → [[DeepEP]]
- GEMM kernels → [[DeepGEMM]]
- Serving → [[vLLM]] / [[SGLang]] / [[TensorRT-LLM]]

## Sources
- https://github.com/deepseek-ai/DeepSeek-V3
- https://arxiv.org/abs/2412.19437
