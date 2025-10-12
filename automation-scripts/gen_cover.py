#!/usr/bin/env python3
"""
Generate per-student, per-lab cover pages in LaTeX (+PDF) for DAA writeups.

Inputs
- automation-scripts/output/commits.csv
- automation-scripts/output/students.csv

Outputs
- LaTeX + PDF under automation-scripts/output/daa-covers/{PRN}/
  Filenames: {PRN}-{slug-name}-lab-{00..10}-cover.tex/.pdf

Includes
- Lab title, lab manual URL
- Submission status, attached PR numbers, files changed, GitHub usernames, commit emails
- Commit summary table: short SHA, PR no, date-time, message, additions, deletions
- PR verification link(s)
- Signature & remarks area

CLI examples
  python3 automation-scripts/gen_cover.py                   # generate all students, labs 00..10
  python3 automation-scripts/gen_cover.py --only BT23F05F002 BT23F05F010
  python3 automation-scripts/gen_cover.py --labs 0 1 2 3 --compile
  python3 automation-scripts/gen_cover.py --out-dir automation-scripts/output/daa-covers --compile
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, List, Optional, Tuple

# Shared helpers
from lib.common import (
    ensure_dir,
    slugify,
    escape_latex,
    latex_manual_url,
    lab_titles_default,
    read_students,
    compile_tex,
    Student,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_COMMITS_CSV = os.path.join(ROOT, "output", "commits.csv")
DEFAULT_STUDENTS_CSV = os.path.join(ROOT, "output", "students.csv")
DEFAULT_OUT_DIR = os.path.join(ROOT, "output", "daa-covers")

# Repository info for PR links
GITHUB_OWNER = "s-m-quadri"
GITHUB_REPO = "geca-labs"


# -----------------------------
# Data models
# -----------------------------

@dataclass
class CommitRow:
    pr_number: Optional[int]
    prn: str
    pr_user: str
    sha: str
    author: str
    email: str
    message: str
    date_iso: str
    files_changed_count: int
    additions: int
    deletions: int
    affected_files_raw: str

    @property
    def affected_files_list(self) -> List[str]:
        txt = (self.affected_files_raw or "").strip()
        if not txt:
            return []
        return [p.strip() for p in txt.split(",") if p.strip()]

    @property
    def date(self) -> Optional[datetime]:
        try:
            return datetime.fromisoformat(self.date_iso.replace("Z", "+00:00"))
        except Exception:
            return None


# -----------------------------
# CSV helpers
# -----------------------------

def _to_int(s: str) -> Optional[int]:
    try:
        return int(str(s).strip())
    except Exception:
        return None


def _to_int_default(s: str, default: int = 0) -> int:
    v = _to_int(s)
    return v if v is not None else default


def read_commits(csv_path: str) -> List[CommitRow]:
    rows: List[CommitRow] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(
                CommitRow(
                    pr_number=_to_int(row.get("PR Number")),
                    prn=str(row.get("PRN", "")).strip(),
                    pr_user=str(row.get("PR User", "")).strip(),
                    sha=str(row.get("Commit SHA", "")).strip(),
                    author=str(row.get("Commit Author", "")).strip(),
                    email=str(row.get("Commit Email", "")).strip(),
                    message=str(row.get("Commit Message", "")).strip(),
                    date_iso=str(row.get("Commit Date", "")).strip(),
                    files_changed_count=_to_int_default(row.get("Files Changed"), 0),
                    additions=_to_int_default(row.get("Total Additions"), 0),
                    deletions=_to_int_default(row.get("Total Deletions"), 0),
                    affected_files_raw=str(row.get("Affected Files", "")).strip(),
                )
            )
    return rows


# -----------------------------
# Lab inference
# -----------------------------

_LAB_MSG_RE = re.compile(r"\b(?:lab|Lab)\s*[-:]?\s*0*([0-9]{1,2})\b")


def infer_lab_from_files(files: Iterable[str]) -> Optional[int]:
    files_list = list(files)
    if not files_list:
        return None

    # Lab 4/5/6 via task_4.x.py etc.
    for lab in (4, 5, 6):
        if any(re.search(fr"task_{lab}\.\d+\.py$", os.path.basename(p)) for p in files_list):
            return lab

    # Lab 3 indicators
    lab3_names = {
        "binary_search.py",
        "binary_search_demo_steps.py",
        "binary_search_demo_visual.py",
        "task_count_occurrences.py",
        "task_find_smallest_missing_positive.py",
        "task_guess_the_peak.py",
    }
    if any(os.path.basename(p) in lab3_names for p in files_list):
        return 3

    # Lab 2 indicators
    lab2_names = {
        "task_count_inversions.py",
        "task_merge_sorted_lists.py",
        "task_sort_student_scores.py",
        "merge_sort_basic.py",
    }
    if any(os.path.basename(p) in lab2_names for p in files_list):
        return 2

    # Lab 1 indicators
    lab1_names = {
        "task_print_array_backward.py",
        "task_reverse_digits.py",
        "task_sum_even_numbers.py",
        "factorial.py",
    }
    if any(os.path.basename(p) in lab1_names for p in files_list):
        return 1

    # Lab 0 indicators (a.py .. z.py, variants)
    base_names = {f"{ch}.py" for ch in list("abcdefghijklmnopqrstuvwxyz")}
    base_names.update(["z+.py", "z++.py", "z+++.py", "output.txt"])  # variants
    if any(os.path.basename(p) in base_names for p in files_list):
        return 0

    return None


def infer_lab(commit: CommitRow) -> Optional[int]:
    m = _LAB_MSG_RE.search(commit.message or "")
    if m:
        try:
            num = int(m.group(1))
            if 0 <= num <= 10:
                return num
        except Exception:
            pass
    lab_from_files = infer_lab_from_files(commit.affected_files_list)
    if lab_from_files is not None:
        return lab_from_files
    return None


# -----------------------------
# LaTeX rendering
# -----------------------------

COURSE_CODE = "CSPCC3004"
COURSE_NAME = "Lab Design and Analysis of Algorithms"
HOMEPAGE_URL = "https://s-m-quadri.me/geca/daa"


def latex_preamble(student: Student, lab: int, title: str) -> str:
    b = "\\"
    head: List[str] = []
    head.append("\\documentclass[11pt]{article}")
    head.append("\\usepackage[a4paper,margin=1in]{geometry}")
    head.append("\\usepackage[hidelinks]{hyperref}")
    head.append("\\usepackage{array}")
    head.append("\\usepackage{booktabs}")
    head.append("\\usepackage{parskip}")
    head.append("\\usepackage{fancyhdr}")
    head.append("\\usepackage[most]{tcolorbox}")
    head.append("\\usepackage{qrcode}")
    head.append("% Slightly tighter line spacing to help fit one page")
    head.append("\\linespread{0.98}")
    head.append("% No paragraph indent")
    head.append("\\setlength{\\parindent}{0pt}")
    head.append("% Chip style for files list")
    head.append("\\newtcbox{\\chip}{on line, arc=3pt, colback=gray!15,colframe=gray!50, boxrule=0.2pt, left=3pt,right=3pt,top=1pt,bottom=1pt}")
    head.append("\\pagestyle{fancy}")
    head.append("\\fancyhf{}")
    head.append(f"{b}fancyhead[L]{{Lab {lab:02d}}}")
    head.append(f"{b}fancyhead[R]{{PRN: {escape_latex(student.prn)}}}")
    head.append(f"{b}fancyfoot[L]{{{b}url{{{HOMEPAGE_URL}}}}}")
    head.append(f"{b}fancyfoot[C]{{{b}thepage}}")
    head.append("\\begin{document}")
    # Custom title block
    head.append("\\begin{center}")
    head.append("\\vspace{0.4em}")
    head.append(f"{{\\large \\textbf{{Lab {lab:02d}}}}}\\\\")
    head.append("\\vspace{0.4em}")
    head.append(f"{{\\LARGE {escape_latex(title)}}}")
    head.append("\\end{center}")
    head.append("\\vspace{0.6em}")
    return "\n".join(head) + "\n"


def latex_course_block(lab: int) -> str:
    lines: List[str] = []
    lines.append(f"Course code: \\textbf{{{COURSE_CODE}}}\\\\")
    lines.append(f"Course name: \\textbf{{{escape_latex(COURSE_NAME)}}}\\\\")
    lines.append(f"Lab manual: \\textbf{{\\url{{{latex_manual_url(lab)}}}}}")
    lines.append("\\vspace{0.6em}")
    return "\n".join(lines) + "\n"


def latex_student_block(student: Student, status: str, pr_users: Iterable[str], emails: Iterable[str]) -> str:
    pr_users_s = sorted({u for u in pr_users if u})
    emails_s = sorted({e for e in emails if e})
    lines: List[str] = []
    lines.append(f"Student name: \\textbf{{{escape_latex(student.name)}}}\\\\")
    lines.append(f"Student PRN: \\textbf{{{escape_latex(student.prn)}}}\\\\")
    lines.append(f"Submission status: \\textbf{{{escape_latex(status)}}}\\\\")
    if pr_users_s:
        lines.append(f"GitHub username(s): \\textbf{{{escape_latex(', '.join(pr_users_s))}}}\\\\")
    if emails_s:
        lines.append(f"Commit email(s): \\textbf{{{escape_latex(', '.join(emails_s))}}}\\\\")
    lines.append("\\vspace{0.6em}")
    return "\n".join(lines) + "\n"


def latex_submission_block(pr_users: Iterable[str], emails: Iterable[str], pr_numbers: Iterable[int], files_changed: Iterable[str]) -> str:
    pr_users_s = sorted({u for u in pr_users if u})
    emails_s = sorted({e for e in emails if e})
    prs = sorted({int(p) for p in pr_numbers if p is not None})
    files = sorted({os.path.basename(f) for f in files_changed if f})
    lines: List[str] = []
    if prs:
        lines.append(f"Pull request number(s): \\textbf{{{', '.join(str(p) for p in prs)}}}\\\\")
    if files:
        # Chips as comma-separated rounded boxes; smaller font to save space
        chips = [f"\\chip{{{escape_latex(f)}}}" for f in files]
        lines.append("Files changed (unique): {\\small " + " \\, ".join(chips) + "}")
    lines.append("\\vspace{0.4em}")
    return "\n".join(lines) + "\n"


def latex_commit_table(commits: List[CommitRow]) -> str:
    if not commits:
        return "\\textit{No commits found for this lab.}\n\n"
    commits_sorted = sorted(commits, key=lambda c: (c.date or datetime.min))
    lines: List[str] = []
    br = "\\\\"
    lines.append("\\begin{table}[!ht]")
    lines.append("\\centering")
    lines.append("\\caption{Commit details}")
    lines.append("{\\small")
    lines.append("\\begin{tabular}{@{}l c l p{9cm} r r@{}}")
    lines.append("\\toprule")
    lines.append(f"SHA & PR & Date (IST) & Message & + & - {br}")
    lines.append("\\midrule")
    for c in commits_sorted:
        short = c.sha[:7] if c.sha else ""
        pr_s = str(c.pr_number) if c.pr_number is not None else ""
        # Prefer parsed datetime; fallback to raw ISO
        if c.date:
            try:
                from datetime import timezone, timedelta
                ist = timezone(timedelta(hours=5, minutes=30))
                dt_ist = c.date.astimezone(ist)
                date_s = dt_ist.strftime("%d/%m/%y %I:%M %p")
            except Exception:
                date_s = c.date_iso or ""
        else:
            date_s = c.date_iso or ""
        msg = c.message or ""
        lines.append(
            f"{escape_latex(short)} & {escape_latex(pr_s)} & {escape_latex(date_s)} & {escape_latex(msg)} & {c.additions} & {c.deletions} {br}"
        )
    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    lines.append("}")
    lines.append("\\end{table}")
    return "\n".join(lines) + "\n"


def latex_verification_block(pr_numbers: Iterable[int]) -> str:
    prs = sorted({int(p) for p in pr_numbers if p is not None})
    lines: List[str] = []
    lines.append("\\textbf{Verification link(s)}:")
    if prs:
        lines.append("\\begin{itemize}")
        for p in prs:
            url = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/pull/{p}"
            lines.append(f"  \\item \\url{{{url}}}")
        lines.append("\\end{itemize}")
    else:
        lines.append("\\textit{—}")
    lines.append("\\vspace{0.6em}")
    return "\n".join(lines) + "\n"


def latex_signature_block(pr_numbers: Iterable[int]) -> str:
    prs = sorted({int(p) for p in pr_numbers if p is not None})
    first_url = None
    if prs:
        first_url = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/pull/{prs[0]}"
    lines: List[str] = []
    lines.append("\\vspace{0.4em}")
    # Two stacked boxes for S/D | S/D
    lines.append("\\noindent")
    lines.append("\\begin{tabular}{@{}p{0.49\\textwidth} p{0.49\\textwidth}@{}}")
    lines.append("\\begin{tcolorbox}[colback=white,colframe=black!30,boxrule=0.3pt,height=2.4cm]")
    lines.append("\\textbf{Student Signature}\\\\[0.8cm]")
    lines.append("\\textbf{Date:} \\rule{3cm}{0.4pt}")
    lines.append("\\end{tcolorbox}")
    lines.append("&")
    lines.append("\\begin{tcolorbox}[colback=white,colframe=black!30,boxrule=0.3pt,height=2.4cm]")
    lines.append("\\textbf{Instructor Signature}\\\\[0.8cm]")
    lines.append("\\textbf{Date:} \\rule{3cm}{0.4pt}")
    lines.append("\\end{tcolorbox}\\\\")
    lines.append("\\end{tabular}")
    lines.append("\\vspace{0.4em}")
    # QR + Remarks grid
    lines.append("\\noindent")
    lines.append("\\begin{tabular}{@{}p{0.18\\textwidth} p{0.80\\textwidth}@{}}")
    if first_url:
        lines.append("\\centering \\qrcode[hyperlink,height=2.2cm]{" + first_url + "} &")
    else:
        lines.append(" \\vspace{0pt} &")
    lines.append("\\begin{tcolorbox}[title=Remarks,colback=white,colframe=black!30,boxrule=0.3pt,height=3.0cm]")
    lines.append("\\end{tcolorbox}\\\\")
    lines.append("\\end{tabular}")
    lines.append("\\end{document}")
    return "\n".join(lines) + "\n"


# -----------------------------
# Aggregation
# -----------------------------

def aggregate_for_student_lab(student: Student, lab: int, all_commits: List[CommitRow]) -> Tuple[List[CommitRow], List[int], List[str], List[str], List[str]]:
    commits: List[CommitRow] = []
    for c in all_commits:
        if (c.prn or "").strip().upper() != student.prn.strip().upper():
            continue
        lab_inferred = infer_lab(c)
        if lab_inferred is None or lab_inferred != lab:
            continue
        commits.append(c)

    pr_numbers = sorted({c.pr_number for c in commits if c.pr_number is not None})
    pr_users = sorted({c.pr_user for c in commits if c.pr_user})
    emails = sorted({c.email for c in commits if c.email})
    files: List[str] = []
    for c in commits:
        files.extend(c.affected_files_list)
    return commits, [int(p) for p in pr_numbers], pr_users, emails, files


# -----------------------------
# Main generation logic
# -----------------------------

def generate_covers(students_csv: str, commits_csv: str, out_dir: str, only_prns: Optional[List[str]], labs: Optional[List[int]], compile_pdf: bool) -> int:
    students = read_students(students_csv)
    if only_prns:
        only = {s.upper() for s in only_prns}
        students = [s for s in students if s.prn.upper() in only]

    commits = read_commits(commits_csv)

    lab_titles = lab_titles_default()
    lab_list = [i for i in range(0, 11)] if not labs else [l for l in labs if 0 <= l <= 10]

    ensure_dir(out_dir)
    total_files = 0
    for stu in students:
        stu_dir = os.path.join(out_dir, stu.prn)
        ensure_dir(stu_dir)
        for lab in lab_list:
            title = lab_titles.get(lab, f"Lab {lab:02d}")
            commits_lab, pr_numbers, pr_users, emails, files = aggregate_for_student_lab(stu, lab, commits)

            parts: List[str] = []
            parts.append(latex_preamble(stu, lab, title))
            # Sections in requested order
            parts.append(latex_course_block(lab))
            parts.append(latex_student_block(stu, "Submitted" if pr_numbers else "Not submitted", pr_users, emails))
            parts.append(latex_submission_block(pr_users, emails, pr_numbers, files))
            parts.append(latex_commit_table(commits_lab))
            parts.append(latex_verification_block(pr_numbers))
            parts.append(latex_signature_block(pr_numbers))

            base = f"{stu.prn}-{slugify(stu.name)}-lab-{lab:02d}-cover"
            tex_path = os.path.join(stu_dir, base + ".tex")
            with open(tex_path, "w", encoding="utf-8") as f:
                f.write("\n".join(parts))
            if compile_pdf:
                try:
                    compile_tex(tex_path, stu_dir)
                except Exception:
                    print(f"LaTeX compile failed for {tex_path}")
            total_files += 1

    print(f"Generated {total_files} cover file(s) in {out_dir}")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Generate DAA lab cover pages (LaTeX/PDF) per student per lab")
    p.add_argument("--students", default=DEFAULT_STUDENTS_CSV, help="Path to students.csv")
    p.add_argument("--commits", default=DEFAULT_COMMITS_CSV, help="Path to commits.csv")
    p.add_argument("--out-dir", default=DEFAULT_OUT_DIR, help="Output folder for covers")
    p.add_argument("--only", nargs="*", help="Only process these PRNs")
    p.add_argument("--labs", nargs="*", type=int, help="Only process these lab numbers (0..10)")
    p.add_argument("--compile", action="store_true", help="Compile LaTeX to PDF")
    args = p.parse_args(argv)

    for need in (args.students, args.commits):
        if not os.path.exists(need):
            print(f"Missing input: {need}", file=sys.stderr)
            return 2

    return generate_covers(args.students, args.commits, args.out_dir, args.only, args.labs, args.compile)


if __name__ == "__main__":
    raise SystemExit(main())
