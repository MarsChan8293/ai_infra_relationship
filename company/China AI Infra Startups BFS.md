---
type: relationship-map
name: China AI Infra Startups BFS
scope: domestic-ai-infra-startups
updated: 2026-09
---
# China AI Infra Startups BFS

以国内 AI infrastructure 软件 / 平台创业公司为 L0，优先遍历创始人、核心技术负责人，再沿学校、实验室、开源项目和明确工程协作扩展。芯片公司不在本图中。中国公司统一采用“中文名（English Name）”展示。

## L0 → L1/L2 核心网络

### [[company/SiliconFlow/SiliconFlow|硅基流动（SiliconFlow）]]
- [[company/SiliconFlow/袁进辉 Jinhui Yuan|袁进辉（Jinhui Yuan）]] — Founder / CEO
- [[company/SiliconFlow/柳俊丞 Juncheng Liu|柳俊丞（Juncheng Liu）]] — CTO；OneFlow 系统论文作者 / CUDA kernel 工程
- [[company/SiliconFlow/赵震 Zhao Zhen|赵震（Zhao Zhen）]] — COO；OneFlow 旧团队
- [[company/SiliconFlow/曾华|曾华]] — Co-Founder；商业化 / 生态

L2：[[OneFlow]] → 袁进辉 / 柳俊丞 / 赵震 → 硅基流动（SiliconFlow）→ SiliconLLM / OneDiff / Token infrastructure。现在已从“匿名 OneFlow 原团队”推进到可核验的核心连续创业人物。

### [[company/Infinigence AI/Infinigence AI|无问芯穹（Infinigence AI）]]
- [[company/Infinigence AI/汪玉 Yu Wang|汪玉（Yu Wang）]] — 发起人；清华电子系教授
- [[company/Infinigence AI/夏立雪 Lixue Xia|夏立雪（Lixue Xia）]] — Co-Founder / CEO
- [[company/Infinigence AI/戴国浩 Guohao Dai|戴国浩（Guohao Dai）]] — Co-Founder / Chief Scientist
- [[company/Infinigence AI/李伯勋 Boxun Li|李伯勋（Boxun Li）]] — CTO

L2：汪玉 → 夏立雪 / 戴国浩 / 李伯勋的清华电子系导师/研究谱系 → 异构算力、软硬协同、Agentic Infra。

### [[company/Qingcheng.ai/Qingcheng.ai|清程极智（Qingcheng.ai）]]
- [[company/Qingcheng.ai/汤雄超 Xiongchao Tang|汤雄超（Xiongchao Tang）]] — Co-Founder / CEO
- [[company/Qingcheng.ai/师天麾 Tianhui Shi|师天麾（Tianhui Shi）]] — Co-Founder；翟季冬博士生
- [[company/Qingcheng.ai/唐适之 Shizhi Tang|唐适之（Shizhi Tang）]] — Co-Founder / Chitu inference lead；翟季冬博士生
- [[company/Qingcheng.ai/马子轩 Zixuan Ma|马子轩（Zixuan Ma）]] — Senior R&D Expert；BaGuaLu 第一作者
- [[company/Qingcheng.ai/靳江明 Jiangming Jin|靳江明（Jiangming Jin）]] — COO
- [[company/Qingcheng.ai/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]] — Chief Scientist
- [[company/Qingcheng.ai/郑纬民 Weimin Zheng|郑纬民（Weimin Zheng）]] — Chief Advisor

L2：翟季冬 → 师天麾 / 唐适之的正式博士导师链；BaGuaLu 将马子轩、唐适之、师天麾、翟季冬、郑纬民直接连成论文协作网络，再产业化到八卦炉 / 赤兔。

### [[company/HPC-AI Tech/HPC-AI Tech|潞晨科技（HPC-AI Tech）]]
- [[company/HPC-AI Tech/尤洋 Yang You|尤洋（Yang You）]] — Founder
- [[company/HPC-AI Tech/Haichen Huang|Haichen Huang]] — current Software Engineer；large-scale LLM training

L2：潞晨科技（HPC-AI Tech）→ [[Colossal-AI]] → [[community/Colossal-AI/Hongxin Liu|Hongxin Liu]] / Haichen Huang；人才继续分叉到 [[company/ByteDance/方佳瑞 Jiarui Fang|方佳瑞（Jiarui Fang）]]（字节跳动 ByteDance AI infra）与 [[community/SGLang/Shenggui Li|Shenggui Li]]（SGLang / SpecForge）。这条线连接 distributed training → inference / speculative decoding。

### [[company/TsingMao/TsingMao|清昴智能（TsingMao）]]
- [[company/TsingMao/关超宇 Chaoyu Guan|关超宇（Chaoyu Guan）]] — Co-Founder / CEO
- [[company/TsingMao/姚航 Hang Yao|姚航（Hang Yao）]] — Co-Founder / COO
- [[company/TsingMao/朱文武 Wenwu Zhu|朱文武（Wenwu Zhu）]] — Scientific Advisor

L2：朱文武 → 关超宇的清华导师/学生关系 → AutoGL → MLGuider / heterogeneous inference。

### [[company/Approaching.AI/Approaching.AI|趋境科技（Approaching.AI）]]
- [[company/Approaching.AI/艾智远 Zhiyuan Ai|艾智远（Zhiyuan Ai）]] — Founder / CEO
- [[company/Approaching.AI/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]] — Chief Scientist
- [[community/Mooncake/任峰 Feng Ren|任峰（Feng Ren）]] — Technical Expert；Mooncake co-founder / Transfer Engine
- [[community/Mooncake/Ke Yang|Ke Yang]] — Mooncake Store Codeowner / Approaching.AI engineer
- [[company/Approaching.AI/卢佳豪 Jiahao Lu|卢佳豪（Jiahao Lu）]] — intern；Mooncake developer
- [[company/Approaching.AI/Hongbo Kang|Hongbo Kang]] / [[company/Approaching.AI/Weiyu Xie|Weiyu Xie]] — 2026 MADSys PhD → first job Approaching.AI

L2：清华 MADSys → Mooncake → 任峰 / Ke Yang / 卢佳豪 → vLLM Mooncake Store；同时 MADSys 博士直接流入趋境科技（Approaching.AI）。任峰个人主页明确 2026–至今在 Approaching.AI；Mooncake MAINTAINERS 的 9#AISoft affiliation 可能更新滞后。

### [[company/基流科技/基流科技|基流科技（InfraWaves）]]
- [[company/基流科技/胡效赫 Xiaohe Hu|胡效赫（Xiaohe Hu）]] — Founder / Chairman / CEO
- [[company/基流科技/Mingjun Zhang|Mingjun Zhang]] — VCCL / collective communication
- [[company/基流科技/Yanmin Jia|Yanmin Jia]] — VCCL / HetCCL
- [[company/基流科技/He Liu|He Liu]] — VCCL / HetCCL
- [[company/基流科技/Wenqi Xie|Wenqi Xie]] — executive director + VCCL author

L2：基流科技（InfraWaves）→ [[VCCL]] → large-scale GPU collective communication；Mingjun / Yanmin / He 继续通过 HetCCL 连接多厂商异构 collective communication。Mingjun 的公开 GitHub 还暴露出与 SGLang、Mooncake、vLLM、DeepEP 等上层 AI infra 项目的潜在下一跳，具体人物边等待 PR/代码证据。

### [[company/PPIO/PPIO|派欧云（PPIO）]]
- [[company/PPIO/姚欣 Bill Yao|姚欣（Bill Yao）]] — Co-Founder / Chairman / CEO
- [[company/PPIO/王闻宇 Wayne Wang|王闻宇（Wayne Wang）]] — Co-Founder / CTO

L2：PPTV P2P / distributed video → 派欧云（PPIO）distributed cloud → GPU Cloud / model serving → Agentic Cloud；技术生态继续连接 [[vLLM]]、[[SGLang]]。

## 下一轮 BFS 优先级
1. [[company/SiliconFlow/SiliconFlow|硅基流动（SiliconFlow）]]：OneDiff / SiliconLLM 的具名核心工程师与 inference 优化负责人。
2. [[VCCL]] / [[company/基流科技/基流科技|基流科技（InfraWaves）]]：Mingjun Zhang 等在 DeepEP、SGLang、Mooncake、vLLM 的具体 PR / code collaboration，建立 cluster networking → serving 的人物强边。
3. [[company/Approaching.AI/Approaching.AI|趋境科技（Approaching.AI）]]：Yue Chen / Zhanhao Cao → SGLang Elastic EP；Zuoyuan Zhang / Zihan Tang → vLLM Mooncake Store。
4. [[company/Qingcheng.ai/Qingcheng.ai|清程极智（Qingcheng.ai）]]：Chitu / ChituDiffusion 当前 maintainer 与 kernel / compiler 核心贡献者。
5. [[Colossal-AI]]：现役 maintainer / SpecForge / 字节跳动（ByteDance）后续网络，继续跟踪 training → inference 人才流。

## 建模原则
- 公司公开职位 ≠ 技术直接合作；只有论文、开源项目、正式导师或明确工程项目才建立强人物边。
- 历史 affiliation 与当前 affiliation 分开；发生冲突时优先采用个人当前主页 / 公司官方资料，并保留项目治理文档滞后的注记。
- 仅有公司生态合作或 GitHub pinned repo 时保留“下一跳线索”，不自动推断人物直接合作、同事或友谊关系。
