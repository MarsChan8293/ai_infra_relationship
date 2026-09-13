---
type: project
name: KTransformers
organization: KVCache.AI
layer: heterogeneous-inference
open_source: true
---
# KTransformers

## 项目简介
KTransformers 是面向 heterogeneous LLM inference / fine-tune 优化的框架，尤其关注 CPU+GPU、多 NUMA 节点和多设备协同，让超大模型可以利用 CPU 内存与计算能力补足 GPU 显存/算力约束。它代表一条不同于“全 GPU 数据中心 serving”的本地与异构推理路线。

## GitHub
https://github.com/kvcache-ai/ktransformers

## 主要维护者 / 组织
项目现由 KVCache.AI 组织维护，核心研发网络与清华大学 MADSys Lab 高度重叠。SOSP 2025 KTransformers 作者网络包括 [[Hongtao Chen]]、[[谢威宇 Weiyu Xie]]、[[Boxin Zhang]]、[[Jingqi Tang]]、[[Jiahao Wang]]、[[Jianwei Dong]]、[[Qingliang Ou]]、[[Ziwei Yuan]] 等。

## 生态关系
[[DeepSeek-Infra]] · [[FlashInfer]] · [[Mooncake]] · KVCache.AI · [[Tsinghua University]]。它与 Mooncake 共同体现清华 MADSys 的“存储/内存层参与模型推理”路线。
