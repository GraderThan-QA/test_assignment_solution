'''
Console program that reads a GPA from the user and prints its academic level.
Uses the gpa_level function from gpa.py.
'''
from gpa import gpa_level

gpa = float(input("Enter GPA: "))
result = gpa_level(gpa)
print(f"For GPA {gpa:.3f} Result: {result}")
