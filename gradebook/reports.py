# reports.py
# Developer C — Reporting & summaries
# Branch: feature/reports

from grades import get_average

def get_top_students(students: dict, grades: dict, n: int = 3) -> list :
    """
    Return the top n students with the highest average scores.

    - Returns a list of (student_id, name, average) tuples.
    - Sorted by average in descending order (highest first).
    - If n is greater than the number of students, return all of them.
    - Students with no grades have an average of 0.0.

    Args:
        students (dict): the students database
        grades (dict): the grades database
        n (int): number of top students to return (default 3)

    Returns:
        list[tuple]: list of (student_id, name, average) sorted descending

    Example:
        >>> students = {
        ...   "S001": {"name": "Alice", "id": "S001"},
        ...   "S002": {"name": "Bob",   "id": "S002"},
        ... }
        >>> grades = {"S001": {"Math": 90}, "S002": {"Math": 70}}
        >>> get_top_students(students, grades, n=1)
        [("S001", "Alice", 90.0)]
    """
    
    number_to_display = n if n<= len(students) else len(students)

    student_average_list = {k : sum(v.values()) / len(v.values()) for k,v in grades.items()}
    tuples =[]
    
    for student_id, average in sorted(student_average_list.items(), key=lambda item: item[1],reverse=True):
        tuples.append((student_id, students[student_id]["name"], average))
        
    return tuples[:number_to_display]

    
        
        
def summarize_class(students: dict, grades: dict) -> tuple:
    """
    Return a summary of the whole class as a single tuple.

    The tuple must contain exactly 4 values in this order:
        (total_students, class_average, highest_average, lowest_average)

    - total_students (int): number of students in the database
    - class_average (float): average of all students' averages, rounded to 2 decimals
    - highest_average (float): the best individual average in the class
    - lowest_average (float): the worst individual average in the class

    - If there are no students, return (0, 0.0, 0.0, 0.0).

    Args:
        students (dict): the students database
        grades (dict): the grades database

    Returns:
        tuple: (total_students, class_average, highest_average, lowest_average)

    Example:
        >>> students = {
        ...   "S001": {"name": "Alice", "id": "S001"},
        ...   "S002": {"name": "Bob",   "id": "S002"},
        ... }
        >>> grades = {"S001": {"Math": 80}, "S002": {"Math": 60}}
        >>> summarize_class(students, grades)
        (2, 70.0, 80.0, 60.0)
    """
    
    total_students = len(students)
    
    if total_students <= 0:
        return 0, 0.0, 0.0, 0
    
    
    student_average_list = {k : sum(v.values()) / len(v.values()) for k,v in grades.items()}
    class_average = sum(student_average_list.values()) / len(student_average_list.values())
    sorted_average = sorted(list(student_average_list.values()),reverse=True)
    
    return total_students, round(class_average,2), sorted_average[0], sorted_average[-1]
    
    


def export_report(students: dict, grades: dict) -> str:
    """
    Generate and return a formatted text report as a single string.

    The report must follow this exact format:
    ─────────────────────────────────
    GRADEBOOK REPORT
    Total students: 3
    Class average:  75.33

    STUDENT DETAILS
    S001 | Alice Smith     | Avg:  85.00 | Subjects: English, Math, Science
    S002 | Bob Martin      | Avg:  62.50 | Subjects: Math, Science
    S003 | Carol White     | Avg:   0.00 | Subjects: none
    ─────────────────────────────────

    Rules:
    - Student names are left-aligned in a field of 16 characters.
    - Averages are right-aligned with 2 decimal places.
    - Subjects are listed in alphabetical order, comma-separated.
    - If a student has no grades, show "none" for subjects.
    - Use summarize_class() to get total_students and class_average.
    - Students are listed in alphabetical order by name.

    Args:
        students (dict): the students database
        grades (dict): the grades database

    Returns:
        str: the complete formatted report
    """

    student_average_list = {k : sum(v.values()) / len(v.values()) for k,v in grades.items()}
    students_report =[]
    student_names = []
    
    for student in students.values():
        student_names.append(student["name"])
    
        
    max_student_name = len(max(student_names, key=len))
    
    
    for student_id, average in student_average_list.items():
        subjects = ', '.join(grades[student_id]) if grades[student_id] else "None"
        space_num = ( max_student_name + 5 ) - len(students[student_id]["name"])
        students_report.append(f"{student_id} | {students[student_id]["name"]}{' '* space_num}| Avg: {'' if average >= 10 else ' '} {average} | Subjects: {subjects}")
        
    students_report.sort(key = lambda item : item[1])  
    
    return\
        f"""
        GRADEBOOK REPORT
        Total students: {summarize_class(students,grades)[0]}
        Class average: {summarize_class(students,grades)[1]}
        
        STUDENT DETAILS
        {'\n        '.join(students_report)}      
        __________________________________________________________________
    """