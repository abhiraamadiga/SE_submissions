# Lab 6: Code and Branch Coverage Analysis

**Student Name**: Abhiraam Adiga  
**SRN**: PES1UG24CS015  
**Section**: A  
**Course**: Software Engineering (Fifth Semester)  
**Assigned Repository**: [SETAPESU26/L6_L7_16_student_grades](https://github.com/SETAPESU26/L6_L7_16_student_grades)  

---

## 1. Objectives

- Understand the difference between **line coverage** and **branch coverage**.
- Use Python's `coverage` tool to measure, analyze, and systematically improve test coverage.
- Interpret coverage reports and identify untested code paths.
- Design targeted test cases covering boundary values, exception handlers, and decision branches.
- Achieve minimum 90% to 100% code coverage and branch coverage.

---

## 2. Environment & Dependencies

- **Python**: 3.12.10
- **pytest**: 9.2.0
- **coverage**: 7.17.0
- **Pillow**: 12.0.0 (for automated high-resolution terminal screenshot generation)

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 3. Module Under Test (`student_grades.py`)

The application module consists of three core business logic functions:
1. `letter_grade(marks)`: Validates marks in range `[0, 100]`, raises `ValueError` for out-of-bounds input, and maps valid scores to letter grades `S`, `A`, `B`, `C`, `D`, `E`, or `F`.
2. `final_marks(internal, external, has_project)`: Validates `internal <= 40` and `external <= 60`, adds a 5-mark project bonus if `has_project` is True, and caps the result at 100.
3. `exam_eligibility(attendance, fees_paid, has_medical)`: Checks if student has cleared fees (returns `"blocked"` if not), checks standard attendance threshold (`>= 75%` -> `"eligible"`), condonation with medical certificate (`>= 65%` and `has_medical` -> `"eligible"`), or `"detained"`.

---

## 4. Phase 1: Baseline Analysis (Initial State)

Running the initial starter test suite (`test_student_grades.py`):
```powershell
coverage run -m pytest test_student_grades.py
coverage report -m
```

### Initial Coverage Report
```text
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
student_grades.py           33     24    27%   3, 6-16, 20-27, 32, 35-37
test_student_grades.py       6      0   100%
------------------------------------------------------
TOTAL                       39     24    38%
```
Initial code coverage for `student_grades.py` is only **27%**, with 24 statements unreached.

---

## 5. Phase 2: Code (Statement) Coverage Test Suite

### Deliverable: `CodeCoverageTest_student_grades.py` / `CodeCoverageTest_student_grades_application.py`

Targeted test cases were authored to execute every single statement across all three functions:
- `test_letter_grade_invalid_negative`: Triggers input validation (`marks < 0`) and exception raise.
- `test_letter_grade_s` through `test_letter_grade_f`: Executes each branch body return statement (`S`, `A`, `B`, `C`, `D`, `E`, `F`).
- `test_final_marks_invalid_internal`: Triggers out-of-range exception.
- `test_final_marks_with_project_and_cap`: Executes total calculation, bonus addition (`total += 5`), cap check (`total > 100`), and cap assignment (`total = 100`).
- `test_exam_eligibility_fees_unpaid`: Triggers `not fees_paid` returning `"blocked"`.
- `test_exam_eligibility_high_attendance`: Triggers `attendance >= 75` returning `"eligible"`.
- `test_exam_eligibility_medical_condonation`: Triggers `attendance >= 65 and has_medical` returning `"eligible"`.
- `test_exam_eligibility_detained`: Triggers fallthrough return `"detained"`.

### Execution Command
```powershell
coverage run -m pytest CodeCoverageTest_student_grades.py
coverage report -m
```

### Code Coverage Results
```text
Name                                 Stmts   Miss  Cover   Missing
------------------------------------------------------------------
CodeCoverageTest_student_grades.py      32      0   100%
student_grades.py                       33      0   100%
------------------------------------------------------------------
TOTAL                                   65      0   100%
```

Achieved **100% Code Coverage** (33/33 statements executed).

### Terminal Screenshot
![Code Coverage Screenshot](code_coverage_screenshot.png)
