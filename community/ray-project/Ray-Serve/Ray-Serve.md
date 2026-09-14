---
type: project
name: Ray Serve
companies: ["Anyscale"]
company_relation: core-commercial-ecosystem
layer: distributed-serving
open_source: true
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
