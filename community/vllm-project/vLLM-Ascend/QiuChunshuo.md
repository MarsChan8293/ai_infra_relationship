---
type: person
name: QiuChunshuo
aliases: ["@QiuChunshuo"]
public_email: qiuchunshuo@huawei.com
email_affiliations:
  - "华为"
linked_companies:
  - "company/华为/华为"
projects: [vLLM-Ascend]
roles: [Attention Performance Contributor, Context Parallelism Contributor]
areas: [attention, mla, sfa, dcp, context-parallelism, kv-cache, triton, ascend]
confidence: high
last_verified: "2026-09"
---
# QiuChunshuo

项目：[[vLLM-Ascend]]

## 身份与组织证据
2026-08 至 2026-09 的 vLLM-Ascend 多个公开提交持续使用 `QiuChunshuo <qiuchunshuo@huawei.com>`。因此记录公开职业邮箱，并由邮箱域名机制生成华为组织关联；当前不据 handle / 邮箱猜中文实名或职级。

## vLLM-Ascend
- 优化 **split MLA DCP attention**，把历史 KV 分支与当前 token FIA 输出的归并合成单个 combine kernel，减少一次 combine launch 与中间 tensor materialization。
- 为 **SFA DCP** 实现 fused output all-to-all，把 output/LSE 的两次 collective 合并为一次 HCCL A2A，并融合稳定 LSE reduction。
- 优化 DeepSeek V4 多组 KV cache 的 slot mapping，将多 attention group 的重复计算融合进单个 Triton launch。
- 推进 DSA / SFA context-parallel 配置迁移与 DCP + MTP slot mapping 容量修复。

## 图谱价值
这是 `attention kernel -> context parallelism -> KV metadata -> collective communication` 的核心性能节点，与 [[weiguihua2]] 的 DCP metadata 路线、[[leolee]] 的 PCP/KV Pool 路线形成互补。

## Sources
- https://github.com/vllm-project/vllm-ascend/commit/81e75f893b7ce98f1633cb66a5408687db6e039b
- https://github.com/vllm-project/vllm-ascend/commit/5c59cfba98045f49645284745be035346a4d82d8
- https://github.com/vllm-project/vllm-ascend/commit/e5b9036207f74658c2d4699e2de290c3a3f2e145
- https://github.com/vllm-project/vllm-ascend/commit/0aa1b486c0e6d3fb457822da2b9b49ede2578562

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/华为/华为|华为]]：公开职业邮箱域名证据；表示组织关联，不单独证明当前任职。

<!-- END AUTO PERSON COMPANIES -->
