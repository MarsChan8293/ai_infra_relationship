---
type: person
name: Alex Yang
aliases: [aleozlx, "@aleozlx"]
current_affiliations: ["NVIDIA"]
communities: [FlashInfer]
roles: [Full Codebase Approver]
areas: [quantization, moe, gpu-inference-kernels, ci, api-governance]
confidence: verified
last_verified: "2026-09"
---
# Alex Yang（aleozlx）

## 身份与当前关联
FlashInfer 官方 GitHub commit metadata 将 GitHub handle `aleozlx` 的提交作者明确标识为 `Alex Yang <aleyang@nvidia.com>`。因此本图谱将此前的 handle-only 节点解析为 **Alex Yang**，并将当前 affiliation 记录为 [[NVIDIA]]。

这类 identity resolution 依赖项目自身的 signed/merged commit metadata，而不是通过用户名相似度或第三方社交账号猜测。

## 社区角色
[[FlashInfer]] Full Codebase Approver，覆盖 Attention、GEMM、MoE、Communication、autotuner 等关键模块。2026-09 的公开工作还包括清理 0.7.0 边界上的 deprecated API，同时检查 SGLang / vLLM 对 legacy FlashInfer API 的真实下游依赖。

## 技术方向
量化、MoE、FlashInfer API 一致性、CI、GPU kernel 工程与 release-quality。

## 人物关系
- [[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪（Zihao Ye）]]：**FlashInfer Full Codebase Approver 同僚**。截至 2026-09 两人共同拥有全代码库审批权限并覆盖多个 kernel 模块。
- [[community/flashinfer-ai/FlashInfer/Jingfan Sun|Jingfan Sun]]：**FlashInfer Full Codebase Approver 同僚**。截至 2026-09 共同参与 Attention、GEMM、MoE、Communication 等模块的 review/approval。
- [[community/flashinfer-ai/FlashInfer/Yang Xu|Yang Xu]]：**FlashInfer Full Codebase Approver 同僚**。截至 2026-09 共同承担代码库治理。
- [[community/flashinfer-ai/FlashInfer/Brian K. Ryu|Brian K. Ryu]]：**FlashInfer Full Codebase Approver 同僚**。截至 2026-09 同具跨模块审批权限；公司 affiliation 可分别由各自公开 commit metadata 独立核验。

## Sources
- https://github.com/flashinfer-ai/flashinfer
- https://github.com/flashinfer-ai/flashinfer/commits?author=aleozlx
- FlashInfer CODEOWNERS / maintainer metadata
