---
type: project
name: FlagTree
status: active
linked_people:
  - "community/flagos-ai/FlagTree/Galaxy1458"
  - "community/flagos-ai/FlagTree/i3wanna2"
  - "community/flagos-ai/FlagTree/menchunlei"
  - "community/flagos-ai/FlagTree/sgjzfzzf"
  - "community/flagos-ai/FlagTree/sunnycase"
  - "community/flagos-ai/FlagTree/zhzhcookie"
  - "company/杭州先进编译科技有限公司/李嘉楠"
  - "company/杭州先进编译科技有限公司/柴赟达"
companies: ["杭州先进编译科技有限公司"]
company_relation: community-led
layer: compiler
repository: https://github.com/flagos-ai/FlagTree
areas:
  - "compiler"
  - "triton"
  - "heterogeneous-computing"
  - "multi-backend"
  - "kernel-dsl"
  - "heterogeneous-codegen"
people:
  - "community/flagos-ai/FlagTree/menchunlei"
  - "community/flagos-ai/FlagTree/zhzhcookie"
  - "community/flagos-ai/FlagTree/sunnycase"
  - "community/flagos-ai/FlagTree/i3wanna2"
  - "community/flagos-ai/FlagTree/Galaxy1458"
  - "community/flagos-ai/FlagTree/sgjzfzzf"
  - "company/杭州先进编译科技有限公司/李嘉楠"
  - "company/杭州先进编译科技有限公司/柴赟达"
integrations: []
last_verified: "2026-09"
linked_companies:
  - "company/杭州先进编译科技有限公司/杭州先进编译科技有限公司"
---
# FlagTree

## 项目简介
FlagTree 是 FlagOS 的统一多后端 AI 编译器，基于 Triton 体系向不同 AI 芯片后端扩展代码生成和优化能力。它承担“同一上层算子/框架表达如何落到多种硬件”的编译桥梁角色，与 [[FlagGems]] 的跨后端算子生态紧密相连。

## GitHub
https://github.com/flagos-ai/FlagTree

## 主要维护者 / 组织
FlagTree 官方 `MAINTAINERS.md` 明确列出 6 位项目维护者：[[community/flagos-ai/FlagTree/menchunlei|menchunlei]]、[[community/flagos-ai/FlagTree/zhzhcookie|zhzhcookie]]、[[community/flagos-ai/FlagTree/sunnycase|sunnycase]]、[[community/flagos-ai/FlagTree/i3wanna2|i3wanna2]]、[[community/flagos-ai/FlagTree/Galaxy1458|Galaxy1458]]、[[community/flagos-ai/FlagTree/sgjzfzzf|sgjzfzzf]]。

这里把官方 governance 文件中的 maintainer 身份视为强角色证据；但不会仅凭邮箱字符串继续猜测实名、学校或雇主。2025 智源大会公开教程由郑杨、杨锐林介绍 FlagTree 多后端统一编译器设计，这类公开分享本身仍不自动等同于 maintainer 身份。

外部核心贡献网络中，[[company/杭州先进编译科技有限公司/李嘉楠|李嘉楠]]被 FlagOS 官方技术文章明确称为“FlagTree 核心开发贡献者”；[[company/杭州先进编译科技有限公司/柴赟达|柴赟达]]在 2026 CNCC 公开介绍 Triton-TLE 在国产平台的适配优化。二者均来自[[company/杭州先进编译科技有限公司/先进编译实验室|先进编译实验室]]。

## TLE 路线
2026 公开资料进一步展示 Triton-TLE 的三层编程抽象：TLE-Lite、TLE-Struct、TLE-Raw。其目标是在可移植性、结构化优化信息和硬件细粒度控制之间分层取舍，并服务国产芯片“一次优化、多芯复用”。本仓库把 TLE 视为 FlagTree 的 compiler-language / programming-abstraction 子层，而不重复制造一个缺乏独立治理证据的项目节点。

## 生态关系
[[FlagOS]] · [[FlagGems]] · [[FlagAttention]] · [[FlagScale]] · [[company/杭州先进编译科技有限公司/先进编译实验室|先进编译实验室]]。在推理链路上，FlagTree 位于上层框架与多种芯片 codegen/runtime 之间。

## Sources
- https://github.com/flagos-ai/FlagTree
- https://github.com/flagos-ai/FlagTree/blob/main/MAINTAINERS.md
- https://hub.baai.ac.cn/view/46246
- https://hub.baai.ac.cn/view/57117
- https://flagos.csdn.net/684f83da870cef7360648130.html
- https://www.ccf.org.cn/Media_list/cncc/2026-09-09/931233.shtml

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/flagos-ai/FlagTree/Galaxy1458|Galaxy1458]]：https://github.com/flagos-ai/FlagTree/blob/main/MAINTAINERS.md
- [[community/flagos-ai/FlagTree/i3wanna2|i3wanna2]]：https://github.com/flagos-ai/FlagTree/blob/main/MAINTAINERS.md
- [[community/flagos-ai/FlagTree/menchunlei|menchunlei]]：https://github.com/flagos-ai/FlagTree/blob/main/MAINTAINERS.md
- [[community/flagos-ai/FlagTree/sgjzfzzf|sgjzfzzf]]：https://github.com/flagos-ai/FlagTree/blob/main/MAINTAINERS.md
- [[community/flagos-ai/FlagTree/sunnycase|sunnycase]]：https://github.com/flagos-ai/FlagTree/blob/main/MAINTAINERS.md
- [[community/flagos-ai/FlagTree/zhzhcookie|zhzhcookie]]：https://github.com/flagos-ai/FlagTree/blob/main/MAINTAINERS.md
- [[company/杭州先进编译科技有限公司/李嘉楠|李嘉楠（Jianan Li）]]：2025 FlagOS 技术文章明确写明：李嘉楠来自[[先进编译实验室]]，是 [[community/flagos-ai/FlagTree/FlagTree|FlagTree]] 核心开发贡献者。
- [[company/杭州先进编译科技有限公司/柴赟达|柴赟达（Yunda Chai）]]：[[community/flagos-ai/FlagTree/FlagTree|FlagTree]] / TLE：2026 CNCC 报告题目为“AI编译优化：Triton-tle在国产平台上的适配优化”，直接连接 TLE-Lite / TLE-Struct / TLE-Raw 路线。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/杭州先进编译科技有限公司/杭州先进编译科技有限公司|杭州先进编译科技有限公司]]：公司页与社区/项目页均有显式记录；关系：`community-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
