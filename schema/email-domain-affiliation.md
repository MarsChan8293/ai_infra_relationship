# 公开邮箱域名 → 公司关联推断规则

本仓库允许把**公开、可验证的职业邮箱域名**作为人物与组织之间的一类强证据，但这条证据有明确边界：它证明“这个人物在公开技术/职业上下文中使用过该组织域名邮箱”，不自动等价于“当前仍在该公司任职”。

## 数据流

1. 人物页先有 `public_email:`。邮箱必须来自可核验公开来源，例如官方主页、论文、公开项目 commit / Signed-off-by / Co-authored-by、MAINTAINERS 或治理记录。
2. `scripts/sync-entity-people.py` 读取 `schema/email-domain-company.json`。
3. 仅当邮箱域名命中 allowlist 时，脚本生成 `email_affiliations:`。
4. `current_affiliations:` 与 `email_affiliations:` 的公司节点并集生成 `linked_companies:`。
5. 同一并集反向写入公司节点 `linked_people:`，从而得到稳定的 人物 ↔ 公司 双向关系。
6. `scripts/audit-entity-reverse-links.py` 校验公司 `linked_people:` 与人物 `linked_companies:` 是否一致。

## 证据等级与边界

- `@company.com` 这类经确认属于公司的职业域名：可生成 organization association。
- 公司子域名，例如 `@china.huawei.com`：只有当父域名已在 allowlist 中时才按最长后缀规则继承。
- 子公司 / 芯片业务域名：只有配置明确指定 canonical parent company 时才归并。例如本图谱把 `hisilicon.com` 映射到 canonical `华为` 节点。
- Gmail、QQ、Outlook、163、126、GitHub noreply 等个人/匿名邮箱：**不能**推出公司。
- 合作伙伴、外包、供应商域名不能因为经常出现在某公司的开源项目里就映射为该公司。
- 不扫描正文里任意 email-like 字符串做自动推断。自动规则只读取结构化 `public_email:`，避免把引用、共同作者或第三方邮箱错挂到当前人物。

## 为什么不用邮箱直接覆盖 `current_affiliations`

邮箱可能来自历史 commit。一个人在 2024 年使用 `@example.com`，不能单凭这条记录断言 2026 年仍在该公司。因此：

- `current_affiliations:`：人类/Agent 基于当前公开证据维护的“当前 affiliation”。
- `email_affiliations:`：自动生成的“邮箱域名组织关联”。
- `linked_companies:`：两者的 canonical company 并集，用于图谱遍历。
- 公司 `linked_people:`：同一并集的反向镜像，并在自动正文里标出证据来自当前 affiliation、邮箱域名，或两者都有。

## 增加新的域名规则

编辑 `schema/email-domain-company.json`，只加入已经核验域名所有权、且目标公司节点已存在的规则。不要根据“公司名看起来像域名”猜映射。

推荐检查顺序：

1. 公司官方站点 / 开源组织资料确认域名归属。
2. 至少一条公开人物证据中实际出现该域名邮箱。
3. 确认应落到哪个 canonical company node，尤其注意子公司、研究院、收购前品牌和业务线。
4. 修改映射后运行：

```bash
python3 scripts/sync-entity-people.py --root .
python3 scripts/audit-entity-reverse-links.py --root . --generated generated
python3 scripts/audit-graph.py --root . --output generated
python3 scripts/generate-node-schemas.py --root . --nodes generated/nodes.json --output schema/nodes --manifest schema/node-manifest.json
```

GitHub Actions 的 `Sync Node Schemas` 工作流也会执行同样的同步和校验。
