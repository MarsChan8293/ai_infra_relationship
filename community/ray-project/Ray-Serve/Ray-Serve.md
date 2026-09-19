---
type: project
name: Ray Serve
status: active
repository: https://github.com/ray-project/ray
docs: https://docs.ray.io/en/latest/serve/
last_verified: "2026-09"
linked_people:
  - "community/vllm-project/vLLM/Simon Mo"
companies: ["Anyscale"]
company_relation: core-commercial-ecosystem
layer: distributed-serving
areas:
  - "distributed-serving"
  - "autoscaling"
  - "multi-model"
  - "pd-disaggregation"
  - "prefix-aware-routing"
hardware:
  - "nvidia"
  - "amd"
  - "intel"
  - "tpu"
  - "ascend"
integrations:
  - "vLLM"
  - "SGLang"
linked_companies:
  - "company/Anyscale/Anyscale"
---
# Ray Serve

## 项目简介
Ray Serve 是 Ray 的 scalable model serving 层，用 Ray actor/task 运行时提供模型副本管理、请求路由、autoscaling、composition 和分布式部署。它是现代 ML serving 到 LLM serving 演进中的重要系统路线，并为后来的 vLLM/LLM serving 人才网络提供了大量实践经验。

## GitHub
Monorepo：https://github.com/ray-project/ray

子路径：`python/ray/serve/`

## 主要贡献公司
- [[company/Anyscale/Anyscale|Anyscale]]：Ray 商业化与长期工程生态的核心公司节点；Ray Serve 仍是开源社区项目，因此该边表示 **core commercial / maintainer ecosystem**。

## 主要维护者 / 组织
由 Ray 开源社区维护，商业生态与 [[Anyscale]] 紧密相连。[[Simon Mo]] 的系统研究/工程经历横跨 Ray Serve 与 vLLM，是 Berkeley/Anyscale/vLLM 网络的重要桥梁。

## 生态关系
[[Anyscale]] · [[vLLM]] · [[Dynamo]] · [[UC Berkeley]]。Ray Serve 位于通用 distributed serving 平台层，而 vLLM/SGLang 更偏 LLM-specialized engine。

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Anyscale/Anyscale|Anyscale]]：公司页与社区/项目页均有显式记录；关系：`core-commercial-ecosystem`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/vllm-project/vLLM/Simon Mo|Simon Mo]]：[[Anyscale]]：Software Engineer，参与 [[community/ray-project/Ray-Serve/Ray-Serve|Ray Serve]]

<!-- END AUTO PROJECT PEOPLE -->
