"""Small class example showing attributes, methods, and return values."""


class Student:
    def __init__(self, name):
        # Instance attributes belong to this specific Student object.
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def calculate_average(self):
        if not self.marks:
            return None
        # The result returns to whichever code called this method.
        return sum(self.marks) / len(self.marks)

    def summary(self):
        average = self.calculate_average()  # Local variable in this method.
        if average is None:
            return f"{self.name} has no marks yet"
        return f"{self.name}'s average is {average:.2f}"


if __name__ == "__main__":
    student = Student("Alan")
    student.add_mark(7)
    student.add_mark(9)
    print(student.summary())

    result = student.calculate_average()
    print("Returned average:", result)
