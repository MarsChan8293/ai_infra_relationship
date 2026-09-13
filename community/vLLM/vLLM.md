---
type: project
name: vLLM
layer: inference-engine
open_source: true
---
# vLLM

## 项目简介
vLLM 是面向大语言模型与多模态模型的高吞吐、低延迟推理与 serving engine。它从 PagedAttention / 高效 KV cache 管理起家，逐步扩展到 continuous batching、tensor / pipeline / expert parallel、prefix caching、speculative decoding、structured output、multimodal、量化与 OpenAI-compatible API 等生产能力。

在本图谱中，vLLM 是最重要的 inference engine 枢纽之一：上接 [[Hugging Face]] / 各类模型实现，下接 [[llm-d]]、[[LMCache]]、[[Mooncake]]、[[NIXL]] 等分布式 serving、KV cache 与数据传输生态，并与 [[SGLang]] 构成当前开源 LLM serving 的两条核心技术路线。

## GitHub
https://github.com/vllm-project/vllm

## 治理与主要组织
vLLM 采用公开 governance，Project Leads / Lead Maintainers / Committers 按 engine core、distributed、kernel、multimodality、API、KV connector 等领域分工。核心贡献者分布于 [[Inferact]]、[[Red Hat]]、[[Meta]]、[[Hugging Face]]、[[TensorMesh]] 等公司和研究机构，因此“同属 vLLM”不等同于“公司同事”。

## 核心人物
- [[Inferact/Woosuk Kwon|Woosuk Kwon]]：联合创建者、Project Lead；engine core / attention
- [[vLLM/李卓翰 Zhuohan Li|李卓翰（Zhuohan Li）]]：联合创建者、Project Lead；RL integration / numerics
- [[vLLM/Simon Mo|Simon Mo]]：Project Lead；API / serving / community
- [[vLLM/游凯超 Kaichao You|游凯超（Kaichao You）]]：Project Lead；distributed / compile
- [[vLLM/Robert Shaw|Robert Shaw]]：Project Lead；core / distributed / disaggregated serving
- [[vLLM/Nick Hill|Nick Hill]]：distributed / API / engine core
- [[vLLM/Roger Wang|Roger Wang]]：Project Lead；multimodality / benchmark
- [[vLLM/Lu Fang|Lu Fang]]：Project Lead；engine core / Llama
- [[vLLM/Ye Charlotte Qi|Ye “Charlotte” Qi]]：Project Lead；benchmark / Llama
- [[TensorMesh/程翊华 Yihua Cheng|程翊华（Yihua Cheng）]]：KV Connector / offloading / LMCache
- [[TensorMesh/杜昆泰 Kuntai Du|杜昆泰（Kuntai Du）]]：KV Connector / LMCache
- [[vLLM/Cyrus Leung|Cyrus Leung]]：multimodality / API server / model support
- [[vLLM/Harry Mellor|Harry Mellor]]：Hugging Face integration / model compatibility
- [[vLLM/Lucas Wilkinson|Lucas Wilkinson]]：attention / kernels / performance
- [[vLLM/Wentao Ye|Wentao Ye]]：kernels / performance

## 生态关系
- [[LMCache]]：通过 KV Connector / offloading 接口连接分层 KV cache。
- [[Mooncake]] / [[NIXL]]：用于 disaggregated serving、远程 KV/data movement 等场景。
- [[llm-d]]：把 vLLM engine 放到 Kubernetes distributed inference 的调度 / routing / data-plane 体系中。
- [[vLLM-Ascend]]：面向 Ascend NPU 的 vLLM hardware plugin / backend 生态。
- [[FlashInfer]]：高性能 attention / GEMM / MoE kernel 生态之一。

## Sources
- https://github.com/vllm-project/vllm
- https://docs.vllm.ai/en/latest/governance/process/
