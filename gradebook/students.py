# students.py
# Developer A — Student management
# Branch: feature/students

# The student database is a dictionary with this structure:
# {
#   "S001": {"name": "Alice", "id": "S001"},
#   "S002": {"name": "Bob",   "id": "S002"},
# }


def add_student(students: dict, name: str, student_id: str) -> dict:
    """
    Add a new student to the students dictionary.

    - If student_id already exists, do NOT overwrite it.
      Print a warning message instead: "Student S001 already exists."
    - Student names should be stored with stripped whitespace and title case.
      Example: "  alice smith  " → "Alice Smith"

    Args:
        students (dict): the current students database
        name (str): full name of the student
        student_id (str): unique identifier (e.g. "S001")

    Returns:
        dict: the updated students dictionary

    Example:
        >>> db = {}
        >>> add_student(db, "alice", "S001")
        >>> db
        {"S001": {"name": "Alice", "id": "S001"}}
    """
    # TODO: implement this function
    raise NotImplementedError("add_student is not implemented yet.")


def remove_student(students: dict, student_id: str) -> dict:
    """
    Remove a student from the students dictionary by their ID.

    - If the student_id does not exist, print a warning:
      "Student S999 not found." and return the dictionary unchanged.

    Args:
        students (dict): the current students database
        student_id (str): the ID of the student to remove

    Returns:
        dict: the updated students dictionary

    Example:
        >>> db = {"S001": {"name": "Alice", "id": "S001"}}
        >>> remove_student(db, "S001")
        >>> db
        {}
    """
    # TODO: implement this function
    raise NotImplementedError("remove_student is not implemented yet.")


def find_student(students: dict, name: str) -> list:
    """
    Search for students whose name contains the given string (case-insensitive).

    - Returns a list of matching student dicts.
    - Returns an empty list if no match is found.
    - The search must be case-insensitive: "alice" matches "Alice Smith".

    Args:
        students (dict): the current students database
        name (str): the search string

    Returns:
        list: a list of matching student dicts

    Example:
        >>> db = {
        ...   "S001": {"name": "Alice Smith", "id": "S001"},
        ...   "S002": {"name": "Bob Martin",  "id": "S002"},
        ... }
        >>> find_student(db, "alice")
        [{"name": "Alice Smith", "id": "S001"}]
        >>> find_student(db, "xyz")
        []
    """
    # TODO: implement this function
    raise NotImplementedError("find_student is not implemented yet.")
