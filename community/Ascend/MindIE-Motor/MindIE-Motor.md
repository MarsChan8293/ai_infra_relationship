---
type: project
name: MindIE-Motor
linked_people:
  - "community/Ascend/MemCache/吕有辉"
companies: ["华为"]
company_relation: company-led
layer: distributed-inference-control-plane
hardware: [Ascend]
open_source: true
linked_companies:
  - "company/华为/华为"
---
# MindIE-Motor

## 项目简介
昇腾侧分布式推理服务与控制面项目，重点覆盖 Coordinator 调度、KV cache affinity、PD 分离、容量规划和 vLLM frontend 接入。

## GitCode
https://gitcode.com/Ascend/MindIE-Motor

## GitHub
未确认官方 GitHub canonical repository；本节点以官方 GitCode 仓库作为源码来源。

## 主要贡献公司
- [[company/华为/华为|华为]]：Ascend/MindIE 官方技术栈的主要开发与维护公司节点。

## 推理优化人物
[[LinWei100]]

## 生态关系
[[vLLM-Ascend]] · [[MindIE-LLM]] · [[Mooncake]]

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/Ascend/MemCache/吕有辉|吕有辉]]：在 MindIE-Motor 推进 **MemCache KvEvent → kv-conductor 缓存感知调度**：kv-conductor 订阅 MemCache MetaService 的 KvEvent 广播，结合引擎 offload 事件做缓存匹配，把请求路由到已经缓存共享前缀的节点，从而提高 KV 复用并降低重复 Prefill / TTFT。

<!-- END AUTO PROJECT PEOPLE -->
