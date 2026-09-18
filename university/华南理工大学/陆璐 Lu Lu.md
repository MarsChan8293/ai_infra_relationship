---
type: person
name: 陆璐
english_name: Lu Lu
aliases: ["Lu Lu", "陆璐"]
current_affiliations:
  - "华南理工大学"
  - "深圳爱特思信息技术有限公司"
public_email: lul@scut.edu.cn
schools:
  - "华南理工大学"
projects:
  - "异构计算平台并行加速解决方案"
  - "国产化人工智能算力平台异构并行加速项目"
areas: [heterogeneous-compute, hpc, operator-optimization, ai-compute, ascend, kunpeng, open-source-os, multi-node-communication, model-deployment]
roles: [Professor, Founder]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/AMD/AMD","type":["career-connection"],"confidence":"high","evidence":["https://scc.ustc.edu.cn/pxxx/201307/t20130720_155061.html"]}'
  - '{"target":"company/超聚变/超聚变","type":["technical-collaboration"],"project":"异构计算平台并行加速解决方案","confidence":"high","evidence":["https://www.xfusion.com/cn/news/fusionos-openeuler-summit-2023","https://www.openeuler.org/zh/showcase/education/huanan/"]}'
---
# 陆璐（Lu Lu）

陆璐是华南理工大学计算机科学与工程学院教授、博士生导师。其公开研究与工程工作横跨软件体系结构、软件可靠性、高性能计算、异构并行加速和国产 AI 算力优化。

2025 年超聚变探索者大会公开嘉宾信息同时列出其为华南理工大学教授、深圳鹏城国家实验室双聘教授、[[company/爱特思/深圳爱特思信息技术有限公司|深圳爱特思信息技术有限公司]]创始人。

## AI Infra 主线

### 鲲鹏 + 昇腾 + openEuler + FusionOS

陆璐团队与 [[company/超聚变/超聚变|超聚变]] 联合建设 [[university/华南理工大学/异构计算平台并行加速解决方案|异构计算平台并行加速解决方案]]。公开案例明确覆盖：

- 鲲鹏 + 昇腾异构平台搭建；
- AI 模型部署与算子迁移；
- GEMM / BLAS / FFT 等核心算子优化；
- HPL / HPL-AI benchmark；
- 多卡、多节点通信优化；
- 从国外计算生态向 openEuler / FusionOS 国产计算平台迁移。

这条线和本仓库已有的 Ascend / CANN / vLLM-Ascend 等软件生态不同：陆璐团队更偏 **底层算子、异构 HPC、系统迁移与平台性能优化**。

### 爱特思：研究成果转化

[[company/爱特思/深圳爱特思信息技术有限公司|深圳爱特思信息技术有限公司]]公开被描述为陆璐教授异构计算算力平台优化成果的转化平台，业务包括：

- 算力资源仿真与评估；
- 核心算子库研发、设计与优化；
- 异构平台性能优化；
- 算力中心应用评测；
- 应用迁移。

2025 年琶洲实验室路演的 [[company/爱特思/国产化人工智能算力平台异构并行加速项目|国产化人工智能算力平台异构并行加速项目]] 进一步把目标明确到国产 AI 加速设备、底层算子库以及大模型训练 / 推理性能优化。

### 昇腾 910 算子优化

深圳爱特思名下公开专利 **CN117851738A** 的发明人包括陆璐，内容是“基于昇腾 910 平台的复数矩阵向量乘法计算方案”，直接在 Ascend 910 AI Core / Vector Unit 上做任务划分、内存搬运和向量化优化。

另有公开专利涉及基于深度学习加速器矩阵核心的高性能 GEMV。这组专利把“国产算力优化”从概念层落到了明确的 kernel / operator 层。

## 产业与职业关系

- [[company/AMD/AMD|AMD]]：2013 年中国科大超算中心公开讲座信息列陆璐为 AMD 应用解决方案部门软件架构师，同时任华南理工大学教授；这是其 GPU / OpenCL / heterogeneous computing 路线的重要历史职业连接。
- [[company/超聚变/超聚变|超聚变]]：2023 年双方公开联合创新，围绕 FusionOS、openEuler、AI 模型部署、底层算子和多卡多节点优化。
- [[university/鹏城实验室/鹏城实验室|鹏城实验室]]：2025 年公开嘉宾资料仍将其列为“双聘教授”。本页保留带时间戳的 affiliation，不把它强写成 2026 年持续在任。
- [[company/爱特思/深圳爱特思信息技术有限公司|深圳爱特思]]：2025–2026 公开资料仍显示其为创始人 / 法定代表人。

## Sources
- https://www.ccf.org.cn/Chapters/TC/11_list/TCSE/
- https://www.xfusion.com/minisite/cn/xfusion-explorer-summit2025
- https://www.openeuler.org/zh/showcase/education/huanan/
- https://www.xfusion.com/cn/news/fusionos-openeuler-summit-2023
- https://scc.ustc.edu.cn/pxxx/201307/t20130720_155061.html
- https://job.zust.edu.cn/positionDetail/2851114f08284a1ab9fa4b872482f94c
- https://www.pazhoulab.com/2025/10/7091/
- https://patents.google.com/patent/CN117851738A/zh
