---
type: research-institution
name: KEG
organization: 清华大学
aliases: ["Knowledge Engineering Group", "Tsinghua KEG", "清华大学知识工程实验室"]
linked_people: []
areas: [foundation-models, pretraining, knowledge-graphs, agents, code-models]
projects: [GLM-130B, CodeGeeX]
website: https://keg.cs.tsinghua.edu.cn/
last_verified: "2026-09"
---
# KEG（Knowledge Engineering Group）

## 机构定位
KEG 是清华大学计算机系知识工程研究团队。对本图谱而言，KEG 的价值不是传统知识图谱本身，而是它从知识工程 / data mining 逐步进入大模型预训练，并形成 GLM、GLM-130B、ChatGLM、CodeGeeX 等模型技术谱系。

## AI Infra 交叉点
- [[university/清华大学/GLM-130B|GLM-130B]]：2021 年底在 KEG 内部构思，2022 年完成 130B 双语稠密模型预训练。项目官方材料明确记录 PACMAN 参与解决大规模训练中的 3D pipeline、显存、硬件故障、异构平台适配等系统问题。
- FastMoE：2021 年由 PACMAN 的何家傲 / 翟季冬与 KEG / GLM 网络的 Jiezhong Qiu、曾奥涵、杨植麟、唐杰共同署名，是 KEG ↔ PACMAN 更早的一条 MoE system co-design 强边。
- [[company/智谱/智谱|智谱]]：GLM 技术产业化主线。唐杰、曾奥涵、杜政晓、郑勤锴等连接 KEG 与后续 GLM 产品 / 工程组织。
- [[company/月之暗面/杨植麟 Zhilin Yang|杨植麟]]：唐杰早期学生、原始 GLM 论文作者，后来创办月之暗面，因此形成 KEG → GLM → Kimi 的人才桥，但不把月之暗面误标为 KEG 产业实体。

## 核心人物
- [[company/智谱/唐杰 Jie Tang|唐杰（Jie Tang）]]：KEG 教授，GLM-130B 项目总负责人。
- [[company/智谱/曾奥涵 Aohan Zeng|曾奥涵（Aohan Zeng）]]：GLM-130B 学生负责人 / Lead Contributor。
- [[company/智谱/杜政晓 Zhengxiao Du|杜政晓（Zhengxiao Du）]]：原始 GLM / GLM-130B 关键作者，博士导师为唐杰。
- [[company/智谱/郑勤锴 Qinkai Zheng|郑勤锴（Qinkai Zheng）]]：GLM-130B contributor、CodeGeeX 学生负责人。

## 关系边界
KEG 更接近 model / algorithm / data 侧，不应与 [[university/清华大学/MADSys|MADSys]] 或 [[university/清华大学/PACMAN|PACMAN]] 合并成笼统“清华系”。强边只在共同论文、项目贡献或明确导师关系下建立。

## Sources
- https://keg.cs.tsinghua.edu.cn/jietang/
- https://keg.cs.tsinghua.edu.cn/glm-130b/zh/posts/glm-130b/
- https://keg.cs.tsinghua.edu.cn/codegeex/index_zh.html
