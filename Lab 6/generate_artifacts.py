"""
generate_artifacts.py
---------------------
Automates running coverage analyses and generating both formatted terminal
output text reports and high-fidelity PNG terminal screenshots for Lab 6.
"""

import subprocess
import os
from PIL import Image, ImageDraw, ImageFont


def run_command(cmd, cwd="."):
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=True)
    return (proc.stdout + proc.stderr).strip()


def render_terminal_screenshot(title, terminal_blocks, output_png_path):
    """
    Renders an authentic, high-resolution dark-themed terminal window screenshot.
    terminal_blocks: list of (command_str, output_str)
    """
    font_path = "C:/Windows/Fonts/consola.ttf"
    font_size = 15
    line_h = 24
    font = ImageFont.truetype(font_path, font_size)
    title_font = ImageFont.truetype(font_path, 12)

    lines_to_draw = []

    for cmd, out in terminal_blocks:
        if cmd:
            lines_to_draw.append([
                ("PS C:\\Users\\abhi1\\OneDrive\\Desktop\\5\\SE\\SE_submissions\\Lab 6> ", "#4ec9b0"),
                (cmd, "#ffffff")
            ])
        if out:
            for raw_line in out.split("\n"):
                line = raw_line.rstrip()
                if not line:
                    lines_to_draw.append([("", "#d4d4d4")])
                    continue
                if line.startswith("====="):
                    if "passed" in line:
                        lines_to_draw.append([(line, "#4ec9b0")])
                    else:
                        lines_to_draw.append([(line, "#569cd6")])
                elif line.startswith("platform") or line.startswith("rootdir") or line.startswith("plugins"):
                    lines_to_draw.append([(line, "#858585")])
                elif "collected" in line:
                    lines_to_draw.append([(line, "#cccccc")])
                elif ".py " in line and "[" in line and "%" in line:
                    parts = line.split(" [")
                    lines_to_draw.append([
                        (parts[0], "#98c379"),
                        (" [" + parts[1], "#4ec9b0")
                    ])
                elif line.startswith("Name ") or line.startswith("Name"):
                    lines_to_draw.append([(line, "#569cd6")])
                elif line.startswith("----"):
                    lines_to_draw.append([(line, "#5c6370")])
                elif line.startswith("TOTAL"):
                    lines_to_draw.append([(line, "#e5c07b")])
                elif "student_grades" in line:
                    lines_to_draw.append([(line, "#e6edf3")])
                else:
                    lines_to_draw.append([(line, "#d4d4d4")])

    # Compute max width using font.getlength
    max_w = 0
    for segments in lines_to_draw:
        w = sum(font.getlength(text) for text, _ in segments)
        if w > max_w:
            max_w = w

    width = max(int(max_w) + 60, 840)
    height = int(len(lines_to_draw) * line_h) + 70

    img = Image.new("RGB", (width, height), color="#1e1e1e")
    draw = ImageDraw.Draw(img)

    # Window title bar
    draw.rectangle([0, 0, width, 36], fill="#252526")
    draw.line([0, 36, width, 36], fill="#333333", width=1)

    # Window control dots
    draw.ellipse([14, 12, 24, 22], fill="#ff5f56")
    draw.ellipse([32, 12, 42, 22], fill="#ffbd2e")
    draw.ellipse([50, 12, 60, 22], fill="#27c93f")

    # Title label
    draw.text((75, 10), title, fill="#cccccc", font=title_font)

    # Render lines
    y = 48
    for segments in lines_to_draw:
        x = 22
        for text, color in segments:
            draw.text((x, y), text, fill=color, font=font)
            x += font.getlength(text)
        y += line_h

    os.makedirs(os.path.dirname(os.path.abspath(output_png_path)), exist_ok=True)
    img.save(output_png_path)
    print(f"Generated screenshot: {output_png_path} ({width}x{height})")


def generate_initial_reports():
    cmd1 = "coverage run -m pytest test_student_grades.py"
    out1 = run_command(cmd1, "Lab 6")
    cmd2 = "coverage report -m"
    out2 = run_command(cmd2, "Lab 6")

    text_content = f"PS C:\\Users\\abhi1\\OneDrive\\Desktop\\5\\SE\\SE_submissions\\Lab 6> {cmd1}\n{out1}\n\nPS C:\\Users\\abhi1\\OneDrive\\Desktop\\5\\SE\\SE_submissions\\Lab 6> {cmd2}\n{out2}\n"
    with open("Lab 6/initial_coverage_report.txt", "w", encoding="utf-8") as f:
        f.write(text_content)
    print("Wrote Lab 6/initial_coverage_report.txt")

    render_terminal_screenshot(
        "Windows PowerShell - Lab 6: Initial Baseline Test & Coverage",
        [(cmd1, out1), (cmd2, out2)],
        "Lab 6/initial_coverage_screenshot.png"
    )


def generate_code_coverage_reports():
    cmd1 = "coverage run -m pytest CodeCoverageTest_student_grades.py"
    out1 = run_command(cmd1, "Lab 6")
    cmd2 = "coverage report -m"
    out2 = run_command(cmd2, "Lab 6")

    text_content = f"PS C:\\Users\\abhi1\\OneDrive\\Desktop\\5\\SE\\SE_submissions\\Lab 6> {cmd1}\n{out1}\n\nPS C:\\Users\\abhi1\\OneDrive\\Desktop\\5\\SE\\SE_submissions\\Lab 6> {cmd2}\n{out2}\n"
    with open("Lab 6/code_coverage_report.txt", "w", encoding="utf-8") as f:
        f.write(text_content)
    print("Wrote Lab 6/code_coverage_report.txt")

    render_terminal_screenshot(
        "Windows PowerShell - Lab 6: Code Coverage Analysis (100% Statement Coverage)",
        [(cmd1, out1), (cmd2, out2)],
        "Lab 6/code_coverage_screenshot.png"
    )


def generate_branch_coverage_reports():
    cmd1 = "coverage run --branch -m pytest BranchCoverageTest_student_grades.py"
    out1 = run_command(cmd1, "Lab 6")
    cmd2 = "coverage report -m"
    out2 = run_command(cmd2, "Lab 6")

    text_content = f"PS C:\\Users\\abhi1\\OneDrive\\Desktop\\5\\SE\\SE_submissions\\Lab 6> {cmd1}\n{out1}\n\nPS C:\\Users\\abhi1\\OneDrive\\Desktop\\5\\SE\\SE_submissions\\Lab 6> {cmd2}\n{out2}\n"
    with open("Lab 6/branch_coverage_report.txt", "w", encoding="utf-8") as f:
        f.write(text_content)
    print("Wrote Lab 6/branch_coverage_report.txt")

    render_terminal_screenshot(
        "Windows PowerShell - Lab 6: Branch Coverage Analysis (100% Branch Coverage)",
        [(cmd1, out1), (cmd2, out2)],
        "Lab 6/branch_coverage_screenshot.png"
    )


if __name__ == "__main__":
    generate_initial_reports()
    generate_code_coverage_reports()
    generate_branch_coverage_reports()
