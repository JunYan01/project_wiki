# 知识图谱工具竞品分析（COMPARISON）

> 本项目用 graphify 做"长期深挖 + 增量维护"的精确知识图谱。本文记录市面同类工具的全景对比与选型决策，供未来切换 / 扩展时参考。
>
> 调研时间：2026-06。这类工具迭代快，结论按需复核。

## 1. 我们的需求（选型出发点）

| # | 需求 | 说明 |
|---|---|---|
| 1 | 学习 / 理解仓库 | 快速搞懂陌生仓的架构、模块、关键组件（**当前主场景**）|
| 2 | 长期精确深挖 | 对持续维护的仓做精确查询：调用关系、影响面、概念关联 |
| 3 | 多仓参考 | 开新项目时参考 N 个相关仓库，从图谱学习 |
| 4 | 跨仓查询 | 跨仓库找关联 / 共用模式（真实需求，**暂搁置**）|
| 5 | 增量同步演化 | 仓库演化后低成本更新图谱，而非全量重建 |

## 2. 全景对比

| 工具 | 类型 | 建图成本 | 查询成本 | 精度/语义 | 多仓 | 多模态 | 增量/缓存 |
|---|---|---|---|---|---|---|---|
| **[graphify](https://github.com/safishamsi/graphify)** | 本地 KG（重）| 🔴 高（LLM 逐 chunk 语义）| 🟢 极低（~71× 压缩）| 🟢 高（AST + 语义推断）| 🟡 弱（`global_add` 有 bug）| ✅ 强（代码+文档+图+PDF）| ✅ `--update` + 缓存 |
| **[code-review-graph](https://github.com/tirth8205/code-review-graph)** | 本地 KG（轻）| 🟢 低（纯 AST，无 LLM）| 🟢 低 | 🟡 中（结构关系）| ✅ 原生（registry + daemon）| ❌ 纯代码 | ✅ 变更检测 + watch |
| **[graphify-rs](https://github.com/TtTRz/graphify-rs)** | 本地 KG（快）| 🟡 中（比 graphify 快 8.5×）| 🟢 低 | 🟢 同 graphify | 🟡 弱 | ✅ | ✅ |
| **[DeepWiki](https://deepwiki.com)** | 托管 wiki（URL 改写）| ⚪ 0（托管免费）| ⚪ 0（读 wiki）| 🟡 中（AI 生成文档 + 架构图）| 按 URL | 部分 | ❌ 每次从头生成 |
| **[GitMCP](https://github.com/idosal/git-mcp)** | 托管 MCP（URL 改写）| ⚪ 0 | 🟢 低（按需取）| 🟡 中 | 按 URL | 部分 | ⚪ 始终取最新 |
| **[Repomix](https://repomix.com) / [Gitingest](https://gitingest.com)** | 扁平打包 | 🟢 极低 | 🔴 高（每次全量塞）| 🔴 低（无结构）| 手动 | ❌ | ❌ |

> URL 改写类用法：`github.com/owner/repo` → `deepwiki.com/...`（人类读的 wiki）/ `gitmcp.io/...`（AI 查的 MCP）/ `gitingest.com/...`（扁平文本）。

## 3. Token 经济账（回答"graphify 重，长远省不省 token"）

关键：**建图成本**和**查询成本**是分开的。

- **建图贵**：graphify 语义提取 LLM 逐 chunk 跑，pi 一个仓烧约 **2.77M tokens**（一次性，可 `--update` 增量）。
- **查询极便宜**：建好后每次查询只返回几百 tokens，对比全量代码（pi 源码约 1-2M tokens），单次查询省 ~99%（官方称混合语料 **71× 压缩**）。
- **增量更新便宜**：仓库演化后 `--update` 仅重提变更文件，纯代码变更 AST 本地重建不走 LLM。

**Break-even 结论：**
- 同一仓**查询几十次以上**（自己的活跃项目、长期维护）→ graphify 划算，建图成本几次查询即回本，之后纯省。**这正是本项目用 graphify 的理由。**
- 只是**学习 / 参考**一个仓（读架构、问几个问题就放）→ graphify **亏**；这种场景 **DeepWiki 免费托管**更合适。
- 第三方数据点：代码知识图谱相对"全量塞"可省 **40-95% token**。

## 4. 增量 / 缓存维度（长期维护关键）

仓库会演化，全量重建不可持续。各工具的增量能力：

| 工具 | 增量机制 |
|---|---|
| graphify | `--update` 仅重提变更文件（`.graphify_cached.json` 缓存未变文件）；纯代码 AST 重建无 LLM；`--watch` / git post-commit hook 自动重建 |
| code-review-graph | `detect_changes` 变更检测 + 风险评分；daemon `--auto-watch` 持续跟踪 |
| DeepWiki / GitMCP | 托管方每次从头生成 / 始终取最新——对用户零成本，但无本地缓存可复用 |
| Repomix / Gitingest | 无增量概念，每次全量打包 |

> 本项目长期维护 = **submodule 拉最新 → `graphify <repo> --update` → 提交产物**（见 [WORKFLOW.md §5.3](WORKFLOW.md)）。

## 5. 各工具详解

### graphify（本项目主线）
AST（tree-sitter，本地、免费）+ LLM 语义提取（调用 / 共享数据 / 概念关联 / 多模态）→ NetworkX 图 + Leiden 社区聚类。输出 `graph.json` / `graph.html` / `GRAPH_REPORT.md`，查询走 BFS/DFS。**强**：多模态同图、语义推断、查询省 token。**弱**：建图贵、大仓扩展性有反馈（openclaw 56K 节点能跑但要并发控制）、多仓合并 `global_add` 当前有 labels/community bug。

### code-review-graph
纯 AST 结构图谱，存 SQLite，MCP + CLI + VS Code 扩展。**强**：无 LLM 零 token 建图、原生多仓 registry/daemon、变更检测 + 风险评分、token 节省估算、13+ 平台。**弱**：无语义推断、纯代码（不处理文档/图）。**适合**本项目"多仓代码导航 / review"与搁置的跨仓需求。

### graphify-rs
graphify 的 Rust 重写，同数据格式，提取快 8.5×。想用 graphify 但嫌慢时的替代。

### DeepWiki
Cognition / Devin 出品，`github.com/x/y` → `deepwiki.com/x/y`，秒生成架构图 + 文档 + 可对话 wiki，免费。**适合**学习陌生仓。有开源可自托管版 DeepWiki-Open。**注意**：AI 生成内容质量随仓库而异，混入人工内容时准确性需核验。

### GitMCP
`github.com/x/y` → `gitmcp.io/x/y`，为任意 GitHub 仓即时起一个 MCP server，AI 助手（Cursor / Claude 等）按需查仓、始终最新。**适合**让 AI 实时查某仓而不本地建图。

### Repomix / Gitingest
把整个仓打包成单个 AI 友好文件（Gitingest 走 URL 改写，Repomix 本地 `npx`）。简单但 token 重、无结构、每次全量。**适合**一次性塞给 AI。

## 6. 选型决策（按需求 → 工具）

| 需求 | 选 | 备注 |
|---|---|---|
| 学习 / 理解陌生仓 | DeepWiki | 免费、秒出、零安装 |
| 长期深挖 + 增量维护（本项目主线）| **graphify** | 精确 + 多模态 + 增量 |
| 多仓代码导航 / review | code-review-graph | 轻 + 原生多仓 |
| 让 AI 实时查仓 | GitMCP | MCP 零安装 |
| 一次性塞给 AI | Repomix / Gitingest | 简单 |
| 跨仓查询 | 暂搁置 | 等 `global_add` 成熟 |

**本项目策略**：已建好的 pi / hermes / openclaw 图谱继续用 graphify 查（沉没成本 + 增量维护）；未来学新仓先用 DeepWiki 快速 skim，确认要长期深挖再上 graphify；出现明确多仓需求时评估 code-review-graph。

## 7. 来源

- [graphify 官网](https://graphify.net) · [graphify GitHub](https://github.com/safishamsi/graphify) · [graphify issues（global_add bug）](https://zread.ai/safishamsi/graphify/6-issues-and-feedbacks)
- [code-review-graph GitHub](https://github.com/tirth8205/code-review-graph) · [架构 / 多仓 / 省 token 文档](https://zread.ai/tirth8205/code-review-graph)
- [graphify-rs](https://github.com/TtTRz/graphify-rs)
- [DeepWiki (Cognition / Devin)](https://docs.devin.ai/work-with-devin/deepwiki)
- [GitMCP](https://github.com/idosal/git-mcp)
- [Gitingest](https://gitingest.com) · [Repomix](https://repomix.com)
- [代码知识图谱省 40-95% token](https://medium.com/@jakenesler/context-compression-to-reduce-llm-costs-and-frequency-of-hitting-limits-e11d43a26589) · [KG 提升代码生成 (arXiv)](https://arxiv.org/html/2505.14394v1)
- [graphify vs code-review-graph (Reddit)](https://www.reddit.com/r/ClaudeCode/comments/1sme1zw/graphify_vs_codereviewgraph_which_is_better_for/)
