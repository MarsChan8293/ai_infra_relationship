---
type: project
name: deepseek-recipe
linked_people: []
companies: ["深度求索"]
company_relation: company-led
layer: serving-api-adapter
open_source: true
repository: https://github.com/deepseek-ai/deepseek-recipe
areas: [llm-serving, api-protocol, prompt-encoding, response-parsing, rust, python, multimodal]
last_verified: "2026-09"
linked_companies:
  - "company/深度求索/深度求索"
---
# deepseek-recipe

deepseek-recipe 是 DeepSeek 2026-09 开源的 serving glue layer：用 Rust libraries + Python bindings 将不同 API request 格式统一转换为内部 Conversation 表示，再编码为 DeepSeek V4 / V4.1 prompt，并把模型输出转换回对应 API response。

## 技术定位
支持 Messages、Chat Completions、Responses、streaming response、thinking、client tool calls 与 V4.1 image preprocessing。README 明确说明 **model inference、tool execution、HTTP transport 由外部提供**，因此它不是 inference engine，而是 API service 与 inference backend 之间的 protocol / encoding adapter。

## 初始贡献线索
初始提交公开 co-author trailers：`xinchengxx`、`XieJiSS`、`yqaty`、`zhu-he`、`season-guo`，均使用公开 `@deepseek.com` 地址。当前缺少稳定实名消歧，本轮不创建人物节点，也不把 handle 自动视作 maintainer。

## Sources
- https://github.com/deepseek-ai/deepseek-recipe
- https://github.com/deepseek-ai/deepseek-recipe/blob/main/README.md
- https://github.com/deepseek-ai/deepseek-recipe/commit/57b9c842429d850b03b5fdbe3fed266c13cc7f2b

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
