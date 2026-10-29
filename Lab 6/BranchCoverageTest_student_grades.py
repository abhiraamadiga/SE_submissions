import pytest
from student_grades import letter_grade, final_marks, exam_eligibility

# -------------------------------------------------------------
# Tests for letter_grade(marks)
# Branches to cover:
# 1. marks < 0 (True)
# 2. marks > 100 (True)
# 3. marks in [0, 100] (False for invalid condition)
# 4. Each grade range: S (>=90), A (>=80), B (>=70), C (>=60), D (>=50), E (>=40), F (<40)
# -------------------------------------------------------------

def test_letter_grade_negative():
    with pytest.raises(ValueError, match='invalid marks'):
        letter_grade(-1)

def test_letter_grade_above_max():
    with pytest.raises(ValueError, match='invalid marks'):
        letter_grade(101)

@pytest.mark.parametrize('marks,expected', [
    (100, 'S'),
    (90, 'S'),
    (89, 'A'),
    (80, 'A'),
    (79, 'B'),
    (70, 'B'),
    (69, 'C'),
    (60, 'C'),
    (59, 'D'),
    (50, 'D'),
    (49, 'E'),
    (40, 'E'),
    (39, 'F'),
    (0, 'F'),
])
def test_letter_grade_boundaries(marks, expected):
    assert letter_grade(marks) == expected


# -------------------------------------------------------------
# Tests for final_marks(internal, external, has_project)
# Branches to cover:
# 1. internal > 40 (True)
# 2. external > 60 (True)
# 3. Both internal <= 40 and external <= 60 (False for validation)
# 4. has_project is False (branch 23 -> 27)
# 5. has_project is True, total > 100 (branch 25 -> 26 -> 27)
# 6. has_project is True, total <= 100 (branch 25 -> 27)
# -------------------------------------------------------------

def test_final_marks_internal_out_of_range():
    with pytest.raises(ValueError, match='marks out of range'):
        final_marks(41, 50, False)

def test_final_marks_external_out_of_range():
    with pytest.raises(ValueError, match='marks out of range'):
        final_marks(35, 61, False)

def test_final_marks_both_out_of_range():
    with pytest.raises(ValueError, match='marks out of range'):
        final_marks(45, 65, True)

def test_final_marks_without_project():
    assert final_marks(30, 45, False) == 75

def test_final_marks_with_project_no_cap():
    assert final_marks(30, 40, True) == 75

def test_final_marks_with_project_exact_100():
    assert final_marks(40, 55, True) == 100

def test_final_marks_with_project_capped():
    assert final_marks(40, 60, True) == 100


# -------------------------------------------------------------
# Tests for exam_eligibility(attendance, fees_paid, has_medical)
# Branches to cover:
# 1. fees_paid is False (branch 31 -> 32)
# 2. fees_paid is True, attendance >= 75 (branch 33 -> 34)
# 3. fees_paid is True, 65 <= attendance < 75, has_medical True (branch 35 -> 36)
# 4. fees_paid is True, 65 <= attendance < 75, has_medical False (branch 35 -> 37)
# 5. fees_paid is True, attendance < 65, has_medical True (branch 35 -> 37)
# 6. fees_paid is True, attendance < 65, has_medical False (branch 35 -> 37)
# -------------------------------------------------------------

def test_exam_eligibility_fees_unpaid():
    assert exam_eligibility(90, False, True) == 'blocked'
    assert exam_eligibility(50, False, False) == 'blocked'

def test_exam_eligibility_attendance_above_75():
    assert exam_eligibility(75, True, False) == 'eligible'
    assert exam_eligibility(85, True, True) == 'eligible'

def test_exam_eligibility_medical_condonation():
    assert exam_eligibility(65, True, True) == 'eligible'
    assert exam_eligibility(70, True, True) == 'eligible'

def test_exam_eligibility_medical_condonation_without_medical():
    assert exam_eligibility(70, True, False) == 'detained'

def test_exam_eligibility_low_attendance_with_medical():
    assert exam_eligibility(64, True, True) == 'detained'

def test_exam_eligibility_low_attendance_without_medical():
    assert exam_eligibility(50, True, False) == 'detained'