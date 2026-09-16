---
type: project
name: BaGuaLu
aliases: ["八卦炉", "BaGuaLu-2"]
companies: ["清程极智"]
company_relation: company-led
layer: distributed-training
open_source: true
repository: https://github.com/thu-pacman/BaGuaLu
areas: [distributed-training, parallelism, communication, moe, activation-memory, heterogeneous-compute]
people:
  - "company/清程极智/马子轩 Zixuan Ma"
  - "company/清程极智/唐适之 Shizhi Tang"
  - "company/清程极智/师天麾 Tianhui Shi"
  - "company/清程极智/翟季冬 Jidong Zhai"
last_verified: "2026-09"
---
# BaGuaLu（八卦炉）

## 项目简介
BaGuaLu（八卦炉）是清华 HPC / AI systems 研究网络发展出的分布式训练系统方向，也是 [[company/清程极智/清程极智|清程极智]] 当前训练与推理加速产品线的重要技术来源。公司官网将“八卦炉”定位为大模型训练加速系统，强调并行方案、分布式通信和国产超算上的大规模训练优化。

当前 upstream `thu-pacman/BaGuaLu` 已公开 BaGuaLu-2 训练系统 artifact，围绕大规模细粒度 MoE 训练中的 activation-memory pressure，提供 pipeline-aware activation offload/reload、interleaved 1F1B、activation-memory model、Transformer Engine patches 与 MoE telemetry。

## 人物连接
- [[company/清程极智/马子轩 Zixuan Ma|马子轩]]：早期 BaGuaLu 论文第一作者。
- [[company/清程极智/唐适之 Shizhi Tang|唐适之]]、[[company/清程极智/师天麾 Tianhui Shi|师天麾]]、[[company/清程极智/翟季冬 Jidong Zhai|翟季冬]]：BaGuaLu 论文 / 清华 PACMAN 研究网络中的直接作者或指导节点。

## 仓库说明
- `thu-pacman/BaGuaLu`：当前 canonical upstream，包含 BaGuaLu-2 公开代码与使用说明。
- `QingCheng-AI/BaGuaLu`：清程极智官方 GitHub 组织中的关联仓库，当前主要保留论文 artifact；不作为本节点 canonical source repository。

## Sources
- https://github.com/thu-pacman/BaGuaLu
- https://github.com/QingCheng-AI/BaGuaLu
- https://www.qc-ai.cn/products/bagualu
- https://pacman.cs.tsinghua.edu.cn/~zjd/projects/bagualu/
