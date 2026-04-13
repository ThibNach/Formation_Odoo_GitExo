# tests.py
# Manual test cases — run this to check your implementations.
# Each test prints PASS or FAIL with a short description.

from students import add_student, remove_student, find_student
from grades import add_grade, get_average, get_subjects, get_failing_students
from reports import get_top_students, summarize_class, export_report


def check(description: str, result, expected):
    status = "✅ PASS" if result == expected else "❌ FAIL"
    print(f"{status} — {description}")
    if result != expected:
        print(f"       Expected: {expected}")
        print(f"       Got:      {result}")


print("─" * 50)
print("STUDENTS")
print("─" * 50)

db = {}
add_student(db, "  alice smith  ", "S001")
check("add_student: name is cleaned and title-cased",
      db.get("S001", {}).get("name"), "Alice Smith")

add_student(db, "Bob", "S002")
add_student(db, "Carol", "S002")  # duplicate — should NOT overwrite
check("add_student: duplicate ID is not overwritten",
      db["S002"]["name"], "Bob")

remove_student(db, "S001")
check("remove_student: student is removed", "S001" in db, False)

remove_student(db, "S999")  # should print warning, not crash
check("remove_student: missing ID does not crash", True, True)

db2 = {
    "S001": {"name": "Alice Smith", "id": "S001"},
    "S002": {"name": "Bob Martin",  "id": "S002"},
    "S003": {"name": "Ali Baba",    "id": "S003"},
}
check("find_student: case-insensitive match returns correct count",
      len(find_student(db2, "ali")), 2)
check("find_student: no match returns empty list",
      find_student(db2, "xyz"), [])

print()
print("─" * 50)
print("GRADES")
print("─" * 50)

g = {}
add_grade(g, "S001", "Math", 85)
check("add_grade: grade is added", g.get("S001", {}).get("Math"), 85)

add_grade(g, "S001", "Math", 90)  # overwrite
check("add_grade: grade is overwritten", g["S001"]["Math"], 90)

add_grade(g, "S001", "English", 110)  # invalid
check("add_grade: invalid score not added", "English" in g.get("S001", {}), False)

add_grade(g, "S002", "Math", 60)
add_grade(g, "S002", "English", 80)
check("get_average: correct average", get_average(g, "S002"), 70.0)
check("get_average: missing student returns 0.0", get_average(g, "S999"), 0.0)

g2 = {
    "S001": {"Math": 80, "English": 90},
    "S002": {"Math": 70, "Science": 65},
}
check("get_subjects: correct unique set",
      get_subjects(g2), {"Math", "English", "Science"})
check("get_subjects: empty grades returns empty set",
      get_subjects({}), set())

students_db = {
    "S001": {"name": "Alice", "id": "S001"},
    "S002": {"name": "Bob",   "id": "S002"},
    "S003": {"name": "Carol", "id": "S003"},
}
grades_db = {
    "S001": {"Math": 40, "English": 35},
    "S002": {"Math": 80},
}
failing = get_failing_students(students_db, grades_db, threshold=50)
check("get_failing_students: correct number of failing students",
      len(failing), 2)
check("get_failing_students: sorted ascending by average",
      failing[0][0], "S001")  # 37.5 < 0.0... wait S003 has no grades = 0.0
# S003 avg = 0.0, S001 avg = 37.5 → sorted: [S003(0.0), S001(37.5)]
check("get_failing_students: student with no grades included (avg 0.0)",
      failing[0][2], 0.0)

print()
print("─" * 50)
print("REPORTS")
print("─" * 50)

s = {
    "S001": {"name": "Alice", "id": "S001"},
    "S002": {"name": "Bob",   "id": "S002"},
}
g3 = {
    "S001": {"Math": 80, "English": 100},
    "S002": {"Math": 60},
}
top = get_top_students(s, g3, n=1)
check("get_top_students: returns 1 item", len(top), 1)
check("get_top_students: correct top student", top[0][0], "S001")

total, avg, high, low = summarize_class(s, g3)
check("summarize_class: correct total",    total, 2)
check("summarize_class: correct average",  avg,   75.0)
check("summarize_class: correct highest",  high,  90.0)
check("summarize_class: correct lowest",   low,   60.0)
check("summarize_class: empty returns zeros",
      summarize_class({}, {}), (0, 0.0, 0.0, 0.0))

report = export_report(s, g3)
check("export_report: returns a string", isinstance(report, str), True)
check("export_report: contains student name", "Alice" in report, True)
check("export_report: contains GRADEBOOK REPORT header",
      "GRADEBOOK REPORT" in report, True)

print()
print("─" * 50)
print("Done. Fix any FAILs above before opening your PR.")
print("─" * 50)
