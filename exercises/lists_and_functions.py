"""Practice using lists, function parameters, and return values."""


def calculate_average(numbers):
    """Return the average of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate an average from an empty list")
    return sum(numbers) / len(numbers)


def add_mark(marks, new_mark):
    """Append a mark to a list, then return the updated list."""
    marks.append(new_mark)
    return marks


if __name__ == "__main__":
    python_marks = [7, 8, 6, 9]
    add_mark(python_marks, 10)
    average = calculate_average(python_marks)
    print("Marks:", python_marks)
    print("Average:", average)
