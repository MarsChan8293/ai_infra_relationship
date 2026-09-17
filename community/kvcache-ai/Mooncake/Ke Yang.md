---
type: person
name: Ke Yang
aliases: ["ykwd", "@ykwd"]
current_affiliations: ["趋境科技"]
communities: [Mooncake]
linked_companies:
  - "company/趋境科技/趋境科技"
projects: [Mooncake, TENT]
roles: [Mooncake Codeowner, Mooncake Store Owner]
areas: [kv-cache, distributed-storage, llm-inference, disaggregated-serving, data-movement]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/趋境科技/武永卫 Yongwei Wu","type":["coworker","paper-coauthor","research-collaboration"],"company":"趋境科技","project":"TENT","confidence":"high","evidence":["https://madsys.cs.tsinghua.edu.cn/publication/","https://github.com/kvcache-ai/Mooncake/blob/main/MAINTAINERS.md"]}'
  - '{"target":"community/kvcache-ai/Mooncake/任峰 Feng Ren","type":["open-source-collaboration","coworker"],"project":"Mooncake","company":"趋境科技","confidence":"high","evidence":["https://libfeng.com/","https://github.com/kvcache-ai/Mooncake/blob/main/MAINTAINERS.md"]}'
---
# Ke Yang

社区：[[Mooncake]]
当前关联：[[趋境科技]]

## 工作经历
- [[趋境科技]]：Mooncake 官方 `MAINTAINERS.md` 将 `@ykwd` 标注为 Approaching AI，并使用 `yangke@approaching.ai` 联系邮箱；这里据此记录当前 affiliation，不从邮箱扩展任何职级。

## Mooncake 角色
- 官方 Codeowner
- 重点负责 Mooncake Store
- 2026 [[TENT]] 论文作者之一，连接 KV cache storage 与新一代异构数据移动层

## 与武永卫 / MADSys 的关系
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]：**TENT 论文合作 + Approaching.AI 同公司网络**。Ke Yang 是 MADSys 2022 Ph.D. alumni；2025 TENT 论文与武永卫共同署名，技术上把早期 graph / storage locality 研究进一步迁移到 disaggregated LLM serving 的 Store 与 data movement。当前公开资料不足以确认正式导师关系，因此不建立 advisor/student 边。

## 人物关系
- [[community/kvcache-ai/Mooncake/任峰 Feng Ren|任峰（Feng Ren）]]：**Approaching.AI / Mooncake 核心维护协作者**。任峰个人主页明确标注 2026–至今为 Approaching AI Technical Expert、此前 2023–2026 为 9#AISoft；Mooncake MAINTAINERS 当前仍显示任峰为 9#AISoft，说明治理文件的公司标签可能存在时间滞后。两人在 Mooncake 中分别覆盖 Transfer Engine 与 Store。
- [[community/kvcache-ai/Mooncake/马腾 Teng Ma|马腾（Teng Ma）]]：**Mooncake 共同维护者，分属不同公司**。截至 2026-09 两人同列 Mooncake 官方 Codeowners；马腾偏社区/生态与 Alibaba Cloud 侧协作，Ke Yang 负责 Store。
- [[community/kvcache-ai/Mooncake/Shangming Cai|Shangming Cai]]：**Mooncake 共同维护者 / Store ↔ SGLang integration 协作**。截至 2026-09 两人同列官方 Codeowners；Shangming Cai 负责 SGLang Integration，Ke Yang 负责 Mooncake Store。
- [[company/趋境科技/艾智远 Zhiyuan Ai|艾智远（Zhiyuan Ai）]]：**Approaching.AI 同事 / 创业团队网络**。艾智远任公司创始人 CEO；不推断直属汇报关系。
- [[company/趋境科技/卢佳豪 Jiahao Lu|卢佳豪（Jiahao Lu）]]：**Approaching.AI + Mooncake 工程协作者**。2026 vLLM × Mooncake Store 官方致谢将 Jiahao Lu 与 Ke Yang 等列为 Approaching.AI 技术反馈贡献者。

## 工程协作
2026 vLLM Mooncake Store 集成官方致谢明确列出 Jiahao Lu、Zuoyuan Zhang、Zihan Tang、Ke Yang 为 Approaching.AI 技术反馈贡献者，形成 Approaching.AI ↔ Mooncake ↔ vLLM 的直接工程桥。

## Sources
- https://github.com/kvcache-ai/Mooncake/blob/main/MAINTAINERS.md
- https://madsys.cs.tsinghua.edu.cn/
- https://madsys.cs.tsinghua.edu.cn/publication/
- https://arxiv.org/abs/2604.00368
- https://vllm.ai/blog/2026-05-06-mooncake-store
- https://github.com/kvcache-ai/Mooncake

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/趋境科技/趋境科技|趋境科技]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
