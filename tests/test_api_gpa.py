'''
Tests for code/api_gpa.py

Uses FastAPI's TestClient, which exercises the app in-process (no running
server or port needed) by making real HTTP-style requests against the ASGI app.

Run from the repo root with:
    pytest tests
'''
import os
import sys

import pytest
from fastapi.testclient import TestClient

CODE_DIR = os.path.join(os.path.dirname(__file__), "..", "code")
# The app does `from gpa import ...`; make code/ importable before importing it.
sys.path.insert(0, CODE_DIR)

from api_gpa import app

client = TestClient(app)


@pytest.mark.parametrize("gpa, expected", [
    (-1.0, "Invalid GPA"),
    (0.0, "Academic Probation"),
    (1.8, "Academic Probation"),
    (3.0, "Passing"),
    (3.4, "Cum Laude"),
    (3.6, "Magna Cum Laude"),
    (3.8, "Summa Cum Laude"),
    (4.0, "Summa Cum Laude"),
    (4.1, "Invalid GPA"),
])
def test_gpa_level_endpoint(gpa, expected):
    response = client.get("/gpa-level", params={"gpa": gpa})
    assert response.status_code == 200
    body = response.json()
    assert body == {"gpa": gpa, "level": expected}


@pytest.mark.parametrize("gpa, expected", [
    (-0.1, False),
    (0.0, True),
    (2.5, True),
    (4.0, True),
    (4.1, False),
])
def test_valid_gpa_endpoint(gpa, expected):
    response = client.get("/valid-gpa", params={"gpa": gpa})
    assert response.status_code == 200
    body = response.json()
    assert body == {"gpa": gpa, "valid": expected}


def test_gpa_level_requires_gpa_param():
    # Missing required query param -> 422 Unprocessable Entity.
    response = client.get("/gpa-level")
    assert response.status_code == 422


def test_gpa_level_rejects_non_numeric():
    response = client.get("/gpa-level", params={"gpa": "abc"})
    assert response.status_code == 422
