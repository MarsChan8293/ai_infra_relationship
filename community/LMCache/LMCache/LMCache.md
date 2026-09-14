---
type: project
name: LMCache
companies: ["TensorMesh"]
company_relation: research-to-startup-core-network
layer: kv-cache-management
open_source: true
---
# LMCache

## 项目简介
LMCache 是 LLM KV cache 的分层存储、传输与复用系统，把 KV 从单 GPU 显存扩展到 CPU、远端存储和跨实例数据路径，并通过 connector 接入 serving engine。它重点解决长上下文、prefill/decode 解耦与跨请求复用下的 KV 数据生命周期问题。

## GitHub
https://github.com/LMCache/LMCache

## 主要贡献公司
- [[company/TensorMesh/TensorMesh|TensorMesh]]：LMCache 核心研究/工程人物进入产业化后的主要公司节点，持续连接 KV cache、disaggregated serving 与 vLLM KV Connector。LMCache 本身起源于学术/开源社区，因此这里是 **core network / commercialization**，不是公司所有权。
- IBM、NVIDIA、Red Hat、Microsoft、AMD、Tencent、ByteDance 等公司人员也曾被 LMCache 社区公开列为产业贡献网络；本图谱暂不把一次性/非核心贡献全部升级为主公司边。

## 主要维护者 / 组织
由 LMCache 社区维护，核心网络与 [[TensorMesh]]、University of Chicago systems 研究及 vLLM KV Connector 生态重叠。已记录人物包括 [[程翊华 Yihua Cheng]]、[[杜昆泰 Kuntai Du]]、[[Baolong Ma]]、[[Samm Shen]]。

## 生态关系
[[vLLM]] · [[TensorMesh]] · [[vLLM-Ascend]] · [[Mooncake]] · [[NIXL]]。LMCache 更偏 engine 外部 KV 管理与复用，Mooncake 更强调分布式 KVCache-centric serving/storage，两者有交叉但并非同一项目。
