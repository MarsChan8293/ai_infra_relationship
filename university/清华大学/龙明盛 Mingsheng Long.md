---
type: person
name: 龙明盛
english_name: Mingsheng Long
aliases: ["龙明盛", "Mingsheng Long"]
current_affiliations: ["Tsinghua University"]
schools:
  - "清华大学"
projects: [Jenga]
areas: [machine-learning, foundation-models, compiler-tooling]
roles: ["Tenured Associate Professor", "Machine Learning Group Lead"]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"community/vllm-project/vLLM/游凯超 Kaichao You","type":["student","paper-coauthor"],"confidence":"high","evidence":["https://ise.thss.tsinghua.edu.cn/~mlong/","https://youkaichao.github.io/research","https://www.thss.tsinghua.edu.cn/info/1131/1765.htm"]}'
---
# 龙明盛（Mingsheng Long）

清华大学软件学院长聘副教授、机器学习课题组负责人。其主体研究方向是 machine learning、foundation models 与 transfer learning，并非传统意义上的 AI Infra faculty；但在本图谱中，他通过学生与系统论文形成一条重要的清华 → vLLM / Inferact 人才桥。

## 人物关系
- [[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超（Kaichao You）]]：**博士导师 / 学生 + 长期论文合作**。龙明盛官方主页将 Kaichao You 列为 2020–2025 博士生，毕业去向为 Inferact 联合创始人；游凯超公开资料也明确写其清华博士导师为 Mingsheng Long。

## AI Infra 关系
- [[community/vllm-project/Jenga/Jenga|Jenga]]：SOSP 2025 作者，与游凯超、翟季冬及 Berkeley / vLLM 作者网络共同署名。
- depyf：与游凯超等共同开发/发表用于打开 PyTorch compiler 黑盒的工具，连接机器学习研究与 `torch.compile` / compiler tooling。

## 图谱意义
这条边补齐了另一条不同于 PACMAN 的清华推理人才谱系：`龙明盛 → 游凯超 → vLLM → Inferact`；它与 `翟季冬 → Chen Zhang → Jenga → vLLM` 在 Jenga / vLLM 处汇合，但不应混为同一实验室谱系。

## 学校关联
- [[university/清华大学/清华大学|清华大学]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources
- https://ise.thss.tsinghua.edu.cn/~mlong/
- https://www.thss.tsinghua.edu.cn/info/1131/1765.htm
- https://youkaichao.github.io/research
- https://arxiv.org/abs/2503.18292
