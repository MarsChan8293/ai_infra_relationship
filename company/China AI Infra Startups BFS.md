---
type: relationship-map
name: China AI Infra Startups BFS
scope: domestic-ai-infra-startups
updated: 2026-09
---
# China AI Infra Startups BFS

以国内 AI infrastructure 软件 / 平台创业公司为 L0，优先遍历创始人、核心技术负责人，再沿学校、实验室、开源项目和明确工程协作扩展。芯片公司不在本图中。

## L0 → L1 核心成员

### [[SiliconFlow]]
- [[company/SiliconFlow/袁进辉 Jinhui Yuan|袁进辉（Jinhui Yuan）]] — Founder / CEO；OneFlow → inference infrastructure
- [[company/SiliconFlow/曾华|曾华]] — Co-Founder；商业化 / 生态

L2：OneFlow 原工程团队、[[Tsinghua University]]、MSRA、OneDiff / SiliconLLM。

### [[Infinigence AI]]
- [[company/Infinigence AI/汪玉 Yu Wang|汪玉（Yu Wang）]] — 发起人；清华电子系教授
- [[company/Infinigence AI/夏立雪 Lixue Xia|夏立雪（Lixue Xia）]] — Co-Founder / CEO
- [[company/Infinigence AI/戴国浩 Guohao Dai|戴国浩（Guohao Dai）]] — Co-Founder / Chief Scientist
- [[company/Infinigence AI/李伯勋 Boxun Li|李伯勋（Boxun Li）]] — CTO

L2：汪玉 → 夏立雪 / 戴国浩 / 李伯勋的清华电子系导师/研究谱系 → 异构算力、软硬协同、Agentic Infra。

### [[Qingcheng.ai]]
- [[company/Qingcheng.ai/汤雄超 Xiongchao Tang|汤雄超（Xiongchao Tang）]] — Co-Founder / CEO
- [[company/Qingcheng.ai/靳江明 Jiangming Jin|靳江明（Jiangming Jin）]] — COO
- [[company/Qingcheng.ai/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]] — Chief Scientist
- [[company/Qingcheng.ai/郑纬民 Weimin Zheng|郑纬民（Weimin Zheng）]] — Chief Advisor

L2：清华 HPC / 八卦炉 → 赤兔推理引擎、并行训练、compiler / scheduler / 国产算力适配。

### [[HPC-AI Tech]]
- [[company/HPC-AI Tech/尤洋 Yang You|尤洋（Yang You）]] — Founder

L2：UC Berkeley HPC / distributed optimization → [[Colossal-AI]] → distributed training / inference。

### [[TsingMao]]
- [[company/TsingMao/关超宇 Chaoyu Guan|关超宇（Chaoyu Guan）]] — Co-Founder / CEO
- [[company/TsingMao/姚航 Hang Yao|姚航（Hang Yao）]] — Co-Founder / COO
- [[company/TsingMao/朱文武 Wenwu Zhu|朱文武（Wenwu Zhu）]] — Scientific Advisor

L2：朱文武 → 关超宇的清华导师/学生关系 → AutoGL → MLGuider / heterogeneous inference。

### [[Approaching.AI]]
- [[company/Approaching.AI/艾智远 Zhiyuan Ai|艾智远（Zhiyuan Ai）]] — Founder / CEO
- [[company/Approaching.AI/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]] — Chief Scientist
- [[community/Mooncake/Ke Yang|Ke Yang]] — Mooncake Store Codeowner / Approaching.AI engineer

L2：清华系统研究 → [[Mooncake]] → Ke Yang → vLLM Mooncake Store integration → Token service / ATaaS。官方工程致谢还确认 Jiahao Lu、Zuoyuan Zhang、Zihan Tang 属 Approaching.AI 技术协作节点，暂不建立个人页。

### [[基流科技]]
- [[company/基流科技/胡效赫 Xiaohe Hu|胡效赫（Xiaohe Hu）]] — Founder / Chairman / CEO

L2：清华系统研究 + UC Berkeley 访问 → high-performance networking / collective communication → GPU cluster / LLM training reliability。

### [[PPIO]]
- [[company/PPIO/姚欣 Bill Yao|姚欣（Bill Yao）]] — Co-Founder / Chairman / CEO
- [[company/PPIO/王闻宇 Wayne Wang|王闻宇（Wayne Wang）]] — Co-Founder / CTO

L2：PPTV P2P / distributed video → PPIO distributed cloud → GPU Cloud / model serving → Agentic Cloud；技术生态继续连接 [[vLLM]]、[[SGLang]]。

## 下一轮 BFS 优先级
1. Approaching.AI：Jiahao Lu / Zuoyuan Zhang / Zihan Tang → vLLM Mooncake Store 的具体 PR / 模块关系。
2. 基流科技：collective communication 论文作者 → 智谱 / 清华 / 北航的大规模训练网络。
3. SiliconFlow：OneFlow 原核心工程师 → SiliconLLM / OneDiff 当前技术负责人。
4. Qingcheng.ai：赤兔 / 八卦炉主要开发者，包括唐适之、师天麾等已公开技术成员。
5. HPC-AI Tech：Colossal-AI 当前 maintainer / contributor → 公司工程团队。

## 建模原则
- 公司公开职位 ≠ 技术直接合作；只有论文、开源项目、正式导师或明确工程项目才建立强人物边。
- 历史 affiliation 与当前 affiliation 分开；例如 Mooncake 当前官方文档已将任峰标为 9#AISoft，因此不再标记为 Approaching.AI 当前同事。
- 仅有公司生态合作时保留公司/项目级边，不自动推断人物友谊或同事关系。
