 # prompt-deep-creator 提示词深度创作

  将口述/随意的提示词深度创作，转化为结构化、专业的正式提示词模板。

  ## 功能

  - 🌱 **智能提取** - 从零散描述中提取核心要素
  - 🎯 **结构化输出** - 生成可直接使用的专业提示词
  - 💬 **智能追问** - 自动识别缺失信息并补充
  - 📚 **多场景覆盖** - 支持文章、方案、代码、课程等多种内容类型

  ## 适用场景

  | 场景 | 说明 |
  |------|------|
  | 写作创作 | 文章、故事、文案、邮件 |
  | 方案设计 | 商业方案、项目计划、产品设计 |
  | 代码开发 | 功能描述、技术文档、代码审查 |
  | 学习教育 | 课程设计、习题生成、知识讲解 |
  | 内容营销 | 社媒帖子、广告文案、推广内容 |
  | 分析报告 | 市场分析、数据报告、调研总结 |

  ## 使用方法

  1. 在 Claude Code 中调用技能：`/prompt-deep-creator`
  2. 输入你的创作需求（可以是口语化、模糊的描述）
  3. 技能会自动深度创作，生成结构化提示词
  4. 根据需要调整后使用

  ## 文件结构

  prompt-deep-creator/
  ├── skill.json           # 技能元数据
  ├── skill.md            # 技能说明文档
  └── references/
      ├── templates.md    # 分类提示词模板库
      └── examples.md     # 完整实战范例

  ## 安装

  ```bash
  skillhub install --index https://你的用户名.github.io/claude-skills/skills.json prompt-deep-creator

  License

  MIT

  ---

  **GitHub 上传顺序：**
  1. 先上传 `skill.json`、`skill.md`、`README.md`
  2. 再上传 `references/` 文件夹里的两个文件
