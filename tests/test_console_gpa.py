'''
Tests for code/console_gpa.py

Runs the console program as a subprocess, feeds a GPA on stdin, and checks
the printed academic level.

Run from the repo root with:
    pytest tests
'''
import os
import sys

import pytest

# Make helpers importable regardless of the working directory pytest runs from.
sys.path.insert(0, os.path.dirname(__file__))

from helpers import run_python_script

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "code", "console_gpa.py")


@pytest.mark.parametrize("input_text, expected_output", [
    ("-1", "Invalid GPA"),
    ("0", "Academic Probation"),
    ("1.8", "Academic Probation"),
    ("3.0", "Passing"),
    ("3.4", "Cum Laude"),
    ("3.6", "Magna Cum Laude"),
    ("3.8", "Summa Cum Laude"),
    ("4.0", "Summa Cum Laude"),
    ("4.1", "Invalid GPA"),
])
def test_console_gpa(input_text, expected_output):
    output_text = run_python_script(SCRIPT, input_text)
    print(f"\nconsole_gpa.py INPUT: {input_text} EXPECT: {expected_output} ACTUAL: {output_text}")
    assert output_text.find(expected_output) >= 0
