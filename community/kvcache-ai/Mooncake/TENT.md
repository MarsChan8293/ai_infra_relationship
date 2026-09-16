---
type: project
name: TENT
layer: data-movement
open_source: true
repository: https://github.com/kvcache-ai/Mooncake
areas: [data-movement, rdma, heterogeneous-interconnect, fault-tolerance, disaggregated-serving, reinforcement-learning]
people:
  - "community/kvcache-ai/Mooncake/任峰 Feng Ren"
  - "university/清华大学/Ruoyu Qin"
  - "community/kvcache-ai/Mooncake/马腾 Teng Ma"
  - "community/kvcache-ai/Mooncake/Shangming Cai"
  - "community/kvcache-ai/Mooncake/Ke Yang"
  - "community/sgl-project/SGLang/Yineng Zhang"
  - "company/趋境科技/武永卫 Yongwei Wu"
  - "university/清华大学/Mingxing Zhang"
governance: Mooncake subproject / Transfer Engine NEXT
last_verified: "2026-09"
---
# TENT

## 项目定位
TENT（Mooncake Transfer Engine NEXT）是 Mooncake 数据移动层的下一代演进。它把应用的 transfer intent 与具体网络路径解耦，将 RDMA、多 rail、NVLink/异构互联等资源抽象为可动态调度的数据平面，并通过 slice spraying、实时链路质量与自动故障绕行提升分布式推理和 RL 数据传输的吞吐与韧性。

2026 年论文《TENT: A Declarative Slice Spraying Engine for Performant and Resilient Data Movement in Disaggregated LLM Serving》指出，TENT 源于 Mooncake Transfer Engine 在数千 GPU 生产环境中的经验；论文评测覆盖 SGLang HiCache 与 Moonshot Checkpoint Engine，并把 Mooncake TE、NIXL、UCCL 作为对比基线。

## Mooncake 关系
- [[Mooncake]]：TENT 是官方 roadmap 中的 `Mooncake Transfer Engine NEXT`，不是独立无关项目。
- [[community/kvcache-ai/Mooncake/任峰 Feng Ren|任峰]]：论文第一作者，也是 Mooncake Transfer Engine Codeowner。
- [[community/kvcache-ai/Mooncake/Ke Yang|Ke Yang]]、[[community/kvcache-ai/Mooncake/Shangming Cai|Shangming Cai]]、[[community/kvcache-ai/Mooncake/马腾 Teng Ma|马腾]]：Mooncake Codeowner 网络与 TENT 作者网络直接重叠。
- [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]]：连接 TENT 与 SGLang serving / HiCache 路径。

## 为什么重要
TENT 显示 Mooncake 的核心能力已经从“KV cache system”扩展到更通用的 tensor/data movement substrate：不仅服务 inference KV transfer，也进入 RL 参数/样本/hidden-state 流动与异构互联调度。

## Sources
- https://arxiv.org/abs/2604.00368
- https://github.com/kvcache-ai/Mooncake/issues/1058
- https://github.com/kvcache-ai/Mooncake
