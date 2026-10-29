"""
test_student_grades.py
-----------------------
Test suite for student_grades.py achieving 100% Code Coverage (Line Coverage).
Software Engineering - Lab 6
"""

import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# Example / starter tests:
def test_s_grade():
    assert letter_grade(95) == "S"


def test_eligible():
    assert exam_eligibility(80, True, False) == "eligible"


# Extended test cases achieving 100% Code (Statement) Coverage:

def test_letter_grade_invalid_negative():
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(-5)


def test_letter_grade_a():
    assert letter_grade(85) == "A"


def test_letter_grade_b():
    assert letter_grade(75) == "B"


def test_letter_grade_c():
    assert letter_grade(65) == "C"


def test_letter_grade_d():
    assert letter_grade(55) == "D"


def test_letter_grade_e():
    assert letter_grade(45) == "E"


def test_letter_grade_f():
    assert letter_grade(35) == "F"


def test_final_marks_invalid_internal():
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(45, 50, False)


def test_final_marks_with_project_and_cap():
    assert final_marks(40, 60, True) == 100


def test_exam_eligibility_fees_unpaid():
    assert exam_eligibility(80, False, False) == "blocked"


def test_exam_eligibility_medical_condonation():
    assert exam_eligibility(70, True, True) == "eligible"


def test_exam_eligibility_detained():
    assert exam_eligibility(50, True, False) == "detained"
