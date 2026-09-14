---
type: project
name: llm-d
governance: cross-company
companies: ["Red Hat","Google","IBM","CoreWeave","NVIDIA"]
company_relation: founding-contributors
layer: kubernetes-distributed-inference
open_source: true
---
# llm-d

## 项目简介
llm-d 是面向 Kubernetes 的分布式 LLM inference serving 项目，目标是在 engine 之上补齐 intelligent routing、disaggregation、KV-aware scheduling、autoscaling、observability 与云原生运维能力。它是连接 vLLM 等 engine 与 Kubernetes production platform 的重要社区。

截至 2026-09，llm-d 已形成按 SIG 划分的清晰技术治理结构。SIG Lead 对各自技术域负责方向、协调与决策，因此比“同属 llm-d 社区”更适合作为人物之间的强关系证据。

## GitHub
https://github.com/llm-d/llm-d

## 主要贡献公司
llm-d 从一开始就是跨公司项目，不应归到单一厂商。官方 founding / launch 网络中最强的公司边为：
- [[company/Red Hat/Red Hat|Red Hat]]：项目 founding / leadership、PD/KV disaggregation 与社区生态。
- [[company/Google/Google|Google]]：项目 founding / leadership、Router、Benchmarking 与 Kubernetes serving 生态。
- [[company/IBM/IBM|IBM]]：项目 founding / leadership、Router、KV-disaggregation 与 research/storage systems。
- [[company/CoreWeave/CoreWeave|CoreWeave]]：founding contributor / production GPU cloud 侧参与。
- [[company/NVIDIA/NVIDIA|NVIDIA]]：founding contributor / GPU platform 与 distributed inference 生态。

AMD、Cisco、Hugging Face、Intel、Lambda、Mistral 等 launch / ecosystem partner 不自动提升为 founding contributor 级别。

## 项目治理骨架
- [[Carlos Costa]]（[[IBM]]）、[[Clayton Coleman]]（[[Google]]）、[[Robert Shaw]]（[[Red Hat]]）：**项目创始/核心维护网络**。三人从 2025 社区发布起持续共同署名 0.2、0.3、0.4、0.5 等主要 release 内容；官方 founding proposal / governance 将其放在跨公司技术领导网络中。Clayton 的页面保留其 leave/inactive 状态说明，不把历史 leadership 自动写成持续活跃维护。
- [[Abdullah Gharaibeh]]（[[Google]]）：项目治理网络成员，同时为 Router SIG Lead；2026 仍持续参与 token-aware routing / predicted-latency scheduling 等核心路由工作。
- [[张家驹 Jiaju Zhang]]（[[Red Hat]]）：主要参与社区孵化、推广、技术布道与中国/APAC 生态连接，不与 core maintainer 角色混写。

## SIG 人才关系
- **Router**：[[Nili Guy]]（IBM Research）↔ [[Abdullah Gharaibeh]]（Google）↔ [[Vita Bortnikov]]（IBM），共同负责 KV-cache-aware routing、load balancing、Gateway API / Inference Gateway 等方向。
- **Benchmarking**：[[Marcio A L Silva]] ↔ [[Ashok Chandrasekar]]（Google），共同负责 benchmark framework、performance regression、workload simulation 与硬件性能分析。
- **PD-Disaggregation**：[[Robert Shaw]] ↔ [[Tyler Michael Smith]]（Red Hat），共同负责 prefill/decode separation、跨实例通信与异构 disaggregated serving。
- **KV-Disaggregation**：[[Maroon Ayoub]] ↔ [[Danny Harnik]]，共同负责 distributed KV cache、prefix sharing、remote storage 与 vLLM KVConnector 集成。Maroon 在 2026 年职业轨迹从 IBM Research 网络转向 Red Hat inference engineering，人物页单独记录该时间差异。

## 生态关系
[[vLLM]] · [[SGLang]] · [[Red Hat]] · [[Google]] · [[IBM]] · [[NVIDIA]] · [[AMD]] · Kubernetes。llm-d 不等同于某一家公司的产品线，其价值恰在跨 engine、跨厂商的 production serving 协作层。

## Sources
- https://github.com/llm-d/llm-d
- https://llm-d.ai/community/sigs
- https://llm-d.ai/blog/llm-d-announce
- https://llm-d.ai/blog/llm-d-v0.5-sustaining-performance-at-scale
