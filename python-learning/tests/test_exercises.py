"""Tests for starter Python examples, using the standard library."""

import unittest

from exercises.lists_and_functions import calculate_average, add_mark
from exercises.dictionaries import calculate_class_average, passing_students
from exercises.oop import Student


class TestListsAndFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(calculate_average([7, 8, 6, 9]), 7.5)

    def test_empty_average(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_add_mark(self):
        marks = [7]
        self.assertEqual(add_mark(marks, 9), [7, 9])


class TestDictionaries(unittest.TestCase):
    def test_average_of_values(self):
        self.assertEqual(calculate_class_average({"Alan": 7, "Maya": 9}), 8)

    def test_passing_students(self):
        self.assertEqual(passing_students({"Alan": 7, "Sam": 4}), ["Alan"])

    def test_empty_dictionary(self):
        with self.assertRaises(ValueError):
            calculate_class_average({})


class TestStudent(unittest.TestCase):
    def test_student_average(self):
        student = Student("Alan")
        student.add_mark(7)
        student.add_mark(9)
        self.assertEqual(student.calculate_average(), 8)

    def test_student_without_marks(self):
        self.assertIsNone(Student("Maya").calculate_average())

    def test_students_have_separate_lists(self):
        alan = Student("Alan")
        maya = Student("Maya")
        alan.add_mark(10)
        self.assertEqual(maya.marks, [])


if __name__ == "__main__":
    unittest.main()
