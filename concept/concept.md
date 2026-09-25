# concept

AI Infra 技术概念的一级入口。这里回答的是“技术机制是什么、为什么存在、和哪些概念/项目相连”，不复制软件项目页的产品介绍。

## 入口

- [Concept Index](../generated/concept-index.md)：由 `scripts/generate-concept-index.py` 自动扫描所有 canonical `type: concept` 节点生成。
- [Project ↔ Concept Coverage](../generated/project-concept-coverage.md)：检查 Concept 的项目证据、Project 反向链接与当前 ontology 覆盖密度。
- [[community/Software|Software]]：从“实现/项目”视角浏览 AI Infra。
- [Graph Explorer](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/)：从概念继续查看项目、人物、公司、学校和相邻概念。

## 组织原则

Concept 与 Project 分工明确：

- **Concept = mechanism**：例如 KV Cache Offloading、Speculative Decoding、Tensor Parallelism。
- **Project = implementation**：例如 vLLM、SGLang、LMCache、Mooncake。
- 缩写、中文译名、旧称放在 `aliases`，不重复创建 canonical 节点。
- 父子关系只表达真正的技术细分；“经常一起出现”放 `related_concepts`。
- 概念与项目的连接必须能在正文中说明证据，不因共同标签自动推断。
- Concept 的 `projects:` 是直接实现/暴露该机制的唯一人工事实源；Project 页的 `linked_concepts` 由脚本反向生成。
- `projects:` 会派生 `project-concept-support` typed edge。仅“相关/集成”不得伪装成直接支持，语义上与 `project-concept-integration` 分离。

## 当前覆盖范围

Ontology 已覆盖 KV Cache、Serving/P-D、Speculative Decoding、Parallelism、Scheduling/Routing、Communication/Data Movement、Kernel/Operator、Quantization、Memory Hierarchy、Compiler Pipeline、Storage 与 Hardware Interconnect 等主要 AI Infra 技术域。后续扩展以现有项目证据密度和实际研究需求驱动，而不是机械追求“概念大全”。
