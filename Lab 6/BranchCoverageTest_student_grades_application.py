"""
BranchCoverageTest_student_grades_application.py
------------------------------------------------
Alias module exposing all test cases from BranchCoverageTest_student_grades.py
to strictly conform to the deliverable naming convention:
BranchCoverageTest_xxxx_application.py
"""

from BranchCoverageTest_student_grades import (
    test_letter_grade_negative,
    test_letter_grade_above_max,
    test_letter_grade_boundaries,
    test_final_marks_internal_out_of_range,
    test_final_marks_external_out_of_range,
    test_final_marks_both_out_of_range,
    test_final_marks_without_project,
    test_final_marks_with_project_no_cap,
    test_final_marks_with_project_exact_100,
    test_final_marks_with_project_capped,
    test_exam_eligibility_fees_unpaid,
    test_exam_eligibility_attendance_above_75,
    test_exam_eligibility_medical_condonation,
    test_exam_eligibility_medical_condonation_without_medical,
    test_exam_eligibility_low_attendance_with_medical,
    test_exam_eligibility_low_attendance_without_medical,
)

__all__ = [
    "test_letter_grade_negative",
    "test_letter_grade_above_max",
    "test_letter_grade_boundaries",
    "test_final_marks_internal_out_of_range",
    "test_final_marks_external_out_of_range",
    "test_final_marks_both_out_of_range",
    "test_final_marks_without_project",
    "test_final_marks_with_project_no_cap",
    "test_final_marks_with_project_exact_100",
    "test_final_marks_with_project_capped",
    "test_exam_eligibility_fees_unpaid",
    "test_exam_eligibility_attendance_above_75",
    "test_exam_eligibility_medical_condonation",
    "test_exam_eligibility_medical_condonation_without_medical",
    "test_exam_eligibility_low_attendance_with_medical",
    "test_exam_eligibility_low_attendance_without_medical",
]
