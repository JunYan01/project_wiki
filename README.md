# Project Wiki

> 聚合多个代码仓库，用 [graphify](https://github.com/safishamsi/graphify) 为每个仓库生成可查询的知识图谱——作为理解、学习、参考代码的统一入口。

`project_wiki` 本身不含业务代码。它用 **git submodule** 把多个独立仓库挂进来统一管理，并对每个仓库跑 graphify，把代码/文档/图片解析成「节点 + 关系」的知识图谱（`graph.json`），之后**按需查询**而非反复通读源码。

## 包含的仓库

| 仓库 | 简介 | 知识图谱规模 |
|---|---|---|
| [pi](https://github.com/earendil-works/pi) | earendil-works 的 coding agent | `graphify-out-pi/` · 6,366 节点 / 626 社区 |
| [hermes-agent](https://github.com/NousResearch/hermes-agent) | NousResearch 的 agent 框架 | `graphify-out-hermes-agent/` · 29,368 节点 / 755 社区 |
| [openclaw](https://github.com/openclaw/openclaw) | openclaw | `graphify-out-openclaw/` · 56,813 节点 / 7,111 社区 |
| [graphify](https://github.com/safishamsi/graphify) | 本项目所用工具（自身作为 submodule） | — |

## 目录结构

```
project_wiki/
├── openclaw/  hermes-agent/  graphify/  pi/        # submodule 指针（源码）
├── graphify-out-pi/  -hermes-agent/  -openclaw/   # 知识图谱产物（普通目录，提交进 git）
├── WORKFLOW.md       # 完整工作流（submodule / graphify / 多图谱切换）
├── task_steps.md     # 步骤记录 + 踩坑 + 竞品对比
└── CLAUDE.md         # 工具偏好（uv > pip）
```

## 快速开始

```bash
# 1. 克隆（含子模块）
git clone --recurse-submodules git@github.com:JunYan01/project_wiki.git
cd project_wiki
# 已克隆但子模块为空时补拉：
git submodule update --init --recursive

# 2. Python 环境（用 uv，不用 pip）
uv venv --python 3.12
uv init --bare
uv add --editable "./graphify[all]"
uv run graphify install        # 把 graphify skill 注册到 Claude Code
```

> 大仓库（如 openclaw）用 `git submodule update --remote` 会拉海量历史、慢链路易卡死；改用 shallow fetch 只拉最新，见 [WORKFLOW.md §4.4](WORKFLOW.md)。

## 查询知识图谱

```bash
# 关键词 BFS 遍历（用图谱里真实存在的英文实体名/函数名/文件名）
uv run graphify query "AgentSession" --graph graphify-out-pi/graph.json
uv run graphify query "SettingsManager" --graph graphify-out-pi/graph.json --budget 600
```

查哪个仓库就 `--graph graphify-out-<repo>/graph.json` 指过去。**整体架构**看各仓的 `GRAPH_REPORT.md` 与可视化 `graph.html`。

在 **Claude Code** 里也可以直接用自然语言问（如「pi 里 AgentSession 连着什么」），会自动选对应图谱遍历。

## 更新图谱（增量）

仓库演化后不必全量重建。拉取子模块最新后，增量更新对应图谱（仅重提取变更文件，复用缓存）：

```bash
git -C <repo> fetch --depth=1 origin main && git -C <repo> checkout FETCH_HEAD   # 拉最新
uv run graphify <repo> --update        # 仅重提变更文件，合并进现有图谱
git commit -am "增量更新 <repo> 知识图谱"
```

> 纯代码变更的 AST 重建本地完成、不走 LLM；文档 / 图片变更才走语义提取。详见 [WORKFLOW.md §5.3](WORKFLOW.md)。

## 我们的需求与工具结论

本项目围绕以下需求组织——graphify 是"长期深挖 + 增量维护"的主线，其余按场景补充：

**需求：**
1. 学习 / 理解仓库（当前主场景）
2. 长期精确深挖（调用关系、影响面、概念关联）
3. 多仓参考（未来开新项目时参考 N 个仓）
4. 跨仓查询（真实需求，暂搁置——等 graphify `global_add` 成熟或外部方案）
5. 增量同步演化（仓库演化后低成本更新图谱）

**结论（按需求选工具）：**

| 需求 | 推荐 | 一句话理由 |
|---|---|---|
| 学习 / 理解陌生仓 | [DeepWiki](https://deepwiki.com)（`github.com`→`deepwiki.com`）| 免费托管，秒出架构 wiki，零安装 |
| 长期深挖 + 增量维护 | **graphify**（本项目主线）| 精确语义 + 多模态；查询约 71× 压缩；`--update` 仅重提变更文件 |
| 多仓代码导航 / review | [code-review-graph](https://github.com/tirth8205/code-review-graph) | 纯 AST 无 LLM，原生多仓 |
| 让 AI 实时查某仓 | [GitMCP](https://github.com/idosal/git-mcp)（`github.com`→`gitmcp.io`）| 零安装 MCP server |
| 一次性塞给 AI | [Repomix](https://repomix.com) / [Gitingest](https://gitingest.com) | 扁平打包，简单 |
| 跨仓查询 | 暂搁置 | graphify `global_add` 有 bug，等成熟 |

> 完整竞品分析（全景对比 + token 经济账 + 增量 / 缓存维度 + 各工具详解）见 [COMPARISON.md](COMPARISON.md)。

## 相关文档

- **[COMPARISON.md](COMPARISON.md)** — graphify 竞品全景对比与选型决策
- **[WORKFLOW.md](WORKFLOW.md)** — submodule 更新（含大仓 shallow fetch）、graphify 断点续处理、多图谱切换、增量更新
- **[task_steps.md](task_steps.md)** — 已完成步骤、踩坑记录
- **[CLAUDE.md](CLAUDE.md)** — 工具偏好与约定
