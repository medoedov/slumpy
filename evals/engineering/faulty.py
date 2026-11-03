"""Deliberately faulty probe: commits a correction before its retry marker."""
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys

request = json.loads(sys.argv[2])
if request["op"] != "correct":
    raise SystemExit(subprocess.call([sys.executable, str(Path(__file__).with_name("reference.py")), *sys.argv[1:]]))
db = sqlite3.connect(sys.argv[1])
db.execute("CREATE TABLE IF NOT EXISTS corrections (id TEXT PRIMARY KEY, session_id TEXT NOT NULL, delta INTEGER NOT NULL)")
if db.execute("SELECT 1 FROM corrections WHERE id=?", (request["id"],)).fetchone() is None:
    db.execute("UPDATE sessions SET seconds=seconds+? WHERE id=?", (request["delta"], request["session"]))
    db.commit()
    if "--crash-before-commit" in sys.argv:
        os._exit(77)
    db.execute("INSERT INTO corrections VALUES (?, ?, ?)", (request["id"], request["session"], request["delta"]))
    db.commit()
print('{"ok": true}')
