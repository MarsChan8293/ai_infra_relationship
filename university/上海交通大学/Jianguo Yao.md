---
type: person
name: Jianguo Yao
aliases:
  - "姚建国"
current_affiliations:
  - "上海交通大学"
  - "燧原科技"
public_email: jianguo.yao@sjtu.edu.cn
schools:
  - "上海交通大学"
projects:
  - "Samoyeds"
  - "SPIDER"
areas:
  - "ai-chips"
  - "intelligent-computing-systems"
  - "compilers"
  - "gpu-kernels"
  - "sparse-tensor-cores"
roles:
  - "Distinguished Professor"
confidence: high
last_verified: "2026-09"
relations:
  - '{"target":"university/上海交通大学/Xiaofeng Guan","type":["paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://tcloud.sjtu.edu.cn/pdf/CGO_2024_PresCount.pdf","https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf"]}'
  - '{"target":"university/上海交通大学/Enming Fan","type":["paper-coauthor"],"confidence":"high","evidence":["https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf"]}'
  - '{"target":"university/上海交通大学/Heng Shi","type":["paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf","https://doi.org/10.1145/3689031.3717455","https://conf.researchr.org/room/CC-2026/hpcc-2026-venue-pyrmont"]}'
---
# 姚建国（Jianguo Yao）

姚建国是 [[上海交通大学]] 计算机学院特聘教授，公开研究方向包括 AI chips / intelligent computing systems、virtualization 与 cloud systems。

在这次 Croqtile 扩图里，他不是因为“直接提交 Croqtile”而进入，而是因为他把 LANCER 周边的 compiler、sparse tensor core 与 SJTU 学术网络连接成了一条连续研究链。

## Compiler / sparse computing 合作

- **PresCount（CGO 2024）**：与 [[Xiaofeng Guan]] 等合作，研究 register allocation / bank conflict reduction。
- **Postiz（CGO 2025）**：与 Xiaofeng Guan、[[Enming Fan]]、[[Heng Shi]] 等合作，研究 post-increment addressing / loop optimization。
- **Samoyeds（EuroSys 2025）**：与 Heng Shi、Chenpeng Wu、Qiqi Gu、Haibing Guan 合作，面向 MoE structured sparsity / Sparse Tensor Core。
- **SPIDER（PPoPP 2026）**：与 Qiqi Gu、Chenpeng Wu、Heng Shi 合作，把 Sparse Tensor Core 用于 stencil computation。

## 与 Croqtile 的边界

目前没有找到足够直接的公开 evidence 证明姚建国是 Croqtile maintainer / contributor，因此本页 **不写 `projects: [Croqtile]`**。

他的价值是研究网络桥梁：`compiler backend optimization → sparse tensor core → AI kernel DSL ecosystem`。这条弱一层但证据更干净的边，比硬塞一个项目归属更适合关系图谱。

## Affiliation

上海交大官方教师主页记录其自 2012 年起在 SJTU 任教，现为特聘教授；公开会议 profile 同时列出 Shanghai Jiao Tong University 与 Shanghai Enflame Technology affiliation。

## Sources

- https://www.cs.sjtu.edu.cn/en/jiaoshiml/yaojianguo.html
- https://conf.researchr.org/profile/jianguoyao
- https://tcloud.sjtu.edu.cn/pdf/CGO_2024_PresCount.pdf
- https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf
- https://doi.org/10.1145/3689031.3717455
- https://conf.researchr.org/room/CC-2026/hpcc-2026-venue-pyrmont
