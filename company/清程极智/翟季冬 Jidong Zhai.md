---
type: person
name: 翟季冬
english_name: Jidong Zhai
aliases: [翟季冬, Jidong Zhai]
current_affiliations: ["Tsinghua University","Qingcheng.ai"]
schools:
  - "清华大学"
linked_companies:
  - "company/清程极智/清程极智"
projects: [Jenga, FastDecode]
roles: [Professor, Chief Scientist]
areas: [high-performance-computing, distributed-training, performance-analysis, compiler-optimization, llm-serving]
last_verified: "2026-09"
relations:
  - '{"target":"company/清程极智/师天麾 Tianhui Shi","type":["cofounder","mentor-network"],"confidence":"high","evidence":["https://pacman.cs.tsinghua.edu.cn/~zjd/people/","https://pacman.cs.tsinghua.edu.cn/~zjd/projects/bagualu/","https://www.tsinghua.org.cn/info/1953/42732.htm"]}'
  - '{"target":"company/清程极智/唐适之 Shizhi Tang","type":["mentor-network"],"confidence":"medium","evidence":["https://pacman.cs.tsinghua.edu.cn/~zjd/people/","https://pacman.cs.tsinghua.edu.cn/~zjd/projects/bagualu/","https://www.tsinghua.org.cn/info/1953/42732.htm"]}'
  - '{"target":"company/清程极智/马子轩 Zixuan Ma","type":["paper-coauthor","mentor-network"],"confidence":"high","evidence":["https://pacman.cs.tsinghua.edu.cn/~zjd/people/","https://pacman.cs.tsinghua.edu.cn/~zjd/projects/bagualu/","https://www.tsinghua.org.cn/info/1953/42732.htm"]}'
  - '{"target":"company/清程极智/汤雄超 Xiongchao Tang","type":["mentor-network"],"confidence":"medium","evidence":["https://pacman.cs.tsinghua.edu.cn/~zjd/people/","https://pacman.cs.tsinghua.edu.cn/~zjd/projects/bagualu/","https://www.tsinghua.org.cn/info/1953/42732.htm"]}'
  - '{"target":"community/vllm-project/vLLM/Chen Zhang","type":["advisor","paper-coauthor"],"confidence":"high","evidence":["https://heheda12345.github.io/","https://arxiv.org/abs/2503.18292","https://pacman.cs.tsinghua.edu.cn/~zjd/people/"]}'
  - '{"target":"company/字节跳动/郑立言 Liyan Zheng","type":["advisor","paper-coauthor"],"confidence":"high","evidence":["https://wintersurf.github.io/","https://pacman.cs.tsinghua.edu.cn/~zjd/projects/einnet/"]}'
  - '{"target":"company/字节跳动/何家傲 Jiaao He","type":["advisor","paper-coauthor"],"confidence":"high","evidence":["https://laekov.com.cn/cv/","https://pacman.cs.tsinghua.edu.cn/~zjd/publication/generated/dblp-journalscorrabs-2403-11421/"]}'
  - '{"target":"company/深度求索/黄可钊 Kezhao Huang","type":["mentor-network","paper-coauthor"],"confidence":"high","evidence":["https://pacman.cs.tsinghua.edu.cn/~zjd/people/","https://pacman.cs.tsinghua.edu.cn/~zjd/author/kezhao-huang/"]}'
  - '{"target":"community/vllm-project/vLLM/游凯超 Kaichao You","type":["paper-coauthor","research-collaboration"],"project":"Jenga","confidence":"high","evidence":["https://arxiv.org/abs/2503.18292"]}'
  - '{"target":"company/TensorMesh/杜昆泰 Kuntai Du","type":["paper-coauthor","research-collaboration"],"project":"Jenga","confidence":"high","evidence":["https://arxiv.org/abs/2503.18292"]}'
---
# 翟季冬（Jidong Zhai）

当前：[[清华大学]] 计算机系长聘教授；公开创业资料列为 [[清程极智]] 首席科学家。

## AI Infra 位置
研究方向覆盖高性能计算、并行系统、编译器、性能分析、大规模 AI 训练与 LLM serving。PACMAN 的技术路线已经从传统 HPC / performance optimization 延展到 tensor compiler、MoE distributed training、异构推理和现代 serving memory management。

## 推理优化 / LLM Systems 主线
- [[university/清华大学/FastDecode|FastDecode]]：与博士生 [[company/字节跳动/何家傲 Jiaao He|何家傲（Jiaao He）]] 合作，将 CPU 集群资源用于处理 memory-bound KV-cache / attention 路径，形成 CPU/GPU heterogeneous LLM serving。
- [[community/vllm-project/Jenga/Jenga|Jenga]]：SOSP 2025，与 [[community/vllm-project/vLLM/Chen Zhang|Chen Zhang]]、[[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰]]、[[community/vllm-project/vLLM/游凯超 Kaichao You|游凯超]]、Woosuk Kwon、Zhuohan Li、Joseph Gonzalez、Ion Stoica 等共同连接 PACMAN 与 Berkeley / vLLM serving 网络。
- [[community/InfiniTensor/InfiniTensor|InfiniTensor]] / EinNet：与 [[company/字节跳动/郑立言 Liyan Zheng|郑立言（Liyan Zheng）]] 等的 tensor compiler / optimizer 研究路线，继续延伸到多硬件推理引擎。

## 人物关系
- [[community/vllm-project/vLLM/Chen Zhang|Chen Zhang]]：**清华博士导师 / 学生 + Jenga 合作者**。PACMAN alumni 页面记录 Chen Zhang 2025 PhD，毕业后赴 Berkeley 做博士后；Jenga 将这条师生线直接接入 Berkeley / vLLM serving 网络。
- [[company/字节跳动/郑立言 Liyan Zheng|郑立言（Liyan Zheng）]]：**清华博士导师 / 学生 + compiler / ML systems 合作者**。2025 PhD 后进入 ByteDance Seed，从事 LLM systems。
- [[company/字节跳动/何家傲 Jiaao He|何家傲（Jiaao He）]]：**清华博士导师 / 学生 + FastDecode / MoE systems 合作者**。2025 PhD 后进入 ByteDance infrastructure research。
- [[company/深度求索/黄可钊 Kezhao Huang|黄可钊（Kezhao Huang）]]：**PACMAN 博士培养/研究网络 + 系统论文合作者**。研究兴趣从 GNN systems 转向 LLM serving / fine-tuning，2025 PhD 后首份工作为 DeepSeek。
- [[company/清程极智/师天麾 Tianhui Shi|师天麾（Tianhui Shi）]]：**清华博士导师 / 学生 + 清程极智产业化**。师天麾参与八卦炉及 AI systems 工作并成为公司联合创始人。
- [[company/清程极智/唐适之 Shizhi Tang|唐适之（Shizhi Tang）]]：**清华博士导师 / 学生 + 清程极智产业化**。2024 PhD 后进入 QingCheng.AI，负责赤兔推理引擎、并行训练/推理及算子优化。
- [[company/清程极智/马子轩 Zixuan Ma|马子轩（Zixuan Ma）]]：**清华 HPC 研究指导网络 + BaGuaLu 论文合作者**。当前在清程任高级研发专家。
- [[company/清程极智/汤雄超 Xiongchao Tang|汤雄超（Xiongchao Tang）]]：**清华 HPC 技术谱系 + 公司技术网络**。
- [[company/清程极智/靳江明 Jiangming Jin|靳江明（Jiangming Jin）]]：**清程极智技术/管理协作网络**。

## BFS 关键人才迁移
`PACMAN / 翟季冬 → Chen Zhang → Berkeley / vLLM → Meta / Inferact / TensorMesh`

`PACMAN / 翟季冬 → 郑立言、何家傲 → ByteDance Seed / Infrastructure`

`PACMAN / 翟季冬 → 黄可钊 → DeepSeek`

这些路线与清华 MADSys → Moonshot / DeepSeek 的谱系相互独立，不因同校自动合并为同一实验室网络。

## Sources
- https://pacman.cs.tsinghua.edu.cn/~zjd/
- https://pacman.cs.tsinghua.edu.cn/~zjd/people/
- https://pacman.cs.tsinghua.edu.cn/~zjd/projects/bagualu/
- https://pacman.cs.tsinghua.edu.cn/~zjd/projects/einnet/
- https://arxiv.org/abs/2503.18292
- https://arxiv.org/abs/2403.11421
- https://wintersurf.github.io/
- https://laekov.com.cn/cv/
- https://www.tsinghua.org.cn/info/1953/42732.htm

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/清程极智/清程极智|清程极智]]：人物页 `current_affiliations:` 明确记录。

<!-- END AUTO PERSON COMPANIES -->
