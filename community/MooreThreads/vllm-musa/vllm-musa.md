---
type: project
name: vllm-musa
aliases: [vLLM-MUSA]
organization: MooreThreads
linked_people:
  - "company/摩尔线程/Xiaodong Ye"
companies: ["摩尔线程"]
company_relation: company-led
layer: llm-serving-hardware-backend
open_source: true
linked_companies:
  - "company/摩尔线程/摩尔线程"
---
# vLLM-MUSA

vLLM-MUSA 是 vLLM 面向摩尔线程 MUSA GPU 的硬件 backend，围绕 vLLM V1、attention、MoE、model support、compiler 与 MUSA kernel 进行持续适配。

## 图谱关系
`vLLM → vLLM-MUSA → MATE / MUSA kernels → 摩尔线程 GPU`

它也可通过 Mooncake Transfer Engine 与 LMCache 连接到 PD 分离和 KV Cache 数据传输层。

## Sources
- https://github.com/MooreThreads/vllm-musa
- https://blog.mthreads.com/blog/AI/2026-07-27-mooncake-transfer-engine-musa/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/摩尔线程/Xiaodong Ye|Xiaodong Ye]]：https://github.com/MooreThreads/vllm-musa/commit/9a90ece5837599d5bf68c6ba3b1891f86c579f71

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/摩尔线程/摩尔线程|摩尔线程]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
