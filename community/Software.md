# Software

AI Infra 软件与系统项目的统一入口。

这里不再人工维护另一份项目清单。完整项目目录由 `scripts/generate-software-project-index.py` 自动扫描仓库中所有 canonical `type: project` 节点生成，因此新增软件只需要维护自己的 canonical Markdown 与 `layer` / `areas` 元数据，就会自动进入总索引。

## 入口

- [全量 Software Project Index](../generated/software-project-index.md)：按技术层浏览全部 canonical project，并显示精确 layer、areas、integration 数量、人物/公司邻接数以及 Graph Explorer 深链。
- [[community|Community / Upstream 视角]]：按 GitHub / GitCode namespace、治理组织和社区浏览项目。
- [Graph Explorer](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/)：从任意项目继续查看人物、公司、学校与项目间关系。

## 按技术层浏览

- [Inference Engine](../generated/software-project-index.md#inference-engine)
- [Distributed Serving](../generated/software-project-index.md#distributed-serving)
- [Gateway / Routing](../generated/software-project-index.md#gateway)
- [KV Cache](../generated/software-project-index.md#kv-cache)
- [Storage](../generated/software-project-index.md#storage)
- [Communication / Data Movement](../generated/software-project-index.md#communication)
- [Runtime / Framework](../generated/software-project-index.md#runtime)
- [Kernel / Operator](../generated/software-project-index.md#kernel)
- [Compiler / DSL](../generated/software-project-index.md#compiler)
- [Training / Post-training](../generated/software-project-index.md#training)
- [Scheduler / Orchestration](../generated/software-project-index.md#scheduler)
- [Device / Resource](../generated/software-project-index.md#device-resource)
- [Benchmark / Profiling](../generated/software-project-index.md#benchmark)
- [Ecosystem](../generated/software-project-index.md#ecosystem)
- [Inference Optimization](../generated/software-project-index.md#optimization)

## 维护原则

`community/Software.md` 是稳定导航入口，`generated/software-project-index.md` 是自动生成的全量视图。前者不复制项目事实，后者不依赖历史迁移清单。

项目事实仍以各 canonical 项目页为唯一来源；`research/software-project-migration.json` 只负责历史 59 项迁移审计，不再决定哪些项目能进入 Software Index。
