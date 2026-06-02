#!/bin/bash
# Language Switch Script for Claude Code Skills
# Usage: ./switch_lang.sh [en|zh]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

show_usage() {
    echo "Claude Code Skills - Language Switcher"
    echo ""
    echo "Usage: ./switch_lang.sh [en|zh]"
    echo ""
    echo "Options:"
    echo "  en    Switch to English (default)"
    echo "  zh    Switch to Chinese"
    echo ""
    echo "Examples:"
    echo "  ./switch_lang.sh en    # Switch to English"
    echo "  ./switch_lang.sh zh    # Switch to Chinese"
    echo ""
    echo "Current files:"
    echo "  README.md        - Main documentation"
    echo "  README_CN.md     - Chinese documentation"
    echo "  SKILL.md         - Main skill file"
    echo "  SKILL_CN.md      - Chinese skill file"
    echo "  scripts/edict.py - CLI script (Chinese)"
    echo "  scripts/edict_en.py - CLI script (English)"
}

switch_to_english() {
    echo "Switching to English..."

    # Copy English versions as default
    if [ -f "$SCRIPT_DIR/README.md" ]; then
        echo "✓ README.md is already English version"
    fi

    if [ -f "$SCRIPT_DIR/SKILL.md" ]; then
        echo "✓ SKILL.md is already English version"
    fi

    # Create symlink for edict.py pointing to English version
    if [ -f "$SCRIPT_DIR/scripts/edict_en.py" ]; then
        cp "$SCRIPT_DIR/scripts/edict_en.py" "$SCRIPT_DIR/scripts/edict.py"
        echo "✓ scripts/edict.py set to English version"
    fi

    if [ -f "$SCRIPT_DIR/scripts/serve_en.py" ]; then
        cp "$SCRIPT_DIR/scripts/serve_en.py" "$SCRIPT_DIR/scripts/serve.py"
        echo "✓ scripts/serve.py set to English version"
    fi

    echo ""
    echo "Switched to English successfully!"
    echo "Main files are now in English."
    echo "Chinese versions available as: README_CN.md, SKILL_CN.md"
}

switch_to_chinese() {
    echo "切换到中文..."

    # Copy Chinese versions as default
    if [ -f "$SCRIPT_DIR/README_CN.md" ]; then
        cp "$SCRIPT_DIR/README_CN.md" "$SCRIPT_DIR/README.md"
        echo "✓ README.md 已切换为中文版本"
    fi

    if [ -f "$SCRIPT_DIR/SKILL_CN.md" ]; then
        cp "$SCRIPT_DIR/SKILL_CN.md" "$SCRIPT_DIR/SKILL.md"
        echo "✓ SKILL.md 已切换为中文版本"
    fi

    # Keep edict.py as Chinese version (original)
    echo "✓ scripts/edict.py 保持中文版本"
    echo "✓ scripts/serve.py 保持中文版本"

    echo ""
    echo "已成功切换到中文！"
    echo "主文件现在是中文版本。"
    echo "英文版本可查看：README.md (英文), SKILL.md (英文)"
}

# Main logic
case "${1:-}" in
    en|english|EN)
        switch_to_english
        ;;
    zh|chinese|ZH)
        switch_to_chinese
        ;;
    *)
        show_usage
        ;;
esac
