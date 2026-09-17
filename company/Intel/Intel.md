---
type: company
name: Intel
linked_people:
  - "community/LMCache/LMCache/Tony Lin"
linked_projects:
  - "company/Intel/xFasterTransformer"
  - "company/Intel/OpenVINO"
  - "company/Intel/OpenVINO GenAI"
---
# Intel

## 公司简介
Intel 是 CPU、数据中心与 AI 加速器厂商。在本图谱中重点关注其与开源 LLM inference、KV cache、非 CUDA 平台适配、存储与内存层次优化相关的工程贡献。

## 当前推理项目
- [[company/Intel/xFasterTransformer|xFasterTransformer]]：Intel GitHub organization 下的 LLM inference runtime，面向 Xeon / x86，支持多 socket / 多节点与 `vllm-xft` serving；2026 年仍持续 release。
- [[company/Intel/OpenVINO|OpenVINO]]：Intel 官方持续发布的跨 CPU / GPU / NPU inference toolkit；2026.x 继续扩展 GenAI / LLM 能力。
- [[company/Intel/OpenVINO GenAI|OpenVINO GenAI]]：OpenVINO 上层生成式 AI inference library，覆盖 continuous batching、prefix caching / KV cache、speculative decoding、sparse attention 等直接 serving 优化能力。

这些边使用 Intel 官方项目 / GitHub organization / 官方产品资料作为 origin 或治理证据，不因为第三方软件“兼容 Intel”就反推成 Intel 项目。

## 历史项目边界
Neural Speed、Intel Extension for Transformers 已在 2024 年归档；Intel Extension for PyTorch 也在 2026 年结束主动开发并归档。它们仍有历史人才 / 技术价值，但本轮 DISCOVER 的 `projects` frontier 以**当前仍活跃**的 inference 项目为主，不用归档仓库填覆盖率。

## LMCache 连接
- [[community/LMCache/LMCache/Tony Lin|Tony Lin]]：LMCache CODEOWNER；公开提交使用 `tony.lin@intel.com`，覆盖 vLLM integration、GPU connector、distributed eviction、platform 与 storage backend 等路径。

这里记录的是可核验的人员/工程关联，不因单个员工贡献自动推断 Intel 对 LMCache 的治理或所有权。

## Sources
- https://github.com/intel/xFasterTransformer
- https://github.com/intel/xFasterTransformer/releases
- https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html
- https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/whats-new.html
- https://github.com/openvinotoolkit/openvino
- https://github.com/openvinotoolkit/openvino.genai
- https://github.com/intel/neural-speed
- https://github.com/intel/intel-extension-for-transformers
- https://github.com/intel/intel-extension-for-pytorch
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://github.com/LMCache/LMCache/commit/10ad9e42d39d513e86647519c30d93a162334c66

<!-- BEGIN AUTO COMPANY PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `current_affiliations:` 与/或 `public_email` 企业域名规则反向汇总。邮箱域名证据表示可核验的组织关联，但不会单独推断当前任职、职级、直属汇报或团队归属。

- [[community/LMCache/LMCache/Tony Lin|Tony Lin]]：当前 affiliation + 公开职业邮箱域名双重证据。

<!-- END AUTO COMPANY PEOPLE -->
