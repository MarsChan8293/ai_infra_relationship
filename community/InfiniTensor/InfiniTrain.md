---
type: project
name: InfiniTrain
linked_people: []
layer: distributed-training
open_source: true
repository: https://github.com/InfiniTensor/InfiniTrain
areas: [distributed-training, tensor-parallel, pipeline-parallel, sequence-parallel, zero, communication-compute-overlap, autograd]
last_verified: "2026-09"
linked_companies: []
---
# InfiniTrain

InfiniTrain 是从零构建的 C++ 大模型训练框架，支持多维分布式并行。虽然本图谱主关注推理优化，但它与九源 runtime / kernel / CCL 抽象共用大量底座，因此保留为重要相邻节点。

## 能力
- DDP、TP、SP、PP、GPipe / 1F1B / virtual pipeline；
- multi-node distributed training；
- ZeRO Stage-1 / Stage-2；
- communication-computation overlap 与 gradient bucketing；
- autograd / autocast / LoRA / profiler；
- 2026 继续推进 external PrivateUse1 backend extension 与 provider-neutral runtime/kernel/CCL registration。

它是识别九源 distributed-systems / backend engineering 人才的重要来源，但不会因为与 InfiniLM 共用底座就自动推断同一维护团队。

## Sources
- https://github.com/InfiniTensor/InfiniTrain
- https://github.com/InfiniTensor/InfiniTrain/blob/master/README.md
