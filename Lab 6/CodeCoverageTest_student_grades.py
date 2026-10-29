"""
CodeCoverageTest_student_grades.py
-----------------------------------
Test suite designed to achieve 100% Code (Line/Statement) Coverage
for student_grades.py (Software Engineering Lab 6).

Covers all 33 executable statements across letter_grade, final_marks,
and exam_eligibility functions.
"""

import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# ============================================================================
# 1. Statement Coverage Tests for letter_grade(marks)
# ============================================================================

def test_letter_grade_invalid_negative():
    """Executes lines 2-3: marks < 0 validation check raising ValueError."""
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(-5)


def test_letter_grade_s():
    """Executes lines 4-5: marks >= 90 returning grade 'S'."""
    assert letter_grade(95) == "S"


def test_letter_grade_a():
    """Executes lines 6-7: marks >= 80 returning grade 'A'."""
    assert letter_grade(85) == "A"


def test_letter_grade_b():
    """Executes lines 8-9: marks >= 70 returning grade 'B'."""
    assert letter_grade(75) == "B"


def test_letter_grade_c():
    """Executes lines 10-11: marks >= 60 returning grade 'C'."""
    assert letter_grade(65) == "C"


def test_letter_grade_d():
    """Executes lines 12-13: marks >= 50 returning grade 'D'."""
    assert letter_grade(55) == "D"


def test_letter_grade_e():
    """Executes lines 14-15: marks >= 40 returning grade 'E'."""
    assert letter_grade(45) == "E"


def test_letter_grade_f():
    """Executes line 16: fallthrough returning grade 'F'."""
    assert letter_grade(35) == "F"


# ============================================================================
# 2. Statement Coverage Tests for final_marks(internal, external, has_project)
# ============================================================================

def test_final_marks_invalid_internal():
    """Executes lines 20-21: internal > 40 validation check raising ValueError."""
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(45, 50, False)


def test_final_marks_with_project_and_cap():
    """Executes lines 22-27: total calculation, has_project bonus, and total > 100 cap."""
    # internal (40) + external (60) = 100 + 5 (project bonus) = 105 -> capped to 100
    assert final_marks(40, 60, True) == 100


# ============================================================================
# 3. Statement Coverage Tests for exam_eligibility(attendance, fees_paid, has_medical)
# ============================================================================

def test_exam_eligibility_fees_unpaid():
    """Executes lines 31-32: not fees_paid returning 'blocked'."""
    assert exam_eligibility(80, False, False) == "blocked"


def test_exam_eligibility_high_attendance():
    """Executes lines 33-34: attendance >= 75 returning 'eligible'."""
    assert exam_eligibility(80, True, False) == "eligible"


def test_exam_eligibility_medical_condonation():
    """Executes lines 35-36: attendance >= 65 and has_medical returning 'eligible'."""
    assert exam_eligibility(70, True, True) == "eligible"


def test_exam_eligibility_detained():
    """Executes line 37: fallthrough returning 'detained'."""
    assert exam_eligibility(50, True, False) == "detained"
