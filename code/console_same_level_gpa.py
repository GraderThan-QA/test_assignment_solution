'''
Console program that reads two GPAs from the user, prints each one's academic
level, and reports whether the two GPAs fall in the same level.
Uses the gpa_level function from gpa.py.
'''
from gpa import gpa_level

gpa1 = float(input("Enter first GPA: "))
gpa2 = float(input("Enter second GPA: "))

level1 = gpa_level(gpa1)
level2 = gpa_level(gpa2)

print(f"For GPA {gpa1:.3f} Result: {level1}")
print(f"For GPA {gpa2:.3f} Result: {level2}")

if level1 == level2:
    print("Same level")
else:
    print("Different level")

