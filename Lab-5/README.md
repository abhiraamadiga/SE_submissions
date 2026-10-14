# Lab 5: Static Code Analysis — Animal Shelter Adoption Register

**Course:** Software Engineering (Fifth Semester)  
**Student:** Abhiraam Adiga  
**SRN:** PES1UG24CS015  
**Assigned Repository:** [SETAPESU26/L5_16_pet_shelter](https://github.com/SETAPESU26/L5_16_pet_shelter)  
**Source Program:** `pet_shelter.py`

---

## 1. Objective

The objective of this lab is to enhance Python code quality, security posture, and PEP 8 style compliance using three industry-standard static analysis tools:
- **Pylint:** Inspects code quality, structural programming defects, dangerous default values, exception handling, and PEP 8 conventions, rating code on a 10-point scale.
- **Bandit:** Audits Python source code for security vulnerabilities and insecure coding patterns (e.g., SQL injection, weak pseudo-random generation, silent error suppression).
- **Flake8:** Enforces PEP 8 style compliance, line length restrictions, whitespace consistency, and syntax rules.

---

## 2. Environment Setup

The lab is configured inside the repository's virtual environment (`.venv`).

### Dependencies
The required packages are defined in `requirements.txt`:
```txt
pylint>=4.1.0
bandit>=1.9.0
flake8>=7.4.0
```

### Installation

#### Windows (PowerShell)
```powershell
# Activate the existing virtual environment
& "..\.venv\Scripts\Activate.ps1"

# Or execute pip directly using the environment's Python binary
& "..\.venv\Scripts\python.exe" -m pip install -r requirements.txt
```

#### Linux / macOS (Bash)
```bash
source ../.venv/bin/activate
python -m pip install -r requirements.txt
```

---

## 3. Running the Program

To run the cleaned animal shelter adoption register script:

#### Windows (PowerShell)
```powershell
& "..\.venv\Scripts\python.exe" pet_shelter.py
```

#### Linux / macOS (Bash)
```bash
python pet_shelter.py
```

**Expected Sample Output:**
```text
Kiwi PET-8823 active
```

---

## 4. Running Static Analysis & Generating Reports

Run the following commands from within the `Lab-5/` directory to generate the static analysis reports:

#### Windows (PowerShell / Command Prompt)
```powershell
# Run Pylint
& "..\.venv\Scripts\python.exe" -m pylint pet_shelter.py > pylint_after.txt

# Run Bandit (security audit)
& "..\.venv\Scripts\python.exe" -m bandit -r pet_shelter.py > bandit_after.txt

# Run Flake8 (style and syntax audit)
& "..\.venv\Scripts\python.exe" -m flake8 pet_shelter.py > flake8_after.txt
```

#### Linux / macOS (Bash)
```bash
pylint pet_shelter.py > pylint_after.txt
bandit -r pet_shelter.py > bandit_after.txt
flake8 pet_shelter.py > flake8_after.txt
```

---

## 5. Summary of Implemented Fixes

1. **SQL Injection Mitigation (Bandit B608, CWE-89):**  
   Replaced insecure `%` string interpolation with parameterized SQL placeholders (`(?, ?, ?, 0)`), preventing arbitrary SQL execution through untrusted input.
2. **Cryptographically Secure Random Generation (Bandit B311, CWE-330):**  
   Replaced predictable `random.randint` with `secrets.SystemRandom().randint(1000, 9999)` for adoption code generation.
3. **Elimination of Silent Exception Suppression (Bandit B110, Pylint W0718):**  
   Replaced broad `except Exception: pass` in `clear_unadopted()` with specific `sqlite3.Error` handling, proper logging via `logging.getLogger`, and return of affected row counts.
4. **Mutable Default Argument Fix (Pylint W0102):**  
   Replaced `tags=[]` in `register_pet` with `tags=None` and initialized `tags = []` conditionally inside the function, preventing cross-call list mutation.
5. **Bare Exception & NoneType Crash Guard (Pylint W0702, Flake8 E722):**  
   Fixed `oldest_available()` to verify `if row is not None:` before subscripting `row[0]`, preventing `TypeError` on empty databases without relying on crash-masking bare `except:` blocks.
6. **Nonexistent Pet Adoption Guard (Manual Review):**  
   Added `AND adopted = 0` and checked `cur.rowcount > 0` in `adopt()` before incrementing adoption counters, preventing corrupt statistics on invalid pet IDs.
7. **Global State Encapsulation (Pylint W0603):**  
   Eliminated `global adoption_count` mutations, managing statistics through structured state encapsulation.
8. **PEP 8 Naming Conventions (Pylint C0103):**  
   Converted camelCase function names to standard snake_case (`register_pet`, `adoption_code`, `oldest_available`, `clear_unadopted`, `shelter_status`).
9. **PEP 8 Line Length & Compound Statement Formatting (Flake8 E501, E701):**  
   Reformatted multi-line SQL strings, wrapped docstrings under 79 characters, and split one-line compound statements (`if ...: return ...`) into indented blocks.
10. **Module & Function Documentation (Pylint C0114, C0116):**  
    Added comprehensive PEP 257 docstrings for the module and all functions.

---

## 6. Verification Results

| Tool | Baseline (Before) | Final (After) | Status |
|---|---|---|---|
| **Pylint** | `3.95/10` | **`10.00/10`** | **Target Achieved (> 9.5/10)** |
| **Bandit** | 3 issues (1 Medium, 2 Low) | **0 issues identified** | **All vulnerabilities resolved** |
| **Flake8** | 5 violations (E501, E722, E701) | **0 violations** | **Clean PEP 8 compliance** |

---

## 7. Deliverables in `Lab-5/`

- `pet_shelter.py`: Cleaned and refactored Python source code.
- `requirements.txt`: Static analysis tool dependencies.
- `issues.md`: Detailed documentation table of all identified and resolved issues.
- `reflection.md`: Technical reflections on static analysis, tool differences, and workflows.
- `pylint_before.txt` & `pylint_after.txt`: Complete baseline and final Pylint reports.
- `bandit_before.txt` & `bandit_after.txt`: Complete baseline and final Bandit reports.
- `flake8_before.txt` & `flake8_after.txt`: Complete baseline and final Flake8 reports.
- `README.md`: Lab overview, setup, execution instructions, and verification summary.
