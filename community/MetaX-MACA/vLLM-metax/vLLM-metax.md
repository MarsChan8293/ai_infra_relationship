---
type: project
name: vLLM-metax
organization: MetaX-MACA
linked_people:
  - "company/沐曦/Xin Li"
companies: ["沐曦"]
company_relation: company-led
layer: llm-serving-hardware-backend
open_source: true
linked_companies:
  - "company/沐曦/沐曦"
---
# vLLM-metax

vLLM-metax 是 vLLM 面向沐曦 GPU / MXMACA 软件栈的硬件 backend / plugin 工程，持续跟随上游 vLLM 演进并承载模型、attention、MoE 与 kernel 适配。

## 图谱关系
`vLLM → vLLM-metax → MetaX kernels / mcoplib → 沐曦 GPU`

沐曦官方公开材料称其已成为 vLLM 社区正式支持的中国 GPU 厂商之一，并持续向上游回馈能力。

## Sources
- https://github.com/MetaX-MACA/vLLM-metax
- https://www.metax-tech.com/en/ndetail/12549.html

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/沐曦/Xin Li|Xin Li]]：vLLM-metax 的 BF16 indexer cache、top-k、自定义算子与 DeepSeek / FusedMoE 路径。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/沐曦/沐曦|沐曦]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
