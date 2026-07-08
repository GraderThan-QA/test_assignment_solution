'''
REST API that exposes the two functions from gpa.py:

    GET /gpa-level?gpa=<float>   -> {"gpa": <float>, "level": <str>}
    GET /valid-gpa?gpa=<float>   -> {"gpa": <float>, "valid": <bool>}

Run with (from the code/ directory). docker-compose maps host 28000 ->
container 8000, so uvicorn must listen on container port 8000:
    uvicorn api_gpa:app --host 0.0.0.0 --port 8000 --reload

Then open the Swagger docs on your machine at:
    http://localhost:28000/docs

In VS Code you can also use the "FastAPI: Current File" debug launch config.
'''
from fastapi import FastAPI

from gpa import gpa_level, valid_gpa

app = FastAPI(title="GPA API")

@app.get("/gpa-level")
def get_gpa_level(gpa: float):
    '''Return the academic level for the given GPA.'''
    return {"gpa": gpa, "level": gpa_level(gpa)}


@app.get("/valid-gpa")
def get_valid_gpa(gpa: float):
    '''Return whether the given GPA is within the valid 0.0 - 4.0 range.'''
    return {"gpa": gpa, "valid": valid_gpa(gpa)}
