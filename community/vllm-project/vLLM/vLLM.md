---
type: project
name: vLLM
companies: [Inferact, Red Hat, Meta, Hugging Face, TensorMesh]
company_relation: cross-company-core-contributors
layer: inference-engine
open_source: true
---
# vLLM

## 项目简介
vLLM 是面向大语言模型与多模态模型的高吞吐、低延迟推理与 serving engine。它从 PagedAttention / 高效 KV cache 管理起家，逐步扩展到 continuous batching、tensor / pipeline / expert parallel、prefix caching、speculative decoding、structured output、多模态、量化与 OpenAI-compatible API 等生产能力。

在本图谱中，vLLM 是 inference engine 枢纽：上接模型生态，下接 [[llm-d]]、[[LMCache]]、[[Mooncake]]、[[NIXL]] 等 distributed serving、KV cache 与数据传输项目，并与 [[SGLang]] 构成两条核心开源 serving 路线。

## GitHub
https://github.com/vllm-project/vllm

## 主要贡献公司
vLLM 采用公开 governance，不归属于单一公司。这里的公司边表示 **核心维护者/长期工程贡献者的主要任职组织**，不是项目所有权：
- [[company/Inferact/Inferact|Inferact]]：vLLM 创建者与多位 core maintainer 的当前创业组织。
- [[company/Red Hat/Red Hat|Red Hat]]：拥有密集的 vLLM project lead / maintainer / kernel & distributed inference 工程网络。
- [[company/Meta/Meta|Meta]]：多位 vLLM contributor / maintainer 与 PyTorch compiler、RL serving 等方向形成直接工程连接。
- [[company/Hugging Face/Hugging Face|Hugging Face]]：模型集成与 Transformers compatibility 方向的重要产业贡献网络。
- [[company/TensorMesh/TensorMesh|TensorMesh]]：KV cache / disaggregated serving 与 vLLM KV Connector 方向的核心产业网络。

## 主要维护者 / 组织
vLLM 采用公开 governance。核心贡献者分布于 [[Inferact]]、[[Red Hat]]、[[Meta]]、[[Hugging Face]]、[[TensorMesh]] 等公司和研究机构，因此“同属 vLLM”不等于“公司同事”。

## 核心人物
[[Woosuk Kwon]] · [[李卓翰 Zhuohan Li]] · [[Simon Mo]] · [[游凯超 Kaichao You]] · [[Robert Shaw]] · [[Nick Hill]] · [[Roger Wang]] · [[Lu Fang]] · [[Ye Charlotte Qi]] · [[程翊华 Yihua Cheng]] · [[杜昆泰 Kuntai Du]] · [[Cyrus Leung]] · [[Harry Mellor]] · [[Lucas Wilkinson]] · [[Wentao Ye]] · [[Matthew Bonanni]]

## 生态关系
- [[LMCache]]：KV Connector / offloading 与分层 KV cache。
- [[Mooncake]] / [[NIXL]]：disaggregated serving、远程 KV/data movement。
- [[llm-d]]：Kubernetes distributed inference 的调度、routing 与 data plane。
- [[vLLM-Ascend]]：Ascend NPU hardware plugin/backend。
- [[FlashInfer]]：高性能 attention/GEMM/MoE kernel 生态。
- [[UC Berkeley]]：项目最早的研究与人才源头之一，并进一步连接 [[Inferact]]。

## Sources
- https://github.com/vllm-project/vllm
- https://docs.vllm.ai/en/latest/governance/process/
