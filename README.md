[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SWuRbOmc)
# IST356 Assignment 01 (assignment_01)

## Meta

### Learning Objectives

This assignment is more about how to complete an assignment in this course than it is about Python programming. By the end of this assignment, you will know how to:

1. run and debug code in the VS Code editor
2. run python tests to verify your code is correct using pytest and the VS Code activity bar
3. install assignment dependencies using `requirements.txt`
4. edit your reflection, required as part of your assignment submission
5. submit your assignment using git

### Assignment Layout

The each assignment will have a common layout.

- `code` folder contains our code / application. This is where you will create files and write code.
- `code/solution` folder contains the solution to the assignment, for reference.
- `tests` folder contains code to test our application
- `requirements.txt` contains the packages we need to `pip install` to execute the application code
- `readme.md` contains these instructions
- `.vscode` folder contains VS Code setup configurations for running / debugging the application and tests.
-  `reflection.md` is where you submit your reflection, comments on what you learned, things that confuse you, etc.

### Prerequisites 

Before starting this assignment you must:

Install the assignment python requirements:

1. From VS Code, open a terminal: Menu => Terminal => New Terminal
2. In the terminal, type and enter: `pip install -r requirements.txt`


### Running Tests

There is some code and tests already working in this assignment. These are sanity checks to ensure VS Code is configured properly.

1. Open **Testing** in the activity bar: Menu => View => Testing
2. Open the **>** by clicking on it next to **assignment_01**. Keep clicking on **>** until you see **test_should_pass** in the **test_assignment.py**
3. Click the Play button `|>` next to **test_should_pass** to execute the test. 
4. A green check means the test code ran and the test has passed.
5. A red X means the test code ran but the test has failed. When a test fails you will be given an error message and stack trace with line numbers.

## Assignment

### gpa.py Walkthough

For this part of the assignment you will learn how to read failed tests and debug them.

1. Open `code/gpa.py` and read the instructions. The code has a couple of bugs. If you see them please do not fix. we will fix as part of the process.
2. Run the program: menu => Run => Run Without Debugging  
In the terminal window, enter a gpa of `3.3`. Based on the instructions, what should be the output? Does the program output correctly in this case?
3. Run it again and try `1.8` as input. Is the output correct?
4. Open the tests file `tests/test_assignment.py` look at the code under `def test_gpa():`. 
5. Lines 10 through 18 list out 9 test cases. For example on line 17 when we input "4.0" the output should be "Summa Cum Laude".
6. The code on lines 21-25 loop through each test case and run `./code/gpa.py` sending in the input gpa and scanning the `print()` output for the expected output.


The test code is correct, the code in `gpa.py` is not. We will use the test code to find the error. This is the proper way to use test code. Assume you can write a test (you know what you *expect* the code to do, but you debug what is *actually* does)


1. Click the red X to run the test. You will get an error. Observe the TEST RESULTS window. The last test before the `===FAILURES===` section is the failing test. 
2. I'll add the test output here for convienence.   
`TEST 3: gpa.py INPUT: 1.8 EXPECT: Academic Probation ACTUAL: Enter GPA: for GPA 1.800 Result: Passing`  
For a `1.8` input we expect `Academic Probation` but we got `Passing`.
3. This might be enough for you to figure out where the error is in the code under test, `gpa.py`. Let's assume its not, and thus we will use the debugger.
4. Open `gpa.py`. We are going to debug this program and find out why an input of `1.8` does not result in `Academic Probation`
5. Place a *breakpoint* on line 19. Do this by clicking to the left of the line. A red dot will appear.
6. Run the program with debugging. menu => Run => Start 
7. In the TERMINAL, enter a gpa of `1.8`
8. Program execution will pause on line 19. To the left of your program, you will see the variable `gpa` in the VARIABLES section. It has the value `1.8`
9. To step through the code a line at a time press the **F10** key or menu => Run => Step Over
10. repeat the process until you are on line 26. Do you see the error? Compare the requirements on line 8 to the code on line 26.
11. change line 26 accordinly `gpa <= 1.8`
12. stop execution menu => Run => Stop Debugging. NOTE: you cannot change code in the middle of execution
13. Re-Test your change! Open the tests file `tests/test_assignment.py` and test the code the code under `def test_gpa():`.
14. It still doesn't pass all tests but it gets to TEST 7 now. repeat these steps to fix this error.
15. Repeat these steps until all tests pass! NOTE: There are 3 bugs total in the code.


### numbers.py

Write the program as per the instructions in `numbers.py` and get the tests to pass in `def test_numbers():` on line 27 of `test_assignment.py`
 

## Grading 

🤖 Beep, Boop. This assignment is bot-graded! When you push your code to GitHub, my graderbot is notified there is something to grade. The bot then takes the following actions:

1. Your assignment repository is cloned from Github
2. The bot checks your code and commits according to guidelines outlined in `assignment-criteria.json` (it runs tests, checking code correctness, etc.)
3. The bot reads your `reflection.md` and provides areas for improvement (based on the instructions in the file).
4. A grade is assigned by the bot. Feedback is generated including justification for the grade given.
5. The grade and feedback are posted to Blackboard.

You are welcome to review the bot's feedback and improve your submission as often as you like.

**NOTE: ** Consider this an experiment in the future of education. The graderbot is an AI teaching assistant. Like a human grader, it will make mistakes. Please feel free to question the bots' feedback! Do not feel as if you should gamify the bot. Talk to me! Like a person, we must teach it how to do its job effectively. 

