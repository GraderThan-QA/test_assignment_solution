'''
Tests for code/console_same_level_gpa.py

Demonstrates feeding MULTIPLE inputs to a program through run_python_script:
the two newline-separated values satisfy the program's two input() calls.

Run from the repo root with:
    pytest tests
'''
import os
import sys

import pytest

# Make helpers importable regardless of the working directory pytest runs from.
sys.path.insert(0, os.path.dirname(__file__))

from helpers import run_python_script

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "code", "console_same_level_gpa.py")


@pytest.mark.parametrize("gpa1, gpa2, level1, level2, same", [
    # same level
    ("3.9", "4.0", "Summa Cum Laude", "Summa Cum Laude", "Same level"),
    ("2.0", "3.0", "Passing", "Passing", "Same level"),
    ("0.0", "1.8", "Academic Probation", "Academic Probation", "Same level"),
    # different level
    ("3.4", "3.6", "Cum Laude", "Magna Cum Laude", "Different level"),
    ("1.0", "3.9", "Academic Probation", "Summa Cum Laude", "Different level"),
    ("-1", "4.1", "Invalid GPA", "Invalid GPA", "Same level"),
])
def test_console_same_level_gpa(gpa1, gpa2, level1, level2, same):
    # Two newline-separated values feed the program's two input() calls.
    input_text = f"{gpa1}\n{gpa2}\n"
    output_text = run_python_script(SCRIPT, input_text)
    print(f"\nsame_level INPUT: {gpa1!r}, {gpa2!r} EXPECT: {level1} / {level2} / {same}\nACTUAL:\n{output_text}")
    assert level1 in output_text
    assert level2 in output_text
    assert same in output_text
