#!/usr/bin/env python3
"""
Three Provinces and Six Ministries · Kanban Server Startup Script (Skill Entry)
Directly calls existing sansheng/server.py
"""
import sys
import os
import subprocess
import pathlib

# Find sansheng project directory
POSSIBLE_PATHS = [
    pathlib.Path.home() / '.gemini' / 'antigravity' / 'scratch' / 'sansheng',
    pathlib.Path(os.getenv('SANSHENG_HOME', '')) if os.getenv('SANSHENG_HOME') else None,
]

sansheng_dir = None
for p in POSSIBLE_PATHS:
    if p and p.exists() and (p / 'server.py').exists():
        sansheng_dir = p
        break

if not sansheng_dir:
    print("Error: sansheng project not found.")
    print("Set SANSHENG_HOME env var or ensure it exists at ~/.gemini/antigravity/scratch/sansheng/")
    sys.exit(1)

print(f"Starting sansheng server from: {sansheng_dir}")
subprocess.run([sys.executable, str(sansheng_dir / 'server.py')] + sys.argv[1:], cwd=str(sansheng_dir))
