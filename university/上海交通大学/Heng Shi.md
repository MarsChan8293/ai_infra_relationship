---
type: person
name: Heng Shi
aliases:
  - "SyntaxArchmage"
current_affiliations: ["燧原科技"]
public_email: heng.shi@sjtu.edu.cn
schools:
  - "上海交通大学"
linked_companies:
  - "company/燧原科技/燧原科技"
projects:
  - "Croqtile"
  - "Samoyeds"
  - "SPIDER"
areas:
  - "ai-compilers"
  - "gpu-kernels"
  - "sparse-tensor-cores"
  - "moe"
  - "structured-sparsity"
confidence: high
last_verified: "2026-09"
relations:
  - '{"target":"university/上海交通大学/Xiaofeng Guan","type":["paper-coauthor"],"confidence":"high","evidence":["https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf"]}'
  - '{"target":"university/上海交通大学/Enming Fan","type":["paper-coauthor"],"confidence":"high","evidence":["https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf"]}'
  - '{"target":"university/上海交通大学/Jianguo Yao","type":["paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf","https://doi.org/10.1145/3689031.3717455","https://conf.researchr.org/room/CC-2026/hpcc-2026-venue-pyrmont"]}'
---
# Heng Shi

Heng Shi 是把 [[Croqtile]] 与 SJTU / 燧原 sparse computing 研究线连接起来的关键人物。

## Croqtile

Croqtile 近期 commit history 中可见 Heng Shi 的直接贡献；官方 README 还把 browser-based playground 指向 GitHub `SyntaxArchmage/croqtile-playground`，而 Croqtile commit identity 也把 `SyntaxArchmage` 对应到 Heng Shi。

因此 `SyntaxArchmage` 在这里作为可核验 GitHub alias 记录。

## Compiler / sparse kernel 谱系

Heng Shi 同时出现在多条连续工作中：

- **Postiz（CGO 2025）**：compiler loop / addressing optimization；
- **Samoyeds（EuroSys 2025）**：MoE structured sparsity 与 Sparse Tensor Core；
- **SPIDER（PPoPP 2026）**：Sparse Tensor Core for stencil computation；
- **Croqtile（2026）**：AI-native kernel DSL / compiler。

这组工作覆盖 compiler transformation、AI kernel、structured sparsity 与 low-level accelerator execution，使其成为本仓库“推理优化人才”视角下比单纯项目 maintainer 更值得追踪的 bridge node。

## Affiliation

- CGO 2025 官方资料将 Heng Shi 标注为 Enflame Tech。
- Samoyeds 论文同时列出 Shanghai Enflame Technology 与 Shanghai Jiao Tong University，并公开 `heng.shi@sjtu.edu.cn`。

本页用 `current_affiliations: [燧原科技]` 记录当前公开职业侧强证据，用 `schools: [上海交通大学]` 表示学术/研究关联，不把它擅自解释为学位或教职。

## 人物关系

- [[Jianguo Yao]]：Postiz、Samoyeds、SPIDER 多次论文合作。
- [[Xiaofeng Guan]]、[[Enming Fan]]：Postiz 共著，并在 Croqtile/LANCER 周边 compiler network 相交。


## 学校关联
- [[university/上海交通大学/上海交通大学|上海交通大学]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources

- https://github.com/SyntaxArchmage
- https://github.com/LancerLab/croqtile
- https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf
- https://doi.org/10.1145/3689031.3717455
- https://conf.researchr.org/profile/hengshi
- https://conf.researchr.org/room/CC-2026/hpcc-2026-venue-pyrmont

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/燧原科技/燧原科技|燧原科技]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
