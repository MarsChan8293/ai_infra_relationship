---
type: project
name: llm-d
linked_people:
  - "community/llm-d/llm-d/Abdullah Gharaibeh"
  - "community/llm-d/llm-d/Ashok Chandrasekar"
  - "community/llm-d/llm-d/Carlos Costa"
  - "community/llm-d/llm-d/Clayton Coleman"
  - "community/llm-d/llm-d/Danny Harnik"
  - "community/llm-d/llm-d/David Simmons"
  - "community/llm-d/llm-d/JJ Asghar"
  - "community/llm-d/llm-d/Marcio A L Silva"
  - "community/llm-d/llm-d/Maroon Ayoub"
  - "community/llm-d/llm-d/Nili Guy"
  - "community/llm-d/llm-d/Pete Cheslock"
  - "community/llm-d/llm-d/Vita Bortnikov"
  - "community/llm-d/llm-d/张家驹 Jiaju Zhang"
  - "community/vllm-project/vLLM/Robert Shaw"
  - "community/vllm-project/vLLM/Tyler Michael Smith"
governance: cross-company
companies: ["Red Hat","Google","IBM","CoreWeave","NVIDIA"]
company_relation: founding-contributors
layer: kubernetes-distributed-inference
open_source: true
linked_companies:
  - "company/CoreWeave/CoreWeave"
  - "company/Google/Google"
  - "company/IBM/IBM"
  - "company/NVIDIA/NVIDIA"
  - "company/Red Hat/Red Hat"
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

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/llm-d/llm-d/Abdullah Gharaibeh|Abdullah Gharaibeh]]：[[Google]]：截至 2026-08，llm-d 官方技术文章列为 Senior Staff Software Engineer, Google。
- [[community/llm-d/llm-d/Ashok Chandrasekar|Ashok Chandrasekar]]：[[llm-d]]：Benchmarking SIG Lead。
- [[community/llm-d/llm-d/Carlos Costa|Carlos Costa]]：[[IBM]]：截至 2026-09，llm-d 官方作者页列为 Distinguished Engineer, IBM。
- [[community/llm-d/llm-d/Clayton Coleman|Clayton Coleman]]：[[Google]]：llm-d 官方作者页列为 Distinguished Engineer, Google。
- [[community/llm-d/llm-d/Danny Harnik|Danny Harnik]]：[[llm-d]]：KV-Disaggregation SIG Lead。
- [[community/llm-d/llm-d/David Simmons|David Simmons]]：[[llm-d]]：Community Manager
- [[community/llm-d/llm-d/JJ Asghar|JJ Asghar]]：[[llm-d]]：Community Manager
- [[community/llm-d/llm-d/Marcio A L Silva|Marcio A L Silva]]：[[llm-d]]：截至 2026-09 为 Benchmarking SIG Lead。
- [[community/llm-d/llm-d/Maroon Ayoub|Maroon Ayoub]]：[[Red Hat]]：2026-06 与 2026-08 的 llm-d 官方技术文章均列为 Senior Principal Machine Learning Engineer, Red Hat。
- [[community/llm-d/llm-d/Nili Guy|Nili Guy]]：[[IBM]] / IBM Research：截至 2026-09，llm-d 官方作者资料列为 Senior Technical Staff Member, IBM Research。
- [[community/llm-d/llm-d/Pete Cheslock|Pete Cheslock]]：[[llm-d]]：Community Manager
- [[community/llm-d/llm-d/Vita Bortnikov|Vita Bortnikov]]：[[IBM]]：截至 2026-09，llm-d 官方作者资料列为 IBM Fellow。
- [[community/llm-d/llm-d/张家驹 Jiaju Zhang|张家驹（Jiaju Zhang）]]：[[llm-d]]：以社区孵化、推广、技术布道和生态连接为主要参与方式，尤其面向中国及 APAC 开发者与产业社区。
- [[community/vllm-project/vLLM/Robert Shaw|Robert Shaw]]：[[llm-d]]：PD-Disaggregation SIG Lead；同时处于项目创始/核心领导网络，连接 vLLM engine 与 Kubernetes-native distributed serving。
- [[community/vllm-project/vLLM/Tyler Michael Smith|Tyler Michael Smith]]：[[llm-d]]：PD-Disaggregation SIG Lead，与 [[Robert Shaw]] 共同负责 prefill/decode separation、跨实例通信、异构资源利用与 distributed serving。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/CoreWeave/CoreWeave|CoreWeave]]：公司页与社区/项目页均有显式记录；关系：`founding-contributors`。
- [[company/Google/Google|Google]]：公司页与社区/项目页均有显式记录；关系：`founding-contributors`。
- [[company/IBM/IBM|IBM]]：公司页与社区/项目页均有显式记录；关系：`founding-contributors`。
- [[company/NVIDIA/NVIDIA|NVIDIA]]：公司页与社区/项目页均有显式记录；关系：`founding-contributors`。
- [[company/Red Hat/Red Hat|Red Hat]]：公司页与社区/项目页均有显式记录；关系：`founding-contributors`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
