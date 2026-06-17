# Task Steps

> **用途**：记录项目中所有已完成的工作步骤，供新 session 恢复上下文。
> **更新时机**：每完成一个步骤后立即追加，保持同步。
> **推广模式**：可复制本文件到任何项目，按以下模板填写。
>
> **模板**：
> ```
> ## <任务名称> (<开始日期>)
> ### 1. <步骤标题>
> - 目标：<做什么>
> - 环境约束：<系统版本、工具版本、路径>
> - 执行命令：<实际运行的命令>
> - 结果：<产出文件、数据量、关键指标>
> - 失败/踩坑记录：<遇到的错误和解决方案>
>
> ### 2. <下一个步骤> ...
> ```
>
> **断点续处理规则**（适用于 graphify 等大规模分块任务）：
> - 使用 JSON 进度文件追踪已完成的 chunk（如 `.graphify_progress.json`）
> - 每个 chunk 的结果独立写入文件（如 `.chunk_result_N.json`）
> - 合并脚本统一合并去重（如 `merge_chunk.py`）
> - 并发度按需控制（串行=1 或并行=N）
> - 每 chunk 完成后 compress 上下文，避免上下文溢出
> - 不预读下一个 chunk 的内容

**Claude Code 记忆迁移**（跨机器/新 session）：
- 记忆文件位置：`~/.claude/projects/<项目绝对路径>/memory/`（不在项目 repo 内）
- 方案 1：将 `memory/` 目录整体复制到新机器的对应路径
- 方案 2：将关键上下文写入项目 repo 中的 `CLAUDE.md`（git pull 后自动生效）
- 方案 3：在新 session 中手动 `/remember` 重建记忆
- 注意：`task_steps.md` 本身已在 repo 中，可替代部分记忆功能

---

## Submodule 管理 (2026-04-26)

- `graphify` → `https://github.com/safishamsi/graphify.git`
- `hermes-agent` → `git@github.com:NousResearch/hermes-agent.git`
- `openclaw` → `git@github.com:openclaw/openclaw.git`

更新命令：`git submodule update --remote`

---

## Graphify 安装 (2026-04-09)

### 1. 克隆仓库

```bash
git clone https://github.com/safishamsi/graphify.git
```

仓库克隆至 `/Users/openclaw1/Developer/project_wiki/graphify`。

### 2. 检查环境

- 系统自带 Python 3.9.6（路径 `/usr/bin/python3`），不满足 graphify 要求的 Python 3.10+
- 确认已安装 `uv`（路径 `~/.local/bin/uv`，版本 0.10.10），优先使用

### 3. 创建虚拟环境

```bash
uv venv
```

在项目目录创建了 `.venv`，使用 CPython 3.12.13。

### 4. 安装 graphify 及全部依赖

```bash
uv pip install -e "./graphify[all]"
```

以可编辑模式安装，共安装 96 个包，包括 tree-sitter（20 种语言）、networkx、graspologic（Leiden 社区检测）、mcp、neo4j、pypdf 等全部可选依赖。

### 5. 创建 CLAUDE.md

在项目根目录创建 `CLAUDE.md`，写入工具偏好：优先使用 `uv` 而非 `pip`。

### 6. 创建 task_steps.md

记录所有已完成的工作步骤（即本文件）。

### 7. Graphify hermes-agent 知识图谱提取

- 目标：对 `hermes-agent/` 目录运行 graphify 知识图谱提取
- 输出目录：`graphify-out/`（与 openclaw 的 `graphify-out-openclaw/` 分开）
- 77 个 chunk，每个约 22 个文件
- AST 提取已完成：27,692 nodes, 101,523 edges
- 语义提取：通过 Agent 子代理逐 chunk 深度提取（非本地 regex 脚本）
- **重要规则**：
  - 并发度为 1（逐个 chunk 串行处理）
  - 每个 chunk 完成后，compress 一次上下文
  - 不要预读下一个 chunk 的文件列表来加速（会影响上下文）
  - Agent 将结果写入 `graphify-out/.chunk_result_N.json`，然后用 `merge_chunk.py` 合并
  - 进度追踪：`graphify-out/.graphify_progress.json`
- **结果**：
  - 全部 77 chunks 已完成（deep Agent 语义提取）
  - AST + semantic 合并：29,573 nodes, 104,426 edges, 152 hyperedges
  - 图谱构建：29,368 nodes, 66,153 edges, 755 communities（Leiden 聚类）
  - 社区自动标签：基于源文件目录路径生成
  - 报告：`graphify-out/GRAPH_REPORT.md`（253K chars）
  - HTML 可视化：`graphify-out/graph.html`（社区级元图谱，755 nodes, 420 edges）

### 8. 注册 graphify 到 AI 编码助手

```bash
uv run graphify install
```

将 graphify skill 注册到当前平台（Claude Code）。

---

## WORKFLOW.md 与 Submodule 更新 (2026-06-18)

### 1. 创建 WORKFLOW.md
- 目标：整理 project_wiki 工作流说明，供温习 / 新 session 恢复上下文
- 结果：WORKFLOW.md（项目定位 / 目录结构 / submodule 工作流 / graphify 工作流 / 命令速查）

### 2. 更新三个 submodule 到各仓库最新
- 目标：openclaw / hermes-agent / graphify 拉到最新
- hermes-agent、graphify：`git submodule update --remote` 成功（完整 fetch）
- **openclaw 卡住的根因（踩坑记录）**：
  - openclaw 是巨型仓库：41715 commits、1.6GB `.git`、单次 fetch pack 含 ~40 万对象
  - `github.com` 被解析到中转 IP `44.0.0.89`（非官方段 `140.82.x` / `192.30.x` / `20.205.x`）
  - 小请求（SSH 握手、`ssh -T` 认证）秒过，但 40 万对象的大 pack 经中转链路传输极易卡死
  - 表现：`git index-pack` 进程 CPU 长期不动（ELAPSED 数分钟、CPU 仅几秒），`.git/objects/pack/` 出现数百 MB 临时 pack
  - 误判教训：后台 fetch 任务的 exit code 可能是脚本**最后一条命令**的（如 `git status`=0），不代表 submodule update 成功；要看 `git submodule status` 的实际 commit
- **解决：shallow fetch 只拉最新（不要历史）**
  ```bash
  git -C openclaw fetch --depth=1 origin main   # 默认分支用 symbolic-ref refs/remotes/origin/HEAD 查
  git -C openclaw checkout FETCH_HEAD
  ```
  - 结果：openclaw `f4e6322` → `baa389e`，**几秒完成**（数据量从近 1GB 降到几十 MB）
  - 已写入 WORKFLOW.md §4.4

### 3. 其他变更
- `.gitignore` 增加 `.obsidian/`（编辑器本地配置）
- 新增 `agent_memory_system_by_ff/`（Agent 记忆系统教程 PDF：Mem0 / Letta / GBrain）
- 修复 openclaw 子模块工作区 18 个 `CLAUDE.md` 被平台展开为普通文件（原本是指向 `AGENTS.md` 的 symlink），`git restore` 恢复
- 提交：`ea9a588`、`f29af92`，已 push origin/main

### 4. 待办（可选）
- openclaw 本地 `.git` 仍有 1.6GB 旧历史（shallow 只浅拉了增量更新，没删旧历史）。若要彻底精简需额外清理（`git gc` / 删 `.git` 重浅 clone）——destructive，待确认。

### 5. 添加 pi submodule
- 新增 submodule：`https://github.com/earendil-works/pi`
- 命令：`git submodule add --depth=1 https://github.com/earendil-works/pi`（shallow clone，默认目录名=仓库名 `pi`）
- 结果：pi `.git` 仅 **4.0K**（对比 openclaw 1.6GB），856 个 tracked files，最新 commit `6d5ede3`
