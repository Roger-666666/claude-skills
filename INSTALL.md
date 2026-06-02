# Claude Code Skills - Installation Guide

This guide provides detailed installation instructions for different AI coding platforms.

---

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Claude Code Installation](#claude-code-installation)
- [OpenAI Codex Installation](#openai-codex-installation)
- [OpenClaw Installation](#openclaw-installation)
- [General Installation](#general-installation)
- [Troubleshooting](#troubleshooting)

---

## 🚀 Quick Start

### 1. Download

```bash
git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git
cd claude-skills-bilingual-codex
```

### 2. Choose Language

```bash
# Switch to English (default)
./switch_lang.sh en

# Switch to Chinese
./switch_lang.sh zh
```

### 3. Verify Installation

```bash
# Test the CLI script
python3 scripts/edict.py '{"task":"Test task", "lang":"en"}'
```

---

## 🤖 Claude Code Installation

Claude Code is Anthropic's official CLI for Claude. These skills are optimized for Claude Code workflows.

### Method 1: Global Installation (Recommended)

```bash
# 1. Create skills directory
mkdir -p ~/.claude/skills

# 2. Clone the repository
git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git ~/.claude/skills/claude-skills-bilingual-codex

# 3. Add to your Claude Code settings
# Edit ~/.claude/settings.json and add:
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

### Method 2: Project-Specific Installation

```bash
# 1. Navigate to your project
cd your-project

# 2. Create local skills directory
mkdir -p .claude/skills

# 3. Clone or copy skills
git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git .claude/skills/claude-skills-bilingual-codex

# 4. Create project-specific settings
cat > .claude/settings.json << 'EOF'
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
EOF
```

### Method 3: Using Claude Code CLI

```bash
# 1. Install skills using Claude Code's built-in command
claude skills install

# 2. Or manually add via Claude Code's interactive mode
claude

# Then in Claude Code, type:
# /skills add ~/.claude/skills/claude-skills-bilingual-codex/SKILL.md
```

### Claude Code Usage Examples

```bash
# In Claude Code, you can now use:
# "Use Sansheng to process this task..."
# "Help me deeply create a prompt about..."

# Or via CLI:
python3 ~/.claude/skills/claude-skills-bilingual-codex/scripts/edict.py '{"task":"Write a technical blog post"}'
```

---

## 🔧 OpenAI Codex Installation

OpenAI Codex is OpenAI's code generation model. These skills can be adapted for Codex workflows.

### Method 1: Codex CLI Integration

```bash
# 1. Install Codex CLI (if not already installed)
npm install -g @openai/codex

# 2. Create Codex skills directory
mkdir -p ~/.codex/skills

# 3. Clone the repository
git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git ~/.codex/skills/claude-skills-bilingual-codex

# 4. Create Codex configuration
cat > ~/.codex/config.json << 'EOF'
{
  "skills": {
    "sansheng": {
      "path": "~/.codex/skills/claude-skills-bilingual-codex/SKILL.md",
      "description": "Three Provinces and Six Ministries multi-agent thinking framework"
    },
    "prompt-deep-creator": {
      "path": "~/.codex/skills/claude-skills-bilingual-codex/prompt-deep-creator/skill.md",
      "description": "Transform vague ideas into professional prompts"
    }
  }
}
EOF
```

### Method 2: Codex API Integration

```python
# Create a Python wrapper for Codex API
# File: codex_skills.py

import json
import os
from openai import OpenAI

class CodexSkills:
    def __init__(self):
        self.client = OpenAI()
        self.skills_dir = os.path.expanduser("~/.codex/skills/claude-skills-bilingual-codex")

    def load_skill(self, skill_name):
        """Load a skill file"""
        skill_path = os.path.join(self.skills_dir, f"{skill_name}.md")
        with open(skill_path, 'r', encoding='utf-8') as f:
            return f.read()

    def process_with_sansheng(self, task, priority="normal"):
        """Process a task using the Three Provinces framework"""
        skill_content = self.load_skill("SKILL")

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": skill_content},
                {"role": "user", "content": f"Task: {task}\nPriority: {priority}"}
            ]
        )

        return response.choices[0].message.content

# Usage
skills = CodexSkills()
result = skills.process_with_sansheng("Design a user authentication system")
print(result)
```

### Method 3: Codex Notebook Integration

```python
# In a Jupyter notebook or Codex notebook:
import sys
sys.path.append(os.path.expanduser("~/.codex/skills/claude-skills-bilingual-codex/scripts"))

from edict_en import run_framework_mode

# Process a task
run_framework_mode("Create a REST API for user management", "high")
```

### Codex Usage Examples

```bash
# Using Codex CLI with skills
codex --skill sansheng "Write a Python function to sort a list"

# Using the Python wrapper
python3 codex_skills.py
```

---

## 🐾 OpenClaw Installation

OpenClaw is an open-source AI agent framework. These skills are compatible with OpenClaw's skill system.

### Method 1: OpenClaw Skill Directory

```bash
# 1. Find your OpenClaw installation directory
# Common locations:
# - ~/.openclaw/
# - /opt/openclaw/
# - Check your OpenClaw documentation

# 2. Create skills directory
mkdir -p ~/.openclaw/skills

# 3. Clone the repository
git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git ~/.openclaw/skills/claude-skills-bilingual-codex

# 4. Register skills with OpenClaw
openclaw skills register ~/.openclaw/skills/claude-skills-bilingual-codex/SKILL.md
openclaw skills register ~/.openclaw/skills/claude-skills-bilingual-codex/prompt-deep-creator/skill.md
```

### Method 2: OpenClaw Configuration File

```bash
# 1. Create or edit OpenClaw configuration
cat > ~/.openclaw/config.yaml << 'EOF'
skills:
  - name: sansheng
    path: ~/.openclaw/skills/claude-skills-bilingual-codex/SKILL.md
    description: "Three Provinces and Six Ministries multi-agent thinking framework"
    enabled: true

  - name: prompt-deep-creator
    path: ~/.openclaw/skills/claude-skills-bilingual-codex/prompt-deep-creator/skill.md
    description: "Transform vague ideas into professional prompts"
    enabled: true

settings:
  default_language: en
  auto_load_skills: true
EOF
```

### Method 3: OpenClaw Python Integration

```python
# Create an OpenClaw skill integration
# File: openclaw_skills.py

import os
import yaml
from openclaw import Agent, Skill

class SanshengSkill(Skill):
    """Three Provinces and Six Ministries skill for OpenClaw"""

    def __init__(self):
        super().__init__(
            name="sansheng",
            description="Multi-agent thinking framework for task processing"
        )
        self.skills_dir = os.path.expanduser("~/.openclaw/skills/claude-skills-bilingual-codex")

    def execute(self, task, priority="normal"):
        """Execute the Three Provinces workflow"""
        # Load the skill content
        skill_path = os.path.join(self.skills_dir, "SKILL.md")
        with open(skill_path, 'r', encoding='utf-8') as f:
            skill_content = f.read()

        # Process with the agent
        agent = Agent()
        return agent.process(
            system_prompt=skill_content,
            user_message=f"Task: {task}\nPriority: {priority}"
        )

# Register the skill with OpenClaw
from openclaw import SkillRegistry

registry = SkillRegistry()
registry.register(SanshengSkill())
```

### Method 4: OpenClaw CLI Usage

```bash
# Using OpenClaw CLI with skills
openclaw run --skill sansheng "Process this complex task"

# Or interactively
openclaw interactive
# Then in the interactive session:
# /skill sansheng "Your task description"
```

### OpenClaw Usage Examples

```bash
# List available skills
openclaw skills list

# Run a specific skill
openclaw skills run sansheng '{"task":"Analyze market trends"}'

# Run with language option
openclaw skills run sansheng '{"task":"分析市场趋势", "lang":"zh"}'
```

---

## 🔧 General Installation

For other AI coding tools or custom setups.

### Method 1: Manual Integration

```bash
# 1. Clone the repository
git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git
cd claude-skills-bilingual-codex

# 2. Choose your language
./switch_lang.sh en  # or zh

# 3. Use the CLI scripts directly
python3 scripts/edict.py '{"task":"Your task here"}'
python3 scripts/edict_en.py '{"task":"Your task here"}'

# 4. Or use the Web Kanban
python3 scripts/serve.py
# Visit http://127.0.0.1:7891
```

### Method 2: Custom Integration

```python
# Create a custom integration for your AI tool
import sys
import os

# Add the skills directory to Python path
skills_dir = os.path.expanduser("~/path/to/claude-skills-bilingual-codex")
sys.path.insert(0, os.path.join(skills_dir, "scripts"))

# Import and use the functions
from edict_en import run_with_llm, run_framework_mode

# Process a task
run_framework_mode("Your task description", "normal")
```

### Method 3: Docker Installation

```dockerfile
# Dockerfile for containerized installation
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone the repository
RUN git clone https://github.com/Roger-666666/claude-skills-bilingual-codex.git /opt/skills

# Set working directory
WORKDIR /opt/skills

# Install Python dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt 2>/dev/null || true

# Default command
CMD ["python3", "scripts/edict.py", '{"task":"Test task"}']
```

```bash
# Build and run the Docker container
docker build -t claude-skills .
docker run -it claude-skills
```

---

## 🛠️ Platform-Specific Configurations

### Claude Code Configuration

```json
// ~/.claude/settings.json
{
  "model": "claude-3-sonnet-20240229",
  "skills": [
    {
      "name": "sansheng",
      "path": "~/.claude/skills/claude-skills-bilingual-codex/SKILL.md",
      "enabled": true
    }
  ],
  "settings": {
    "theme": "dark",
    "verbose": true
  }
}
```

### Codex Configuration

```json
// ~/.codex/config.json
{
  "model": "gpt-4",
  "skills": {
    "sansheng": {
      "path": "~/.codex/skills/claude-skills-bilingual-codex/SKILL.md",
      "parameters": {
        "temperature": 0.7,
        "max_tokens": 4096
      }
    }
  }
}
```

### OpenClaw Configuration

```yaml
# ~/.openclaw/config.yaml
agent:
  name: "Claude Skills Agent"
  model: "gpt-4"

skills:
  - name: sansheng
    path: ~/.openclaw/skills/claude-skills-bilingual-codex/SKILL.md
    enabled: true
    priority: 1

  - name: prompt-deep-creator
    path: ~/.openclaw/skills/claude-skills-bilingual-codex/prompt-deep-creator/skill.md
    enabled: true
    priority: 2

settings:
  default_language: en
  auto_load_skills: true
  log_level: info
```

---

## 🐛 Troubleshooting

### Issue: Python not found

```bash
# Check Python version
python3 --version

# If not found, install Python 3
# Ubuntu/Debian:
sudo apt-get update && sudo apt-get install python3

# macOS:
brew install python3

# Windows:
# Download from https://www.python.org/downloads/
```

### Issue: Claude CLI not detected

```bash
# Install Claude CLI
# Method 1: Using npm
npm install -g @anthropic-ai/claude-cli

# Method 2: Using pip
pip install claude-cli

# Verify installation
claude --version

# Select an available model
claude --model
```

### Issue: Codex CLI not found

```bash
# Install Codex CLI
npm install -g @openai/codex

# Verify installation
codex --version
```

### Issue: OpenClaw not found

```bash
# Install OpenClaw
# Check your OpenClaw documentation for installation instructions
# Common methods:
pip install openclaw
# or
npm install -g openclaw

# Verify installation
openclaw --version
```

### Issue: Permission denied

```bash
# Make scripts executable
chmod +x switch_lang.sh
chmod +x scripts/*.py

# If on macOS/Linux, you may need to use sudo
sudo chmod +x switch_lang.sh
sudo chmod +x scripts/*.py
```

### Issue: Skills not loading

```bash
# Verify skill files exist
ls -la ~/.claude/skills/claude-skills-bilingual-codex/
# or
ls -la ~/.codex/skills/claude-skills-bilingual-codex/
# or
ls -la ~/.openclaw/skills/claude-skills-bilingual-codex/

# Check file permissions
ls -la ~/.claude/skills/claude-skills-bilingual-codex/SKILL.md

# Verify configuration
cat ~/.claude/settings.json
# or
cat ~/.codex/config.json
# or
cat ~/.openclaw/config.yaml
```

---

## 📚 Additional Resources

- **README.md**: Main documentation (English)
- **README_CN.md**: Main documentation (Chinese)
- **USAGE.md**: Detailed usage examples
- **SUMMARY.md**: Complete overview

---

## 🤝 Getting Help

1. **Check the documentation**: Review the files in this repository
2. **Search existing issues**: Look for similar problems on GitHub
3. **Open a new issue**: Describe your problem with details
4. **Join the discussion**: Participate in GitHub Discussions

---

*Generated by Claude Code Skills Hub v1.0.0*
