"""Portable acceptance-fixture oracle; not application code or a storage recommendation."""
import argparse
import json
import os
import sqlite3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("database")
    parser.add_argument("request", help="JSON operation")
    parser.add_argument("--stage", choices=("initial", "followup"), default="followup")
    parser.add_argument("--crash-before-commit", action="store_true")
    args = parser.parse_args()
    request = json.loads(args.request)
    db = sqlite3.connect(args.database)
    db.execute("PRAGMA synchronous=FULL")
    db.execute("CREATE TABLE IF NOT EXISTS sessions (id TEXT PRIMARY KEY, seconds INTEGER NOT NULL, completion_seconds INTEGER NOT NULL)")
    if args.stage == "followup":
        db.execute("CREATE TABLE IF NOT EXISTS corrections (id TEXT PRIMARY KEY, session_id TEXT NOT NULL, delta INTEGER NOT NULL)")
    db.commit()
    try:
        with db:
            if request["op"] == "list":
                result = dict(db.execute("SELECT id, seconds FROM sessions ORDER BY id"))
            elif request["op"] == "finish":
                if type(request["seconds"]) is not int or request["seconds"] < 0:
                    raise ValueError("duration must be a nonnegative integer")
                existing = db.execute("SELECT completion_seconds FROM sessions WHERE id=?", (request["id"],)).fetchone()
                if existing is not None and existing[0] != request["seconds"]:
                    raise ValueError("completion id reused with different input")
                if existing is None:
                    db.execute("INSERT INTO sessions VALUES (?, ?, ?)", (request["id"], request["seconds"], request["seconds"]))
                result = {"ok": True}
            elif request["op"] == "correct" and args.stage == "followup":
                if type(request["delta"]) is not int:
                    raise ValueError("correction must be an integer")
                previous = db.execute("SELECT session_id, delta FROM corrections WHERE id=?", (request["id"],)).fetchone()
                identity = (request["session"], request["delta"])
                if previous is not None and previous != identity:
                    raise ValueError("operation id reused with different input")
                if previous is None:
                    changed = db.execute("UPDATE sessions SET seconds=seconds+? WHERE id=? AND seconds+?>=0", (request["delta"], request["session"], request["delta"]))
                    if changed.rowcount != 1:
                        raise ValueError("missing session or negative duration")
                    db.execute("INSERT INTO corrections VALUES (?, ?, ?)", (request["id"], *identity))
                result = {"ok": True}
            else:
                raise ValueError("unsupported operation")
            if args.crash_before_commit:
                os._exit(77)
        print(json.dumps(result, sort_keys=True))
    finally:
        db.close()


if __name__ == "__main__":
    main()
