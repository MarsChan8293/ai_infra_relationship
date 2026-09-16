---
type: person
name: Brian K. Ryu
aliases: [Brian Ryu, bkryu]
current_affiliations: ["NVIDIA"]
communities: [FlashInfer]
roles: [Full Codebase Approver]
areas: [gpu-inference-kernels, attention, moe, low-precision, blackwell]
confidence: verified
last_verified: "2026-09"
---
# Brian K. Ryu

## 社区角色
[[FlashInfer]] Full Codebase Approver，CODEOWNERS 中覆盖 Attention、GEMM、MoE、Communication、Norm 等多个核心模块。

## 当前关联
FlashInfer 官方 GitHub commit metadata 将 `bkryu` 的提交作者标识为 `Brian K. Ryu <bryu@nvidia.com>`。结合其持续承担全代码库审批与 NVIDIA GPU kernel / low-precision 路径开发，本图谱将当前 affiliation 记录为 [[NVIDIA]]。这里不从公司邮箱继续推断内部团队或汇报关系。

## 技术方向
GPU inference kernels、Attention、MoE、low precision、Blackwell performance。2026-09 的公开提交继续覆盖 cuTile fused MoE 的 MXFP4 / NVFP4 W4A4/W4A16 路径。

## 人物关系
- [[community/flashinfer-ai/FlashInfer/叶子豪 Zihao Ye|叶子豪（Zihao Ye）]]：**FlashInfer Full Codebase Approver 同僚**。截至 2026-09 两人共同承担全代码库审批与核心 kernel review。
- [[community/flashinfer-ai/FlashInfer/Jingfan Sun|Jingfan Sun]]：**FlashInfer Full Codebase Approver 同僚**。截至 2026-09 共同覆盖 Attention、GEMM、MoE、Communication 等关键模块。
- [[community/flashinfer-ai/FlashInfer/Yang Xu|Yang Xu]]：**FlashInfer Full Codebase Approver 同僚**。截至 2026-09 两人在 kernel / low-precision / release-quality 维护网络持续交叉。
- [[community/flashinfer-ai/FlashInfer/aleozlx|Alex Yang]]：**FlashInfer Full Codebase Approver 同僚**。截至 2026-09 同具跨模块 code review / approval 权限；公司 affiliation 可分别由各自公开 commit metadata 独立核验。

## Sources
- https://github.com/flashinfer-ai/flashinfer
- https://github.com/flashinfer-ai/flashinfer/commits?author=bkryu
- FlashInfer CODEOWNERS / maintainer metadata
