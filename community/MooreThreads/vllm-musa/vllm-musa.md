---
type: project
name: vllm-musa
aliases: [vLLM-MUSA]
organization: MooreThreads
companies: ["摩尔线程"]
company_relation: company-led
layer: llm-serving-hardware-backend
open_source: true
linked_companies:
  - "company/摩尔线程/摩尔线程"
linked_people:
  - "company/摩尔线程/Xiaodong Ye"
---
# vLLM-MUSA

vLLM-MUSA 是 vLLM 面向摩尔线程 MUSA GPU 的硬件 backend，围绕 vLLM V1、attention、MoE、model support、compiler 与 MUSA kernel 进行持续适配。

## 图谱关系
`vLLM → vLLM-MUSA → MATE / MUSA kernels → 摩尔线程 GPU`

它也可通过 Mooncake Transfer Engine 与 LMCache 连接到 PD 分离和 KV Cache 数据传输层。

## Sources
- https://github.com/MooreThreads/vllm-musa
- https://blog.mthreads.com/blog/AI/2026-07-27-mooncake-transfer-engine-musa/
