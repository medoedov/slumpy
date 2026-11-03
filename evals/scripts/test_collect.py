"""Regression for collection without deleting directories named by trace metadata."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CollectionTests(unittest.TestCase):
    def test_collects_records_without_deleting_trace_directory_or_owner_data(self):
        root = Path(__file__).resolve().parents[2]
        base = root / "evals" / ".build"
        base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="test-collect-", dir=base) as temp:
            fixture = Path(temp)
            output = fixture / "results"
            output.mkdir()
            # A plausible prefix is not proof that the collector owns this directory.
            protected = fixture / "claude-eval-owner-data"
            transcripts = protected / "transcripts"
            transcripts.mkdir(parents=True)
            marker = protected / "owner-data.txt"
            marker.write_text("preserve owner data", encoding="utf-8")
            trace = transcripts / "trace.jsonl"
            messages = [
                {"type": "assistant", "message": {"content": [
                    {"type": "tool_use", "name": "Skill", "input": {"skill": "engineering-design"}}]}},
                {"type": "result", "result": "verified result",
                 "subagent_stats": {"by_type": {"reviewer": {"count": 1}}}},
            ]
            trace.write_text("".join(json.dumps(message) + "\n" for message in messages), encoding="utf-8")
            aggregate = {"cases": [{"name": "fixture", "arms": {"with": [
                {"tracePath": str(trace), "score": 1, "costUsd": 0.5, "turns": 2,
                 "graders": [{"name": "correctness", "passed": True}]}]}}]}
            (output / "aggregate-result.json").write_text(json.dumps(aggregate), encoding="utf-8")
            result = subprocess.run([sys.executable, "-I", str(root / "evals/scripts/collect.py"), str(output)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            records = [json.loads(line) for line in (output / "runs.jsonl").read_text().splitlines()]
            self.assertEqual(len(records), 1)
            record = records[0]
            self.assertEqual((record["case"], record["arm"], record["run"]), ("fixture", "with", 0))
            self.assertEqual((record["score"], record["costUsd"], record["turns"]), (1, 0.5, 2))
            self.assertEqual(record["graders"], {"correctness": True})
            self.assertEqual(record["skills"], ["engineering-design"])
            self.assertEqual(record["subagents"], {"reviewer": {"count": 1}})
            self.assertEqual(record["final"], "verified result")
            self.assertTrue(marker.exists(), "collector deleted unrelated owner data")
            self.assertEqual(marker.read_text(), "preserve owner data")
            self.assertTrue(trace.exists(), "collection must retain the input trace")


if __name__ == "__main__":
    unittest.main(verbosity=2)
