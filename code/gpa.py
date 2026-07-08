def gpa_level(gpa : float) -> str:
    '''
    Determines the academic level based on the GPA.
    Args:
        gpa (float): The grade point average.
    Returns:
        str: The academic level.
    '''
    if not valid_gpa(gpa):
        return "Invalid GPA"

    if gpa >= 3.8:
        result = "Summa Cum Laude"
    elif gpa >= 3.6:
        result = "Magna Cum Laude"
    elif gpa >= 3.4:
        result = "Cum Laude"
    elif gpa <= 1.8:
        result = "Academic Probation"
    else:
        result = "Passing"
    return result

def valid_gpa(gpa : float) -> bool:
    '''
    Validates the GPA value.
    Args:
        gpa (float): The grade point average.
    Returns:
        bool: True if valid, False otherwise.
    '''
    return 0 <= gpa <= 4.0

