'''
Tests for code/streamlit_same_level_gpa.py

Uses Streamlit's built-in headless test framework (streamlit.testing.v1.AppTest).
Demonstrates driving MULTIPLE widgets: both number_inputs are set before the
Compare button is clicked, then we inspect the levels and the same/different
message.

Run from the repo root with:
    pytest tests
'''
import os
import sys

import pytest
from streamlit.testing.v1 import AppTest

CODE_DIR = os.path.join(os.path.dirname(__file__), "..", "code")
SCRIPT = os.path.join(CODE_DIR, "streamlit_same_level_gpa.py")

# The app does `from gpa import gpa_level`; make code/ importable for the run.
sys.path.insert(0, CODE_DIR)


@pytest.mark.parametrize("gpa1, gpa2, level1, level2, same", [
    # same level -> st.success("Same level")
    (3.9, 4.0, "Summa Cum Laude", "Summa Cum Laude", True),
    (2.0, 3.0, "Passing", "Passing", True),
    (0.0, 1.8, "Academic Probation", "Academic Probation", True),
    # different level -> st.warning("Different level")
    (3.4, 3.6, "Cum Laude", "Magna Cum Laude", False),
    (1.0, 3.9, "Academic Probation", "Summa Cum Laude", False),
])
def test_streamlit_same_level_gpa(gpa1, gpa2, level1, level2, same):
    at = AppTest.from_file(SCRIPT).run()
    at.number_input[0].set_value(gpa1)
    at.number_input[1].set_value(gpa2)
    at.run()
    at.button[0].click().run()

    assert not at.exception

    output = " ".join(md.value for md in at.markdown)
    assert level1 in output
    assert level2 in output

    if same:
        assert any("Same level" in s.value for s in at.success)
        assert len(at.warning) == 0
    else:
        assert any("Different level" in w.value for w in at.warning)
        assert len(at.success) == 0


def test_message_hidden_until_compare_pressed():
    at = AppTest.from_file(SCRIPT).run()
    at.number_input[0].set_value(3.9)
    at.number_input[1].set_value(4.0)
    at.run()
    # No Compare click yet -> no same/different message.
    assert len(at.success) == 0
    assert len(at.warning) == 0
