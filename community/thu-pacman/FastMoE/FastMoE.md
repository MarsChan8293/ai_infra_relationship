---
type: project
name: FastMoE
organization: thu-pacman
linked_people: []
areas: [moe, distributed-training, all-to-all-communication, load-balancing, large-model-training]
layer: distributed-moe-training
open_source: true
repository: https://github.com/laekov/fastmoe
last_verified: "2026-09"
linked_companies: []
---
# FastMoE

FastMoE 是 PACMAN 早期进入大模型系统的重要项目，面向 PyTorch 的分布式 Mixture-of-Experts 训练，支持 GPU 与超算平台，并围绕 expert placement、跨节点通信与负载均衡优化 MoE 训练。

## 图谱意义
FastMoE 的作者网络非常关键：何家傲、Jiezhong Qiu、曾奥涵、杨植麟、翟季冬、唐杰共同署名，使它成为 [[university/清华大学/PACMAN|PACMAN]] 与 [[university/清华大学/KEG|KEG]] 在 GLM-130B 之前就已存在的 model-system co-design 强边。

后续 FasterMoE / SmartMoE 继续解决 MoE load imbalance 与 communication scheduling；PACMAN 的研究路线再延伸到 FastDecode、Jenga、QFactory 等 LLM serving 系统。

## Sources
- https://pacman.cs.tsinghua.edu.cn/~zjd/projects/fastmoe/
- https://pacman.cs.tsinghua.edu.cn/~zjd/projects/fastermoe/
- https://keg.cs.tsinghua.edu.cn/glm-130b/posts/glm-130b/
