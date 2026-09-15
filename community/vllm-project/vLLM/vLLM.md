---
type: project
name: vLLM
linked_people:
  - "community/llm-d/llm-d/张家驹 Jiaju Zhang"
  - "community/Project-HAMi/HAMi/chaunceyjiang"
  - "community/vllm-project/vLLM/Chen Zhang"
  - "community/vllm-project/vLLM/Matthew Bonanni"
  - "community/vllm-project/vLLM/Patrick von Platen"
  - "community/vllm-project/vLLM/Yongye Zhu"
  - "community/vllm-project/vLLM/乔一凡 Yifan Qiao"
  - "community/vllm-project/vLLM/李卓翰 Zhuohan Li"
  - "community/vllm-project/vLLM/游凯超 Kaichao You"
  - "company/Inferact/Ion Stoica"
  - "company/Inferact/Joseph Gonzalez"
  - "company/Inferact/Woosuk Kwon"
  - "company/Meta/Richard Zou"
  - "company/OpenAI/柳晓萱 Xiaoxuan Liu"
  - "company/TensorMesh/杜昆泰 Kuntai Du"
  - "company/TensorMesh/程翊华 Yihua Cheng"
  - "university/UC Berkeley/Xiangxi Mo"
companies: ["Inferact","Red Hat","Meta","Hugging Face","TensorMesh","Neural Magic"]
company_relation: cross-company-core-contributors
layer: inference-engine
open_source: true
linked_companies:
  - "company/Hugging Face/Hugging Face"
  - "company/Inferact/Inferact"
  - "company/Meta/Meta"
  - "company/Neural Magic/Neural Magic"
  - "company/Red Hat/Red Hat"
  - "company/TensorMesh/TensorMesh"
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

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/llm-d/llm-d/张家驹 Jiaju Zhang|张家驹（Jiaju Zhang）]]：[[vLLM]]：社区 contributor / ambassador，并通过 meetup、workshop 等活动连接开发者、模型团队、硬件厂商与云原生生态。
- [[community/Project-HAMi/HAMi/chaunceyjiang|chaunceyjiang]]：[[vLLM]]：截至 2026-09，官方 Committers 页面列为 committer，主要负责 **Tool use and reasoning parser**；area owners 也将其列入 reasoning / tool calling parsers。
- [[community/vllm-project/vLLM/Chen Zhang|Chen Zhang]]：[[vLLM]]：参与 V1 KV cache manager 重构、模型支持与 LLM serving 系统研究
- [[community/vllm-project/vLLM/Matthew Bonanni|Matthew Bonanni]]：[[vLLM]]：Maintainer，主要连接高性能计算、GPU inference 与 serving engine 优化。
- [[community/vllm-project/vLLM/Patrick von Platen|Patrick von Platen]]：[[community/vllm-project/vLLM/Harry Mellor|Harry Mellor]]：**Hugging Face 同事 + 模型实现/serving integration 协作者**。截至 2026-09 两人均公开关联 Hugging Face；Patrick 长期参与 Transformers / Diffusers 与模型实现生态，Harry 负责 vLLM 的 Hugging Face integration、config 与...
- [[community/vllm-project/vLLM/Yongye Zhu|Yongye Zhu]]：[[vLLM]]：长期 contributor；参与模型 day-0 support、backend interface 与 inference serving 工程
- [[community/vllm-project/vLLM/乔一凡 Yifan Qiao|乔一凡（Yifan Qiao）]]：[[vLLM]] × [[Mooncake]]：2026-05 参与 distributed KV cache integration，用于大规模 agentic workloads；这里记录为项目集成，不将乔一凡标成 Mooncake 核心社区成员
- [[community/vllm-project/vLLM/李卓翰 Zhuohan Li|李卓翰（Zhuohan Li）]]：[[Inferact/Woosuk Kwon|Woosuk Kwon]]：**UC Berkeley 同实验室研究者 + vLLM 共同创始/共同维护者**。李卓翰 2019–2024、Woosuk 2021–2025 在 Berkeley CS 博士阶段有 2021–2024 的重叠，并都处于 [[Ion Stoica]] 的系统研究网络；2023 共同创建 / 推动 [[vLLM]]。
- [[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超（Kaichao You）]]：[[university/清华大学/龙明盛 Mingsheng Long|龙明盛（Mingsheng Long）]]：**清华博士导师 + 长期论文合作者**。龙明盛官方主页将游凯超列为 2020–2025 博士生；双方共同署名多项 machine-learning 工作、depyf 与 2025 Jenga。该导师关系与游凯超后来进入 Berkeley / vLLM 网络是两段不同阶段，不应把龙明盛直接标成 vLLM maintainer。
- [[company/Inferact/Ion Stoica|Ion Stoica]]：[[Inferact/Woosuk Kwon|Woosuk Kwon]]：**UC Berkeley 博士导师 / 学生 + vLLM 研究网络**。Woosuk 2021–2025 在 Berkeley CS 博士阶段由 Ion Stoica 指导，博士论文主题为 vLLM / efficient LLM inference；此后两人又同属 Inferact founding network。
- [[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]]：[[community/vllm-project/vLLM/Simon Mo|Simon Mo]]：**UC Berkeley 博士共同导师 / 学生 + inference serving 研究网络**。Simon 2026 博士论文《Building Open Source Inference Serving Systems》由 Joseph Gonzalez 与 [[Inferact/Ion Stoica|Ion Stoica]] 共同指导；研究覆盖 Ray Se...
- [[company/Inferact/Woosuk Kwon|Woosuk Kwon]]：[[vLLM]] 创始人；2023 起推动项目与 PagedAttention / engine core
- [[company/Meta/Richard Zou|Richard Zou]]：[[vLLM]]：通过 torch.compile integration 与硬件可移植性工作连接到 vLLM serving stack
- [[company/OpenAI/柳晓萱 Xiaoxuan Liu|柳晓萱（Xiaoxuan Liu）]]：[[vLLM]]：博士阶段参与高效 LLM inference 与 vLLM 团队
- [[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰（Kuntai Du）]]：[[vLLM]]：KV Connector 与 LMCache 集成方向重要贡献者
- [[company/TensorMesh/程翊华 Yihua Cheng|程翊华（Yihua Cheng）]]：[[vLLM]]：KV Connector / offloading 生态的重要贡献者
- [[university/UC Berkeley/Xiangxi Mo|Xiangxi Mo]]：[[community/vllm-project/Jenga/Jenga|Jenga]]：SOSP 2025 作者，连接 Berkeley systems 与现代 LLM serving memory management。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Hugging Face/Hugging Face|Hugging Face]]：公司页与社区/项目页均有显式记录；关系：`cross-company-core-contributors`。
- [[company/Inferact/Inferact|Inferact]]：公司页与社区/项目页均有显式记录；关系：`cross-company-core-contributors`。
- [[company/Meta/Meta|Meta]]：公司页与社区/项目页均有显式记录；关系：`cross-company-core-contributors`。
- [[company/Neural Magic/Neural Magic|Neural Magic]]：公司页与社区/项目页均有显式记录；关系：`cross-company-core-contributors`。
- [[company/Red Hat/Red Hat|Red Hat]]：公司页与社区/项目页均有显式记录；关系：`cross-company-core-contributors`。
- [[company/TensorMesh/TensorMesh|TensorMesh]]：公司页与社区/项目页均有显式记录；关系：`cross-company-core-contributors`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
