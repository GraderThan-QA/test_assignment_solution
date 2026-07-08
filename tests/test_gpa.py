'''
Unit tests for code/gpa.py

Run from the repo root with:
    pytest tests
'''
import os
import sys

import pytest

# Make code/ importable regardless of the working directory pytest runs from.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

from gpa import gpa_level, valid_gpa


@pytest.mark.parametrize("gpa, expected", [
    (-1.0, "Invalid GPA"),
    (0.0, "Academic Probation"),
    (1.0, "Academic Probation"),
    (1.8, "Academic Probation"),
    (2.0, "Passing"),
    (3.0, "Passing"),
    (3.39, "Passing"),
    (3.4, "Cum Laude"),
    (3.59, "Cum Laude"),
    (3.6, "Magna Cum Laude"),
    (3.79, "Magna Cum Laude"),
    (3.8, "Summa Cum Laude"),
    (4.0, "Summa Cum Laude"),
    (4.1, "Invalid GPA"),
])
def test_gpa_level(gpa, expected):
    assert gpa_level(gpa) == expected


@pytest.mark.parametrize("gpa, expected", [
    (-0.1, False),
    (0.0, True),
    (2.5, True),
    (4.0, True),
    (4.1, False),
])
def test_valid_gpa(gpa, expected):
    assert valid_gpa(gpa) == expected
