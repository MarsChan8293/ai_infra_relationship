---
type: project
name: FlashMLA
parent: DeepSeek-Infra
companies: [DeepSeek]
company_relation: company-led
layer: attention-kernels
open_source: true
---
# FlashMLA

## 项目简介
FlashMLA 是 DeepSeek 面向 Multi-head Latent Attention（MLA）与相关 sparse/efficient attention 路径的 GPU kernel 项目，把 DeepSeek 模型架构中的 attention 特性下沉为可复用、高性能实现。

## GitHub
https://github.com/deepseek-ai/FlashMLA

## 主要贡献公司
- [[company/DeepSeek/DeepSeek|DeepSeek]]：发起并通过 deepseek-ai 维护。

## 主要维护者 / 组织
由 [[DeepSeek]] / deepseek-ai 维护。原始公开作者节点包括 [[Jiashi Li]] 与 [[刘胜与 Shengyu Liu]]。

## 生态关系
[[FlashInfer]] · [[vLLM]] · [[SGLang]] · [[DeepGEMM]]。FlashMLA 是模型特定 attention kernel 与通用 serving kernel 生态之间的连接点。
