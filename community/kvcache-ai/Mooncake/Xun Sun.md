---
type: person
name: Xun Sun
aliases: ["UNIDY2002", "@UNIDY2002"]
current_affiliations: ["Tsinghua University"]
schools:
  - "清华大学"
communities: [Mooncake, SGLang]
projects: [Mooncake]
roles: [Mooncake Maintainer, Mooncake EP Codeowner, Mooncake PG Codeowner]
areas: [expert-parallelism, distributed-communication, llm-inference, fault-tolerance, data-movement]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"university/清华大学/Mingxing Zhang","type":["advisor"],"confidence":"high","evidence":["https://github.com/UNIDY2002"]}'
---
# Xun Sun

GitHub：`@UNIDY2002`

## 身份与研究背景
- 清华大学 MADSys 成员。其公开 GitHub 主页明确写明由 [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]] 指导，因此记录为高置信度导师/学生强边。
- Mooncake maintainer；当前 `CODEOWNERS` 将 `@UNIDY2002` 列为 Mooncake EP、Mooncake PG 以及相关 Python EP 路径的 codeowner。
- 研究和工程重点集中在 expert parallelism、PyTorch process group、GPU/设备侧通信以及弹性故障恢复。

## Mooncake / SGLang
2026 年 Elastic EP 工作中，Xun Sun 是论文第一作者之一，并被 SGLang 官方文章列在 Mooncake Team。该工作将 Mooncake EP/PG 接入 SGLang，在 wide-EP MoE serving 中实现 partial-rank failure tolerance。

Mooncake 2026 年的 PG RFC 也由其发起，目标包括 device-API-based collectives、NVLink 热路径和更可扩展的 collective framework。

## 人物关系
- [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]：**导师 / 学生强边**；Xun Sun 个人主页明确写明 advised by Mingxing Zhang。
- [[community/kvcache-ai/Mooncake/任峰 Feng Ren|任峰（Feng Ren）]]：共同处于 Mooncake 数据移动 / EP 系统网络；Elastic EP 工作共同作者。
- [[community/kvcache-ai/Mooncake/Shangming Cai|Shangming Cai]]：Mooncake / SGLang 集成协作者；Elastic EP 共同作者。
- [[community/kvcache-ai/Mooncake/Ke Yang|Ke Yang]]：Elastic EP 共同作者，连接 Mooncake Store 与 EP/PG 子系统。

## 学校关联
- [[university/清华大学/清华大学|清华大学]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources
- https://github.com/UNIDY2002
- https://github.com/kvcache-ai/Mooncake/blob/main/.github/CODEOWNERS
- https://github.com/kvcache-ai/Mooncake/issues/2716
- https://www.lmsys.org/blog/2026-03-25-eep-partial-failure-tolerance
- https://arxiv.org/abs/2605.10670
