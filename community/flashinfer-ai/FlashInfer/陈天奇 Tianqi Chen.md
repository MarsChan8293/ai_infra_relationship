---
type: person
name: 陈天奇
english_name: Tianqi Chen
aliases: [Tianqi Chen, 陈天奇]
schools:
  - "Carnegie Mellon University"
  - "University of Washington"
  - "上海交通大学"
communities: [FlashInfer]
roles:
  - "Associate Professor, Carnegie Mellon University"
  - "Distinguished Engineer, NVIDIA"
  - "FlashInfer Original Paper Author"
---
# 陈天奇（Tianqi Chen）

## 当前角色

陈天奇是 Carnegie Mellon University Machine Learning Department 与 Computer Science Department 的 Associate Professor，同时任 NVIDIA Distinguished Engineer。其研究长期位于 machine learning、compiler、runtime 与 hardware backend 的交叉层。

## 教育与工作经历

- [[university/上海交通大学/上海交通大学|上海交通大学]]：ACM Honors Class，本科与硕士。
- [[university/University of Washington/University of Washington|University of Washington]]：2013–2019，Computer Science PhD；导师 Carlos Guestrin，并与 Luis Ceze、Arvind Krishnamurthy 有研究合作。
- [[university/Carnegie Mellon University/Carnegie Mellon University|Carnegie Mellon University]]：现任 ML / CS faculty，并参与 [[university/Carnegie Mellon University/Catalyst Group|Catalyst Group]]。
- NVIDIA：现任 Distinguished Engineer；此前为 OctoAI Chief Technologist，OctoAI 后被 NVIDIA 收购。

## 2025–2026 AI Infra 主线

### Kernel / Agent / Harness

- [[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]]：MLSys 2025 论文作者之一；面向 LLM attention / KV cache 的高性能 inference kernel engine。
- [[community/flashinfer-ai/FlashInfer-Bench/FlashInfer-Bench|FlashInfer-Bench]]：MLSys 2026 论文作者之一；把 AI-generated kernel 的 trace、correctness、benchmark 与 SGLang / vLLM production substitution 串成闭环。
- [[community/NVIDIA/AVO/AVO|AVO]]：2026 论文作者之一；用 autonomous coding agent 取代传统 evolutionary search 中固定的 mutation / crossover。
- [[community/research/CAKE/CAKE|CAKE]]：2026 论文作者之一；提出 compiler-agent co-design，让 IR、verifier、cost model、diagnostics 与 kernel agent 一起演化。

### Compiler / Runtime

- [[university/Carnegie Mellon University/Catalyst Group/Mirage Persistent Kernel|Mirage Persistent Kernel]]：OSDI 2026 论文作者之一；把多算子、多 GPU inference 编译为 high-performance megakernel。
- [[university/Carnegie Mellon University/Catalyst Group/Event Tensor|Event Tensor]]：MLSys 2026 论文作者之一；用 event dependency 抽象动态 shape 和 data-dependent workload，生成 dynamic megakernel。
- [[university/Carnegie Mellon University/Catalyst Group/XGrammar|XGrammar]]：MLSys 2025 论文作者之一；面向 structured generation / constrained decoding 的高性能 runtime。

这些工作形成一条连续路线：从传统 tensor compiler / kernel optimization，进一步走向 **Agent + Compiler + Benchmark Harness + Production Runtime** 的自动优化闭环。

## 早期代表性系统

Apache TVM · MLC-LLM · XGBoost · Apache MXNet

## 关联人物

- [[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪（Zihao Ye）]]：FlashInfer、FlashInfer-Bench、MPK、Event Tensor、CAKE 等公开论文/项目存在共同作者或研究协作关系。
- [[community/flashinfer-ai/FlashInfer/赖睿航 Ruihang Lai|赖睿航（Ruihang Lai）]]：CMU Catalyst 博士生；公开资料显示由陈天奇与 Todd C. Mowry 共同指导，并在 FlashInfer、XGrammar、MPK、Event Tensor 等方向形成研究连接。

## Sources

- https://tqchen.com/
- https://www.csd.cmu.edu/people/faculty/tianqi-chen
- https://catalyst.cs.cmu.edu/
- https://github.com/flashinfer-ai/flashinfer
- https://github.com/flashinfer-ai/flashinfer-bench
- https://arxiv.org/abs/2608.12629
- https://arxiv.org/abs/2604.13327
- https://arxiv.org/abs/2512.22219
- https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html
