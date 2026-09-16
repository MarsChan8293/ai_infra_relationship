---
type: project
name: MemFabric
linked_people: []
companies: ["华为"]
company_relation: company-led
layer: communication
hardware: [Ascend]
open_source: true
repository: https://gitcode.com/Ascend/memfabric_hybrid
areas: [memory-pooling, data-movement, disaggregated-serving, kv-cache, rdma, ascend]
last_verified: "2026-09"
linked_companies:
  - "company/华为/华为"
---
# MemFabric

## 项目简介
MemFabric 是 Ascend 生态的开源内存池化与高性能数据移动底座，将多节点 DRAM / HBM 等异构内存统一池化，并提供接近内存语义的跨机直接访问接口。

对 AI Infra 图谱而言，它更接近 **KV Cache / PD 分离背后的 data plane**，而不是 serving engine：上层系统可以把 KV、模型参数或训练/推理中间数据放在统一内存池中，再利用 Ascend 的 Device RoCE、SDMA、UB / URMA 等链路进行高速搬运。

## GitCode
https://gitcode.com/Ascend/memfabric_hybrid

## 推理优化主线
- **DRAM + HBM 混合池化**：把多机多层内存抽象为统一的全局内存空间。
- **跨机直接访问**：覆盖 H2D、D2H、D2RH、RH2D、D2D 等数据路径，减少传统中转拷贝。
- **Ascend A2 / A3 / A5 数据通路**：官方文档持续扩展 Device RoCE、SDMA、URMA、UBOE 等后端。
- **LLM 数据面**：官方列出的应用包括 KV cache、PD 传输、模型参数缓存、参数 reshard 等。

## 生态关系
- [[MemCache]]：**强依赖关系**。MemCache 以 MemFabric 作为多级内存和异构网络传输底座。
- [[vLLM-Ascend]]：官方资料明确给出 MemFabric + MemCache 作为 vLLM-Ascend backend 使能推理加速的路径。
- [[Mooncake]]：MemFabric 官方性能测试直接对接 Mooncake Transfer Engine，说明两者在 data movement 接口层存在真实工程邻接；后续应继续核验对应集成代码与贡献者。

## 第一轮人物探索候选
MemFabric 与 MemCache 的提交/合并记录中出现明显重叠的 handle，例如 `yrewzjsx`、`chenyz6`、`shilinlee_com` / `shilinlee`、`p3rry` 等。这种跨两个仓库的重复工程活动是很强的 BFS 线索，但仍需 governance、review ownership 或 release 责任证据后再升级为 maintainer / core reviewer 节点。

## BFS 下一跳
1. `MemFabric -> maintainers / reviewers`：寻找稳定治理角色与 release owner。
2. `MemFabric -> MemCache`：识别跨仓库核心工程师和接口 owner。
3. `MemFabric -> Mooncake Transfer Engine`：确认适配代码、性能测试负责人和接口边界。
4. `MemFabric -> vLLM-Ascend`：追 backend 集成 PR、KV connector 和数据搬运路径。

## Sources
- https://gitcode.com/Ascend/memfabric_hybrid/tree/master
- https://gitcode.com/Ascend/memfabric_hybrid/blob/develop/README.md
- https://gitcode.com/Ascend/memfabric_hybrid/tree/master/benchmark

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
