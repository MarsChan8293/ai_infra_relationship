# concept

AI Infra 技术概念的一级入口。这里回答的是“技术机制是什么、为什么存在、和哪些概念/项目相连”，不复制软件项目页的产品介绍。

## 入口

- [Concept Index](../generated/concept-index.md)：由 `scripts/generate-concept-index.py` 自动扫描所有 canonical `type: concept` 节点生成。
- [[community/Software|Software]]：从“实现/项目”视角浏览 AI Infra。
- [Graph Explorer](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/)：从概念继续查看项目、人物、公司、学校和相邻概念。

## 组织原则

Concept 与 Project 分工明确：

- **Concept = mechanism**：例如 KV Cache Offloading、Speculative Decoding、Tensor Parallelism。
- **Project = implementation**：例如 vLLM、SGLang、LMCache、Mooncake。
- 缩写、中文译名、旧称放在 `aliases`，不重复创建 canonical 节点。
- 父子关系只表达真正的技术细分；“经常一起出现”放 `related_concepts`。
- 概念与项目的连接必须能在正文中说明证据，不因共同标签自动推断。

## 首轮建设范围

第一阶段优先建设四条 inference 主线：

1. KV Cache / Memory
2. Serving / P-D Disaggregation
3. Decoding / Speculative Decoding
4. Parallelism / TP-EP-DP-PP

完整批次和验收规则见 [Concept Ontology 分批实施计划](https://github.com/MarsChan8293/ai_infra_relationship/blob/main/docs/concept-ontology-plan.md)。
