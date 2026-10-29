"""
test_student_grades.py
-----------------------
Comprehensive test suite for student_grades.py achieving:
- 100% Code / Statement Coverage (33/33 statements)
- 100% Branch Coverage (26/26 branches)

Software Engineering - Lab 6
"""

import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# ============================================================================
# Starter test cases
# ============================================================================

def test_s_grade():
    assert letter_grade(95) == "S"


def test_eligible():
    assert exam_eligibility(80, True, False) == "eligible"


# ============================================================================
# Comprehensive Branch & Code Coverage Tests for letter_grade(marks)
# ============================================================================

def test_letter_grade_negative():
    """Branch: marks < 0 (True)."""
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(-1)


def test_letter_grade_above_max():
    """Branch: marks > 100 (True)."""
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(101)


@pytest.mark.parametrize("marks,expected", [
    (100, "S"),  # Boundary: upper max valid
    (90, "S"),   # Boundary: lower threshold for 'S'
    (89, "A"),   # Boundary: upper threshold for 'A'
    (80, "A"),   # Boundary: lower threshold for 'A'
    (79, "B"),   # Boundary: upper threshold for 'B'
    (70, "B"),   # Boundary: lower threshold for 'B'
    (69, "C"),   # Boundary: upper threshold for 'C'
    (60, "C"),   # Boundary: lower threshold for 'C'
    (59, "D"),   # Boundary: upper threshold for 'D'
    (50, "D"),   # Boundary: lower threshold for 'D'
    (49, "E"),   # Boundary: upper threshold for 'E'
    (40, "E"),   # Boundary: lower threshold for 'E'
    (39, "F"),   # Boundary: upper threshold for 'F'
    (0, "F"),    # Boundary: lowest valid mark
])
def test_letter_grade_boundaries(marks, expected):
    """Branches: Each threshold evaluated for both True and False."""
    assert letter_grade(marks) == expected


# ============================================================================
# Comprehensive Branch & Code Coverage Tests for final_marks(...)
# ============================================================================

def test_final_marks_internal_out_of_range():
    """Branch: internal > 40 (True), external <= 60 (False)."""
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(41, 50, False)


def test_final_marks_external_out_of_range():
    """Branch: internal <= 40 (False), external > 60 (True)."""
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(35, 61, False)


def test_final_marks_both_out_of_range():
    """Branch: internal > 40 (True), external > 60 (True)."""
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(45, 65, True)


def test_final_marks_without_project():
    """Branch: has_project is False (branch 23 -> 27)."""
    assert final_marks(30, 45, False) == 75


def test_final_marks_with_project_no_cap():
    """Branch: has_project is True, total <= 100 (branch 25 -> 27)."""
    assert final_marks(30, 40, True) == 75


def test_final_marks_with_project_exact_100():
    """Branch: has_project is True, total == 100 boundary."""
    assert final_marks(40, 55, True) == 100


def test_final_marks_with_project_capped():
    """Branch: has_project is True, total > 100 -> capped to 100 (branch 25 -> 26)."""
    assert final_marks(40, 60, True) == 100


# ============================================================================
# Comprehensive Branch & Code Coverage Tests for exam_eligibility(...)
# ============================================================================

def test_exam_eligibility_fees_unpaid():
    """Branch: not fees_paid is True (branch 31 -> 32)."""
    assert exam_eligibility(90, False, True) == "blocked"
    assert exam_eligibility(50, False, False) == "blocked"


def test_exam_eligibility_attendance_above_75():
    """Branch: fees_paid True, attendance >= 75 is True (branch 33 -> 34)."""
    assert exam_eligibility(75, True, False) == "eligible"
    assert exam_eligibility(85, True, True) == "eligible"


def test_exam_eligibility_medical_condonation():
    """Branch: fees_paid True, 65 <= attendance < 75 and has_medical is True (branch 35 -> 36)."""
    assert exam_eligibility(65, True, True) == "eligible"
    assert exam_eligibility(70, True, True) == "eligible"


def test_exam_eligibility_medical_condonation_without_medical():
    """Branch: fees_paid True, 65 <= attendance < 75 and has_medical is False (branch 35 -> 37)."""
    assert exam_eligibility(70, True, False) == "detained"


def test_exam_eligibility_low_attendance_with_medical():
    """Branch: fees_paid True, attendance < 65 even with medical (branch 35 -> 37)."""
    assert exam_eligibility(64, True, True) == "detained"


def test_exam_eligibility_low_attendance_without_medical():
    """Branch: fees_paid True, attendance < 65 without medical (branch 35 -> 37)."""
    assert exam_eligibility(50, True, False) == "detained"
