#!/bin/sh
# graderthan sandbox entrypoint: run the autograder and emit /work/.grader/results.json
cd /work && exec python3 grader/grade.py