#!/usr/bin/env python3
"""
Generate per-student, per-lab cover pages (LaTeX/PDF).

Inputs (defaults from ``courses/<course>.json``):
- ``output/<course>/commits.csv``, ``output/students.csv`` (or per-course path)

Outputs
- ``output/<course>/covers/{PRN}_{slug}_covers.tex`` (+ optional PDF)
- PDFs use an extra blank page when needed so the total page count is even (duplex printing).

CLI examples
  python3 automation-scripts/gen_cover.py --course daa --compile
  python3 automation-scripts/gen_cover.py --course dbms --only BT24F05F001 --labs 0 1
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import Iterable, List, Optional, Tuple

# Shared helpers
from lib.common import (
    ensure_dir,
    slugify,
    escape_latex,
    lab_titles_default,
    lab_titles_dbms,
    read_students,
    compile_tex,
    Student,
)
from lib.latex_duplex import latex_duplex_even_page_suffix
from lib.lab_course import LabCourse, repo_root_from_scripts

ROOT = os.path.dirname(os.path.abspath(__file__))

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


# -----------------------------
# Small helpers
# -----------------------------

def _ellipsize(text: str, max_len: int) -> str:
    if text is None:
        return ""
    s = str(text)
    return s if len(s) <= max_len else s[: max_len - 1] + "…"


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


def read_pull_requests(csv_path: str) -> List[dict]:
    rows: List[dict] = []
    if not os.path.exists(csv_path):
        return rows
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({k: (v or "").strip() for k, v in r.items()})
    return rows


def load_analysis(course: "LabCourse") -> dict:
    """Load analysis/pr_analysis.json if available. Returns {prn: {lab_str: [flags]}}"""
    path = course.path_in_output("analysis/pr_analysis.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_from_pr_details(pr_details_path: str, course: "LabCourse") -> Tuple[List["CommitRow"], dict]:
    """Load CommitRows and pr_lab_map from pr_details.json."""
    with open(pr_details_path, encoding="utf-8") as f:
        data = json.load(f)
    prs = list(data.values()) if isinstance(data, dict) else data

    rows: List[CommitRow] = []
    pr_lab_map: dict = {}

    for pr in prs:
        pr_num = pr["number"]
        prn = pr.get("prn", "") or ""
        user = pr.get("user", "") or ""
        head_ref = pr.get("head_ref", "") or ""

        m = re.search(rf"lab[-_]{re.escape(course.id)}[-_](\d+)", head_ref, re.I)
        if m:
            pr_lab_map[pr_num] = int(m.group(1))

        for commit in pr.get("commits", []):
            stats = commit.get("stats") or {}
            files = commit.get("files") or []
            affected = ",".join(f.get("filename", "") for f in files if f.get("filename"))
            rows.append(CommitRow(
                pr_number=pr_num,
                prn=prn,
                pr_user=user,
                sha=commit.get("sha", ""),
                author=commit.get("author_name", ""),
                email=commit.get("author_email", ""),
                message=commit.get("message", ""),
                date_iso=commit.get("author_date", ""),
                files_changed_count=len(files),
                additions=stats.get("additions", 0),
                deletions=stats.get("deletions", 0),
                affected_files_raw=affected,
            ))

    return rows, pr_lab_map


# -----------------------------
# Lab inference
# -----------------------------

_LAB_MSG_RE = re.compile(r"\b(?:lab|Lab)\s*[-:]?\s*0*([0-9]{1,2})\b")


def infer_lab_from_files_daa(files: Iterable[str]) -> Optional[int]:
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


def infer_lab_daa(commit: CommitRow) -> Optional[int]:
    # Prefer explicit lab mention in commit message
    m = _LAB_MSG_RE.search(commit.message or "")
    if m:
        try:
            num = int(m.group(1))
            if 0 <= num <= 10:
                return num
        except Exception:
            pass
    lab_from_files = infer_lab_from_files_daa(commit.affected_files_list)
    if lab_from_files is not None:
        return lab_from_files
    return None


def infer_lab_dbms(commit: CommitRow) -> Optional[int]:
    msg = commit.message or ""
    m_branch = re.search(r"lab-dbms-(\d+)(?:-v\d+)?", msg, re.I)
    if m_branch:
        try:
            num = int(m_branch.group(1))
            if 0 <= num <= 30:
                return num
        except ValueError:
            pass
    m = _LAB_MSG_RE.search(msg)
    if m:
        try:
            num = int(m.group(1))
            if 0 <= num <= 30:
                return num
        except Exception:
            pass
    for p in commit.affected_files_list:
        path = p.replace("\\", "/")
        mm = re.search(r"lab-dbms-(\d+)(?:-v\d+)?", path, re.I)
        if mm:
            try:
                num = int(mm.group(1))
                if 0 <= num <= 30:
                    return num
            except ValueError:
                continue
        mm = re.search(r"lab[-_/ ](\d+)", path, re.I)
        if mm:
            try:
                num = int(mm.group(1))
                if 0 <= num <= 30:
                    return num
            except ValueError:
                continue
    return None


def infer_lab(commit: CommitRow, course: LabCourse) -> Optional[int]:
    if course.id == "dbms":
        return infer_lab_dbms(commit)
    return infer_lab_daa(commit)


def infer_lab_from_pr_row(pr_row: dict) -> Optional[int]:
    """Infer lab number from a pull request row (title/labels).

    This prefers explicit labels like 'Lab 03' or titles containing 'Lab 03'.
    """
    if not pr_row:
        return None
    # Try labels first (often contains 'Lab 03')
    labels = pr_row.get("Labels", "")
    m = _LAB_MSG_RE.search(labels)
    if m:
        try:
            num = int(m.group(1))
            if 0 <= num <= 10:
                return num
        except Exception:
            pass
    # Next try Title
    title = pr_row.get("Title", "")
    m = _LAB_MSG_RE.search(title)
    if m:
        try:
            num = int(m.group(1))
            if 0 <= num <= 10:
                return num
        except Exception:
            pass
    for blob in (labels, title):
        m2 = re.search(r"lab-dbms-(\d+)(?:-v\d+)?", blob or "", re.I)
        if m2:
            try:
                num = int(m2.group(1))
                if 0 <= num <= 30:
                    return num
            except ValueError:
                pass
    return None


# -----------------------------
# LaTeX rendering
# -----------------------------


def latex_global_preamble(student: Student, course: LabCourse) -> str:
    b = "\\"
    head: List[str] = []
    head.append("\\documentclass[11pt]{article}")
    head.append("\\usepackage[a4paper,margin=1in]{geometry}")
    head.append("\\usepackage[hidelinks]{hyperref}")
    head.append("\\usepackage{array}")
    head.append("\\usepackage{booktabs}")
    head.append("\\usepackage{tabularx}")
    head.append("\\usepackage{parskip}")
    head.append("\\usepackage{fancyhdr}")
    head.append("\\usepackage[most]{tcolorbox}")
    head.append("\\usepackage{tikz}")
    head.append("\\usepackage{amssymb}")
    head.append("\\usepackage{qrcode}")
    head.append("\\usepackage{xcolor}")
    head.append("\\usepackage{listings}")
    head.append("\\usepackage{listingsutf8}")
    head.append("\\usepackage{enumitem}")
    head.append("\\usepackage{truncate}")
    head.append("% Slightly tighter line spacing to help fit one page")
    head.append("\\linespread{0.98}")
    head.append("% No paragraph indent")
    head.append("\\setlength{\\parindent}{0pt}")
    head.append("% Chip style for files list")
    head.append("\\newtcbox{\\chip}{on line, arc=3pt, colback=gray!15,colframe=gray!50, boxrule=0.2pt, left=3pt,right=3pt,top=1pt,bottom=1pt}")
    # Listings style for Python
    head.append("\\definecolor{pykeyword}{RGB}{33,80,162}")
    head.append("\\definecolor{pycomment}{RGB}{0,128,0}")
    head.append("\\definecolor{pystring}{RGB}{163,21,21}")
    head.append("\\lstdefinestyle{pycode}{%")
    head.append("  language=Python,")
    head.append("  basicstyle=\\ttfamily\\small,")
    head.append("  numbers=left,")
    head.append("  numberstyle=\\tiny, numbersep=6pt,")
    head.append("  showstringspaces=false,")
    head.append("  breaklines=true, breakatwhitespace=true,")
    head.append("  tabsize=4,")
    head.append("  keywordstyle=\\color{pykeyword}\\bfseries,")
    head.append("  commentstyle=\\color{pycomment}\\itshape,")
    head.append("  stringstyle=\\color{pystring},")
    head.append("  frame=single, framerule=0.2pt, rulecolor=\\color{black!20}")
    head.append("}")
    head.append("\\lstset{style=pycode,inputencoding=utf8}")
    head.append("\\lstdefinestyle{sqlcode}{%")
    head.append("  language=SQL,")
    head.append("  basicstyle=\\ttfamily\\small,")
    head.append("  numbers=left,")
    head.append("  numberstyle=\\tiny, numbersep=6pt,")
    head.append("  showstringspaces=false,")
    head.append("  breaklines=true, breakatwhitespace=true,")
    head.append("  tabsize=4,")
    head.append("  keywordstyle=\\color{pykeyword}\\bfseries,")
    head.append("  commentstyle=\\color{pycomment}\\itshape,")
    head.append("  stringstyle=\\color{pystring},")
    head.append("  frame=single, framerule=0.2pt, rulecolor=\\color{black!20}")
    head.append("}")
    # Duplex-friendly: jump to next odd (front) page, with blank marker
    head.append("\\newcommand{\\cleartooddpage}{%")
    head.append("  \\clearpage")
    head.append("  \\ifodd\\value{page}\\else")
    head.append("    \\thispagestyle{empty}")
    head.append("    \\vspace*{\\fill}")
    head.append("    {\\centering\\small\\textcolor{black!35}{\\textit{This page is intentionally left blank for two-sided printing.}}\\par}")
    head.append("    \\vspace*{\\fill}")
    head.append("    \\clearpage")
    head.append("  \\fi")
    head.append("}")
    # Fancy header/footer (no page number in center)
    head.append("\\pagestyle{fancy}")
    head.append("\\fancyhf{}")
    head.append("\\setlength{\\headheight}{14pt}")
    head.append(f"{b}fancyhead[R]{{PRN: {escape_latex(student.prn)}}}")
    head.append(f"{b}fancyfoot[L]{{{b}url{{{course.homepage_url}}}}}")
    head.append("\\begin{document}")
    return "\n".join(head) + "\n"


def latex_title_block(lab: int, title: str) -> str:
    lines: List[str] = []
    lines.append("\\begin{center}")
    lines.append("\\vspace{0.4em}")
    lines.append(f"{{\\large \\textbf{{Lab {lab:02d}}}}}\\\\")
    lines.append("\\vspace{0.4em}")
    lines.append(f"{{\\LARGE {escape_latex(title)}}}")
    lines.append("\\end{center}")
    lines.append("\\vspace{0.6em}")
    return "\n".join(lines) + "\n"


def latex_course_block(lab: int, course: LabCourse) -> str:
    lines: List[str] = []
    lines.append(f"Course code: \\textbf{{{course.course_code}}}\\\\")
    lines.append(f"Course name: \\textbf{{{escape_latex(course.course_name_short)}}}\\\\")
    lines.append(f"Lab manual: \\textbf{{\\url{{{course.manual_url(lab)}}}}}")
    lines.append("\\vspace{0.6em}")
    return "\n".join(lines) + "\n"


def latex_set_header_lab(lab: int) -> str:
    """Set header-left with current lab label (persists across pages until changed)."""
    return f"\\fancyhead[L]{{Lab {lab:02d}}}\n"


def latex_student_block(student: Student, status: str, pr_users: Iterable[str], emails: Iterable[str]) -> str:
    pr_users_s = sorted({u for u in pr_users if u})
    emails_s = sorted({e for e in emails if e})
    lines: List[str] = []
    lines.append(f"Student name: \\textbf{{{escape_latex(student.name)}}}\\\\")
    lines.append(f"Student PRN: \\textbf{{{escape_latex(student.prn)}}}\\\\")
    lines.append(f"Submission status: \\textbf{{{escape_latex(status)}}}\\\\")
    if pr_users_s:
        lines.append(f"GitHub username(s): \\textbf{{{escape_latex(', '.join(pr_users_s))}}}")
        if emails_s:
            lines.append("\\\\")
    if emails_s:
        emails_joined = ", ".join(emails_s)
        # Prevent overflow by breaking into separate lines when long or too many emails
        if len(emails_joined) > 55 or len(emails_s) > 2:
            lines.append("Commit email(s):")
            for e in emails_s:
                lines.append(f"\\\\ \\textbullet\\, \\textbf{{{escape_latex(e)}}}")
        else:
            lines.append(f"Commit email(s): \\textbf{{{escape_latex(emails_joined)}}}")
    lines.append("\\vspace{0.6em}")
    return "\n".join(lines) + "\n"


def latex_submission_block(pr_users: Iterable[str], emails: Iterable[str], pr_numbers: Iterable[int], files_changed: Iterable[str]) -> str:
    """Cover-page summary: PR links + brief unique file count."""
    prs = sorted({int(p) for p in pr_numbers if p is not None})
    files = sorted({os.path.basename(f) for f in files_changed if f})
    lines: List[str] = []
    if prs:
        nums = ", ".join(f"\\#{p}" for p in prs)
        lines.append(f"Pull request(s): \\textbf{{{nums}}}\\\\")
    file_count = len(files)
    if file_count:
        lines.append(f"Files changed (unique): \\textbf{{{file_count}}}")
    lines.append("\\vspace{0.4em}")
    return "\n".join(lines) + "\n"


def latex_files_chips_block(files_changed: Iterable[str]) -> str:
    """Page-2 full file list as chips."""
    files = sorted({os.path.basename(f) for f in files_changed if f})
    if not files:
        return ""
    chips = [f"\\chip{{{escape_latex(f)}}}" for f in files]
    lines = [
        "\\textbf{Files changed (unique)}\\\\[4pt]",
        "{\\small\\setlength{\\baselineskip}{1.6em}\\raggedright\\noindent " + " \\allowbreak ".join(chips) + "\\par}",
        "\\vspace{0.6em}",
    ]
    return "\n".join(lines) + "\n"


def _commit_table_rows(commits_sorted: List[CommitRow]) -> List[str]:
    from datetime import timezone, timedelta
    IST = timezone(timedelta(hours=5, minutes=30))
    br = "\\\\"
    rows = []
    for c in commits_sorted:
        short = c.sha[:7] if c.sha else ""
        pr_s = str(c.pr_number) if c.pr_number is not None else ""
        if c.date:
            try:
                dt_ist = c.date.astimezone(IST)
                date_s = dt_ist.strftime("%d/%m/%y %I:%M %p")
            except Exception:
                date_s = c.date_iso or ""
        else:
            date_s = c.date_iso or ""
        msg = _ellipsize(c.message or "", 90)
        rows.append(f"{escape_latex(short)} & {escape_latex(pr_s)} & {escape_latex(date_s)} & {escape_latex(msg)} & {c.additions} & {c.deletions} {br}")
    return rows


def _commit_table_wrap(row_lines: List[str]) -> str:
    br = "\\\\"
    lines = [
        "\\begin{table}[!ht]", "\\centering", "{\\small",
        "\\begin{tabularx}{\\linewidth}{@{} l c p{3.2cm} X r r @{}}",
        "\\toprule",
        f"SHA & PR & Date (IST) & Message & + & - {br}",
        "\\midrule",
    ]
    lines.extend(row_lines)
    lines += ["\\bottomrule", "\\end{tabularx}", "}", "\\end{table}"]
    return "\n".join(lines) + "\n"


def latex_commit_table(commits: List[CommitRow], lab: Optional[int] = None, max_shown: int = 5) -> str:
    if not commits:
        lines: List[str] = []
        lines.append("\\begin{tcolorbox}[colback=yellow!8,colframe=yellow!50!black,boxrule=0.3pt,title={No submission on Github repository found!}]")
        lines.append("\\textbf{For Student:} Attach your complete source code for this lab along with this write-up. If you improved the code after the printing, add a short note about it.")
        lines.append("\\\\\\\\\n\\textbf{For Student:} If you've already submitted via GitHub, or completed locally, but couldn't push to GitHub, or faced technical issues, or don't see here, please add a short note explaining the situation.")
        lines.append("\\\\\\\\\n\\textbf{For Instructor:} The student has not submitted code on GitHub for this lab. Please review the attached source code in the write-up. Verification links and commit details are omitted here.")
        if lab is not None and lab >= 7:
            lines.append("\\\\\\\\\n\\textbf{Note on Lab 07+:} \\textit{These labs were conducted in short time frames; many students may not have GitHub submissions. Attaching source code in the write-up is acceptable.}")
        lines.append("\\end{tcolorbox}")
        lines.append("\\vspace{0.4em}")
        return "\n".join(lines) + "\n"

    commits_sorted = sorted(commits, key=lambda c: (c.date or datetime.min))
    shown = commits_sorted[:max_shown]
    rest = len(commits_sorted) - len(shown)
    lines: List[str] = []
    lines.append("\\textbf{Commit details}")
    lines.append(_commit_table_wrap(_commit_table_rows(shown)))
    if rest > 0:
        lines.append(f"\\vspace{{0.2em}}{{\\small \\textit{{Showing {len(shown)} of {len(commits_sorted)} commits --- see next page for full history.}}}}")
        lines.append("\\vspace{0.4em}")
    return "\n".join(lines) + "\n"


def latex_commit_table_full(commits: List[CommitRow]) -> str:
    """All commits for the sources page when cover was truncated."""
    if not commits:
        return ""
    commits_sorted = sorted(commits, key=lambda c: (c.date or datetime.min))
    lines = ["\\textbf{Full commit history}", _commit_table_wrap(_commit_table_rows(commits_sorted))]
    return "\n".join(lines) + "\n"


def _format_flag(f) -> str:
    if isinstance(f, str):
        return f
    t = f.get("type", "")
    if t == "late_night":
        from datetime import datetime as _dt
        ist = _dt.fromisoformat(f["datetime_ist"])
        return f"Late night commit: PR #{f['pr_number']} at {ist.strftime('%I:%M %p')} IST on {ist.strftime('%d %b %Y')}"
    if t == "fast_completion":
        s = f["span_seconds"]
        return f"Fast completion: {f['commits']} commits in {int(s//60)}m {int(s%60)}s (PR #{f['pr_number']})"
    if t == "high_commit_count":
        return f"High commit count: {f['commits']} commits (PR #{f['pr_number']})"
    if t == "empty_merged_pr":
        return f"Merged with 0 changed files (PR #{f['pr_number']})"
    if t == "attempt_history":
        parts = []
        for a in f["attempts"]:
            status = "accepted" if a["accepted"] else a["outcome"]
            lbl = f" [{', '.join(a['issue_labels'])}]" if a.get("issue_labels") else ""
            parts.append(f"PR #{a['pr_number']} → {status}{lbl}")
        return f"Multiple attempts: {'; '.join(parts)}"
    if t == "rejected_pr":
        reason = (", ".join(f["issue_labels"])) if f.get("issue_labels") else "closed without merge"
        return f"PR #{f['pr_number']} rejected: {reason}"
    if t == "review_changes_requested":
        reason = (", ".join(f["issue_labels"])) if f.get("issue_labels") else ""
        return f"Changes requested on PR #{f['pr_number']}" + (f": {reason}" if reason else "")
    if t == "label_issue":
        return f"PR #{f['pr_number']} flagged: {', '.join(f['labels'])}"
    if t == "conversation":
        parts = []
        if f["student_comments"]:
            parts.append(f"{f['student_comments']} by student")
        if f["instructor_comments"]:
            parts.append(f"{f['instructor_comments']} by instructor")
        return f"PR #{f['pr_number']} had comments: {', '.join(parts)}"
    if t == "generic_commits":
        samples = "; ".join(f"'{s}'" for s in f.get("samples", []))
        return f"Generic commit messages on PR #{f['pr_number']} ({f['generic_count']}/{f['total_commits']}): {samples}"
    if t == "no_sql_submitted":
        return f"No .sql files in PR #{f['pr_number']} ({f['changed_files']} other files changed)"
    if t == "bulk_same_day":
        return f"Multiple labs on {f['date']}: {', '.join(str(l) for l in f['labs'])} (#{', #'.join(str(n) for n in f['pr_numbers'])})"
    if t == "rapid_succession":
        return f"Labs {f['lab_a']} and {f['lab_b']} submitted {f['gap_minutes']}min apart (#{f['pr_a']} \u2192 #{f['pr_b']})"
    if t == "solution_file_submitted":
        files = ", ".join(os.path.basename(fn) for fn in f.get("files", []))
        return f"Solution file committed in PR #{f['pr_number']}: {files}"
    if t == "unique_submission":
        score = f["uniqueness_score"] * 100
        return f"Top {f['top_percentile']}% unique submission (uniqueness: {score:.0f}%)"
    if t == "commit_quality":
        score = f["quality_score"] * 100
        return f"Top {f['top_percentile']}% commit quality ({score:.0f}% meaningful messages)"
    if t == "clean_submission":
        return f"Clean submission: no temp/leftover files (PR #{f['pr_number']}, {f['files']} files)"
    if t == "first_attempt_clean":
        return f"Accepted on first attempt (PR #{f['pr_number']})"
    if t == "iterative_development":
        return f"Iterative work across {f['commit_days']} days ({f['total_commits']} commits, PR #{f['pr_number']})"
    if t == "plagiarism":
        return f"Similarity with {f['matched_prn']}: {f['similarity']*100:.0f}%"
    return str(f)


def _flag_category(f) -> str:
    t = f.get("type", "") if isinstance(f, dict) else ""
    return "positive" if t in {
        "unique_submission", "commit_quality", "clean_submission",
        "first_attempt_clean", "iterative_development",
    } else "negative"


def _name_for(prn: str, prn_to_name: dict) -> str:
    n = prn_to_name.get(prn.upper(), "")
    return n.title() if n else prn


def _ist_display(iso: str) -> str:
    from datetime import datetime as _dt
    try:
        d = _dt.fromisoformat(iso)
        return d.strftime("%-I:%M %p, %-d %B %Y")
    except Exception:
        return iso


def _ist_display_short(iso: str) -> str:
    from datetime import datetime as _dt
    try:
        d = _dt.fromisoformat(iso)
        return d.strftime("%d/%m/%y %I:%M %p")
    except Exception:
        return iso


def _pr_link(pr_number: int) -> str:
    url = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/pull/{pr_number}"
    return f"\\href{{{url}}}{{[PR \\#{pr_number}]}}"


def _build_narrative(flags: List, prn_to_name: dict) -> List:
    """Returns list of (cat, latex_text) tuples. cat in {'pos', 'neg', 'info'}."""
    items: List = []
    seen_types: set = set()

    def typed(t: str) -> List:
        return [f for f in flags if isinstance(f, dict) and f.get("type") == t]

    for f in typed("attempt_history"):
        attempts = f.get("attempts", [])
        parts = []
        for a in attempts:
            lbls = a.get("issue_labels", [])
            status = "accepted" if a.get("accepted") else a.get("outcome", "closed")
            lbl_str = f", {', '.join(lbls)}" if lbls else ""
            parts.append(f"{_pr_link(a['pr_number'])} {escape_latex(status)}{escape_latex(lbl_str)}")
        if parts:
            items.append(("info", "Submission history: " + "; ".join(parts) + "."))
        seen_types.add("attempt_history")

    if "attempt_history" not in seen_types:
        for f in typed("rejected_pr"):
            reason = escape_latex(", ".join(f.get("issue_labels", ["closed without merge"])))
            items.append(("neg", f"{_pr_link(f['pr_number'])} was not accepted ({reason}). Review and address the raised concerns."))

    for f in typed("review_changes_requested"):
        labels = f.get("issue_labels", [])
        extra = f": {escape_latex(', '.join(labels))}" if labels else ""
        items.append(("neg", f"Changes were requested before {_pr_link(f['pr_number'])} could be accepted{extra}. Indicates submission was not ready."))

    for f in typed("label_issue"):
        lbls = escape_latex(", ".join(f.get("labels", [])))
        items.append(("neg", f"{_pr_link(f['pr_number'])} carries issue label(s) \\textbf{{{lbls}}}. These must be resolved."))

    plag_flags = typed("plagiarism")
    if plag_flags:
        exact = [f for f in plag_flags if f["similarity"] >= 0.99]
        high  = [f for f in plag_flags if 0.90 <= f["similarity"] < 0.99]
        mod   = [f for f in plag_flags if f["similarity"] < 0.90]
        parts = []
        if exact:
            names = ", ".join(f"\\textit{{{escape_latex(_name_for(f['matched_prn'], prn_to_name))}}}" for f in exact[:4])
            more = f" and {len(exact)-4} others" if len(exact) > 4 else ""
            parts.append(f"\\textbf{{Exact match}} with submission of {names}{more}")
        if high:
            names = ", ".join(f"\\textit{{{escape_latex(_name_for(f['matched_prn'], prn_to_name))}}}" for f in high[:3])
            parts.append(f"\\textbf{{Significant match}} with work of {names}")
        if mod:
            names = ", ".join(f"\\textit{{{escape_latex(_name_for(f['matched_prn'], prn_to_name))}}}" for f in mod[:2])
            parts.append(f"\\textbf{{Moderate match}} with submission of {names}")
        if parts:
            items.append(("neg", ". ".join(parts) + ". See plagiarism table on next page."))

    for f in typed("conversation"):
        sc, ic = f.get("student_comments", 0), f.get("instructor_comments", 0)
        if ic and sc:
            items.append(("info", f"Discussion on {_pr_link(f['pr_number'])}: {sc} student and {ic} instructor comment(s)."))
        elif ic:
            items.append(("info", f"Instructor left {ic} comment(s) on {_pr_link(f['pr_number'])}. Check if addressed."))
        elif sc:
            items.append(("info", f"Student left {sc} comment(s) on {_pr_link(f['pr_number'])}."))

    ln_flags = typed("late_night")
    if ln_flags:
        sample = ln_flags[0]
        items.append(("neg", f"Lab submitted at \\textbf{{late night}} at {_ist_display(sample['datetime_ist'])}, {_pr_link(sample['pr_number'])}. Consistent late-night work may indicate last-minute effort."))

    for f in typed("fast_completion"):
        s = f["span_seconds"]
        t_str = f"{int(s//60)}m {int(s%60)}s" if s >= 60 else f"{int(s)}s"
        items.append(("neg", f"{_pr_link(f['pr_number'])} was completed in just \\textbf{{{escape_latex(t_str)}}}, which is suspiciously fast for a lab exercise."))

    for f in typed("generic_commits"):
        samples = ", ".join(f"``{escape_latex(s)}''" for s in f.get("samples", [])[:2])
        ratio = f"{f['generic_count']}/{f['total_commits']}"
        items.append(("neg", f"\\textbf{{{ratio}}} commit messages in {_pr_link(f['pr_number'])} are non-descriptive (e.g.~{samples}). Poor commit hygiene."))

    for f in typed("high_commit_count"):
        items.append(("info", f"{_pr_link(f['pr_number'])} has an unusually high commit count of \\textbf{{{f['commits']}}}."))

    for f in typed("no_sql_submitted"):
        items.append(("neg", f"\\textbf{{No .sql files}} found in {_pr_link(f['pr_number'])} with {f['changed_files']} other file(s) changed. Lab deliverable may be missing."))

    for f in typed("solution_file_submitted"):
        fnames = escape_latex(", ".join(os.path.basename(fn) for fn in f.get("files", [])))
        items.append(("neg", f"Solution reference file \\textbf{{{fnames}}} was committed in {_pr_link(f['pr_number'])}. This should not be part of the submission."))

    bulk_flags = typed("bulk_same_day")
    if bulk_flags:
        for f in bulk_flags:
            labs_str = ", ".join(str(l) for l in f.get("labs", []))
            items.append(("neg", f"Labs {labs_str} submitted on the same day, {escape_latex(f.get('date',''))}."))
        items.append(("neg", "Submitting multiple labs together suggests rushed or batched work rather than consistent effort."))

    rapid_flags = typed("rapid_succession")
    if rapid_flags:
        for f in rapid_flags:
            items.append(("neg", f"Labs {f['lab_a']} and {f['lab_b']} submitted just \\textbf{{{f['gap_minutes']} min}} apart."))
        items.append(("neg", "Labs submitted in rapid succession are likely batched, not developed independently."))

    for f in typed("empty_merged_pr"):
        items.append(("neg", f"{_pr_link(f['pr_number'])} was accepted but contained \\textbf{{no changed files}}. Verify this was intentional."))

    for f in typed("first_attempt_clean"):
        items.append(("pos", f"Accepted on \\textbf{{first attempt}}. {_pr_link(f['pr_number'])} merged cleanly with no issues."))

    for f in typed("clean_submission"):
        items.append(("pos", f"Submission in {_pr_link(f['pr_number'])} is well-organized: \\textbf{{{f['files']} file(s)}}, no stray or solution files."))

    for f in typed("iterative_development"):
        items.append(("pos", f"Development spread across \\textbf{{{f['commit_days']} days}} with {f['total_commits']} commit(s) in {_pr_link(f['pr_number'])}. Shows consistent effort."))

    uq = typed("unique_submission")
    if uq:
        best = min(uq, key=lambda x: x.get("top_percentile", 100))
        score = int(best["uniqueness_score"] * 100)
        items.append(("pos", f"Originality in \\textbf{{top {best['top_percentile']}\\%}} for this lab ({score}\\% uniqueness score)."))

    cq = typed("commit_quality")
    if cq:
        best = min(cq, key=lambda x: x.get("top_percentile", 100))
        score = int(best["quality_score"] * 100)
        items.append(("pos", f"Commit quality in \\textbf{{top {best['top_percentile']}\\%}} ({score}\\% meaningful messages)."))

    return items


def _render_behavior_items(items: List, title: str = "Summary") -> str:
    _ICONS = {"pos": "[+]", "neg": "[-]", "info": "[i]"}
    inner_lines = [f"\\noindent{{\\small\\textbf{{{title}}}}}\\\\[2pt]"]
    for cat, text in items:
        if cat == "cont":
            inner_lines.append(
                f"{{\\footnotesize\\hangindent=1.0em\\hangafter=1"
                f"\\noindent {text}\\\\[1pt]}}"
            )
        else:
            icon = _ICONS.get(cat, _ICONS["info"])
            inner_lines.append(
                f"{{\\small\\hangindent=1.6em\\hangafter=1"
                f"\\noindent\\texttt{{{icon}}}~{text}\\\\[1pt]}}"
            )
    inner = "\n    ".join(inner_lines)
    return (
        "\\begin{tcolorbox}[colback=white,colframe=black!65,boxrule=0.5pt,"
        "left=7pt,right=7pt,top=6pt,bottom=5pt,arc=0pt]\n"
        "    " + inner + "\n"
        "\\end{tcolorbox}\n"
        "\\vspace{2pt}\n"
    )


def _collect_behavior_items(flags: List, prn_to_name: dict, has_submission: bool, lab: int) -> List:
    pn = prn_to_name or {}
    items = _build_narrative(flags, pn)
    if not has_submission:
        # Only the status bullet on cover; instructions go to sources page
        items = [("neg", "No GitHub submission found for this lab. Write justification on the next page."), ] + items
    return items


def _collect_nosub_instructions(lab: int) -> List:
    """Verbose Student/Instructor instructions shown only on sources page."""
    if lab == 7:
        return [
            ("info", "No GitHub submission found for this lab (take-home capstone)."),
            ("info", "\\textbf{Student:} Attach all project files: \\texttt{ddl.sql}, \\texttt{seed.sql}, \\texttt{queries.sql}, ER diagram / \\texttt{schema.md}, and \\texttt{report.md} (or PDF)."),
            ("info", "\\textbf{Instructor:} Review attached project resources. No GitHub commit history is expected for this lab."),
        ]
    return [
        ("info", "\\textbf{Student:} Attach complete source code (.sql files) with this write-up."),
        ("info", "\\textbf{Student:} If you submitted elsewhere or faced issues, add a short note."),
        ("info", "\\textbf{Instructor:} Verify attached source code; no commit history available."),
    ]


def latex_behavior_block(flags: List, prn_to_name: dict = None, has_submission: bool = True, lab: int = None, max_items: int = None) -> str:
    items = _collect_behavior_items(flags, prn_to_name or {}, has_submission, lab)
    if not items:
        return ""
    if max_items is not None and len(items) > max_items:
        n_overflow = len(items) - (max_items - 1)
        items = items[:max_items - 1] + [("cont", f"\\textbf{{\\textit{{\\ldots~{n_overflow} more observation(s) on the next page.}}}}")]
    return _render_behavior_items(items)


def latex_behavior_overflow_block(flags: List, prn_to_name: dict = None, has_submission: bool = True, lab: int = None, max_items: int = None) -> str:
    """Renders the overflow items (beyond max_items) for the sources page."""
    if max_items is None:
        return ""
    items = _collect_behavior_items(flags, prn_to_name or {}, has_submission, lab)
    if len(items) <= max_items:
        return ""
    n_prev = max_items - 1
    overflow = [(
        "cont",
        f"\\textbf{{\\textit{{\\ldots~Continued from previous page ({n_prev} observation(s) above).}}}}",
    )] + items[max_items - 1:]
    return _render_behavior_items(overflow)


def latex_plagiarism_table(flags: List, prn_to_name: dict = None, lab: int = None, prn_lab_pr_map: dict = None) -> str:
    """Detailed plagiarism/similarity table for the sources page."""
    plag = [f for f in flags if isinstance(f, dict) and f.get("type") == "plagiarism"]
    if not plag:
        return ""
    pn = prn_to_name or {}
    plm = prn_lab_pr_map or {}
    plag_sorted = sorted(plag, key=lambda x: -x.get("similarity", 0))

    lines = [
        "\\vspace{0.6em}",
        "\\textbf{Plagiarism / Similarity Details}\\\\[2pt]",
        "{\\small",
        "\\begin{tabularx}{\\linewidth}{@{} p{2.2cm} p{3.5cm} p{1.0cm} p{3.2cm} r p{1.6cm} @{}}",
        "\\toprule",
        "PRN & Name & PR & Date (IST) & Sim. & Notes \\\\",
        "\\midrule",
    ]
    for f in plag_sorted:
        prn = f["matched_prn"]
        name = escape_latex(_name_for(prn, pn))
        sim = f"{f['similarity']*100:.0f}\\%"
        note = "Exact" if f["similarity"] >= 0.99 else ("High" if f["similarity"] >= 0.90 else "Moderate")
        match_info = plm.get(prn.upper(), {}).get(lab) if lab is not None else None
        if match_info:
            pr_num = match_info.get("pr_number")
            last_c = match_info.get("last_commit")
            pr_url = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/pull/{pr_num}"
            pr_str = f"\\href{{{pr_url}}}{{\\#{pr_num}}}" if pr_num else "--"
            time_str = escape_latex(_ist_display_short(last_c)) if last_c else "--"
        else:
            pr_str, time_str = "--", "--"
        lines.append(f"  {escape_latex(prn)} & \\truncate{{3.4cm}}{{{name}}} & {pr_str} & {time_str} & {sim} & {note} \\\\")
    lines += ["\\bottomrule", "\\end{tabularx}", "}", "\\vspace{0.4em}"]
    return "\n".join(lines) + "\n"


def latex_verification_block(pr_numbers: Iterable[int]) -> str:
    prs = sorted({int(p) for p in pr_numbers if p is not None})
    first_url = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/pull/{prs[0]}" if prs else None
    display_url = first_url or "—"
    display_label = _ellipsize(display_url, 80)
    lines: List[str] = []
    lines.append("\\begin{tabular}{@{}p{0.23\\textwidth} p{0.74\\textwidth}@{}}")
    # Left QR
    if first_url:
        lines.append("\\begin{minipage}[t]{\\linewidth}\\centering\\vspace{0pt}\\qrcode[hyperlink,height=2.4cm]{" + first_url + "}\\end{minipage}")
    else:
        # Keep column height consistent even when there's no URL
        lines.append("\\begin{minipage}[t]{\\linewidth}\\vspace{2.4cm}\\end{minipage}")
    lines.append("&")
    # Right instruction + link
    lines.append("\\begin{minipage}[t]{\\linewidth}")
    lines.append("\\vspace{0.6em}")
    lines.append("\\noindent\\textbf{Verification}:\n")
    lines.append("\\vspace{0.4em}")
    lines.append("To verify the submission, open the pull request link below or scan the QR code.\\\\")
    if first_url:
        lines.append("\\href{" + first_url + "}{" + escape_latex(display_label) + "}")
    else:
        lines.append("—")
    lines.append("\\end{minipage}\\\\")
    lines.append("\\end{tabular}")
    lines.append("\\vspace{0.6em}")
    return "\n".join(lines) + "\n"


def latex_justification_lines_block(line_count: int = 7) -> str:
    prompts = [
        "Reason for not submitting on GitHub (technical issue, access problem, other):",
        "Have you completed this lab locally? If yes, briefly describe what you did:",
        "What specific SQL tasks / queries did you attempt for this lab:",
        "Any challenges faced or concepts you are unclear about:",
        "Additional remarks or clarifications for the instructor:",
    ]
    lines = [
        "\\vspace{0.8em}",
        "\\noindent\\textbf{Justification} {\\small\\textit{(to be filled by student)}}",
        "\\vspace{0.6em}",
        "",
    ]
    for i in range(line_count):
        prompt = prompts[i] if i < len(prompts) else ""
        if prompt:
            lines.append(f"\\noindent{{\\footnotesize\\textit{{{escape_latex(prompt)}}}}}\\\\[2pt]")
        else:
            lines.append("\\vspace{4pt}")
        lines.append("\\noindent\\rule{\\linewidth}{0.3pt}\\\\[14pt]")
    return "\n".join(lines) + "\n"


def latex_verification_caution_block(pr_numbers) -> str:
    prs = sorted({int(p) for p in pr_numbers if p is not None})
    first_url = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/pull/{prs[0]}" if prs else None
    display_label = escape_latex(_ellipsize(first_url, 70)) if first_url else "—"
    link_part = (
        f"\\href{{{first_url}}}{{{display_label}}}"
        if first_url else "—"
    )
    lines: List[str] = []
    # QR + verification (mirror of cover page)
    lines.append("\\begin{tabular}{@{}p{0.23\\textwidth} p{0.74\\textwidth}@{}}")
    if first_url:
        lines.append("\\begin{minipage}[t]{\\linewidth}\\centering\\vspace{0pt}\\qrcode[hyperlink,height=2.4cm]{" + first_url + "}\\end{minipage}")
    else:
        lines.append("\\begin{minipage}[t]{\\linewidth}\\vspace{2.4cm}\\end{minipage}")
    lines.append("&")
    lines.append("\\begin{minipage}[t]{\\linewidth}")
    lines.append("\\vspace{0.6em}")
    lines.append("\\noindent\\textbf{Verification}:\\\n")
    lines.append("\\vspace{0.4em}")
    lines.append("To verify the submission, open the pull request link below or scan the QR code.\\\\")
    lines.append(link_part)
    lines.append("\\\\[0.6em]")
    lines.append(
        "\\noindent\\textit{\\textbf{Note:} Students must not alter any details on this cover page "
        "or the source files digitally. Any modification invalidates the submission record.}"
    )
    lines.append("\\end{minipage}\\\\")
    lines.append("\\end{tabular}")
    lines.append("\\vspace{0.6em}")
    return "\n".join(lines) + "\n"


def latex_nosub_declaration_block() -> str:
    cb = "$\\square$"
    lines = [
        "\\begin{tcolorbox}[colback=white,colframe=black!30,boxrule=0.3pt,"
        "left=5pt,right=5pt,top=5pt,bottom=5pt,arc=0pt]",
        "{\\small",
        f"\\noindent {cb}\\hspace{{0.5em}}I have completed this lab locally and the source code is attached with this write-up.\\\\ [3pt]",
        f"\\noindent {cb}\\hspace{{0.5em}}The reason(s) for not submitting on GitHub are stated on the next page and are accurate to the best of my knowledge.\\\\ [3pt]",
        f"\\noindent {cb}\\hspace{{0.5em}}I understand that GitHub submissions are required because version control is a practical skill expected across all software and data-related roles, and submission via GitHub provides verifiable, timestamped records of work. My non-submission this time is circumstantial and does not reflect a disregard for this requirement.",
        "}",
        "\\end{tcolorbox}",
        "\\vspace{4pt}",
    ]
    return "\n".join(lines) + "\n"


def latex_bottom_row(height_cm: float = 3.0, nosub: bool = False) -> str:
    cb = "$\\square$"
    decl_text = escape_latex(
        "I hereby declare that I have not digitally altered or modified "
        "this cover page or any attached source files after generation."
    )
    if nosub:
        nosub_lines = (
            f"\\noindent{{\\small{cb}\\hspace{{0.5em}}I have completed this lab locally and the source code is attached with this write-up.}}\\\\[3pt]\n"
            f"\\noindent{{\\small{cb}\\hspace{{0.5em}}The reason(s) for not submitting on GitHub are stated on the next page and are accurate to the best of my knowledge.}}\\\\[3pt]\n"
            f"\\noindent{{\\small{cb}\\hspace{{0.5em}}I understand that GitHub submission is strongly preferred by the instructor, "
            f"though manual attachment of source files is also accepted as an alternative. "
            f"Version control is a foundational skill expected across software engineering, data science, and related fields. "
            f"It enables structured collaboration, provides a verifiable and timestamped commit history, and demonstrates "
            f"discipline in code management and progress tracking. Employers and academic reviewers routinely inspect "
            f"repositories as evidence of consistent, independent work habits developed over time. "
            f"Failure to submit via GitHub, regardless of the reason, reduces the verifiability of the submitted work. "
            f"My non-submission is circumstantial and does not reflect a disregard for this standard or its importance.}}\\\\[6pt]\n"
            f"\\noindent\\textcolor{{black!25}}{{\\rule{{\\linewidth}}{{0.3pt}}}}\\\\[4pt]\n"
        )
    else:
        nosub_lines = ""
    declaration_row = (
        "\\noindent\\begin{tcolorbox}[colback=white,colframe=black!30,boxrule=0.3pt,"
        "left=5pt,right=5pt,top=4pt,bottom=4pt,arc=0pt]\n"
        + nosub_lines +
        f"\\noindent$\\square$\\hspace{{0.6em}}{{{decl_text}}}\n"
        "\\end{tcolorbox}\n"
        "\\vspace{2pt}\n"
    )
    # Three columns: Student S/D, Instructor S/D, Remarks
    def sign_box(label: str) -> List[str]:
        box: List[str] = []
        box.append(f"\\begin{{tcolorbox}}[colback=white,colframe=black!30,boxrule=0.3pt,height={height_cm}cm]")
        box.append("\\vspace{1.2cm}")
        box.append("\\rule{\\linewidth}{0.4pt}\\\\")
        box.append(f"\\textbf{{{escape_latex(label)}}}\\\\")
        box.append("Date: \\rule{3cm}{0pt}")
        box.append("\\end{tcolorbox}")
        return box

    def remarks_box() -> List[str]:
        box: List[str] = []
        box.append(f"\\begin{{tcolorbox}}[colback=white,colframe=black!30,boxrule=0.3pt,height={height_cm}cm]")
        box.append("\\textbf{Remarks}\\\\")
        box.append("\\vspace{1.6cm}")
        box.append("\\end{tcolorbox}")
        return box

    lines: List[str] = []
    lines.append(declaration_row)
    lines.append("\\noindent")
    lines.append("\\begin{tabular}{@{}p{0.32\\textwidth} p{0.32\\textwidth} p{0.32\\textwidth}@{}}")
    lines.extend(sign_box("Student Signature"))
    lines.append("&")
    lines.extend(sign_box("Instructor Signature"))
    lines.append("&")
    lines.extend(remarks_box())
    lines.append("\\\\")
    lines.append("\\end{tabular}")
    return "\n".join(lines) + "\n"


# -----------------------------
# Source files rendering
# -----------------------------

_SKIP_FILE_RE = re.compile(r'(?i)(^readme|check.?status|\.solution\.|^\.gitignore|^run_source)')
_SETUP_FILE_RE = re.compile(r'(?i)^(\d+_)?setup\.sql$')


def _sanitize_listing(text: str) -> str:
    return ''.join(ch if ord(ch) < 128 else '?' for ch in text)


def _listing_opts(filename: str) -> str:
    if filename.lower().endswith('.sql'):
        return 'style=sqlcode'
    return 'language={},basicstyle=\\ttfamily\\small,breaklines=true,frame=single,framerule=0.2pt,rulecolor=\\color{black!20}'


def _ps_file_github_url(lab: int, filename: str, course: LabCourse) -> str:
    branch = course.problem_set_branch(lab)
    return f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{branch}/{filename}"


def _list_problem_set_task_files(lab: int, course: LabCourse, output_dir: str) -> List[Tuple[str, str]]:
    """Return [(filename, temp_basename)] of task SQL files from the problem set git branch."""
    branch = course.problem_set_branch(lab)
    repo_root = repo_root_from_scripts()
    try:
        r = subprocess.run(
            ["git", "ls-tree", "--name-only", branch],
            capture_output=True, text=True, cwd=repo_root, timeout=10,
        )
        names = [n.strip() for n in r.stdout.splitlines() if n.strip()]
    except Exception:
        return []
    out = []
    for name in sorted(names):
        if not name.lower().endswith('.sql'):
            continue
        if _SKIP_FILE_RE.search(name):
            continue
        if _SETUP_FILE_RE.match(name):
            continue
        try:
            rc = subprocess.run(
                ["git", "show", f"{branch}:{name}"],
                capture_output=True, text=True, cwd=repo_root, timeout=10,
            )
            content = _sanitize_listing(rc.stdout)
        except Exception:
            content = ""
        temp_name = f"__ps__{name}"
        with open(os.path.join(output_dir, temp_name), 'w', encoding='utf-8') as fh:
            fh.write(content)
        out.append((name, temp_name))
    return out



def _problem_set_url(lab: int, course) -> str:
    branch = course.problem_set_branch(lab)
    return f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/tree/{branch}"


def _student_lab_dir(prn: str, lab: int, course: LabCourse) -> str:
    repo_root = repo_root_from_scripts()
    return os.path.join(repo_root, course.labs_repo_subdir, f"lab-{lab:02d}", prn)


def _list_source_files_for_lab(prn: str, lab: int, course: LabCourse) -> List[str]:
    lab_dir = _student_lab_dir(prn, lab, course)
    if not os.path.isdir(lab_dir):
        return []
    files: List[str] = []
    try:
        for name in sorted(os.listdir(lab_dir)):
            p = os.path.join(lab_dir, name)
            if not os.path.isfile(p):
                continue
            if course.id == "dbms":
                low = name.lower()
                if _SKIP_FILE_RE.search(name):
                    continue
                if low.endswith(".sql") or low.endswith(".md"):
                    files.append(p)
            elif lab == 0:
                # Match single-letter files like a.py .. z.py. The previous pattern used a double
                # backslash which failed to match names like 'a.py'. Use a single escaped dot.
                if re.fullmatch(r"[a-z]\.py", name) or name in {"z+.py", "z++.py", "z+++.py"}:
                    files.append(p)
            else:
                if name.startswith("task_") and name.endswith(".py"):
                    files.append(p)
    except Exception:
        return []
    return files


def _file_github_url(lab: int, prn: str, filename: str, course: LabCourse) -> str:
    blob_branch = course.github_blob_branch
    sub = course.labs_repo_subdir
    return f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/blob/{blob_branch}/{sub}/lab-{lab:02d}/{prn}/{filename}"


def latex_sources_for_lab(student: Student, lab: int, output_dir: str, course: LabCourse) -> str:
    lines: List[str] = []

    def _write_student_listing(abs_path: str) -> str:
        filename = os.path.basename(abs_path)
        rel = os.path.relpath(abs_path, start=output_dir)
        try:
            with open(abs_path, 'r', encoding='utf-8') as fh:
                txt = fh.read()
            if any(ord(ch) > 127 for ch in txt):
                ext = os.path.splitext(filename)[1]
                safe_base = os.path.splitext(filename)[0] + f".__ascii__{ext}"
                with open(os.path.join(output_dir, safe_base), 'w', encoding='utf-8') as wf:
                    wf.write(_sanitize_listing(txt))
                return safe_base
            return rel
        except Exception:
            pass
        try:
            with open(abs_path, 'rb') as rf:
                raw = rf.read()
            ext = os.path.splitext(filename)[1]
            safe_base = os.path.splitext(filename)[0] + f".__utf8__{ext}"
            with open(os.path.join(output_dir, safe_base), 'w', encoding='utf-8') as wf:
                wf.write(_sanitize_listing(raw.decode('utf-8', errors='replace')))
            return safe_base
        except Exception:
            return rel

    def _file_heading(label: str, filename: str, url: str) -> List[str]:
        return [
            f"\\noindent\\textbf{{{label}}}: \\chip{{{escape_latex(filename)}}}\\\\",
            f"{{\\small\\url{{{url}}}}}",
            "\\vspace{0.4em}",
        ]

    # Collect student files into buckets
    student_setup: Optional[str] = None
    student_check_status: Optional[str] = None
    student_files_map: dict = {}
    lab_dir = _student_lab_dir(student.prn, lab, course)
    if os.path.isdir(lab_dir):
        for name in sorted(os.listdir(lab_dir)):
            p = os.path.join(lab_dir, name)
            if not os.path.isfile(p):
                continue
            low = name.lower()
            if not (low.endswith('.sql') or low.endswith('.md')):
                continue
            if re.search(r'(?i)(^readme|\.solution\.)', name):
                continue
            if re.search(r'(?i)check.?status', name):
                student_check_status = p
            elif _SETUP_FILE_RE.match(name):
                student_setup = p
            else:
                student_files_map[name] = p

    ps_files = _list_problem_set_task_files(lab, course, output_dir)

    # Problem set URL heading
    lines.append(f"\\noindent{{\\textbf{{Problem Set}}}}\\\\")
    lines.append(f"{{\\small\\url{{{_problem_set_url(lab, course)}}}}}")
    lines.append("\\vspace{0.8em}")

    # setup.sql — student copy only (context)
    if student_setup:
        fn = os.path.basename(student_setup)
        src = _write_student_listing(student_setup)
        url = _file_github_url(lab, student.prn, fn, course)
        lines.extend(_file_heading("[Common] Setup", fn, url))
        lines.append(f"\\lstinputlisting[{_listing_opts(fn)}]{{{src.replace(chr(92)*2, '/')}}}")
        lines.append("\\vspace{0.8em}")

    # Interleaved Task / Solution pairs
    for fname, temp_name in ps_files:
        ps_url = _ps_file_github_url(lab, fname, course)
        lines.extend(_file_heading("Task", fname, ps_url))
        lines.append(f"\\lstinputlisting[{_listing_opts(fname)}]{{{temp_name}}}")
        lines.append("\\vspace{0.6em}")
        stu_path = student_files_map.get(fname)
        if stu_path:
            stu_url = _file_github_url(lab, student.prn, fname, course)
            lines.extend(_file_heading("Solution", fname, stu_url))
            src = _write_student_listing(stu_path)
            lines.append(f"\\lstinputlisting[{_listing_opts(fname)}]{{{src.replace(chr(92)*2, '/')}}}")
        else:
            lines.append("{\\small\\textit{No student solution found for this task.}}")
        lines.append("\\vspace{0.8em}")

    # check_status.sql — student copy only
    if student_check_status:
        fn = os.path.basename(student_check_status)
        src = _write_student_listing(student_check_status)
        url = _file_github_url(lab, student.prn, fn, course)
        lines.extend(_file_heading("[Common] Check Status", fn, url))
        lines.append(f"\\lstinputlisting[{_listing_opts(fn)}]{{{src.replace(chr(92)*2, '/')}}}")
        lines.append("\\vspace{0.6em}")

    # Remaining student files that didn't match any PS task
    unmatched = [
        (name, p) for name, p in sorted(student_files_map.items())
        if name not in {f for f, _ in ps_files}
    ]
    if unmatched:
        for name, p in unmatched:
            url = _file_github_url(lab, student.prn, name, course)
            lines.extend(_file_heading("File", name, url))
            src = _write_student_listing(p)
            lines.append(f"\\lstinputlisting[{_listing_opts(name)}]{{{src.replace(chr(92)*2, '/')}}}")
            lines.append("\\vspace{0.8em}")

    if not ps_files and not student_setup and not student_check_status and not student_files_map:
        lines.append("\\begin{tcolorbox}[colback=gray!5,colframe=gray!40,boxrule=0.3pt]")
        lines.append("No source files found for this lab.")
        lines.append("\\end{tcolorbox}")

    return "\n".join(lines) + "\n"


# -----------------------------
# Aggregation
# -----------------------------

def aggregate_for_student_lab(
    student: Student,
    lab: int,
    all_commits: List[CommitRow],
    pr_lab_map: Optional[dict],
    course: LabCourse,
) -> Tuple[List[CommitRow], List[int], List[str], List[str], List[str]]:
    """Collect commits for a student and lab.

    If pr_lab_map is provided (mapping PR number -> lab), prefer that mapping when
    selecting commits by lab. Falls back to commit message / files inference.
    """
    commits: List[CommitRow] = []
    for c in all_commits:
        if (c.prn or "").strip().upper() != student.prn.strip().upper():
            continue
        # If commit is associated with a PR and mapping exists, prefer it
        lab_from_pr = None
        if pr_lab_map and c.pr_number is not None:
            lab_from_pr = pr_lab_map.get(int(c.pr_number))
        if lab_from_pr is not None:
            if lab_from_pr != lab:
                continue
            commits.append(c)
            continue

        # Otherwise infer from commit message / files
        lab_inferred = infer_lab(c, course)
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

def _print_progress(current: int, total: int, prefix: str = "") -> None:
    # Simple in-place progress bar
    width = 30
    done = int(width * current / max(total, 1))
    bar = "#" * done + "." * (width - done)
    msg = f"\r{prefix}[{bar}] {current}/{total}"
    sys.stdout.write(msg)
    sys.stdout.flush()


def _cleanup_keep_only(pdf_path: str, folder: str) -> None:
    # Remove files in folder that share the same base filename as pdf_path
    base = os.path.basename(pdf_path)
    prefix = base.split(".")[0]
    for name in os.listdir(folder):
        p = os.path.join(folder, name)
        if os.path.isdir(p):
            continue
        # Keep the final merged PDF itself
        if os.path.abspath(p) == os.path.abspath(pdf_path):
            continue
        # Remove only files that share the same prefix to avoid deleting other students' files
        if os.path.basename(name).startswith(prefix):
            try:
                os.remove(p)
            except Exception:
                pass


def generate_covers(
    students_csv: str,
    commits_csv: str,
    out_dir: str,
    only_prns: Optional[List[str]],
    labs: Optional[List[int]],
    compile_pdf: bool,
    course: LabCourse,
) -> int:
    students = read_students(students_csv)
    if only_prns:
        only = {s.upper() for s in only_prns}
        students = [s for s in students if s.prn.upper() in only]

    prn_to_name: dict = {s.prn.upper(): s.name for s in read_students(students_csv)}

    # Prefer pr_details.json (richer data); fall back to commits.csv
    pr_details_path = course.path_in_output("pr_details.json")
    if os.path.exists(pr_details_path):
        commits, pr_lab_map = load_from_pr_details(pr_details_path, course)
        # Build prn → lab → {pr_number, last_commit} lookup for plagiarism table
        prn_lab_pr_map: dict = {}
        try:
            import json as _json
            _prd = _json.load(open(pr_details_path, encoding="utf-8"))
            for _pr in _prd:
                _prn = (_pr.get("prn") or "").upper()
                _pnum = _pr.get("number")
                if not _prn or _pnum is None:
                    continue
                _lab = pr_lab_map.get(int(_pnum))
                if _lab is None:
                    continue
                _cs = _pr.get("commits", [])
                _last = _cs[-1].get("author_date") if _cs else None
                entry = {"pr_number": _pnum, "last_commit": _last}
                prn_lab_pr_map.setdefault(_prn, {})
                if _lab not in prn_lab_pr_map[_prn] or _pr.get("merged"):
                    prn_lab_pr_map[_prn][_lab] = entry
        except Exception:
            pass
    else:
        commits = read_commits(commits_csv)
        pr_csv = os.path.join(os.path.dirname(commits_csv), "pull_requests.csv")
        pr_rows = read_pull_requests(pr_csv)
        pr_lab_map: dict = {}
        for r in pr_rows:
            pr_no = _to_int(r.get("PR Number"))
            if pr_no is None:
                continue
            lab_n = infer_lab_from_pr_row(r)
            if lab_n is not None:
                pr_lab_map[int(pr_no)] = lab_n
        prn_lab_pr_map = {}

    analysis = load_analysis(course)

    lab_titles = lab_titles_dbms() if course.id == "dbms" else lab_titles_default()
    allowed_labs = set(course.lab_numbers())
    lab_list = list(course.lab_numbers()) if not labs else [l for l in labs if l in allowed_labs]

    ensure_dir(out_dir)
    total_students = len(students)
    for stu_idx, stu in enumerate(students, start=1):
        stu_dir = out_dir
        ensure_dir(stu_dir)
        doc_parts: List[str] = []
        doc_parts.append(latex_global_preamble(stu, course))
        for idx, lab in enumerate(lab_list):
            title = lab_titles.get(lab, f"Lab {lab:02d}")
            commits_lab, pr_numbers, pr_users, emails, files = aggregate_for_student_lab(
                stu, lab, commits, pr_lab_map, course
            )
            prn_upper = stu.prn.strip().upper()
            prn_analysis = analysis.get(prn_upper, {})
            flags = prn_analysis.get(str(lab), []) + prn_analysis.get("-1", [])

            # --- Cover page ---
            doc_parts.append(latex_set_header_lab(lab))
            doc_parts.append(latex_title_block(lab, title))
            doc_parts.append(latex_course_block(lab, course))
            doc_parts.append(latex_student_block(stu, "Submitted" if pr_numbers else "Not submitted", pr_users, emails))
            doc_parts.append(latex_submission_block(pr_users, emails, pr_numbers, files))
            doc_parts.append(latex_behavior_block(flags, prn_to_name, has_submission=bool(pr_numbers), lab=lab, max_items=8))
            if pr_numbers:
                doc_parts.append(latex_verification_block(pr_numbers))
            doc_parts.append("\\vspace*{\\fill}")
            doc_parts.append(latex_bottom_row(3.0, nosub=not bool(pr_numbers)))
            first_pr = pr_numbers[0] if pr_numbers else None
            pr_text = f"PR: {first_pr}" if first_pr is not None else "PR: —"
            files_count = len(set(files))
            doc_parts.append(f"\\fancyfoot[R]{{{escape_latex(pr_text)}\\,\\, Files: {files_count}}}")

            # --- Sources page ---
            doc_parts.append("\\newpage")
            doc_parts.append(latex_set_header_lab(lab))
            overflow_block = latex_behavior_overflow_block(flags, prn_to_name, has_submission=bool(pr_numbers), lab=lab, max_items=8)
            if not pr_numbers and not commits_lab:
                # No submission: show only the note, then instructions + justification lines on sources page
                doc_parts.append(
                    "\\noindent\\textit{\\textbf{Note:} Students must not alter any details on this cover page "
                    "or the source files digitally. Any modification invalidates the submission record.}"
                    "\\\\[0.8em]\n"
                )
                nosub = _collect_nosub_instructions(lab)
                if nosub:
                    doc_parts.append(_render_behavior_items(nosub, title="Instructions"))
                doc_parts.append(latex_justification_lines_block(8))
            else:
                doc_parts.append(latex_verification_caution_block(pr_numbers))
                if overflow_block:
                    doc_parts.append(overflow_block)
                doc_parts.append(latex_files_chips_block(files))
                doc_parts.append(latex_commit_table_full(commits_lab) or latex_commit_table(commits_lab, lab))
                doc_parts.append(latex_plagiarism_table(flags, prn_to_name, lab, prn_lab_pr_map))
            doc_parts.append("\\cleartooddpage")
            if (pr_numbers or commits_lab) and lab != 7:
                doc_parts.append(latex_sources_for_lab(stu, lab, stu_dir, course))

            # Page break between labs
            if idx != len(lab_list) - 1:
                doc_parts.append("\\cleartooddpage")

        doc_parts.append("\\end{document}")

        base = f"{stu.prn}_{slugify(stu.name)}_covers"
        tex_path = os.path.join(stu_dir, base + ".tex")
        pdf_path = os.path.join(stu_dir, base + ".pdf")
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write("\n".join(doc_parts))

        print(f"Generating {stu_idx}/{total_students}: {stu.prn}")

        if compile_pdf:
            try:
                compile_tex(tex_path, stu_dir)
            except Exception:
                print(f"\nLaTeX compile failed for {tex_path}")
            _cleanup_keep_only(pdf_path, stu_dir)

    if total_students:
        sys.stdout.write("\n")
        sys.stdout.flush()
    print(f"Generated {total_students} merged cover PDF(s) in {out_dir}")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Generate lab cover pages (LaTeX/PDF) per student per lab")
    p.add_argument("--course", default="daa", help="Course id (daa, dbms) — see courses/<id>.json")
    p.add_argument("--students", default=None, help="Path to students.csv (default: from course config)")
    p.add_argument("--commits", default=None, help="Path to commits.csv (default: output/<course>/commits.csv)")
    p.add_argument("--out-dir", default=None, help="Output folder for covers (default: output/<course>/covers)")
    p.add_argument("--only", nargs="*", help="Only process these PRNs")
    p.add_argument("--labs", nargs="*", type=int, help="Only process these lab numbers (must be in course lab_range)")
    p.add_argument("--compile", action="store_true", help="Compile LaTeX to PDF")
    args = p.parse_args(argv)

    course = LabCourse.load(args.course, root=ROOT)
    students_path = args.students or course.students_csv
    commits_path = args.commits or course.commits_csv
    out_dir = args.out_dir or course.covers_dir

    pr_details_path = course.path_in_output("pr_details.json")
    needs_commits = not os.path.exists(pr_details_path)

    required = [students_path] + ([commits_path] if needs_commits else [])
    for need in required:
        if not os.path.exists(need):
            print(f"Missing input: {need}", file=sys.stderr)
            return 2

    return generate_covers(students_path, commits_path, out_dir, args.only, args.labs, args.compile, course)


if __name__ == "__main__":
    raise SystemExit(main())
