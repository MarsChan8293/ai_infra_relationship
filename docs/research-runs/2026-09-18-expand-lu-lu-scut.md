# 2026-09-18 EXPAND 陆璐教授

## Operator

- operator: `EXPAND`
- seed: `陆璐（华南理工大学）`
- objective: 从人物节点扩展 AI Infra 系统路线、国产异构算力、产业转化与高价值机构连接。

## Identity resolution

本轮确认目标是 **华南理工大学计算机科学与工程学院陆璐教授**，不是 Yale 的同名 Lu Lu。

公开来源显示其研究 / 工程方向包括软件体系与架构、软件可靠性、高性能计算、异构并行加速，并有华南理工、鹏城实验室、AMD 历史经历和爱特思成果转化网络。

## Added canonical nodes

- `university/华南理工大学/陆璐 Lu Lu`
- `university/华南理工大学/异构计算平台并行加速解决方案`
- `company/超聚变/超聚变`
- `company/爱特思/深圳爱特思信息技术有限公司`
- `company/爱特思/国产化人工智能算力平台异构并行加速项目`

## Strengthened existing nodes

- `university/华南理工大学/华南理工大学`
- `university/鹏城实验室/鹏城实验室`
- `company/AMD/AMD`

## High-value bridges

### 陆璐 → 华工 × 超聚变 → openEuler / FusionOS

2023–2024 公开材料明确记录华南理工陆璐团队与超聚变在异构加速领域联合创新，覆盖 openEuler / FusionOS、AI 模型部署、算子迁移、BLAS / FFT、HPL-AI 与多卡多节点通信。

### 异构平台 → Kunpeng + Ascend

华南理工案例明确写出“鲲鹏 + 昇腾”异构平台，因此这是 SCUT 学术系统团队到 Ascend 硬件生态的一条直接工程边。

### 陆璐 → 深圳爱特思 → 国产 AI 算力优化

2025–2026 公开资料仍显示陆璐为深圳爱特思创始人 / 法定代表人。该公司作为其异构算力优化成果转化平台，当前仍招聘算子开发与并行加速工程岗位。

### 爱特思 → Ascend 910 operator optimization

专利 CN117851738A 由深圳爱特思申请，发明人陆璐、钟昊阳，明确针对华为昇腾 910 NPU 的 complex GEMV 做任务划分、vector unit、memory movement 与并行优化。

### 陆璐 → AMD

2013 年中国科大超算中心公开活动将陆璐列为 AMD 应用解决方案部门软件架构师、华南理工教授。这条历史职业关系解释了其长期 GPU / OpenCL / heterogeneous computing 技术轨迹。

### 陆璐 → 鹏城实验室

2025 年公开会议资料仍列其为“深圳鹏城国家实验室双聘教授”。由于未找到 2026 年机构名录确认，本轮保留为带时间戳强关系，不写入人物 `current_affiliations`。

## Evidence boundaries

- “使用 Ascend / Kunpeng”不等于参与 Huawei / CANN 官方治理。
- “依托 openEuler”不等于 openEuler maintainer。
- 超聚变与陆璐是公开技术合作，不推断雇佣。
- 深圳爱特思是当前公开的成果转化与公司关联，但不把其所有专利自动视为华南理工学校项目。
- 鹏城实验室 affiliation 有 2025 公开证据，但未强推为 2026 current affiliation。

## Follow-up

1. VERIFY 爱特思的公开代码仓库、kernel library、benchmark 或 operator package。
2. EXPAND 爱特思专利 / 工程人员网络，优先钟昊阳及 Ascend 910 / Atlas operator work。
3. DISCOVER 陆璐团队参与 openEuler 的具体 SIG、PR、maintainer 或 repo 贡献，区分“生态参与”与“代码维护”。
4. VERIFY 超聚变 × 华工联合方案是否已有 FusionOS 26 / 新一代 Ascend 平台更新。
5. EXPAND AMD 历史合作线，确认陆璐在 AMD 的具体时间段和 HSA/OpenCL 项目参与范围。

## Primary sources

- https://www.ccf.org.cn/Chapters/TC/11_list/TCSE/
- https://www.xfusion.com/minisite/cn/xfusion-explorer-summit2025
- https://www.openeuler.org/zh/showcase/education/huanan/
- https://www.xfusion.com/cn/news/fusionos-openeuler-summit-2023
- https://scc.ustc.edu.cn/pxxx/201307/t20130720_155061.html
- https://job.zust.edu.cn/positionDetail/2851114f08284a1ab9fa4b872482f94c
- https://www.pazhoulab.com/2025/10/7091/
- https://patents.google.com/patent/CN117851738A/zh
