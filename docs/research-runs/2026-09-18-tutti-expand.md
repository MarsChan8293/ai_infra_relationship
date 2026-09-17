# Tutti EXPAND — 2026-09-18

## Execution boundary

- Operator: `EXPAND`
- Seed: `Tutti`
- Objective: expand a new GPU-storage / SSD-backed KV-cache frontier and connect it to the existing inference-optimization graph.
- Evidence policy: project repository, paper, USENIX, official faculty/profile pages, direct commits / PRs.

## Outcome

Status: `success` with one unresolved governance dimension.

### Added canonical nodes

1. `community/xPU-IO/xPU-IO`
2. `community/xPU-IO/Tutti/Tutti`
3. `university/厦门大学/GeminiFS`
4. `university/厦门大学/Shi Qiu`
5. `university/上海交通大学/张一鸣 Yiming Zhang`

### High-confidence edges / links

- Shi Qiu → Yiming Zhang: advisor + paper-coauthor + research-collaboration.
- Yiming Zhang → Shi Qiu: student + paper-coauthor + research-collaboration.
- GeminiFS → Tutti: direct technical / research lineage, based on the deprecated GeminiFS repository pointing to Tutti as its successor based on GeminiFS ideas.
- Tutti → vLLM: implemented KV connector / serving-engine integration.
- Tutti ↔ LMCache: benchmark / alternative-system relation only; no collaboration claim.
- Tutti → Mooncake: design-inspiration for the vendor-neutral GPU framework only; no shared-governance claim.
- Tutti → MetaX/MACA: direct hardware-port evidence from merged PR / commit; no company-ownership claim.

### Unresolved / intentionally not promoted

- Tutti formal maintainer roster / project governance remains unresolved. README provides a community contact but does not publish a formal maintainer list.
- xPU-IO is modeled as a GitHub technical community / organization, not a company.
- Tutti contact email domain is not promoted to current employment without separate evidence.

## Evidence

- https://arxiv.org/abs/2605.03375
- https://github.com/xPU-IO/Tutti
- https://github.com/nicexlab/GeminiFS
- https://www.usenix.org/conference/fast25/presentation/qiu
- https://www.qiushi.host/
- https://www.cs.sjtu.edu.cn/jiaoshiml/zhangyiming.html
- https://github.com/xPU-IO/Tutti/commit/8ffd81f294b85dadc80e40aa04a58b56d010bec7
- https://github.com/xPU-IO/Tutti/pull/11
- https://github.com/xPU-IO/Tutti/commit/2f1c7f91513f17cf157da5c159c635a71096d32c

## Follow-up VERIFY

Priorities for the next verification cycle:

1. formal Tutti governance / maintainers if a stable roster appears;
2. Shi Qiu current industry relationship, if any, separately from the public project contact email;
3. additional GeminiFS/Tutti recurring authors only when they add new graph connectivity rather than a flat paper-author fan-out.
