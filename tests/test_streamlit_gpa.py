'''
Tests for code/streamlit_gpa.py

Uses Streamlit's built-in headless test framework (streamlit.testing.v1.AppTest).
No browser or server is started: AppTest runs the app script in-process, lets us
set widget values and click buttons, then inspect the rendered elements.

Run from the repo root with:
    pytest tests
'''
import os
import sys

import pytest
from streamlit.testing.v1 import AppTest

CODE_DIR = os.path.join(os.path.dirname(__file__), "..", "code")
SCRIPT = os.path.join(CODE_DIR, "streamlit_gpa.py")

# The app does `from gpa import gpa_level`; make code/ importable for the run.
sys.path.insert(0, CODE_DIR)


@pytest.mark.parametrize("gpa, expected", [
    (0.0, "Academic Probation"),
    (1.8, "Academic Probation"),
    (3.0, "Passing"),
    (3.4, "Cum Laude"),
    (3.6, "Magna Cum Laude"),
    (3.8, "Summa Cum Laude"),
    (4.0, "Summa Cum Laude"),
])
def test_streamlit_gpa(gpa, expected):
    at = AppTest.from_file(SCRIPT).run()
    at.number_input[0].set_value(gpa).run()
    at.button[0].click().run()

    assert not at.exception
    # st.write(str) renders as a markdown element.
    output = " ".join(md.value for md in at.markdown)
    assert expected in output


def test_level_hidden_until_button_pressed():
    at = AppTest.from_file(SCRIPT).run()
    at.number_input[0].set_value(3.9).run()
    # No button click yet -> no result markdown rendered.
    assert all("Result" not in md.value for md in at.markdown)
