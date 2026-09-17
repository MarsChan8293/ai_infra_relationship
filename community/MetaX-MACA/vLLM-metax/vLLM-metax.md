---
type: project
name: vLLM-metax
organization: MetaX-MACA
companies: ["沐曦"]
company_relation: company-led
layer: llm-serving-hardware-backend
open_source: true
linked_companies:
  - "company/沐曦/沐曦"
linked_people:
  - "company/沐曦/Xin Li"
---
# vLLM-metax

vLLM-metax 是 vLLM 面向沐曦 GPU / MXMACA 软件栈的硬件 backend / plugin 工程，持续跟随上游 vLLM 演进并承载模型、attention、MoE 与 kernel 适配。

## 图谱关系
`vLLM → vLLM-metax → MetaX kernels / mcoplib → 沐曦 GPU`

沐曦官方公开材料称其已成为 vLLM 社区正式支持的中国 GPU 厂商之一，并持续向上游回馈能力。

## Sources
- https://github.com/MetaX-MACA/vLLM-metax
- https://www.metax-tech.com/en/ndetail/12549.html
