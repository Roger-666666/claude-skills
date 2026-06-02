# 🛡️ Claude Code 技能合集 - 双语版 (中/英)

[![GitHub stars](https://img.shields.io/github/stars/Roger-666666/claude-skills-bilingual-codex?style=social)](https://github.com/Roger-666666/claude-skills-bilingual-codex/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Roger-666666/claude-skills-bilingual-codex?style=social)](https://github.com/Roger-666666/claude-skills-bilingual-codex/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Roger-666666/claude-skills-bilingual-codex)](https://github.com/Roger-666666/claude-skills-bilingual-codex/issues)
[![GitHub license](https://img.shields.io/github/license/Roger-666666/claude-skills-bilingual-codex)](https://github.com/Roger-666666/claude-skills-bilingual-codex/blob/main/LICENSE)

欢迎来到 **Claude Code 技能合集** - 一个全面的、双语（中/英）结构化 AI 技能库，专为 **Claude CLI**、**Claude Code** 和 **OpenAI Codex** 优化。

---

## 📖 快速导航

- **[English Documentation / 英文文档](README.md)**
- **[中文文档](README_CN.md)** (当前)
- **[安装指南](INSTALL.md)**
- **[使用指南](USAGE.md)**
- **[完整总结](SUMMARY.md)**

---

## 🎯 本仓库提供什么

本仓库提供了一个完整的双语技能系统，旨在增强 AI 辅助编码和任务处理能力。无论你使用 Claude CLI、Claude Code 还是 OpenAI Codex，这些技能都将显著提高你的生产力和 AI 生成输出的质量。

### 核心特性

- **🌐 完整双语支持**：所有文档、技能和脚本都有完整的中英文版本
- **🔄 轻松语言切换**：一条命令即可在中英文之间切换
- **⚡ 专为 Claude 优化**：专为 Claude CLI 和 Claude Code 工作流设计
- **🤖 多 Agent 框架**：用于复杂任务处理的高级思维框架
- **📊 Web 看板界面**：用于任务管理和监控的可视化界面
- **🔧 CLI 工具**：用于自动化任务处理的命令行工具
- **📝 全面文档**：详细的指南、示例和 API 参考

---

## 🛠️ 可用技能

### 1️⃣ 深度提示词创作助手 (Prompt Deep Creator)

**将模糊想法转化为专业、结构化的提示词**

这个技能将你零散、口语化甚至模糊的创意想法，转化为高质量、结构清晰、可直接使用的正式提示词。

#### 功能特点
- **智能要素提取**：自动识别核心目标、目标受众、风格偏好和约束条件
- **结构化输出生成**：创建包含角色设定、任务背景、核心目标和禁止事项的标准化模板
- **智能追问**：当输入信息不足时，主动引导你补充关键要素
- **多语言支持**：在中英文环境中无缝工作

#### 适用场景
- **内容创作**：技术博客、深度文章、研究论文、文档编写
- **商业规划**：商业方案、产品需求文档 (PRD)、项目计划
- **学术写作**：研究论文、论文陈述、文献综述
- **创意写作**：故事、剧本、营销文案、社交媒体内容

#### 安装方法
1. 下载 `prompt-deep-creator.zip` 并解压
2. 将 `skill.md` 内容复制到你的 Claude 预设指令中，或将解压后的文件夹放入软件的 `skills` 目录
3. 如果使用 `skills.json` 管理，请添加对应路径

---

### 2️⃣ 三省六部 · 多Agent思维框架 (Sansheng)

**通用任务处理行政系统**

这是一个复杂的多 Agent 思维框架，按照中国传统行政体系"三省六部"来结构化处理任何复杂任务。它通过分拣、规划、审议、派发、执行、汇总的严格工作流程，确保任务得到彻底处理。

#### 功能特点
- **太子 · 接旨分拣**：判断任务类型并提取核心需求
- **中书省 · 起草方案**：制定具体、可执行的方案（拒绝空话）
- **门下省 · 审议把关**：**核心特色** - 不合格的方案会被直接"封驳"并给出详细反馈
- **六部 · 实际执行**：专业部门产出实际成果：
  - **户部**：数据分析、资源管理、预算统计
  - **礼部**：文档撰写、规范制定、沟通协调
  - **兵部**：工程开发、代码实现、技术方案
  - **刑部**：安全审计、合规检查、风险评估
  - **工部**：基础设施、部署运维、自动化脚本
  - **吏部**：人事协调、团队管理、资源调配

#### 安装方法
1. 下载技能包并解压
2. **CLI 模式**：
   - 确保安装了 Python 3
   - 在终端运行 `python3 edict.py '{"task":"任务内容"}'` 即可触发流转
3. **Web 看板模式**：
   - 运行 `python3 scripts/serve.py` 启动可视化界面（访问 127.0.0.1:7891）

---

## 📥 安装与配置

### 🤖 Claude Code 安装

Claude Code 是 Anthropic 官方的 Claude CLI 工具。这些技能专为 Claude Code 工作流优化。

#### 方法 1：全局安装（推荐）
```bash
# 1. 创建技能目录
mkdir -p ~/.claude/skills

# 2. 克隆仓库
git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git ~/.claude/skills/claude-skills-bilingual-codex

# 3. 添加到你的 Claude Code 设置（~/.claude/settings.json）：
```

```json
{
  "skills": [
    {
      "name": "sansheng",
      "path": "~/.claude/skills/claude-skills-bilingual-codex/SKILL.md"
    },
    {
      "name": "prompt-deep-creator",
      "path": "~/.claude/skills/claude-skills-bilingual-codex/prompt-deep-creator/skill.md"
    }
  ]
}
```

#### 方法 2：项目特定安装
```bash
# 1. 进入你的项目目录
cd your-project

# 2. 创建本地技能目录
mkdir -p .claude/skills

# 3. 克隆或复制技能
git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git .claude/skills/claude-skills-bilingual-codex

# 4. 创建项目特定设置（.claude/settings.json）：
```

```json
{
  "skills": [
    {
      "name": "sansheng",
      "path": ".claude/skills/claude-skills-bilingual-codex/SKILL.md"
    },
    {
      "name": "prompt-deep-creator",
      "path": ".claude/skills/claude-skills-bilingual-codex/prompt-deep-creator/skill.md"
    }
  ]
}
```

#### 方法 3：使用 Claude Code CLI
```bash
# 使用 Claude Code 内置命令安装技能
claude skills install

# 或通过 Claude Code 交互模式手动添加
claude
# 然后输入：/skills add ~/.claude/skills/claude-skills-bilingual-codex/SKILL.md
```

---

### 🔧 OpenAI Codex 安装

OpenAI Codex 是 OpenAI 的代码生成模型。这些技能可以适配 Codex 工作流。

#### 方法 1：Codex CLI 集成
```bash
# 1. 安装 Codex CLI（如果尚未安装）
npm install -g @openai/codex

# 2. 创建 Codex 技能目录
mkdir -p ~/.codex/skills

# 3. 克隆仓库
git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git ~/.codex/skills/claude-skills-bilingual-codex

# 4. 创建 Codex 配置（~/.codex/config.json）：
```

```json
{
  "skills": {
    "sansheng": {
      "path": "~/.codex/skills/claude-skills-bilingual-codex/SKILL.md",
      "description": "三省六部多Agent思维框架"
    },
    "prompt-deep-creator": {
      "path": "~/.codex/skills/claude-skills-bilingual-codex/prompt-deep-creator/skill.md",
      "description": "将模糊想法转化为专业提示词"
    }
  }
}
```

#### 方法 2：Codex API 集成
```python
# 创建 Codex API 的 Python 包装器
import os
from openai import OpenAI

class CodexSkills:
    def __init__(self):
        self.client = OpenAI()
        self.skills_dir = os.path.expanduser("~/.codex/skills/claude-skills-bilingual-codex")

    def load_skill(self, skill_name):
        skill_path = os.path.join(self.skills_dir, f"{skill_name}.md")
        with open(skill_path, 'r', encoding='utf-8') as f:
            return f.read()

    def process_with_sansheng(self, task, priority="normal"):
        skill_content = self.load_skill("SKILL")
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": skill_content},
                {"role": "user", "content": f"任务: {task}\n优先级: {priority}"}
            ]
        )
        return response.choices[0].message.content

# 使用
skills = CodexSkills()
result = skills.process_with_sansheng("设计一个用户认证系统")
print(result)
```

---

### 🐾 OpenClaw 安装

OpenClaw 是一个开源 AI Agent 框架。这些技能与 OpenClaw 的技能系统兼容。

#### 方法 1：OpenClaw 技能目录
```bash
# 1. 创建技能目录
mkdir -p ~/.openclaw/skills

# 2. 克隆仓库
git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git ~/.openclaw/skills/claude-skills-bilingual-codex

# 3. 向 OpenClaw 注册技能
openclaw skills register ~/.openclaw/skills/claude-skills-bilingual-codex/SKILL.md
openclaw skills register ~/.openclaw/skills/claude-skills-bilingual-codex/prompt-deep-creator/skill.md
```

#### 方法 2：OpenClaw 配置文件
```yaml
# ~/.openclaw/config.yaml
skills:
  - name: sansheng
    path: ~/.openclaw/skills/claude-skills-bilingual-codex/SKILL.md
    description: "三省六部多Agent思维框架"
    enabled: true

  - name: prompt-deep-creator
    path: ~/.openclaw/skills/claude-skills-bilingual-codex/prompt-deep-creator/skill.md
    description: "将模糊想法转化为专业提示词"
    enabled: true

settings:
  default_language: zh
  auto_load_skills: true
```

#### 方法 3：OpenClaw Python 集成
```python
# 创建 OpenClaw 技能集成
import os
from openclaw import Agent, Skill

class SanshengSkill(Skill):
    def __init__(self):
        super().__init__(
            name="sansheng",
            description="用于任务处理的多Agent思维框架"
        )
        self.skills_dir = os.path.expanduser("~/.openclaw/skills/claude-skills-bilingual-codex")

    def execute(self, task, priority="normal"):
        skill_path = os.path.join(self.skills_dir, "SKILL.md")
        with open(skill_path, 'r', encoding='utf-8') as f:
            skill_content = f.read()

        agent = Agent()
        return agent.process(
            system_prompt=skill_content,
            user_message=f"任务: {task}\n优先级: {priority}"
        )

# 向 OpenClaw 注册技能
from openclaw import SkillRegistry
registry = SkillRegistry()
registry.register(SanshengSkill())
```

---

### 🔧 通用安装

适用于其他 AI 编码工具或自定义设置。

#### 方法 1：手动集成
```bash
# 1. 克隆仓库
git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git
cd claude-skills-bilingual-codex

# 2. 选择语言
./switch_lang.sh en  # 或 zh

# 3. 直接使用 CLI 脚本
python3 scripts/edict.py '{"task":"你的任务"}'
python3 scripts/edict_en.py '{"task":"Your task here"}'

# 4. 或使用 Web 看板
python3 scripts/serve.py
# 访问 http://127.0.0.1:7891
```

#### 方法 2：Docker 安装
```dockerfile
# 用于容器化安装的 Dockerfile
FROM python:3.9-slim

# 安装依赖
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# 克隆仓库
RUN git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git /opt/skills

# 设置工作目录
WORKDIR /opt/skills

# 默认命令
CMD ["python3", "scripts/edict.py", '{"task":"测试任务"}']
```

```bash
# 构建并运行 Docker 容器
docker build -t claude-skills .
docker run -it claude-skills
```

---

## 🌐 语言切换

### 快速切换脚本
```bash
# 切换到英文（默认）
./switch_lang.sh en

# 切换到中文
./switch_lang.sh zh
```

### 手动选择
- **英文**：使用 `README.md`、`SKILL.md`、`scripts/edict_en.py`
- **中文**：使用 `README_CN.md`、`SKILL_CN.md`、`scripts/edict.py`

### 编程 API
```bash
# 英文模式
python3 scripts/edict.py '{"task":"Your task", "lang":"en"}'

# 中文模式
python3 scripts/edict.py '{"task":"你的任务", "lang":"zh"}'
```

---

## 🚀 快速开始示例

### 示例 1：创建专业提示词
```bash
# 英文
python3 scripts/edict_en.py '{"task":"Create a prompt for writing technical documentation"}'

# 中文
python3 scripts/edict.py '{"task":"帮我创建一个写技术文档的提示词", "lang":"zh"}'
```

### 示例 2：使用三省六部处理复杂任务
```bash
# 英文
python3 scripts/edict_en.py '{"task":"Design a user authentication system with OAuth2", "priority":"high"}'

# 中文
python3 scripts/edict.py '{"task":"设计一个基于OAuth2的用户认证系统", "priority":"high"}'
```

### 示例 3：启动 Web 看板
```bash
# 英文版本
python3 scripts/serve_en.py

# 中文版本
python3 scripts/serve.py

# 然后访问 http://127.0.0.1:7891
```

---

## 📁 仓库结构

```
claude-skills-bilingual-codex/
├── README.md                 # 英文文档
├── README_CN.md              # 中文文档（当前）
├── SKILL.md                  # 英文技能文件
├── SKILL_CN.md               # 中文技能文件
├── skills.json               # 双语配置
├── switch_lang.sh            # 语言切换脚本
├── USAGE.md                  # 使用指南
├── INSTALL.md                # 安装指南
├── SUMMARY.md                # 完整总结
├── _meta.json                # 元数据
├── prompt-deep-creator.zip   # 深度提示词创作助手技能
└── scripts/
    ├── edict.py              # CLI 脚本（支持 lang 参数）
    ├── edict_en.py           # 英文 CLI 脚本
    ├── serve.py              # 中文 Web 看板服务器
    └── serve_en.py           # 英文 Web 看板服务器
```

---

## 🎨 功能详解

### 双语文档
- 所有文档都有完整的中英文版本
- 两种语言之间内容一致
- 轻松在语言之间切换
- 翻译中保留文化背景

### 高级思维框架
- 多 Agent 协作处理复杂任务
- 结构化工作流程确保任务彻底完成
- 通过审查和把关机制进行质量控制
- 专业部门产出实际成果

### 开发者友好工具
- 用于自动化任务处理的 CLI 工具
- 用于可视化任务管理的 Web 界面
- 用于集成到现有工作流的编程 API
- 全面的错误处理和日志记录

### 跨平台兼容性
- 适用于 Claude CLI、Claude Code 和兼容工具
- 可适配 OpenAI Codex 和其他 AI 助手
- 标准 JSON 配置便于集成
- 模块化设计允许自定义和扩展

---

## 🤝 贡献指南

欢迎贡献！以下是你可以帮助的方式：

1. **Fork 仓库**
2. **创建功能分支**：`git checkout -b feature/amazing-feature`
3. **提交更改**：`git commit -m 'Add amazing feature'`
4. **推送到分支**：`git push origin feature/amazing-feature`
5. **打开 Pull Request**

### 贡献想法
- 为特定用例添加新技能
- 改进现有技能文档
- 添加对其他 AI 平台的支持
- 创建教程和示例
- 报告错误和改进建议

---

## 📚 文档

| 文档 | 语言 | 说明 |
|------|------|------|
| [README.md](README.md) | English | 英文文档 |
| [README_CN.md](README_CN.md) | 中文 | 中文文档（当前） |
| [INSTALL.md](INSTALL.md) | English | 安装指南 |
| [USAGE.md](USAGE.md) | English | 使用指南和示例 |
| [SUMMARY.md](SUMMARY.md) | English | 完整总结和概述 |

---

## 🔧 技术要求

- **Python 3.6+**：运行 CLI 脚本必需
- **Claude CLI**：完整 LLM 集成（可选）
- **Git**：版本控制和仓库管理
- **Web 浏览器**：访问 Web 看板界面（可选）

---

## 📊 技能对比

| 特性 | 深度提示词创作助手 | 三省六部 |
|------|-------------------|----------|
| **主要用途** | 提示词创建 | 任务处理 |
| **复杂度** | 简单到中等 | 中等到复杂 |
| **输出** | 结构化提示词 | 任务结果和报告 |
| **语言** | 中/英 | 中/英 |
| **模式** | 仅 CLI | CLI + Web 看板 |
| **需要 LLM** | 否（框架模式） | 可选（增强结果） |

---

## 🎓 学习资源

### 入门
1. 阅读[安装指南](INSTALL.md)
2. 按照[使用指南](USAGE.md)操作
3. 尝试上面的快速开始示例
4. 探索技能文档

### 进阶使用
- 为你的特定需求自定义技能
- 集成到现有工作流中
- 基于框架创建新技能
- 回馈社区

---

## 🐛 故障排除

### 常见问题

**Q: 找不到 Python**
A: 确保 Python 3 已安装并在 PATH 中：
```bash
python3 --version
```

**Q: 未检测到 Claude CLI**
A: 技能将在没有 Claude CLI 的"框架模式"下工作。要启用完整的 LLM 模式，请安装 Claude CLI 并运行：
```bash
claude --model
```

**Q: 权限被拒绝**
A: 使脚本可执行：
```bash
chmod +x switch_lang.sh
chmod +x scripts/*.py
```

**Q: 语言未切换**
A: 确保你在正确的目录中，并且脚本有执行权限。

---

## 📈 路线图

### 版本 1.0（当前）
- ✅ 完整双语文档
- ✅ 深度提示词创作助手技能
- ✅ 三省六部思维框架
- ✅ 语言切换支持
- ✅ Web 看板界面

### 版本 1.1（计划中）
- 🔜 更多语言支持（日语、韩语等）
- 🔜 针对不同领域的更多专业技能
- 🔜 增强的 Web 看板，支持实时协作
- 🔜 与更多 AI 平台集成

### 版本 2.0（未来）
- 🔜 高级分析和报告
- 🔜 自定义扩展的插件系统
- 🔜 基于云的部署选项
- 🔜 企业功能和团队协作

---

## 📜 许可证

本项目根据 MIT 许可证授权 - 有关详情，请参阅 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- 原始仓库：[Roger-666666/claude-skills](https://github.com/Roger-666666/claude-skills)
- 为 Claude AI 社区用心打造
- 灵感来源于中国传统行政体系
- 为现代 AI 辅助开发工作流设计

---

## 📞 支持

- **问题反馈**：[GitHub Issues](https://github.com/Roger-666666/claude-skills-bilingual-codex/issues)
- **讨论交流**：[GitHub Discussions](https://github.com/Roger-666666/claude-skills-bilingual-codex/discussions)
- **详细文档**：请查看 docs 文件夹中的指南

---

**由 Roger-666666 用心打造**

*最后更新：2026-06-02*
