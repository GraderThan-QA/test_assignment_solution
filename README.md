# IST356 Test Assignment

## Meta

### Learning Objectives

By the end of this assignment you should be able to:

1. these are in active voice
2. e.g. Debug your program with the vscode debugger.

### Prerequisites

Before you can work on this assignment you will need to make sure you've completed the one time course setup, here: https://mafudge.github.io/ist356/0-intro/0-0-setup.html 

### Project Layout

Each assignment in this course shares a common layout.

- `code/` — the code / application. This is where you will write code the code to complete the assignment.
- `tests/` — the tests that verify your code is correct.
- `code/reflection.txt` — where you submit your reflection. Read `reflection.md` for instructions
- `README.md` — these instructions.

> **NOTE**‼️ Only files in the `code` folder will be reviewed for grading.

## Instructions

### Running the Code

1. Open the file you want to run, for example: `code/gpa.py`.
2. Open the **Run and Debug** activity bar:   
**Menu: View ==> Run**.
3. Next to RUN AND DEBUG you will see a drop down. select the method of code execution:  
    - **Python Debugger: Current File** - Run or debug a python file.
    - **Stream Run: Current File** - Run or debug a python streamlit file.
    - **Fast API: Current File** - Run or debug a python FastAPI file.
4. Interacting with your code:  
    - For regular python programs, the input/output will be in the  **TERMINAL** panel at the bottom. 
    - For streamlit, open a web browser http://localhost:28502
    - For FastAPI, open a web browser here: http://localhost:28000/docs

### Running the Tests

Some code and tests are already working. These are sanity checks to confirm the container and VS Code are configured properly.

1. Open **Testing** in the activity bar:   
   **Menu: View => Testing**.
2. Expand the tree by clicking the **`>`** arrows: **Project: Workspace** => **tests** until you can see the individual tests such as **test_should_pass**.
3. Click the **Run Test** button `▶` next to a test to run it.
4. A **green check** ✅ means the test passed.
5. A **red X** ❌ means the test failed. When a test fails you'll get an error message and a stack trace with line numbers to help you find the problem.

## The Assignment

### `gpa.py` Walkthrough

For this part of the assignment you will learn how to read failed tests and debug them.

1. Open `code/gpa.py` and read the instructions at the top. The code has a couple of bugs. **If you spot them, do not fix them yet** — we'll fix them together as part of the process.
2. Run the program (**Run => Run Without Debugging**). In the terminal, enter a GPA of `3.3`. Based on the instructions, what *should* the output be? Does it output correctly in this case?
3. Run it again and try `1.8` as input. Is the output correct?
4. Open the tests file `tests/test_assignment.py` and look at `def test_gpa():`.
5. The list of tuples inside `tests` lists 9 test cases. For example, when we input `"4.0"` the output should be `"Summa Cum Laude"`.
6. The loop that follows runs `./code/gpa.py` for each case, sends in the input GPA, and scans the `print()` output for the expected result.

The test code is correct; the code in `gpa.py` is not. We will use the test code to find the error. This is the proper way to use test code: you know what you *expect* the code to do, and you debug what it *actually* does.

1. Run the `test_gpa` test. You will get a failure. Observe the **TEST RESULTS** panel. The last test printed before the `=== FAILURES ===` section is the failing one.
2. For convenience, the failing output looks like this:
   `TEST 3: gpa.py INPUT: 1.8 EXPECT: Academic Probation ACTUAL: Enter GPA: for GPA 1.800 Result: Passing`
   For a `1.8` input we expect `Academic Probation` but we got `Passing`.
3. That might be enough to spot the bug. Let's assume it isn't, and use the debugger.
4. Open `gpa.py`. We're going to debug this program and find out why an input of `1.8` does not result in `Academic Probation`.
5. Set a **breakpoint** on the line `if gpa >=0 and gpa <= 4.0:` by clicking to the left of the line number — a red dot appears.
6. Run with debugging: **Run => Start Debugging**.
7. In the **TERMINAL**, enter a GPA of `1.8`.
8. Execution pauses at your breakpoint. In the **VARIABLES** panel on the left you'll see `gpa` with the value `1.8`.
9. Step through the code one line at a time with **F10** (or **Run => Step Over**).
10. Repeat until you reach the `elif` comparisons. Do you see the error? Compare the requirements in the instructions at the top of the file to the comparison in the code.
11. Fix the comparison so a `1.8` input results in `Academic Probation`.
12. Stop execution: **Run => Stop Debugging**. (You cannot change code in the middle of execution.)
13. **Re-run the test!** Open `tests/test_assignment.py` and run `test_gpa` again.
14. It still won't pass every case, but it should get further now. Repeat the process to find the next bug.
15. Keep going until all tests pass. **NOTE: there are 3 bugs total in the code.**

### `numbers.py`

Write the program as described in the instructions at the top of `code/numbers.py`, and get the tests in `def test_numbers():` to pass.

### Reflection

Open `reflection.md` and complete it as instructed in the file. Your reflection is part of your submission.


## Submitting Your Work And Getting Automated Feedback

You are encouraged to submit your assignment for automated feedback anytime you need it prior to the due date. You can request feedback multiple times and use advice you recieve to improve your submission.

Its a simple, two-step process.

1. Commit and push your code changes to Github.
2. Ask GraderThan for feedback.

### Commit and Push

First the changes you've made locally (on your computer or in Github Codespaces) need to be sync'd with your Github repository.

1. Open **Source Control** in the activity bar: **Menu: View => Source Control** 
2. Review your changed files under **Changes**.
3. Hover a file and click the **`+`** to **stage** it, or click the **`+`** next to **Changes** to stage everything.
4. Type a short **commit message** in the text box. The message should summarize the work you did. 
5. Click the **Commit** button (the checkmark).
6. Click **Sync Changes** (or **Push**) to send your commit to GitHub.

### Option B — Terminal

In the TERMINAL panel, run:

```bash
git add .
git commit -m "fix gpa bugs and complete numbers"
git push
```

You can commit and push as many times as you like. Each push is a new submission.

---

## Grading

🤖 Beep, Boop. This assignment is bot-graded! When you push your code to GitHub, my graderbot is notified there is something to grade. The bot then takes the following actions:

1. Your assignment repository is cloned from GitHub.
2. The bot checks your code and commits according to the guidelines outlined in `rubric.json` (it runs tests, checks code correctness, etc.).
3. The bot reads your `reflection.md` and provides areas for improvement (based on the instructions in the file).
4. A grade is assigned by the bot. Feedback is generated, including justification for the grade given.
5. The grade and feedback are posted to Blackboard.

You are welcome to review the bot's feedback and improve your submission as often as you like.

**NOTE:** Consider this an experiment in the future of education. The graderbot is an AI teaching assistant. Like a human grader, it will make mistakes. Please feel free to question the bot's feedback! Do not feel as if you should gamify the bot. Talk to me! Like a person, we must teach it how to do its job effectively.
