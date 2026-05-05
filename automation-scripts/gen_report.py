import argparse
import os

import numpy as np
import pandas as pd
import re

from lib.common import load_pull_requests_df, student_sort_key
from lib.lab_course import LabCourse
from lib.latex_duplex import latex_duplex_even_page_suffix

SCRIPT_ROOT = os.path.dirname(os.path.abspath(__file__))

# ------------------------
# CONFIG (per --course)
# ------------------------
REPO_URL = "https://github.com/s-m-quadri/geca-labs"

_ap = argparse.ArgumentParser(description="Summary CSV/Markdown/LaTeX from pull_requests + attendance.")
_ap.add_argument("--course", default="daa", help="Course id (see courses/<id>.json)")
_args = _ap.parse_args()
course = LabCourse.load(_args.course, root=SCRIPT_ROOT)

LAB_RANGE = course.lab_numbers()
INPUT_FILE = course.pull_requests_csv
STUDENT_FILE = course.students_csv
ATTENDANCE_FILE = course.attendance_csv
OUTPUT_FILE_CSV = course.summary_csv
OUTPUT_FILE_MD = os.path.join(SCRIPT_ROOT, "report", f"summary-{course.id}.md")
LATEX_FILE = os.path.join(SCRIPT_ROOT, "report", f"summary-{course.id}.tex")

# ------------------------
# HELPER FUNCTIONS
# ------------------------
def extract_lab(labels):
    """Extract lab number from label like 'Lab 01'."""
    if pd.isna(labels):
        return None
    for lbl in labels.split(","):
        match = re.search(r"Lab\s*0*([0-9]+)", lbl.strip(), re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None

def status_from_rows(rows, lab_num):
    """Decide status for a specific lab from multiple PR rows (deduplicated)."""
    merged = set()
    open_prs = set()
    closed_prs = set()

    for _, r in rows.iterrows():
        pr_id = f"#{r['PR Number']}"
        # Check if this PR is really for this lab
        if not re.search(fr"Lab\s*0*{lab_num}\b", str(r["Labels"]), re.IGNORECASE):
            continue

        if pd.notna(r["Merged At"]) and r["Merged At"] != "":
            merged.add(pr_id)
        elif r["State"] == "open":
            open_prs.add(pr_id)
        elif r["State"] == "closed":
            closed_prs.add(pr_id)

    def clickable(prs):
        return [f"[{p}]({REPO_URL}/pull/{p.strip('#')})" for p in prs]

    if merged:
        if len(merged) > 1:
            largest = max(int(p.strip("#")) for p in merged)
            merged = {f"#{largest}"}
        return f"Acc {', '.join(clickable(sorted(merged)))}"
    elif open_prs:
        return f"Wip {', '.join(clickable(sorted(open_prs)))}"
    elif closed_prs:
        return f"Err {', '.join(clickable(sorted(closed_prs)))}"
    else:
        return "-"

# ------------------------
# MAIN SCRIPT
# ------------------------
df = load_pull_requests_df(course)
students_df = pd.read_csv(STUDENT_FILE)

summary = []
for _, student in students_df.iterrows():
    prn = student["PRN"]
    name = student["Name"]

    group = df[df["PRN"] == prn]
    if not group.empty:
        user = group["User"].iloc[0]
    else:
        user = "-"

    row = {"PRN": prn, "Name": name, "User": user}

    labs_started = 0
    labs_completed = 0

    for lab in LAB_RANGE:
        lab_rows = group[group["Labels"].str.contains(f"Lab 0*{lab}", na=False, case=False)]
        if not lab_rows.empty:
            labs_started += 1
            status = status_from_rows(lab_rows, lab)
            if status.startswith("A"):
                labs_completed += 1
        else:
            status = "-"
        row[f"Lab {lab}"] = status

    row["Start"] = labs_started
    row["Done"] = labs_completed
    _den = len(LAB_RANGE)
    row["Total"] = _den
    row["Percent"] = f"{(labs_completed / _den) * 100:.2f}%" if _den else "0.00%"
    summary.append(row)

summary_df = pd.DataFrame(summary)
summary_df = summary_df.sort_values(
    by="PRN",
    key=lambda col: col.map(lambda p: student_sort_key(str(p))),
)

# ------------------------
# EXPORT CSV
# ------------------------
summary_df.to_csv(OUTPUT_FILE_CSV, index=False, encoding="utf-8")
print(f"Summary saved to {OUTPUT_FILE_CSV}")

# ------------------------
# EXPORT MARKDOWN
# ------------------------
with open(OUTPUT_FILE_MD, "w", encoding="utf-8") as f:
    # Header
    headers = summary_df.columns.tolist()
    f.write("| " + " | ".join(headers) + " |\n")
    f.write("|" + " --- |" * len(headers) + "\n")

    # Rows
    for _, r in summary_df.iterrows():
        row_md = []
        for col in headers:
            val = r[col]
            if col == "User" and val != "ghost":
                if "-" == val:
                    val = f"`{val}`"
                else:
                    val = f"[`{val}`](https://github.com/{val})"
            row_md.append(str(val))
        f.write("| " + " | ".join(row_md) + " |\n")

print(f"Markdown summary saved to {OUTPUT_FILE_MD}")

# ------------------------
# EXPORT TO LATEX
# ------------------------
# Make a copy of the dataframe to preserve original
latex_df = summary_df.copy()

def escape_latex(text):
    """Escape special LaTeX characters but leave LaTeX commands intact."""
    if not isinstance(text, str):
        return text
    # Skip already LaTeX commands like \href
    if text.startswith("\\") and ("href" in text or "texttt" in text):
        return text
    replacements = {
        "&": r"\&",
        # "%": r"\%",
        "$": r"\$",
        # "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
        "\\": r"\textbackslash{}"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def format_github_user(user):
    """Format GitHub username as clickable link or code if ghost/hyphen."""
    if not isinstance(user, str):
        return user
    if user == "ghost" or user == "-":
        return r"\texttt{" + escape_latex(user) + "}"
    # return r"\href{https://github.com/" + user + r"}{\texttt{" + escape_latex(user) + "}}"
    return r"\href{https://github.com/" + user + r"}{\ulined{\texttt{" + escape_latex(user) + "}}}"


def format_pr_link(pr):
    """Convert PR number or text containing #123 to clickable LaTeX link."""
    if not isinstance(pr, str):
        return pr
    
    # Replace all #PR_NUMBER references with proper LaTeX \href
    def replace_match(m):
        num = m.group(1)
        return r"\href{https://github.com/s-m-quadri/geca-labs/pull/" + num + r"}{\ulined{\texttt{\#" + num + "}}}"

    # Remove any raw Markdown syntax like []() if present
    pr = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", pr)  # optional
    
    return re.sub(r"#(\d+)", replace_match, pr)

def process_lab_column(val):
    """Handle Lab 0 special formatting, then general PR formatting."""
    if isinstance(val, str) and ("merged" in val or "in progress" in val):
        # Extract PR number from string (if present)
        match = re.search(r"#(\d+)", val)
        if match:
            return format_pr_link(match.group(0))
    return format_pr_link(val)

# ------------------------
# Apply formatting
# ------------------------
# Escape all textual data first
latex_df = latex_df.map(escape_latex)

# Format GitHub usernames
if "User" in latex_df.columns:
    latex_df["User"] = latex_df["User"].apply(format_github_user)

# Format PR links for all Lab columns
for col in latex_df.columns:
    if col.startswith("Lab "):
        latex_df[col] = latex_df[col].apply(process_lab_column)

if "Percent" in latex_df.columns:
    latex_df["Percent"] = latex_df["Percent"].apply(
        lambda x: str(x).replace("%", r"\%") if x is not np.nan else x
    )

# Load attendance data
attendance_df = pd.read_csv(ATTENDANCE_FILE)

# remove Unicode if any
attendance_df = attendance_df.map(
    lambda x: x.encode("ascii","ignore").decode("ascii") if isinstance(x,str) else x
)

# keep NaN as "-" for clarity
attendance_df = attendance_df.fillna("n/a")

# Prepare PR DataFrame
pr_latex_df = df.copy()[["PR Number","PRN","Title","User","Labels","State","Created At","Closed At","Merged At"]]

# --- remove PRN UNKNOWN ---
pr_latex_df = pr_latex_df[pr_latex_df["PRN"] != "UNKNOWN"]

# --- add Name column by merging with students_df ---
pr_latex_df = pr_latex_df.merge(students_df[["PRN","Name"]], on="PRN", how="left")
pr_latex_df = pr_latex_df[["PR Number", "PRN","Name","Title","User","Labels","State","Created At","Closed At","Merged At"]]

# --- convert dates to IST, indian format ---
def to_ist(date_str):
    if pd.isna(date_str) or str(date_str).strip()=="":
        return "-"
    try:
        dt = pd.to_datetime(date_str, utc=True).tz_convert("Asia/Kolkata")
        return dt.strftime("%d-%m-%Y %I:%M %p")
    except Exception:
        return "-"

for col in ["Created At","Closed At","Merged At"]:
    pr_latex_df[col] = pr_latex_df[col].apply(to_ist)
    
# --- remove Unicode from Labels ---
pr_latex_df["Labels"] = pr_latex_df["Labels"].str.encode("ascii","ignore").str.decode("ascii")

def sort_labels(label_str):
    if pd.isna(label_str) or label_str.strip() == "":
        return "-"
    labels = [lbl.strip() for lbl in label_str.split(",")]
    def label_key(lbl):
        match = re.search(r"Lab\s*0*([0-9]+)", lbl, re.IGNORECASE)
        if match:
            return (0, int(match.group(1)))  # Lab labels come first, sorted by number
        return (1, lbl.lower())  # Other labels come later, sorted alphabetically
    labels.sort(key=label_key)
    return ", ".join(labels)
pr_latex_df["Labels"] = pr_latex_df["Labels"].apply(sort_labels)

pr_latex_df = pr_latex_df.map(escape_latex)
pr_latex_df["User"] = pr_latex_df["User"].apply(format_github_user)
pr_latex_df["PR Number"] = pr_latex_df["PR Number"].apply(lambda x: format_pr_link(f"#{x}"))

# ------------------------
# Helper: longtable without jinja2 dependency
# ------------------------
def df_to_longtable(df, caption=""):
    cols = df.columns.tolist()
    col_spec = "l" * len(cols)
    header = " & ".join(escape_latex(str(c)) for c in cols) + r" \\"
    lines = [
        f"\\begin{{longtable}}{{{col_spec}}}",
        f"\\caption{{{escape_latex(caption)}}} \\\\",
        "\\toprule",
        header,
        "\\midrule",
        "\\endfirsthead",
        "\\toprule",
        header,
        "\\midrule",
        "\\endhead",
        "\\midrule \\multicolumn{" + str(len(cols)) + r"}{r}{\small\textit{continued\ldots}} \\",
        "\\endfoot",
        "\\bottomrule",
        "\\endlastfoot",
    ]
    for _, row in df.iterrows():
        lines.append(" & ".join(str(row[c]) for c in cols) + r" \\")
    lines.append("\\end{longtable}")
    return "\n".join(lines) + "\n"

# ------------------------
# Export to LaTeX
# ------------------------
with open(LATEX_FILE, "w", encoding="utf-8") as f:
    f.write(
        r"""\documentclass[10pt]{article}
\usepackage{booktabs}
\usepackage{geometry}
\usepackage{longtable}
\usepackage{xcolor}
\usepackage[normalem]{ulem} % for underline
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=orange!70!black,
    urlcolor=orange!70!black,
    citecolor=orange!70!black
}
\usepackage{colortbl}
\usepackage{xcolor}
\definecolor{rowgray}{gray}{0.95}
\definecolor{colgray}{gray}{0.90}
\rowcolors{2}{rowgray}{white}
\newcommand{\ulined}[1]{\uline{#1}}
\usepackage{pdflscape}
\renewcommand{\familydefault}{\rmdefault}
\geometry{a3paper,margin=0.5in}
\begin{document}
\begin{landscape}
\small
\begin{center}
    {\LARGE \textbf{"""
        + escape_latex(course.label)
        + r"""} Attendance and Submission Report \textbf{Jan-Apr 2026}}
\end{center}
\vspace{1em} % small space before first table
"""
    )
    f.write(r"""
\section*{1. Student Attendance}
This table shows the attendance record for each student.
""")
    f.write(df_to_longtable(attendance_df, caption="Student Attendance Record"))
    f.write(r"""
\section*{2. Summary of Lab Submissions}
This table summarizes the lab submissions for each student, including their PR status and overall performance.
\begin{longtable}{ll}
\toprule
Abbreviation & Meaning \\
\midrule
Acc & Accepted (Merged) \\
Wip & Work in Progress (Open) \\
Err & Error (Closed without merge) \\
\bottomrule
\end{longtable}
""")
    f.write(df_to_longtable(latex_df, caption="Summary of Lab Submissions"))
    f.write(r"""
\section*{3. Summary of Pull Requests}
This table lists all pull requests made by students, along with their details.
""")
    f.write(df_to_longtable(pr_latex_df, caption="List of Pull Requests"))
    f.write("\n")
    f.write(latex_duplex_even_page_suffix())
    f.write(r"""
\end{landscape}
\end{document}""")

print(f"LaTeX summary saved to {LATEX_FILE}")