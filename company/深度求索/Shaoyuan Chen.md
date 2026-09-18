---
type: person
name: Shaoyuan Chen
aliases: ["Shaoyuan Chen"]
current_affiliations: ["深度求索"]
schools:
  - "清华大学"
linked_companies:
  - "company/深度求索/深度求索"
projects: [KTransformers, DualPath, DeepSpec, EPLB]
areas: [llm-inference, heterogeneous-inference, kv-cache, speculative-decoding, distributed-systems]
confidence: high
last_verified: "2026-09"
relations:
  - '{"target":"university/清华大学/Mingxing Zhang","type":["paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://sigops.org/s/conferences/sosp/2025/accepted.html","https://conferences.sigcomm.org/sigcomm/2026/accepted/"]}'
  - '{"target":"company/深度求索/梁文锋 Liang Wenfeng","type":["paper-coauthor"],"project":"DeepSpec","confidence":"high","evidence":["https://github.com/deepseek-ai/DeepSpec"]}'
---
# Shaoyuan Chen

清华大学 MADSys 系统研究网络出身、后进入 [[company/深度求索/深度求索|深度求索]] 的 AI Infra 研究人员，是章明星研究网络向 DeepSeek inference systems 扩散的一条关键人才边。

## 教育与去向
- [[university/清华大学/清华大学|清华大学]] / MADSys：2026 年博士毕业。MADSys alumni 页面公开列出的第一份工作为 Hangzhou DeepSeek Artificial Intelligence Co., Ltd。
- [[company/深度求索/深度求索|深度求索]]：SIGCOMM 2026 DualPath 作者单位同时列出 Tsinghua University 与 DeepSeek-AI，和 MADSys alumni 去向互相印证。

## AI Infra 关系
- [[community/kvcache-ai/KTransformers/KTransformers|KTransformers]]：SOSP 2025 论文作者，与 [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]] 共同研究 CPU/GPU hybrid MoE inference。
- [[community/deepseek-ai/DualPath/DualPath|DualPath]]：SIGCOMM 2026 作者；项目聚焦 agentic LLM inference 中 disaggregated KV-cache storage I/O，并再次与章明星共同署名。
- [[community/deepseek-ai/DeepSpec/DeepSpec|DeepSpec]] / DSpark：2026 DSpark 作者网络成员，进入 DeepSeek speculative decoding 全栈研究线；与 [[company/深度求索/梁文锋 Liang Wenfeng|梁文锋（Wenfeng Liang）]] 同属论文作者网络。\n- [[community/deepseek-ai/DeepSeek-Infra/EPLB|EPLB]]：2025-02 初始提交公开 author；记录 project contribution，不自动等价为长期 maintainer。

## 图谱意义
Shaoyuan Chen 把 `MADSys → KTransformers` 这条清华异构推理技术线直接连接到 `DeepSeek → DualPath / DeepSpec`。相比仅按“同实验室”扩图，这里同时有毕业去向、顶会论文和项目作者三类公开证据支撑。

## Sources
- https://madsys.cs.tsinghua.edu.cn/people/
- https://madsys.cs.tsinghua.edu.cn/author/shaoyuan-chen/
- https://sigops.org/s/conferences/sosp/2025/accepted.html
- https://conferences.sigcomm.org/sigcomm/2026/accepted/
- https://github.com/deepseek-ai/DeepSpec\n- https://github.com/deepseek-ai/EPLB/commit/f9bc62e84182eee311ec97c3ec3ce38f5073a646

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/深度求索/深度求索|深度求索]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
