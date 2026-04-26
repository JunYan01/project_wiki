# Task Steps

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
