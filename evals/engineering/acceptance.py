"""External CLI acceptance. Candidate never imports this test or modifies its criteria."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

PARSER = argparse.ArgumentParser()
PARSER.add_argument("candidate", type=Path)
PARSER.add_argument("--stage", choices=("initial", "followup"), default="followup")
ARGS = PARSER.parse_args()
CANDIDATE = ARGS.candidate.resolve(strict=True)
TEMP_ROOT = Path(__file__).resolve().parent / ".tmp"
if TEMP_ROOT.is_symlink() or TEMP_ROOT.resolve().parent != Path(__file__).resolve().parent:
    raise SystemExit("fixture temporary root must stay beside acceptance.py")
TEMP_ROOT.mkdir(exist_ok=True)


class Acceptance(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="run-", dir=TEMP_ROOT)
        if Path(self.directory.name).resolve().parent != TEMP_ROOT.resolve():
            raise RuntimeError("fixture escaped temporary root")
        self.addCleanup(self.directory.cleanup)
        self.database = str(Path(self.directory.name) / "sessions.sqlite")

    def call(self, request, *, stage="followup", crash=False, fail=False):
        command = [sys.executable, "-I", str(CANDIDATE), self.database, json.dumps(request), "--stage", stage]
        if crash:
            command.append("--crash-before-commit")
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        if crash:
            self.assertEqual(result.returncode, 77, result.stderr)
        elif fail:
            self.assertNotEqual(result.returncode, 0)
        else:
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)

    def finish(self):
        return self.call({"op": "finish", "id": "s1", "seconds": 600}, stage="initial")

    def state(self):
        return self.call({"op": "list"}, stage=ARGS.stage)

    def test_initial_retry_survives_reopen(self):
        self.finish()
        self.finish()
        self.assertEqual(self.state(), {"s1": 600})

    def test_initial_rejects_negative_duration(self):
        self.call({"op": "finish", "id": "s1", "seconds": -1}, stage="initial", fail=True)
        self.assertEqual(self.state(), {})

    def test_initial_rejects_conflicting_completion(self):
        self.finish()
        self.call({"op": "finish", "id": "s1", "seconds": 601}, stage="initial", fail=True)
        self.assertEqual(self.state(), {"s1": 600})

    def test_initial_unacknowledged_finish_can_retry(self):
        self.call({"op": "finish", "id": "s1", "seconds": 600}, stage="initial", crash=True)
        self.finish()
        self.assertEqual(self.state(), {"s1": 600})

    @unittest.skipIf(ARGS.stage == "initial", "follow-up contract")
    def test_followup_preserves_previous_store_and_retry(self):
        self.finish()
        correction = {"op": "correct", "id": "c1", "session": "s1", "delta": -60}
        self.call(correction)
        self.call(correction)
        self.assertEqual(self.state(), {"s1": 540})
        self.finish()  # Delayed completion retry must not undo a correction.
        self.assertEqual(self.state(), {"s1": 540})

    @unittest.skipIf(ARGS.stage == "initial", "follow-up contract")
    def test_followup_crash_then_retry_applies_once(self):
        self.finish()
        correction = {"op": "correct", "id": "c1", "session": "s1", "delta": 60}
        self.call(correction, crash=True)
        self.call(correction)
        self.assertEqual(self.state(), {"s1": 660})

    @unittest.skipIf(ARGS.stage == "initial", "follow-up contract")
    def test_followup_rejects_conflicting_retry(self):
        self.finish()
        self.call({"op": "correct", "id": "c1", "session": "s1", "delta": 60})
        self.call({"op": "correct", "id": "c1", "session": "s1", "delta": 120}, fail=True)
        self.assertEqual(self.state(), {"s1": 660})

    @unittest.skipIf(ARGS.stage == "initial", "follow-up contract")
    def test_followup_completion_identity_survives_correction(self):
        self.finish()
        self.call({"op": "correct", "id": "c1", "session": "s1", "delta": 60})
        self.call({"op": "finish", "id": "s1", "seconds": 660}, stage="initial", fail=True)
        self.assertEqual(self.state(), {"s1": 660})
        self.finish()
        self.assertEqual(self.state(), {"s1": 660})

    @unittest.skipIf(ARGS.stage == "initial", "follow-up contract")
    def test_followup_rejects_noninteger_delta_without_consuming_id(self):
        for index, delta in enumerate((1.5, True, "1", None)):
            with self.subTest(delta=delta):
                self.database = str(Path(self.directory.name) / f"invalid-{index}.sqlite")
                self.finish()
                operation = {"op": "correct", "id": f"c{index}", "session": "s1", "delta": delta}
                self.call(operation, fail=True)
                self.assertEqual(self.state(), {"s1": 600})
                operation["delta"] = 1
                self.call(operation)
                self.assertEqual(self.state(), {"s1": 601})

    @unittest.skipIf(ARGS.stage == "initial", "follow-up contract")
    def test_followup_rejects_missing_and_negative(self):
        self.finish()
        self.call({"op": "correct", "id": "c1", "session": "missing", "delta": 60}, fail=True)
        self.call({"op": "correct", "id": "c2", "session": "s1", "delta": -601}, fail=True)
        self.assertEqual(self.state(), {"s1": 600})


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]], verbosity=2)
