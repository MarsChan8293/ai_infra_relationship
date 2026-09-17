---
type: project
name: SiliconLLM
organization: siliconflow
linked_people: []
companies: ["硅基流动"]
company_relation: company-led
layer: llm-inference-engine
open_source: false
linked_companies:
  - "company/硅基流动/硅基流动"
---
# SiliconLLM

SiliconLLM 是硅基流动自研的大模型高性能推理引擎，是公司从模型 API / MaaS 向 production Token infrastructure 延伸的核心技术层。

## AI Infra 位置
公开技术材料显示，硅基流动围绕推理引擎持续做模型、机制、框架和算子层联合优化，并将能力扩展到：
- high-throughput / low-latency model serving
- MoE 与大规模并行
- Prefill / Decode separation
- KV Cache 与 Prefix Cache aware routing
- 异构 GPU / NPU backend
- 模型实例弹性调度与生产级 SLA

## PD / KV Cache 异构实践
2026 年硅基流动与摩尔线程发布 PD 分离异构混部方案，在 Prefill 侧使用 MTT S5000，在 Decode 侧使用另一类高带宽 GPU，并通过 [[Mooncake]] RDMA 做 KV Cache 跨芯片传输。硅基流动推理引擎负责统一模型加载、执行与调度；摩尔线程 [[MATE]] 提供硬件算子优化。

因此 SiliconLLM 在本图谱里的关键技术链为：
`SiliconLLM → PD separation → Mooncake / KV transfer → MUSA / MATE → heterogeneous inference`

## 人物证据边界
- 袁进辉公开介绍过 SiliconLLM 与国产推理生态。
- 柳俊丞作为 CTO 连接公司总体技术研发路线，但当前公开资料不足以把某个 SiliconLLM 代码模块直接归于其个人维护。
- 唐安波公开披露 production inference 的 PD、KV Cache、routing 与调度架构，属于架构实践接口人物，不等同于代码 maintainer。

## Sources
- https://siliconflow.cn/news/zj5pf6x81ka0q6gf17jusbnq
- https://www.siliconflow.cn/news/pbjrn9ci5sgyvljkzs90gp05
- https://siliconflow.cn/news/vztpt9m5ijsupt2k2quotssg
- https://siliconflow.cn/news/y9r99a4bmvehkr9u3os87dhe

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/硅基流动/硅基流动|硅基流动]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
