# AI Practice 项目集

> 探索 AI 前沿技术的实验场 —— 多 Agent 协作、AI 创意工具、智能编程助手技能开发

[![GitHub](https://img.shields.io/badge/GitHub-IceFoxH/AI__Practice-blue)](https://github.com/IceFoxH/AI_Practice)

---

## 📦 项目一览

| 项目 | 技术栈 | 说明 |
|------|--------|------|
| [CrewAI 多 Agent 系统](#crewai-多-agent-系统) | Python, CrewAI, DeepSeek | 多 Agent 协作与子代理层级模式 |
| [中文名生成器](#中文名生成器) | Node.js, DeepSeek API, HTML/CSS | 输入英文名，生成富含中国文化趣味的中文名 |
| [表情包生成器](#表情包生成器) | HTML/CSS/JS | 纯前端表情包制作工具 |
| [表情包生成器 (Cloudflare)](#表情包生成器-cloudflare-部署) | Cloudflare Workers, Coze Proxy | 表情包生成器的云端部署版 |
| [图片字幕生成器](#图片字幕生成器) | HTML/CSS/JS | 为图片添加字幕文字的在线工具 |
| [智能编程助手技能](#智能编程助手技能) | Trae/Claude Code Skills | 自定义技能开发与使用指南 |

---

## 🤖 CrewAI 多 Agent 系统

基于 [CrewAI](https://www.crewai.com/) 框架的多 Agent 协作实验。

- **`multi_agent.py`** — 多 Agent 顺序协作：研究员 → 分析师 → 撰稿人 流水线，使用 DeepSeek LLM
- **`multi_agent_parallel.py`** — 多 Agent 并行执行：多个 Agent 同时处理独立任务
- **`subagent_hierarchical.py`** — 子代理层级模式：主 Agent 动态委派子 Agent 执行子任务
- **`MULTI_AGENT_VS_SUBAGENT.md`** — 两种架构模式的深度对比分析

**运行方式：**

```bash
cd CrewAI
pip install crewai
export DEEPSEEK_API_KEY="sk-xxx"
python multi_agent.py
```

---

## 🇨🇳 中文名生成器

输入英文名，通过 DeepSeek API 生成 3 个富有中国文化特色的趣味中文名。

**技术栈：** Node.js + DeepSeek API + 纯前端 HTML

**功能：**
- 调用 DeepSeek 大模型生成中文名
- 每个名字包含中文寓意、英文解释、文化典故
- 融入诗词、网络梗等趣味元素

**运行方式：**

```bash
cd chinese-name-generator
# 修改 server.js 中的 API_KEY
node server.js
# 访问 http://localhost:3001
```

---

## 🎭 表情包生成器

纯前端表情包制作工具，在浏览器中直接添加文字生成自定义表情包图片。

- **`表情包生成器.html`** — 本地版，直接在浏览器打开使用
- **Cloudflare 部署版** — 通过 Cloudflare Workers + Coze Proxy 部署到云端

---

## 🖼️ 图片字幕生成器

为图片添加字幕/标题文字的在线工具，纯前端实现。

- **`subtitle_generator.html`** — 直接在浏览器打开使用

---

## 🧠 智能编程助手技能

为 Trae/Claude Code 开发的自定义技能系统。

### 已安装技能 (20+)

| 技能 | 功能 | 触发方式 |
|------|------|----------|
| `daily-report` | 自动生成工作日报，追加到日报.md | `/daily-report [补充内容]` |
| `brainstorming` | 需求分析与方案设计 | 自动触发 |
| `test-driven-development` | 测试驱动开发 | 自动触发 |
| `writing-skills` | 技能创建与开发 | 手动调用 |
| `writing-plans` | 多步骤任务规划 | 自动触发 |
| `systematic-debugging` | 系统化调试 | 自动触发 |
| `verification-before-completion` | 完成前验证 | 自动触发 |

### 使用指南文档

- **`superpowers-zh-使用指南.md`** — superpowers-zh 中文技能框架使用说明
- **`oh-my-claudecode使用指南.md`** — Oh-My-ClaudeCode 多 AI 编排插件使用说明

### 日报系统

- **`日报.md`** — 工作日报记录（2026年5月18日起）

---

## 🛠️ 通用设置

```bash
# Python 虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate    # Windows

# Node.js (中文名生成器)
cd chinese-name-generator
npm init -y
node server.js
```

---

## 📄 许可证

MIT © IceFoxH
