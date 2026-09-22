---
type: research-institution
name: LANCER Lab
aliases:
  - "LANCER"
  - "Language And Compilation Optimization for Next-gen High Performance Computing Research"
linked_people: []
areas:
  - "ai-compilers"
  - "kernel-dsl"
  - "gpu-kernels"
  - "high-performance-computing"
  - "compiler-optimization"
projects:
  - "Croqtile"
website: https://github.com/LancerLab
country: China
city: Shanghai
last_verified: "2026-09"
---
# LANCER Lab

LANCER Lab（Language And Compilation Optimization for Next-gen High Performance Computing Research）是 [[上海交通大学]] 与 [[company/燧原科技/燧原科技|燧原科技]] 的联合实验室。

这里特意不把 frontmatter 的 `organization` 写成单一母机构，因为公开介绍明确是 **SJTU × Shanghai Enflame Technology joint lab**。把它机械归到学校或公司任何一侧，都会把联合治理结构压扁。

## 技术方向

LANCER 的公开愿景是用新的 programming language / compiler abstraction 降低高性能 kernel 开发难度，同时保留底层性能与可移植性。公开组织页强调的方向包括：

- intuitive tile / dataflow abstractions；
- symbolic shape / static analysis；
- compile-time bug detection；
- write once, run across GPUs、CPUs 与 domain-specific accelerators；
- AI-assisted / agent-driven kernel development。

## 核心项目

### [[Croqtile]]

[[Croqtile]] 是目前最清晰的主项目，也是 LANCER 从 compiler research 进入现代 AI kernel DSL 的核心载体。它把 tile、warp role、pipeline、DMA/TMA、MMA 与 symbolic verification 暴露给开发者和 AI agent，并提供 autotuning / harness 配套。

### SPIDER / Samoyeds

LANCER GitHub 组织还 pin 了 SPIDER 与 Samoyeds 的 fork：

- **Samoyeds（EuroSys 2025）**：面向 MoE LLM 的 structured sparsity 与 Sparse Tensor Core 加速。
- **SPIDER（PPoPP 2026）**：把 Sparse Tensor Core 扩展到 stencil computation。

这两项不是 Croqtile 的软件依赖，因此本图谱不建立 integration 边；它们更适合作为同一研究网络在 sparse tensor core / GPU kernel 优化上的旁支证据。

## 人物桥梁

当前最值得保留的不是“联合实验室成员名单”，因为公开组织页没有给出稳定 roster，而是几条可以直接核验的 project / paper bridge：

- [[Xiaofeng Guan]]：Croqtile 高频 contributor，燧原 compiler researcher；Postiz / PresCount 作者。
- [[Enming Fan]]：Croqtile 高频 contributor；Postiz 作者。
- [[Heng Shi]]：Croqtile contributor；Postiz、Samoyeds、SPIDER 作者。
- [[Jianguo Yao]]：SJTU 教授；与 Xiaofeng Guan、Heng Shi 等在 compiler / sparse computing 方向持续合作。

因此这里不把“共同贡献同一个仓库”自动升级成同组、导师或汇报关系，只保留 project collaboration 与 paper coauthor 这类可验证关系。

## 图谱位置

LANCER 让上海交大的 AI Infra 图从原先偏 serving / OS 的 [[university/上海交通大学/IPADS|IPADS]]、NNE-Lab/LightLLM，再多出一条 **compiler → kernel DSL → accelerator engineering** 主线。

它与北大 [[TileLang]] 谱系形成很自然的技术邻接：

`PKU/MSRA → TileLang`
`SJTU/Enflame → LANCER → Croqtile`

两条线都在探索“如何让现代 GPU/accelerator kernel 更可编程”，但组织来源、compiler architecture 与 agent-facing design 重点不同。

## Sources

- https://github.com/LancerLab
- https://github.com/LancerLab/croqtile
- https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf
- https://doi.org/10.1145/3689031.3717455
- https://conf.researchr.org/room/CC-2026/hpcc-2026-venue-pyrmont
