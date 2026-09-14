---
type: relationship-map
name: China AI Infra Startups BFS
scope: domestic-ai-infra-startups
updated: 2026-09
---
# China AI Infra Startups BFS

以国内 AI infrastructure 软件 / 平台创业公司为 L0，优先遍历创始人、核心技术负责人，再沿学校、实验室、开源项目和明确工程协作扩展。芯片公司不在本图中。中国公司统一采用“中文名（English Name）”展示。

## L0 → L1/L2 核心网络

### [[company/硅基流动/硅基流动|硅基流动]]
- [[company/硅基流动/袁进辉 Jinhui Yuan|袁进辉（Jinhui Yuan）]] — Founder / CEO
- [[company/硅基流动/柳俊丞 Juncheng Liu|柳俊丞（Juncheng Liu）]] — CTO；OneFlow 系统论文作者 / CUDA kernel 工程
- [[company/硅基流动/赵震 Zhao Zhen|赵震（Zhao Zhen）]] — COO；OneFlow 旧团队
- [[company/硅基流动/曾华|曾华]] — Co-Founder；商业化 / 生态

L2：[[OneFlow]] → 袁进辉 / 柳俊丞 / 赵震 → 硅基流动→ SiliconLLM / OneDiff / Token infrastructure。现在已从“匿名 OneFlow 原团队”推进到可核验的核心连续创业人物。

### [[company/无问芯穹/无问芯穹|无问芯穹]]
- [[company/无问芯穹/汪玉 Yu Wang|汪玉（Yu Wang）]] — 发起人；清华电子系教授
- [[company/无问芯穹/夏立雪 Lixue Xia|夏立雪（Lixue Xia）]] — Co-Founder / CEO
- [[company/无问芯穹/戴国浩 Guohao Dai|戴国浩（Guohao Dai）]] — Co-Founder / Chief Scientist
- [[company/无问芯穹/李伯勋 Boxun Li|李伯勋（Boxun Li）]] — CTO

L2：汪玉 → 夏立雪 / 戴国浩 / 李伯勋的清华电子系导师/研究谱系 → 异构算力、软硬协同、Agentic Infra。

### [[company/清程极智/清程极智|清程极智]]
- [[company/清程极智/汤雄超 Xiongchao Tang|汤雄超（Xiongchao Tang）]] — Co-Founder / CEO
- [[company/清程极智/师天麾 Tianhui Shi|师天麾（Tianhui Shi）]] — Co-Founder；翟季冬博士生
- [[company/清程极智/唐适之 Shizhi Tang|唐适之（Shizhi Tang）]] — Co-Founder / Chitu inference lead；翟季冬博士生
- [[company/清程极智/马子轩 Zixuan Ma|马子轩（Zixuan Ma）]] — Senior R&D Expert；BaGuaLu 第一作者
- [[company/清程极智/靳江明 Jiangming Jin|靳江明（Jiangming Jin）]] — COO
- [[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]] — Chief Scientist
- [[company/清程极智/郑纬民 Weimin Zheng|郑纬民（Weimin Zheng）]] — Chief Advisor

L2：翟季冬 → 师天麾 / 唐适之的正式博士导师链；BaGuaLu 将马子轩、唐适之、师天麾、翟季冬、郑纬民直接连成论文协作网络，再产业化到八卦炉 / 赤兔。

### [[company/潞晨科技/潞晨科技|潞晨科技]]
- [[company/潞晨科技/尤洋 Yang You|尤洋（Yang You）]] — Founder
- [[company/潞晨科技/Haichen Huang|Haichen Huang]] — current Software Engineer；large-scale LLM training

L2：潞晨科技→ [[Colossal-AI]] → [[community/hpcaitech/Colossal-AI/Hongxin Liu|Hongxin Liu]] / Haichen Huang；人才继续分叉到 [[company/字节跳动/方佳瑞 Jiarui Fang|方佳瑞（Jiarui Fang）]]（字节跳动 ByteDance AI infra）与 [[community/sgl-project/SGLang/Shenggui Li|Shenggui Li]]（SGLang / SpecForge）。这条线连接 distributed training → inference / speculative decoding。

### [[company/清昴智能/清昴智能|清昴智能]]
- [[company/清昴智能/关超宇 Chaoyu Guan|关超宇（Chaoyu Guan）]] — Co-Founder / CEO
- [[company/清昴智能/姚航 Hang Yao|姚航（Hang Yao）]] — Co-Founder / COO
- [[company/清昴智能/朱文武 Wenwu Zhu|朱文武（Wenwu Zhu）]] — Scientific Advisor

L2：朱文武 → 关超宇的清华导师/学生关系 → AutoGL → MLGuider / heterogeneous inference。

### [[company/趋境科技/趋境科技|趋境科技]]
- [[company/趋境科技/艾智远 Zhiyuan Ai|艾智远（Zhiyuan Ai）]] — Founder / CEO
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]] — Chief Scientist
- [[community/kvcache-ai/Mooncake/任峰 Feng Ren|任峰（Feng Ren）]] — Technical Expert；Mooncake co-founder / Transfer Engine
- [[community/kvcache-ai/Mooncake/Ke Yang|Ke Yang]] — Mooncake Store Codeowner / Approaching.AI engineer
- [[company/趋境科技/卢佳豪 Jiahao Lu|卢佳豪（Jiahao Lu）]] — intern；Mooncake developer
- [[company/趋境科技/Hongbo Kang|Hongbo Kang]] / [[company/趋境科技/Weiyu Xie|Weiyu Xie]] — 2026 MADSys PhD → first job Approaching.AI

L2：清华 MADSys → Mooncake → 任峰 / Ke Yang / 卢佳豪 → vLLM Mooncake Store；同时 MADSys 博士直接流入趋境科技。任峰个人主页明确 2026–至今在 Approaching.AI；Mooncake MAINTAINERS 的 9#AISoft affiliation 可能更新滞后。

### [[company/基流科技/基流科技|基流科技（InfraWaves）]]
- [[company/基流科技/胡效赫 Xiaohe Hu|胡效赫（Xiaohe Hu）]] — Founder / Chairman / CEO
- [[company/基流科技/Mingjun Zhang|Mingjun Zhang]] — VCCL / collective communication
- [[company/基流科技/Yanmin Jia|Yanmin Jia]] — VCCL / HetCCL
- [[company/基流科技/He Liu|He Liu]] — VCCL / HetCCL
- [[company/基流科技/Wenqi Xie|Wenqi Xie]] — executive director + VCCL author

L2：基流科技（InfraWaves）→ [[VCCL]] → large-scale GPU collective communication；Mingjun / Yanmin / He 继续通过 HetCCL 连接多厂商异构 collective communication。Mingjun 的公开 GitHub 还暴露出与 SGLang、Mooncake、vLLM、DeepEP 等上层 AI infra 项目的潜在下一跳，具体人物边等待 PR/代码证据。

### [[company/派欧云/派欧云|派欧云]]
- [[company/派欧云/姚欣 Bill Yao|姚欣（Bill Yao）]] — Co-Founder / Chairman / CEO
- [[company/派欧云/王闻宇 Wayne Wang|王闻宇（Wayne Wang）]] — Co-Founder / CTO

L2：PPTV P2P / distributed video → 派欧云distributed cloud → GPU Cloud / model serving → Agentic Cloud；技术生态继续连接 [[vLLM]]、[[SGLang]]。

## 下一轮 BFS 优先级
1. [[company/硅基流动/硅基流动|硅基流动]]：OneDiff / SiliconLLM 的具名核心工程师与 inference 优化负责人。
2. [[VCCL]] / [[company/基流科技/基流科技|基流科技（InfraWaves）]]：Mingjun Zhang 等在 DeepEP、SGLang、Mooncake、vLLM 的具体 PR / code collaboration，建立 cluster networking → serving 的人物强边。
3. [[company/趋境科技/趋境科技|趋境科技]]：Yue Chen / Zhanhao Cao → SGLang Elastic EP；Zuoyuan Zhang / Zihan Tang → vLLM Mooncake Store。
4. [[company/清程极智/清程极智|清程极智]]：Chitu / ChituDiffusion 当前 maintainer 与 kernel / compiler 核心贡献者。
5. [[Colossal-AI]]：现役 maintainer / SpecForge / 字节跳动后续网络，继续跟踪 training → inference 人才流。

## 建模原则
- 公司公开职位 ≠ 技术直接合作；只有论文、开源项目、正式导师或明确工程项目才建立强人物边。
- 历史 affiliation 与当前 affiliation 分开；发生冲突时优先采用个人当前主页 / 公司官方资料，并保留项目治理文档滞后的注记。
- 仅有公司生态合作或 GitHub pinned repo 时保留“下一跳线索”，不自动推断人物直接合作、同事或友谊关系。
