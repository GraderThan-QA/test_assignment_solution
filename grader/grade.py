"""Autograder for the graderthan sandbox (G5 `tests[]` contract, #168).

Runs the full pytest suite once with ``--json-report`` and emits a per-test
``tests[]`` stream (``file``, ``name``, ``outcome``, ``message``) to
``/work/.grader/results.json``. The harness attributes each test to the rubric
``auto`` case that claims its file (see rubric.json ``tests`` lists and
``docs/grading-runner.md``). Requires pytest + pytest-json-report in the image.
"""
import json
import os
import subprocess

OUT = "/work/.grader"
os.makedirs(OUT, exist_ok=True)
REPORT = os.path.join(OUT, "pytest.report.json")

_VALID = {"passed", "failed", "error", "skipped"}
_COERCE = {"xpassed": "passed", "xfailed": "skipped"}   # map pytest xfail outcomes
_MAX_MSG = 200


def _message(t):
    """A concise one-line failure message for a non-passing test."""
    call = t.get("call") or {}
    crash = call.get("crash") or {}
    msg = crash.get("message") or call.get("longrepr") or ""
    return " ".join(str(msg).split())[:_MAX_MSG]


# Run the whole suite once; --json-report captures per-test outcomes with nodeids.
subprocess.run(
    ["python3", "-m", "pytest", "tests/", "-q", "-p", "no:cacheprovider",
     "--json-report", f"--json-report-file={REPORT}"],
    cwd="/work", capture_output=True, text=True,
)

try:
    data = json.load(open(REPORT))
except Exception:  # noqa: BLE001 — no report (e.g. collection crash) → empty stream
    data = {"tests": []}

tests = []
for t in data.get("tests", []):
    nodeid = t.get("nodeid", "")
    file = nodeid.split("::", 1)[0]                       # e.g. tests/test_gpa.py
    name = nodeid.split("::", 1)[1] if "::" in nodeid else (nodeid or "?")
    outcome = _COERCE.get(t.get("outcome"), t.get("outcome"))
    if outcome not in _VALID:
        outcome = "error"
    entry = {"file": file, "name": name, "outcome": outcome}
    if outcome in ("failed", "error"):
        m = _message(t)
        if m:
            entry["message"] = m
    tests.append(entry)

with open(os.path.join(OUT, "results.json"), "w") as fh:
    json.dump({"tests": tests}, fh)
print(f"grade.py done: {len(tests)} tests emitted")
