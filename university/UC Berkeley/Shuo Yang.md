---
type: person
name: Shuo Yang
aliases: ["Shuo Yang", "Andy Yang", "andy-yang-1", "Andy_ShuoYang"]
current_affiliations: ["UC Berkeley", "Sky Computing Lab", "LMSYS"]
schools:
  - "UC Berkeley"
communities: [FreeToken]
roles: [PhD Student, Researcher, FreeToken Co-first Author]
areas: [llm-serving, moe-inference, gpu-kernels, sparse-attention, multimodal-systems, edge-inference, algorithm-system-codesign]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/Inferact/Ion Stoica","type":["advisor","student","research-collaboration","paper-coauthor"],"confidence":"high","evidence":["https://andy-yang-1.github.io/","https://arxiv.org/abs/2608.16157"]}'
  - '{"target":"university/上海交通大学/Xiaoze Fan","type":["mentor-network","paper-coauthor","research-collaboration"],"project":"FreeToken","start":"2026","confidence":"high","evidence":["https://jasonfxz.top/","https://arxiv.org/abs/2608.16157"]}'
---
# Shuo Yang

UC Berkeley EECS 博士生，Sky Computing Lab / LMSYS 成员，导师为 [[company/Inferact/Ion Stoica|Ion Stoica]]。研究覆盖 full-stack machine learning systems，尤其是 LLM serving、GPU kernel、sparse attention、multimodal systems 与 algorithm-system co-design。

## FreeToken

[[community/FlashML-org/FreeToken/FreeToken|FreeToken]] 论文共同一作，也是代码核心贡献网络成员。

FreeToken 与 Shuo Yang 既有论文作者证据，也有 GitHub 代码证据：仓库近期模型支持提交中存在 `Co-authored-by: Shuo Yang <...andy-yang-1...>`，早期 PR #1 / #4 由 `andy-yang-1` 发起，对应 MiniMax / Muse-Glimmer 支持。

FreeToken 把他此前在高性能 LLM serving / sparse systems 上的研究线进一步推到消费级硬件：CPU、GPU、host DRAM、PCIe 共同组成运行时资源池，重点解决大 MoE 模型在显存受限机器上的 execution / residency / memory orchestration。

## Berkeley systems 网络

个人主页明确写明：
- UC Berkeley EECS PhD；
- advised by Ion Stoica；
- Sky Computing Lab / LMSYS；
- 研究从 kernel optimization 延伸到 large-scale inference / generation 与 multimodal algorithms。

Berkeley Sky 官方 people 页面也将 Shuo Yang 列为 GSR。

## 与 Xiaoze Fan 的关系

[[university/上海交通大学/Xiaoze Fan|Xiaoze Fan（范晓泽）]] 的个人主页明确写明在 Berkeley Sky 访问研究期间由 Ion Stoica supervised、由 **Shuo Yang mentored**。两人同时是 FreeToken 论文共同一作，因此这里建立 `mentor-network + paper-coauthor + research-collaboration`，不是仅凭共同项目推断。

## 其他 AI Infra 线索

- BlendServe：资源感知 offline inference batching；
- S-LoRA：大规模 LoRA serving；
- HashAttention / Double Sparsity / vAttention：稀疏 attention 与 inference acceleration；
- UCCL：GPU networking / collective communication 研究网络。

这些经历说明 Shuo Yang 在图谱中不是单一 FreeToken 项目作者，而是 Berkeley inference systems / algorithm-system co-design 的桥节点。

## Sources
- https://andy-yang-1.github.io/
- https://sky.cs.berkeley.edu/people/
- https://sky.cs.berkeley.edu/publications/
- https://arxiv.org/abs/2608.16157
- https://github.com/FlashML-org/FreeToken
- https://github.com/FlashML-org/FreeToken/commit/a2538a428baa4c6d823c76efe96cb3bc0cbd1f86
- https://jasonfxz.top/
