import numpy as np
import pandas as pd
import re

# ------------------------
# CONFIG
# ------------------------
REPO_URL = "https://github.com/s-m-quadri/geca-labs"
STUDENT_FILE = "output/students.csv"
LATEX_FILE = "report/overview.tex"
INPUT_FILE = "output/pull_requests.csv"
ATTENDANCE_FILE = "output/attendance.csv"
LAB_RANGE = range(0, 11)   # Lab 0 to Lab 10

# Submitted rolls
submitted_bt23 = [2,3,4,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,35,36,38,39,42,43,44,45,46,47,48,49,50,51,52,53,56,57,58,60,61,62,63,64,65,66,67]
submitted_bt24 = [1,2,3,4,5,6,8,9,10]

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

def escape_latex(text):
    """Escape special LaTeX characters."""
    if not isinstance(text, str):
        return text
    replacements = {
        # "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# ------------------------
# MAIN SCRIPT
# ------------------------
students_df = pd.read_csv(STUDENT_FILE)
df = pd.read_csv(INPUT_FILE)
attendance_df = pd.read_csv(ATTENDANCE_FILE)

# Prepare attendance_df
attendance_df = attendance_df.fillna("n/a")

overview_data = []
for _, student in students_df.iterrows():
    prn = student["PRN"]
    name = student["Name"]
    
    # Extract batch and roll
    batch = prn[:4]  # BT23 or BT24
    roll = int(prn[-3:])
    
    if (batch == "BT23" and roll in submitted_bt23) or (batch == "BT24" and roll in submitted_bt24):
        writeup_status = "submitted"
        marks = 24
    elif prn in ["BT23F05F005", "BT24S05F007", "BT23F05F059"]:
        writeup_status = "informed"
        marks = 0
    else:
        writeup_status = "-"
        marks = 0
    
    sign = ""  # Empty for now
    
    # Calculate labs_completed
    group = df[df["PRN"] == prn]
    labs_completed = 0
    for lab in LAB_RANGE:
        lab_rows = group[group["Labels"].str.contains(f"Lab 0*{lab}", na=False, case=False)]
        if not lab_rows.empty:
            status = status_from_rows(lab_rows, lab)
            if status.startswith("A"):
                labs_completed += 1
    
    # Calculate attended and conducted
    student_attendance = attendance_df[attendance_df["PRN"] == prn]
    if not student_attendance.empty:
        row = student_attendance.iloc[0]
        # Assuming columns after PRN and Name are sessions
        session_cols = [col for col in attendance_df.columns if col not in ["PRN", "Name"]]
        # conducted: count sessions that are not 'n/a'
        conducted = sum(1 for col in session_cols if str(row[col]).strip().lower() != "n/a")
        # attended: consider anything that's not 'n/a' or an absent marker as present
        absent_values = {"n/a", "absent", "a"}
        attended = sum(1 for col in session_cols if str(row[col]).strip().lower() not in absent_values)
    else:
        conducted = 0
        attended = 0

    # Attendance string with integer percentage (no decimals). If conducted is 0, show 0/0 (0%)
    if conducted > 0:
        attendance_percent = int(round((attended / conducted) * 100))
        attendance_str = f"{attended}/{conducted} ({attendance_percent}%)"
    else:
        attendance_str = "0/0 (0%)"

    # Submission: denominator is always 7 as requested. Compute integer percentage.
    SUBMISSION_DENOM = 7
    submission_percent = int(round((labs_completed / SUBMISSION_DENOM) * 100)) if SUBMISSION_DENOM > 0 else 0
    submission_str = f"{labs_completed}/{SUBMISSION_DENOM} ({submission_percent}%)"
    
    # Place Sign and Marks at the end; Marks should be the very last column
    overview_data.append({
        "PRN": prn,
        "Name": name,
        "Writeup": writeup_status,
        "Attendance": attendance_str,
        "Submission": submission_str,
        "Sign": sign
    })

overview_dff = pd.DataFrame(overview_data)
overview_dff = overview_dff.sort_values(by="PRN")

# Apply LaTeX escaping
overview_dff = overview_dff.applymap(escape_latex)

# ------------------------
# EXPORT TO LATEX
# ------------------------
with open(LATEX_FILE, "w", encoding="utf-8") as f:
    f.write(r"""\documentclass[10pt]{article}
\usepackage{booktabs}
\usepackage{geometry}
\usepackage{longtable}
\usepackage{xcolor}
\usepackage[normalem]{ulem}
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=orange!70!black,
    urlcolor=orange!70!black,
    citecolor=orange!70!black
}
\usepackage{colortbl}
\definecolor{rowgray}{gray}{0.95}
\definecolor{colgray}{gray}{0.90}
\rowcolors{2}{rowgray}{white}
\newcommand{\ulined}[1]{\uline{#1}}
\renewcommand{\familydefault}{\rmdefault}
\geometry{a4paper,margin=0.5in}
\begin{document}
\begin{center}
    {\LARGE \textbf{DAA Labs Report Overview 2025}}
\end{center}
\vspace{1em}
\begin{center}
    {\large This table shows the attendance, submission, and writeup status for each student.}
\end{center}
\vspace{1em}
""")
    f.write(overview_dff.to_latex(index=False, longtable=True, escape=False, column_format='lllllp{2cm}'))
    f.write(r"""
\end{document}""")

print(f"LaTeX overview report saved to {LATEX_FILE}")