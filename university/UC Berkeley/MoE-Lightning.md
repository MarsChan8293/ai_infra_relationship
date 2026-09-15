---
type: project
name: MoE-Lightning
organization: UC Berkeley
layer: inference-engine
areas: [moe-inference, heterogeneous-inference, cpu-gpu-offloading, memory-optimization]
people:
  - "university/UC Berkeley/Shiyi Cao"
  - "university/UC Berkeley/Shu Liu"
last_verified: "2026-09"
---
# MoE-Lightning

## 项目简介
MoE-Lightning 是 ASPLOS 2025 的高吞吐 MoE inference 系统，目标是在 GPU 显存受限时仍高效运行超出显存容量的 Mixture-of-Experts 模型。

系统通过 CPU–GPU–I/O pipeline、paged weights 与计算/数据移动重叠，把 host memory / storage 纳入推理热路径。论文报告相较已有 offloading baseline 可获得最高约 10.3× throughput 提升。

## 人物网络
- [[university/UC Berkeley/Shiyi Cao|Shiyi Cao]]：第一作者，Berkeley ML systems / SGLang 网络。
- [[university/UC Berkeley/Shu Liu|Shu Liu]]：共同作者，Jenga / Berkeley Sky systems 网络。
- Xiaoxuan Liu、Ying Sheng、Joseph Gonzalez、Matei Zaharia、Ion Stoica 等也在论文作者网络中；本轮不为这些已有或未点名节点额外扩边。

## 图谱意义
MoE-Lightning 把 Jenga 的 memory-management 路线继续推进到 MoE heterogeneous inference：`Jenga → Shu Liu → MoE-Lightning → Shiyi Cao → SGLang`。

## Sources
- https://doi.org/10.1145/3669940.3707267
- https://sky.cs.berkeley.edu/publications/
