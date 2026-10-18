"""Practice dictionary keys, values, and items."""


def calculate_class_average(student_marks):
    """Use .values() to obtain all marks without needing student names."""
    if not student_marks:
        raise ValueError("The dictionary must contain at least one student")
    return sum(student_marks.values()) / len(student_marks)


def passing_students(student_marks, pass_mark=5):
    """Use .items() when both a key (name) and value (mark) are needed."""
    return [name for name, mark in student_marks.items() if mark >= pass_mark]


if __name__ == "__main__":
    marks = {"Alan": 7, "Maya": 9, "Sam": 4}
    marks["Nina"] = 8  # Adds a new key at the end of insertion order.

    print("All names:", list(marks.keys()))
    print("All marks:", list(marks.values()))
    print("Name/mark pairs:", list(marks.items()))
    print("Average mark:", calculate_class_average(marks))
    print("Passing students:", passing_students(marks))
