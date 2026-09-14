---
type: project
name: DeepGEMM
parent: DeepSeek-Infra
companies: [深度求索]
company_relation: company-led
layer: gpu-kernels
open_source: true
---
# DeepGEMM

## 项目简介
DeepGEMM 是 DeepSeek 开源的高性能 GEMM/MoE kernel 项目，覆盖 FP8/FP4、grouped GEMM 与大规模 MoE 执行等路径。它展示了模型低精度与专家混合设计如何被落实到可复用 GPU kernel。

## GitHub
https://github.com/deepseek-ai/DeepGEMM

## 主要贡献公司
- [[company/深度求索/深度求索|深度求索]]：发起并通过 deepseek-ai 维护。

## 主要维护者 / 组织
由 [[深度求索]] / deepseek-ai 维护。公开作者网络包括 [[赵成钢 Chenggang Zhao]]、[[Zhean Xu]]、[[Liang Zhao]]、[[Jiashi Li]]、[[Chenhao Xu]]、[[Anyi Xu]]、[[刘胜与 Shengyu Liu]]、[[周可行 Kexing Zhou]]、[[Kuai Yu]]。

## 生态关系
[[FlashInfer]] · [[vLLM]] · [[SGLang]] · [[DeepEP]] · [[DeepJIT]]。DeepGEMM 位于 GPU kernel 层，与 serving engine 是上下游而非同层竞争。
