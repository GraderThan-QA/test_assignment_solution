from helpers import  run_python_script

def test_add():
    tests = [("3\n5\n", "8"), ("2\n4\n", "6"), ("6\n9\n", "15")]
    i = 1
    for input_text, expected_output in tests:
        print(f"\nTest {i}: add.py with keyboard input\n\tinput: {input_text.strip().replace('\n',',')}\n\texpect: {expected_output}")
        output_text = run_python_script("./code/add.py", input_text)
        assert output_text.find(expected_output) >=0
        i += 1

def test_hello():
    print("Testing for Hello, World!")
    output_text = run_python_script("./code/hello.py", input_text="")
    assert output_text == 'Hello, World!'
