#!/usr/bin/env python3
"""
Three Provinces and Six Ministries · CLI Skill Script (English Version)
Usage: python3 edict_en.py '{"task":"...", "priority":"normal"}'

Two running modes:
1. With Claude CLI → Call real LLM, each Agent thinks independently
2. Without Claude CLI → Output Three Provinces and Six Ministries thinking framework template for host AI to reference
"""
import sys
import json
import os
import io
import pathlib
import subprocess
import shutil

# Windows UTF-8 output compatibility
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent

# Find sansheng project directory (with SOUL.md personality file)
_POSSIBLE = [
    pathlib.Path.home() / '.gemini' / 'antigravity' / 'scratch' / 'sansheng',
    pathlib.Path(os.getenv('SANSHENG_HOME', '')) if os.getenv('SANSHENG_HOME') else None,
]
SANSHENG_DIR = next((p for p in _POSSIBLE if p and p.exists()), None)

# Detect if Claude CLI is available
HAS_CLAUDE = shutil.which('claude') is not None

# Agent flow definition
FLOW = [
    ('taizi',    'Crown Prince',   'Task Sorting'),
    ('zhongshu', 'Secretariat', 'Plan Drafting'),
    ('menxia',   'Chancellery', 'Review & Gatekeeping'),
    ('shangshu', 'Department of State Affairs', 'Dispatch'),
]

DEPARTMENTS = {
    'hubu':    ('Ministry of Revenue', 'Data analysis, resource management, budget statistics'),
    'libu':    ('Ministry of Rites', 'Document writing, specification development, communication coordination'),
    'bingbu':  ('Ministry of War', 'Engineering development, code implementation, technical solutions'),
    'xingbu':  ('Ministry of Justice', 'Security audit, compliance check, risk assessment'),
    'gongbu':  ('Ministry of Works', 'Infrastructure, deployment operations, tool construction'),
    'libu_hr': ('Ministry of Personnel', 'HR coordination, team management, resource allocation'),
}


def section(title):
    """Output separator line"""
    print(f"\n{'='*56}")
    print(f"  {title}")
    print(f"{'='*56}\n")


def load_soul(agent_id):
    """Load Agent's SOUL.md"""
    if SANSHENG_DIR:
        soul_path = SANSHENG_DIR / 'agents' / agent_id / 'SOUL.md'
        if soul_path.exists():
            return soul_path.read_text(encoding='utf-8')
    return None


def probe_claude():
    """Probe if Claude CLI can be called normally (model available)"""
    try:
        result = subprocess.run(
            ['claude', '-p', 'reply OK', '--output-format', 'text', '--bare'],
            capture_output=True, text=True, timeout=15, encoding='utf-8'
        )
        if result.returncode == 0 and result.stdout.strip():
            return True
        # Detect common errors
        output = (result.stdout or '') + (result.stderr or '')
        if 'model' in output.lower() and ('not exist' in output.lower() or 'issue' in output.lower()):
            sys.stderr.write(f"[Probe] Current model unavailable: {output.strip()[:150]}\n")
            return False
    except Exception:
        pass
    return False


def call_claude(system_prompt, user_message):
    """Call LLM through Claude CLI"""
    try:
        cmd = ['claude', '-p', user_message, '--system-prompt', system_prompt,
               '--output-format', 'text', '--bare']
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=120, encoding='utf-8'
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        # Debug information
        output = (result.stdout or '') + (result.stderr or '')
        if output.strip():
            sys.stderr.write(f"[Claude CLI] {output.strip()[:200]}\n")
    except subprocess.TimeoutExpired:
        sys.stderr.write("[Claude CLI] Call timeout\n")
    except Exception as e:
        sys.stderr.write(f"[Claude CLI] Exception: {e}\n")
    return None


def run_with_llm(task, priority):
    """Execute Three Provinces and Six Ministries workflow using real LLM"""
    context = f"Task: {task}\nPriority: {priority}"
    accumulated = ""

    for agent_id, name, role in FLOW:
        section(f'{name} · {role}')
        soul = load_soul(agent_id) or f"You are {name}, responsible for {role}."
        message = f"{context}\n\nPrevious processing records:\n{accumulated}" if accumulated else context
        reply = call_claude(soul, message)
        if reply:
            print(reply)
            accumulated += f"\n[{name}]: {reply[:500]}\n"
        else:
            print(f"(LLM call failed, skipping {name})")

    # After Department of State Affairs dispatch, determine which departments need to execute
    section('Six Ministries · Execution')
    for dept_id, (dept_name, dept_desc) in DEPARTMENTS.items():
        soul = load_soul(dept_id) or f"You are the Minister of {dept_name}, responsible for {dept_desc}."
        message = f"{context}\n\nExecution plan:\n{accumulated}\n\nPlease output the actual results for your responsible part based on your duties. If this task is unrelated to your duties, briefly explain."
        reply = call_claude(soul, message)
        if reply and 'unrelated' not in reply and 'not involved' not in reply and len(reply) > 20:
            section(f'{dept_name} · Execution')
            print(reply)
            accumulated += f"\n[{dept_name}]: {reply[:300]}\n"

    section('Final Results · Summary')
    soul = "You are the Crown Prince, responsible for summarizing department results into a final report for the Emperor. Requirements: concise, complete, ready-to-use."
    reply = call_claude(soul, f"Task: {task}\n\nDepartment execution records:\n{accumulated}\n\nPlease summarize into final results report.")
    if reply:
        print(reply)
    else:
        print(f"Task '{task}' has completed the full workflow processing.")


def run_framework_mode(task, priority):
    """When no LLM is available, output thinking framework guidelines for host AI to reference"""
    section('Three Provinces and Six Ministries · Task Processing Framework')
    print(f"""Please process this task according to the following workflow:

Task: {task}
Priority: {priority}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【Step 1: Crown Prince - Task Sorting】
- Determine task type and complexity
- Extract core requirements, constraints, deliverables
- Identify involved departments

【Step 2: Secretariat - Draft Plan】
- Break down into specific subtasks (each with clear input/output)
- Mark responsible departments
- Estimate resources and risks
  Note: Plans must be specific, not vague statements like "requirements analysis and planning"

【Step 3: Chancellery - Review】
- Check plan coverage, feasibility, division reasonableness
- Reject and revise if substandard

【Step 4: Department of State Affairs - Dispatch】
- Determine execution order and dependencies
- Clarify each department's input/output

【Step 5: Six Ministries Execution】
Each department completes tasks according to division of labor, outputs specific results:
  - Ministry of Revenue: Data analysis, resource lists, cost estimates
  - Ministry of Rites: Full document text, email drafts, meeting minutes
  - Ministry of War: Code implementation, technical solutions, architecture design
  - Ministry of Justice: Security review, risk lists, compliance reports
  - Ministry of Works: Deployment plans, environment configuration, automation scripts
  - Ministry of Personnel: Personnel division, team suggestions

【Step 6: Summary】
- Integrate department results into final deliverables

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Please now process this task by playing each role sequentially according to the above workflow.
Each role must output actual content, not empty talk.""")


def main():
    if len(sys.argv) < 2:
        print("Three Provinces and Six Ministries · CLI Skill")
        print("")
        print("Usage: python3 edict_en.py '<JSON>'")
        print("")
        print("Parameters:")
        print("  task      - Task description (required)")
        print("  priority  - Priority: high/normal/low (default normal)")
        print("")
        print("Examples:")
        print('  python3 edict_en.py \'{"task":"Help me write a project weekly report"}\'')
        print('  python3 edict_en.py \'{"task":"Design technical solution for user points system","priority":"high"}\'')
        print('  python3 edict_en.py \'{"task":"Polish prompt: A cat watching rain on the windowsill"}\'')
        print("")
        print(f"Claude CLI: {'Detected' if HAS_CLAUDE else 'Not detected (will use framework mode)'}")
        print(f"SANSHENG_DIR: {SANSHENG_DIR or 'Not found'}")
        sys.exit(0)

    try:
        params = json.loads(sys.argv[1])
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        sys.exit(1)

    task = params.get('task', '')
    if not task:
        print("Error: Missing task parameter")
        sys.exit(1)

    priority = params.get('priority', 'normal')

    if HAS_CLAUDE:
        print("[Probing Claude CLI model availability...]")
        if probe_claude():
            print("[Mode: LLM Scheduling | Claude CLI]")
            run_with_llm(task, priority)
        else:
            print("[Claude CLI model unavailable, switching to framework mode]")
            print("[Hint: Please run 'claude --model' to select an available model]")
            print("")
            run_framework_mode(task, priority)
    else:
        print("[Mode: Framework Guidelines | No LLM]")
        run_framework_mode(task, priority)


if __name__ == '__main__':
    main()
