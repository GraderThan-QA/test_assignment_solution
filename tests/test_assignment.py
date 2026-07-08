from helpers import  run_python_script

def test_should_pass():
    print("This will always pass!")
    assert True


def test_gpa():
    tests = [
        ("-1", "Invalid GPA"),
        ("0", "Academic Probation"),
        ("1.8", "Academic Probation"),
        ("3.0", "Passing"),
        ("3.4", "Cum Laude"),
        ("3.6", "Magna Cum Laude"),
        ("3.8", "Summa Cum Laude"),
        ("4.0", "Summa Cum Laude"),
        ("4.1", "Invalid GPA"),
    ]
    i = 1
    for input_text, expected_output in tests:
        output_text = run_python_script("./code/gpa.py", input_text)
        print(f"\nTEST {i}: gpa.py INPUT: {input_text} EXPECT: {expected_output} ACTUAL: {output_text}")
        assert output_text.find(expected_output) >=0
        i += 1

def test_numbers():
    import json
    tests = [
        ("2 \n 3 \n 5 \n 4 \n 6 \n 0 \n", '{"odd": [3, 5], "even": [2, 4, 6]}'),
        ("2 \n 4 \n 6 \n 0 \n", '{"odd": [], "even": [2, 4, 6]}'),
        ("3 \n 5 \n 0 \n", '{"odd": [3, 5], "even": []}'),
    ]
    i = 1
    for input_text, expected_output in tests:
        expected_dict = json.loads(expected_output)
        output_text = run_python_script("./code/numbers.py", input_text)
        print(f"\nTEST {i}: numbers.py INPUT: {input_text} EXPECT: {expected_output} ACTUAL: {output_text}")
        tmp = "{" + output_text.split("{")[-1].replace("'", '"')
        actual_dict = json.loads(tmp)
        assert expected_dict == actual_dict
        i += 1
