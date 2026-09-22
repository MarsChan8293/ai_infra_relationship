---
type: person
name: Enming Fan
aliases:
  - "fanenming"
  - "fanenmingsh"
current_affiliations:
  - "燧原科技"
public_email: morgan.fan@enflame-tech.com
projects:
  - "Croqtile"
areas:
  - "compilers"
  - "gpu-kernels"
  - "loop-optimization"
  - "code-generation"
confidence: high
last_verified: "2026-09"
relations:
  - '{"target":"university/上海交通大学/Xiaofeng Guan","type":["paper-coauthor"],"confidence":"high","evidence":["https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf"]}'
  - '{"target":"university/上海交通大学/Heng Shi","type":["paper-coauthor"],"confidence":"high","evidence":["https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf"]}'
  - '{"target":"university/上海交通大学/Jianguo Yao","type":["paper-coauthor"],"confidence":"high","evidence":["https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf"]}'
---
# Enming Fan

Enming Fan 是 [[Croqtile]] 2026 年近期非常活跃的 compiler contributor，也是 Postiz（CGO 2025）作者之一。

## Croqtile

公开 commit history 中，GitHub 身份 `fanenmingsh` / author name `fanenming` 参与了大量 compiler correctness、buffer / memory analysis、reduction lowering、resource facts 等工作。

近期代表改动包括：

- buffer sum reduction 的 validation / specialization；
- runtime-shaped local buffer array；
- compiler facts / static workflow report；
- DMA、alias、memory/resource 相关检查与 lowering。

这些提交使他成为理解 Croqtile“compiler as agent feedback loop”实现细节的重要工程节点。

## Postiz

Postiz（CGO 2025）论文中 Enming Fan 为作者，公开 affiliation 为 Shanghai Enflame Technology，公开邮箱为 `morgan.fan@enflame-tech.com`。该工作关注 post-increment addressing 与 loop optimization，显示其研究背景与 Croqtile compiler implementation 之间存在很自然的技术连续性。

## 人物关系

与 [[Xiaofeng Guan]]、[[Heng Shi]]、[[Jianguo Yao]] 的关系在本图谱中只标记为 **paper coauthor**，不从共同论文或共同仓库自动推断同组、上下级或长期同事关系。

## Sources

- https://github.com/fanenmingsh
- https://github.com/LancerLab/croqtile
- https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf
- https://conf.researchr.org/track/cgo-2025/cgo-2025-papers
