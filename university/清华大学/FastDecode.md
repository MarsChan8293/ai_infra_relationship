---
type: project
name: FastDecode
organization: PACMAN Lab, Tsinghua University
linked_people:
  - "company/字节跳动/何家傲 Jiaao He"
  - "company/清程极智/翟季冬 Jidong Zhai"
layer: distributed-serving
areas: [llm-serving, heterogeneous-inference, kv-cache, cpu-gpu-pipeline]
people:
  - "company/字节跳动/何家傲 Jiaao He"
  - "company/清程极智/翟季冬 Jidong Zhai"
last_verified: "2026-09"
linked_companies: []
---
# FastDecode

## 项目简介
FastDecode 是清华 PACMAN 面向 LLM serving 的 CPU/GPU heterogeneous pipeline 系统。它针对生成阶段 KV cache 占用大量 GPU memory、限制 batch size 的问题，将 Transformer 中 memory-bound 的 KV-cache / attention 路径与 GPU 更擅长的计算路径拆分，并利用多节点 CPU 的聚合内存容量、带宽和算力承担前者。

公开论文报告，在使用相同 GPU 数量的条件下，FastDecode serving throughput 可达到 vLLM 的约 1.88×–5.04×。

## 人物网络
- [[company/字节跳动/何家傲 Jiaao He|何家傲（Jiaao He）]]：FastDecode 主要作者；2025 清华博士毕业后进入字节基础设施研究。
- [[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]]：论文作者、何家傲博士导师，连接 PACMAN 的 HPC / performance modeling 与现代 LLM inference serving。

## 图谱意义
FastDecode 是 PACMAN 从 MoE distributed training / HPC 向推理优化迁移的直接技术节点。相比纯 GPU serving，它代表“利用 CPU 集群资源缓解 KV cache / GPU memory 瓶颈”的异构推理路线。

## Sources
- https://arxiv.org/abs/2403.11421
- https://pacman.cs.tsinghua.edu.cn/~zjd/publication/generated/dblp-journalscorrabs-2403-11421/
- https://laekov.com.cn/cv/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/字节跳动/何家傲 Jiaao He|何家傲（Jiaao He）]]：[[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]]：**博士导师 + 系统论文长期合作者**。合作覆盖 [[community/thu-pacman/FastMoE/FastMoE|FastMoE]] / FasterMoE / SmartMoE 与 [[university/清华大学/FastDecode|FastDecode]]。
- [[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]]：[[university/清华大学/FastDecode|FastDecode]]：与博士生 [[company/字节跳动/何家傲 Jiaao He|何家傲（Jiaao He）]] 合作，将 CPU 集群资源用于处理 memory-bound KV-cache / attention 路径，形成 CPU/GPU heterogeneous LLM serving。

<!-- END AUTO PROJECT PEOPLE -->
