---
type: project
name: smallpond
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/Runji Wang"
  - "community/deepseek-ai/DeepSeek-Infra/Yiliang Xiong"
companies: ["深度求索"]
company_relation: company-led
layer: distributed-data-processing
open_source: true
repository: https://github.com/deepseek-ai/smallpond
areas: [data-processing, distributed-query, duckdb, 3fs, parquet, training-data]
people:
  - "community/deepseek-ai/DeepSeek-Infra/Runji Wang"
  - "community/deepseek-ai/DeepSeek-Infra/Yiliang Xiong"
last_verified: "2026-09"
linked_companies:
  - "company/深度求索/深度求索"
---
# smallpond

smallpond 是 DeepSeek 基于 DuckDB 与 [[3FS]] 构建的轻量级分布式数据处理框架，面向 PB 级数据集与无需长期常驻服务的数据流水线。

## 与 3FS 的关系
官方 README 直接将 smallpond 定义为 “built on DuckDB and 3FS”。其 GraySort benchmark 使用 50 个 compute nodes 与 25 个 3FS storage nodes，对 110.5 TiB 数据进行排序，形成 `3FS → data processing` 的明确系统栈下游关系。

## 人物
`pyproject.toml` 列出 DeepSeek-AI、Runji Wang、Yiliang Xiong 等多名作者。本轮先实体化跨证据更强的 [[Runji Wang]] 与 [[Yiliang Xiong]]，其余作者后续按跨项目重叠展开。

## Sources
- https://github.com/deepseek-ai/smallpond
- https://github.com/deepseek-ai/smallpond/blob/main/README.md
- https://github.com/deepseek-ai/smallpond/blob/main/pyproject.toml

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/Runji Wang|Runji Wang]]：https://github.com/deepseek-ai/smallpond/blob/main/pyproject.toml
- [[community/deepseek-ai/DeepSeek-Infra/Yiliang Xiong|Yiliang Xiong]]：https://github.com/deepseek-ai/smallpond/blob/main/pyproject.toml

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
