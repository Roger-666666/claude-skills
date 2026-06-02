# 🛡️ Claude Code Skills Library - Bilingual Edition (EN/CN)

[![GitHub stars](https://img.shields.io/github/stars/Roger-666666/claude-skills-bilingual-codex?style=social)](https://github.com/Roger-666666/claude-skills-bilingual-codex/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Roger-666666/claude-skills-bilingual-codex?style=social)](https://github.com/Roger-666666/claude-skills-bilingual-codex/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Roger-666666/claude-skills-bilingual-codex)](https://github.com/Roger-666666/claude-skills-bilingual-codex/issues)
[![GitHub license](https://img.shields.io/github/license/Roger-666666/claude-skills-bilingual-codex)](https://github.com/Roger-666666/claude-skills-bilingual-codex/blob/main/LICENSE)

Welcome to the **Claude Code Skills Library** - a comprehensive, bilingual (English/Chinese) collection of structured AI skills optimized for **Claude CLI**, **Claude Code**, and **OpenAI Codex**.

---

## 📖 Quick Navigation

- **[English Documentation](README.md)** (Current)
- **[中文文档 / Chinese Version](README_CN.md)**
- **[Installation Guide](INSTALL.md)**
- **[Usage Guide](USAGE.md)**
- **[Complete Summary](SUMMARY.md)**

---

## 🎯 What This Repository Offers

This repository provides a complete bilingual skill system designed to enhance AI-assisted coding and task processing. Whether you're using Claude CLI, Claude Code, or OpenAI Codex, these skills will significantly improve your productivity and the quality of AI-generated outputs.

### Key Features

- **🌐 Full Bilingual Support**: Complete English and Chinese versions of all documentation, skills, and scripts
- **🔄 Easy Language Switching**: Switch between English and Chinese with a single command
- **⚡ Optimized for Claude**: Specifically designed for Claude CLI and Claude Code workflows
- **🤖 Multi-Agent Framework**: Advanced thinking framework for complex task processing
- **📊 Web Kanban Interface**: Visual interface for task management and monitoring
- **🔧 CLI Tools**: Command-line tools for automated task processing
- **📝 Comprehensive Documentation**: Detailed guides, examples, and API references

---

## 🛠️ Available Skills

### 1️⃣ Prompt Deep Creator (深度提示词创作助手)

**Transform vague ideas into professional, structured prompts**

This skill takes your scattered, colloquial, or even vague creative ideas and converts them into high-quality, well-structured, ready-to-use formal prompts.

#### Features
- **Smart Element Extraction**: Automatically identifies core objectives, target audience, style preferences, and constraints
- **Structured Output Generation**: Creates standardized templates with role settings, task background, core objectives, and prohibitions
- **Intelligent Follow-up**: When input information is insufficient, proactively guides you to supplement key elements
- **Multi-Language Support**: Works seamlessly in both English and Chinese

#### Use Cases
- **Content Creation**: Technical blogs, in-depth articles, research papers, documentation
- **Business Planning**: Business proposals, Product Requirements Documents (PRD), project plans
- **Academic Writing**: Research papers, thesis statements, literature reviews
- **Creative Writing**: Stories, scripts, marketing copy, social media content

#### Installation
1. Download `prompt-deep-creator.zip` and extract it
2. Copy the `skill.md` content to your Claude preset instructions, or place the extracted folder in your software's `skills` directory
3. If using `skills.json` management, add the corresponding path

---

### 2️⃣ Three Provinces and Six Ministries (三省六部 · 多Agent思维框架)

**Universal Task Processing Administrative System**

This is a sophisticated multi-agent thinking framework that structures any complex task according to the traditional Chinese administrative system of "Three Provinces and Six Ministries." It ensures thorough task processing through a rigorous workflow of sorting, planning, review, dispatch, execution, and summary.

#### Features
- **Crown Prince · Task Sorting**: Determines task type and extracts core requirements
- **Secretariat · Plan Drafting**: Formulates specific, executable plans (rejects empty talk)
- **Chancellery · Review & Gatekeeping**: **Core Feature** - substandard plans are directly "rejected" with detailed feedback
- **Six Ministries · Actual Execution**: Specialized departments produce tangible results:
  - **Ministry of Revenue (户部)**: Data analysis, resource management, budget statistics
  - **Ministry of Rites (礼部)**: Document writing, specifications, communication
  - **Ministry of War (兵部)**: Engineering, code implementation, technical solutions
  - **Ministry of Justice (刑部)**: Security audit, compliance, risk assessment
  - **Ministry of Works (工部)**: Infrastructure, deployment, automation
  - **Ministry of Personnel (吏部)**: HR coordination, team management

#### Installation
1. Download the skill package and extract it
2. **CLI Mode**:
   - Ensure Python 3 is installed
   - Run `python3 edict.py '{"task":"task content"}'` in the terminal to trigger the workflow
3. **Web Kanban Mode**:
   - Run `python3 scripts/serve.py` to start the visual interface (visit 127.0.0.1:7891)

---

## 📥 Installation & Configuration

### For Claude CLI / Claude Code

#### Method 1: Directory Integration (Recommended)
1. Find your Claude CLI skills directory (e.g., `~/.claude/skills/` or `~/.gemini/antigravity/scratch/skills/`)
2. Copy the corresponding skill folders to the `skills/` directory
3. Restart Claude CLI and try:
   - "Use Sansheng to process this task..."
   - "Help me deeply create a prompt about..."

#### Method 2: Configuration File
Add to your `skills.json`:
```json
{
  "skills": [
    {
      "name": "sansheng",
      "path": "./skills/sansheng/SKILL.md"
    },
    {
      "name": "prompt-deep-creator",
      "path": "./skills/prompt-deep-creator/skill.md"
    }
  ]
}
```

### For OpenAI Codex

These skills can be adapted for use with OpenAI Codex by:
1. Converting the skill files to Codex-compatible format
2. Integrating the thinking framework into your Codex workflow
3. Using the bilingual documentation for cross-platform understanding

---

## 🌐 Language Switching

### Quick Switch Script
```bash
# Switch to English (default)
./switch_lang.sh en

# Switch to Chinese
./switch_lang.sh zh
```

### Manual Selection
- **English**: Use `README.md`, `SKILL.md`, `scripts/edict_en.py`
- **Chinese**: Use `README_CN.md`, `SKILL_CN.md`, `scripts/edict.py`

### Programmatic API
```bash
# English mode
python3 scripts/edict.py '{"task":"Your task", "lang":"en"}'

# Chinese mode
python3 scripts/edict.py '{"task":"你的任务", "lang":"zh"}'
```

---

## 🚀 Quick Start Examples

### Example 1: Create a Professional Prompt
```bash
# English
python3 scripts/edict_en.py '{"task":"Create a prompt for writing technical documentation"}'

# Chinese
python3 scripts/edict.py '{"task":"帮我创建一个写技术文档的提示词", "lang":"zh"}'
```

### Example 2: Process a Complex Task with Sansheng
```bash
# English
python3 scripts/edict_en.py '{"task":"Design a user authentication system with OAuth2", "priority":"high"}'

# Chinese
python3 scripts/edict.py '{"task":"设计一个基于OAuth2的用户认证系统", "priority":"high"}'
```

### Example 3: Launch Web Kanban
```bash
# English version
python3 scripts/serve_en.py

# Chinese version
python3 scripts/serve.py

# Then visit http://127.0.0.1:7891
```

---

## 📁 Repository Structure

```
claude-skills-bilingual-codex/
├── README.md                 # English documentation (current)
├── README_CN.md              # Chinese documentation
├── SKILL.md                  # English skill file
├── SKILL_CN.md               # Chinese skill file
├── skills.json               # Bilingual configuration
├── switch_lang.sh            # Language switching script
├── USAGE.md                  # Usage guide
├── INSTALL.md                # Installation guide
├── SUMMARY.md                # Complete summary
├── _meta.json                # Metadata
├── prompt-deep-creator.zip   # Prompt Deep Creator skill
└── scripts/
    ├── edict.py              # CLI script (supports lang parameter)
    ├── edict_en.py           # English CLI script
    ├── serve.py              # Chinese Web Kanban server
    └── serve_en.py           # English Web Kanban server
```

---

## 🎨 Features in Detail

### Bilingual Documentation
- Complete English and Chinese versions of all documentation
- Consistent content across both languages
- Easy switching between languages
- Cultural context preserved in translations

### Advanced Thinking Framework
- Multi-agent collaboration for complex task processing
- Structured workflow ensures thorough task completion
- Quality control through review and gatekeeping mechanisms
- Tangible outputs from specialized departments

### Developer-Friendly Tools
- CLI tools for automated task processing
- Web interface for visual task management
- Programmatic API for integration into existing workflows
- Comprehensive error handling and logging

### Cross-Platform Compatibility
- Works with Claude CLI, Claude Code, and compatible tools
- Can be adapted for OpenAI Codex and other AI assistants
- Standard JSON configuration for easy integration
- Modular design allows for customization and extension

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the Repository**
2. **Create a Feature Branch**: `git checkout -b feature/amazing-feature`
3. **Commit Your Changes**: `git commit -m 'Add amazing feature'`
4. **Push to the Branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Contribution Ideas
- Add new skills for specific use cases
- Improve existing skill documentation
- Add support for additional AI platforms
- Create tutorials and examples
- Report bugs and suggest improvements

---

## 📚 Documentation

| Document | Language | Description |
|----------|----------|-------------|
| [README.md](README.md) | English | Main documentation (current) |
| [README_CN.md](README_CN.md) | 中文 | Chinese documentation |
| [INSTALL.md](INSTALL.md) | English | Installation guide |
| [USAGE.md](USAGE.md) | English | Usage guide with examples |
| [SUMMARY.md](SUMMARY.md) | English | Complete summary and overview |

---

## 🔧 Technical Requirements

- **Python 3.6+**: Required for running CLI scripts
- **Claude CLI**: For full LLM integration (optional)
- **Git**: For version control and repository management
- **Web Browser**: For accessing Web Kanban interface (optional)

---

## 📊 Skill Comparison

| Feature | Prompt Deep Creator | Three Provinces & Six Ministries |
|---------|---------------------|-----------------------------------|
| **Primary Use** | Prompt creation | Task processing |
| **Complexity** | Simple to Medium | Medium to Complex |
| **Output** | Structured prompts | Task results and reports |
| **Languages** | EN/CN | EN/CN |
| **Modes** | CLI only | CLI + Web Kanban |
| **LLM Required** | No (framework mode) | Optional (enhances results) |

---

## 🎓 Learning Resources

### Getting Started
1. Read the [Installation Guide](INSTALL.md)
2. Follow the [Usage Guide](USAGE.md)
3. Try the quick start examples above
4. Explore the skill documentation

### Advanced Usage
- Customize skills for your specific needs
- Integrate with existing workflows
- Create new skills based on the framework
- Contribute back to the community

---

## 🐛 Troubleshooting

### Common Issues

**Q: Python not found**
A: Ensure Python 3 is installed and in your PATH:
```bash
python3 --version
```

**Q: Claude CLI not detected**
A: The skills will work in "framework mode" without Claude CLI. To enable full LLM mode, install Claude CLI and run:
```bash
claude --model
```

**Q: Permission denied**
A: Make scripts executable:
```bash
chmod +x switch_lang.sh
chmod +x scripts/*.py
```

**Q: Language not switching**
A: Ensure you're in the correct directory and the script has execute permissions.

---

## 📈 Roadmap

### Version 1.0 (Current)
- ✅ Complete bilingual documentation
- ✅ Prompt Deep Creator skill
- ✅ Three Provinces and Six Ministries framework
- ✅ Language switching support
- ✅ Web Kanban interface

### Version 1.1 (Planned)
- 🔜 Additional language support (Japanese, Korean, etc.)
- 🔜 More specialized skills for different domains
- 🔜 Enhanced Web Kanban with real-time collaboration
- 🔜 Integration with more AI platforms

### Version 2.0 (Future)
- 🔜 Advanced analytics and reporting
- 🔜 Plugin system for custom extensions
- 🔜 Cloud-based deployment options
- 🔜 Enterprise features and team collaboration

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Original repository: [Roger-666666/claude-skills](https://github.com/Roger-666666/claude-skills)
- Built with ❤️ for the Claude AI community
- Inspired by traditional Chinese administrative systems
- Designed for modern AI-assisted development workflows

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Roger-666666/claude-skills-bilingual-codex/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Roger-666666/claude-skills-bilingual-codex/discussions)
- **Documentation**: See the docs folder for detailed guides

---

**Made with ❤️ by Roger-666666**

*Last updated: 2026-06-02*
