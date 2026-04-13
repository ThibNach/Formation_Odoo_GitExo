# main.py
# Demo runner — shared by the whole team
# Run this file to see the full system in action once all functions are implemented.

from students import add_student, remove_student, find_student
from grades import add_grade, get_average, get_subjects, get_failing_students
from reports import get_top_students, summarize_class, export_report

# ── Build the student database ─────────────────────────────────────────────────
students = {}
add_student(students, "Alice Smith",  "S001")
add_student(students, "Bob Martin",   "S002")
add_student(students, "Carol White",  "S003")
add_student(students, "David Lee",    "S004")
add_student(students, "Eve Johnson",  "S005")
add_student(students, "  alice smith  ", "S001")  # duplicate — should warn, not overwrite

# ── Build the grades database ──────────────────────────────────────────────────
grades = {}
add_grade(grades, "S001", "Math",    92)
add_grade(grades, "S001", "English", 88)
add_grade(grades, "S001", "Science", 95)

add_grade(grades, "S002", "Math",    55)
add_grade(grades, "S002", "English", 48)

add_grade(grades, "S003", "Math",    70)
add_grade(grades, "S003", "Science", 65)
add_grade(grades, "S003", "English", 80)

add_grade(grades, "S004", "Math",    30)
add_grade(grades, "S004", "English", 40)

add_grade(grades, "S005", "Math",    110)  # invalid score — should warn

# ── Run queries ────────────────────────────────────────────────────────────────
print("=== Search: 'lee' ===")
print(find_student(students, "lee"))

print("\n=== Average for S001 ===")
print(get_average(grades, "S001"))

print("\n=== All subjects in the class ===")
print(get_subjects(grades))

print("\n=== Failing students (below 50) ===")
for entry in get_failing_students(students, grades, threshold=50):
    print(entry)

print("\n=== Top 3 students ===")
for entry in get_top_students(students, grades, n=3):
    print(entry)

print("\n=== Class summary ===")
total, avg, high, low = summarize_class(students, grades)
print(f"Total: {total} | Class avg: {avg} | Best: {high} | Worst: {low}")

print("\n=== Full report ===")
print(export_report(students, grades))
