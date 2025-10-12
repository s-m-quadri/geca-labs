#!/usr/bin/env python3
"""
Generate per-student LaTeX writeups for Labs 00–10.

Features
- Three sections per lab: Subjective, Objective, Code Digest
- Objective & Code Digest contain personalized numeric inputs per student
- Deterministic per-student randomization (seeded by PRN)
- Reads students from automation-scripts/output/students.csv
- Reads lab titles from automation-scripts/labs/index.md
- Outputs .tex in automation-scripts/output/writeups and optionally compiles PDFs

Usage examples
  - Generate all students and compile to PDF:
      python3 automation-scripts/gen_writeup.py --compile
  - Only generate 3 students (preview), no compile:
      python3 automation-scripts/gen_writeup.py --limit 3
  - Generate only specific PRNs:
      python3 automation-scripts/gen_writeup.py --only BT23F05F002 BT23F05F010 --compile
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import math
import os
import random
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from typing import Dict, List, Tuple


ROOT = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(ROOT, "output", "writeups")
STUDENTS_CSV = os.path.join(ROOT, "output", "students.csv")
LABS_INDEX = os.path.join(ROOT, "labs", "index.md")
LABS_DIR = os.path.join(ROOT, "labs")


# -----------------------------
# Utilities
# -----------------------------

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "file"


def escape_latex(text: str) -> str:
    if text is None:
        return ""
    if not isinstance(text, str):
        text = str(text)
    repl = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for k, v in repl.items():
        text = text.replace(k, v)
    return text


def to_ascii(text: str) -> str:
    if text is None:
        return ""
    if not isinstance(text, str):
        text = str(text)
    # Map common unicode punctuation/symbols to ASCII equivalents BEFORE stripping
    replacements = {
        "→": "->",
        "←": "<-",
        "↔": "<->",
        "≤": "<=",
        "≥": ">=",
        "≠": "!=",
        "×": "x",
        "·": "-",
        "•": "-",
        "–": "-",
        "—": "-",
        "−": "-",
        "’": "'",
        "‘": "'",
        "“": '"',
        "”": '"',
        " ": " ",  # non-breaking space
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    # Strip remaining accents/symbols
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    # Collapse excessive whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def latex_text(text: str) -> str:
    return escape_latex(to_ascii(text))


def seeded_rng_for(prn: str) -> random.Random:
    # Stable seed using PRN (hash to int)
    h = hashlib.sha256(prn.encode("utf-8")).hexdigest()
    seed = int(h[:16], 16)
    return random.Random(seed)


# -----------------------------
# Data loading
# -----------------------------

@dataclass
class Student:
    prn: str
    name: str


def read_students(csv_path: str) -> List[Student]:
    students: List[Student] = []
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Missing students CSV at {csv_path}. Run misc_students.py first.")
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            prn = str(row.get("PRN", "")).strip()
            name = str(row.get("Name", "")).strip()
            if prn:
                students.append(Student(prn=prn, name=name))
    return students


def read_lab_titles(index_path: str) -> Dict[int, str]:
    mapping: Dict[int, str] = {}
    if not os.path.exists(index_path):
        # Fallback mapping if index file missing
        defaults = [
            (0, "Python Warm-up and Submission Guidelines"),
            (1, "Recursive vs Non-Recursive Algorithms"),
            (2, "Merge Sort (Divide and Conquer)"),
            (3, "Binary Search (Iterative & Recursive)"),
            (4, "Greedy Knapsack Problem (Fractional)"),
            (5, "Prim’s Algorithm for Minimum Spanning Tree"),
            (6, "Kruskal’s Algorithm for Minimum Spanning Tree"),
            (7, "Single Source Shortest Path (Multistage Graph)"),
            (8, "All-Pairs Shortest Paths (Multistage Graph)"),
            (9, "Huffman Coding (Greedy Tree Construction)"),
            (10, "Combinatorial Problems (Knapsack / 8 Queens / Flow Shop)"),
        ]
        return dict(defaults)

    with open(index_path, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\s*Lab\s*0*([0-9]+)\s*:\s*(.+)$", line.strip())
            if m:
                # Normalize to ASCII to avoid LaTeX unicode issues later
                mapping[int(m.group(1))] = to_ascii(m.group(2).strip())
    return mapping


# -----------------------------
# Question banks
# -----------------------------

def subjective_questions(lab_num: int, title: str) -> List[str]:
    # Common, concise theory Qs per lab
    common = {
        0: [
            "State two submission guidelines you will strictly follow.",
            "Define an invariant in your own words (1–2 lines).",
            "What is a docstring? Give a short example (≤2 lines).",
        ],
        1: [
            "Define recursion and iteration in 1–2 lines each.",
            "State the base case and inductive step for factorial(n).",
            "Explain stack overflow risk in recursive calls (concise).",
        ],
        2: [
            "Define Divide-and-Conquer. Where does merge sort use it?",
            "State merge sort’s time and space complexity (short).",
            "When does the iterative (bottom-up) variant help?",
        ],
        3: [
            "Define binary search and its precondition (sorted?).",
            "State best/avg/worst-case time in Big-O (one line).",
            "How do bounds change when key < arr[mid]?",
        ],
        4: [
            "Define fractional knapsack and density (value/weight).",
            "Why sorting by ratio is optimal (1–2 lines intuition).",
            "State when item is taken partially (≤1 line).",
        ],
        5: [
            "Define MST and Prim’s choice rule (short).",
            "What is a key[] array used for in Prim’s?",
            "How many edges are in an MST of V vertices?",
        ],
        6: [
            "Define union–find with path compression (concise).",
            "What does union by rank prevent?",
            "Kruskal’s sorting criterion for edges (≤1 line).",
        ],
        7: [
            "Define multistage graph and stages concept.",
            "Why is backward DP used here?",
            "What value is set at the sink initially and why?",
        ],
        8: [
            "Contrast 1-indexed vs 0-indexed DP tables (brief).",
            "What is recorded in the path[] array?",
            "When is an edge considered absent in cost matrix?",
        ],
        9: [
            "Define prefix-free code in 1 line.",
            "Why does Huffman pick two least-frequent nodes?",
            "What determines a symbol’s code length?",
        ],
        10: [
            "State the N-Queens constraint succinctly.",
            "What does is_safe check (3 checks, one phrase)?",
            "How many solutions exist for N=8 (state number only).",
        ],
    }
    return common.get(lab_num, [f"Briefly state two key concepts of: {title}."])


def objective_questions(lab_num: int, rng: random.Random) -> List[str]:
    Q: List[str] = []
    if lab_num == 1:
        n = rng.randint(4, 10)
        Q += [
            f"For factorial({n}), how many multiplications are performed?",
            f"In recursion, how many stack frames exist at peak for n={n}?",
        ]
    elif lab_num == 2:
        n = rng.randrange(8, 33, 2)
        Q += [
            f"For merge sort on n={n}, how many levels of splitting occur?",
            f"At the last merge level, how many subarrays are merged?",
        ]
    elif lab_num == 3:
        n = rng.choice([11, 15, 17, 31])
        idx = rng.randint(0, n - 1)
        Q += [
            f"Sorted array size n={n}. If key is at index {idx}, what is the maximum mid checks in iterative binary search?",
            f"If key absent, what is the worst-case number of mid checks for n={n}?",
        ]
    elif lab_num == 4:
        W = rng.randint(20, 60)
        items = rng.randint(3, 6)
        Q += [
            f"With capacity W={W} and {items} items, which greedy sorting key is used?",
            "When do we take a fractional part of an item (state the condition)?",
        ]
    elif lab_num == 5:
        V = rng.randint(4, 7)
        Q += [
            f"In Prim’s on a connected graph with V={V}, how many edges in MST?",
            "What criterion picks the next vertex (state in ≤1 line)?",
        ]
    elif lab_num == 6:
        e = rng.randint(5, 10)
        Q += [
            f"Kruskal sorts how many edges if E={e}?",
            "Write the stopping condition for Kruskal in terms of edges/vertices.",
        ]
    elif lab_num == 7:
        nodes = rng.randint(6, 10)
        Q += [
            f"In backward DP on a multistage graph with {nodes} nodes, which node’s dist is set to 0 initially?",
            "What is stored in next_node[i] (≤1 line)?",
        ]
    elif lab_num == 8:
        N = rng.randint(6, 10)
        Q += [
            f"For 1→N shortest path with N={N}, what is cost[N] initialized to?",
            "What does path[i] represent (≤1 line)?",
        ]
    elif lab_num == 9:
        unique = rng.randint(3, 6)
        Q += [
            f"For a string with {unique} distinct symbols, what is the range of possible code lengths in Huffman?",
            "Is Huffman code unique for a given frequency table? (Yes/No + 1 line)",
        ]
    elif lab_num == 10:
        N = rng.choice([4, 5, 6, 8])
        Q += [
            f"For N={N}, how many queens are placed per valid solution?",
            "Name the three conflict directions checked before placing a queen (≤1 line).",
        ]
    else:
        Q += ["State two short properties relevant to this lab."]
    return Q


def make_int_array(rng: random.Random, n: int, lo: int, hi: int, distinct: bool = False) -> List[int]:
    if distinct:
        pool = list(range(lo, hi + 1))
        rng.shuffle(pool)
        return pool[:n]
    return [rng.randint(lo, hi) for _ in range(n)]


def code_digest_questions(lab_num: int, rng: random.Random) -> List[str]:
    Q: List[str] = []
    if lab_num == 0:
        a = make_int_array(rng, 5, 1, 9)
        Q += [
            f"Hand-run a Python function sum(arr) on arr={a}. Show running total after each addition.",
            "Write 2 lines of pseudocode to reverse a list in-place.",
        ]
    elif lab_num == 1:
        n = rng.randint(4, 8)
        Q += [
            f"Trace factorial_recursive({n}) showing the call stack (one line per call).",
            f"Compute factorial_iterative({n}) and list intermediate result after each multiplication.",
        ]
    elif lab_num == 2:
        arr = make_int_array(rng, rng.choice([6, 8, 10]), 1, 50)
        Q += [
            f"Run one full merge_sort_recursive on arr={arr}. Write the sequence of merged subarrays.",
            "State the final sorted array.",
        ]
    elif lab_num == 3:
        n = rng.choice([9, 11, 15])
        arr = sorted(make_int_array(rng, n, 1, 60, distinct=True))
        key = rng.choice(arr)
        miss = rng.randint(61, 90)
        Q += [
            f"On arr={arr}, trace binary_search_iterative for key={key}: write low, high, mid at each step.",
            f"Repeat for an absent key={miss} and show termination condition.",
        ]
    elif lab_num == 4:
        items = [(rng.randint(10, 120), rng.randint(5, 30)) for _ in range(rng.randint(3, 5))]
        W = rng.randint(20, 60)
        Q += [
            f"Given items (value,weight)={items} and capacity W={W}, order items by ratio and compute total value taken.",
            "Specify which item (if any) is taken fractionally and by what fraction.",
        ]
    elif lab_num == 5:
        V = rng.randint(4, 6)
        # Build a connected symmetric adjacency matrix with small weights
        graph = [[0] * V for _ in range(V)]
        for i in range(V):
            for j in range(i + 1, V):
                w = rng.randint(1, 9) if rng.random() < 0.7 else 0
                if w == 0:
                    # ensure connectivity by forcing at least a spanning tree structure
                    if i == j - 1:
                        w = rng.randint(1, 9)
                graph[i][j] = graph[j][i] = w
        Q += [
            f"Run Prim’s algorithm starting at vertex 0 on graph={graph}. List edges picked in order with weights.",
            "State the final MST total weight.",
        ]
    elif lab_num == 6:
        V = rng.randint(4, 6)
        E = rng.randint(V, V * (V - 1) // 2)
        edges: List[Tuple[int, int, int]] = []
        used = set()
        while len(edges) < E:
            u, v = rng.sample(range(V), 2)
            if u > v:
                u, v = v, u
            if (u, v) in used:
                continue
            used.add((u, v))
            w = rng.randint(1, 15)
            edges.append((w, u, v))
        Q += [
            f"Apply Kruskal’s to edges (w,u,v)={edges}. Show the sorted order and union steps. Write the resulting MST.",
            "Give the total weight of the MST.",
        ]
    elif lab_num == 7:
        n = rng.randint(6, 8)
        INF = 10 ** 9
        cost = [[INF] * n for _ in range(n)]
        for i in range(n - 1):
            edges_out = rng.randint(1, min(3, n - i - 1))
            targets = rng.sample(range(i + 1, n), edges_out)
            for j in targets:
                cost[i][j] = rng.randint(1, 12)
        cost[n - 1][n - 1] = 0
        Q += [
            f"Using backward DP on cost-matrix (INF={INF}), compute dist[0] and the path from 0→{n-1}. Matrix={cost}.",
            "List dist[i] for all i.",
        ]
    elif lab_num == 8:
        N = rng.randint(6, 9)
        # Build 1-indexed cost matrix encoded as list of triples for brevity
        edges: List[Tuple[int, int, int]] = []
        for i in range(1, N):
            out_deg = rng.randint(1, min(3, N - i))
            targets = rng.sample(range(i + 1, N + 1), out_deg)
            for j in targets:
                edges.append((i, j, rng.randint(1, 9)))
        Q += [
            f"For N={N} and edges (u,v,w)={edges}, compute cost[1] and the 1→N path as in the lab code.",
            "Write cost[i] for i=1..N.",
        ]
    elif lab_num == 9:
        alphabet = rng.sample(list("abcdefg hijklmnopqrstuvwxyz".replace(" ", "")), rng.randint(4, 7))
        # Build a short text using these letters with random frequencies
        text = "".join(rng.choices(alphabet, k=rng.randint(12, 20)))
        Q += [
            f"Build the Huffman tree for text=\"{text}\". Write the code for each character and the encoded length.",
            "Is this encoding optimal given these frequencies? (justify in 1 line)",
        ]
    elif lab_num == 10:
        N = rng.choice([4, 5, 6])
        Q += [
            f"Run the backtracking solver for N={N}. Show one valid board configuration as a 0/1 matrix.",
            "Briefly list the (row,col) placements in order.",
        ]
    else:
        Q += ["Hand-run the core algorithm on a small example of your choice."]
    return Q


# -----------------------------
# LaTeX rendering
# -----------------------------

def latex_preamble(title: str, student: Student) -> str:
        b = "\\"
        lines = []
        lines.append("\\documentclass[11pt]{article}")
        lines.append("\\usepackage[a4paper,margin=0.8in]{geometry}")
        lines.append("\\usepackage[hidelinks]{hyperref}")
        lines.append("\\usepackage{enumitem}")
        lines.append("\\usepackage{titlesec}")
        lines.append("\\usepackage{parskip}")
        lines.append("\\usepackage{xcolor}")
        lines.append("\\usepackage{listings}")
        # listings style (avoid \t sequences by inserting backslash via variable)
        lines.append("\\lstdefinestyle{py}{")
        lines.append("  language=Python,")
        lines.append(f"  basicstyle={b}ttfamily{b}small,")
        lines.append("  keywordstyle=\\color[rgb]{0.0,0.0,0.6}\\bfseries,")
        lines.append("  commentstyle=\\color[rgb]{0.0,0.5,0.0}\\itshape,")
        lines.append("  stringstyle=\\color[rgb]{0.6,0.0,0.0},")
        lines.append("  numbers=left,")
        lines.append(f"  numberstyle={b}tiny\\color{{gray}},")
        lines.append("  stepnumber=1,")
        lines.append("  numbersep=8pt,")
        lines.append("  showstringspaces=false,")
        lines.append("  breaklines=true,")
        lines.append("  frame=single,")
        lines.append("  tabsize=4,")
        lines.append("  keepspaces=true")
        lines.append("}")
        lines.append("\\setlist[itemize]{noitemsep, topsep=2pt}")
        lines.append("\\setlist[enumerate]{noitemsep, topsep=2pt}")
        lines.append(f"{b}title{{{latex_text(title)}}}")
        lines.append(f"{b}author{{PRN: {latex_text(student.prn)}{b}{b}{b}{b}Name: {latex_text(student.name)}}}")
        lines.append(f"{b}date{{}}")
        lines.append(f"{b}begin{{document}}")
        lines.append(f"{b}maketitle")
        lines.append(f"{b}small")
        lines.append(f"{b}textbf{{Instructions}}: {latex_text('Keep answers brief (1-3 lines) unless specified. Focus on thinking, not writing. Your numeric data is personalized; do not copy.')}")
        lines.append("")
        return "\n".join(lines) + "\n"


def latex_lab_section(lab_num: int, title: str, subj: List[str], obj: List[str], code_qs: List[str], source_tuple: Tuple[str, str] | None) -> str:
    lab_title = f"Lab {lab_num:02d}: {title}"
    parts = [f"\\section*{{{latex_text(lab_title)}}}"]
    # Subjective
    parts.append("\\subsection*{Subjective}")
    parts.append(latex_text("Answer in 1-3 lines each."))
    parts.append("\\begin{enumerate}")
    for q in subj:
        parts.append(f"  \\item {latex_text(q)}")
    parts.append("\\end{enumerate}")
    # Objective
    parts.append("\\subsection*{Objective}")
    parts.append(latex_text("Very short answers, often numeric or a phrase."))
    parts.append("\\begin{enumerate}")
    for q in obj:
        parts.append(f"  \\item {latex_text(q)}")
    parts.append("\\end{enumerate}")
    # Source code (if available)
    if source_tuple is not None:
        fname, code = source_tuple
        parts.append("\\subsection*{Source code}")
        parts.append(f"\\noindent\\textit{{{latex_text(fname)}}}")
        parts.append("\\begin{lstlisting}[style=py]")
        parts.append(code)
        parts.append("\\end{lstlisting}")
    # Code digest
    parts.append("\\subsection*{Code Digest}")
    parts.append(latex_text("Hand-run or compute using the lab's source code behavior."))
    parts.append("\\begin{enumerate}")
    for q in code_qs:
        parts.append(f"  \\item {latex_text(q)}")
    parts.append("\\end{enumerate}")
    parts.append("\\vspace{0.5em}")
    parts.append("\\hrule\\vspace{0.5em}")
    return "\n".join(parts) + "\n"


def latex_footer() -> str:
    return "\\end{document}\n"


# -----------------------------
# Generation pipeline
# -----------------------------

def build_writeup_for_student(student: Student, lab_titles: Dict[int, str], compile_pdf: bool) -> Tuple[str, str]:
    rng = seeded_rng_for(student.prn)
    doc_title = "DAA Labs Writeup (Personalized)"
    content = [latex_preamble(doc_title, student)]

    # Labs 00..10
    for lab in range(0, 11):
        title = lab_titles.get(lab, f"Lab {lab:02d}")
        subj = subjective_questions(lab, title)
        obj = objective_questions(lab, rng)
        code_qs = code_digest_questions(lab, rng)
        source = lab_source_tuple(lab)
        content.append(latex_lab_section(lab, title, subj, obj, code_qs, source))

    content.append(latex_footer())
    tex_text = "\n".join(content)

    ensure_dir(OUT_DIR)
    base = f"{student.prn}-{slugify(student.name)}-writeup"
    tex_path = os.path.join(OUT_DIR, base + ".tex")
    pdf_path = os.path.join(OUT_DIR, base + ".pdf")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_text)

    if compile_pdf:
        compile_tex(tex_path, OUT_DIR)

    return tex_path, pdf_path


def lab_source_tuple(lab_num: int) -> Tuple[str, str] | None:
    """Return (filename, code) for the lab, or None if not available."""
    mapping = {
        1: "1.recursion.py",
        2: "2.merge_sort.py",
        3: "3.binary_search.py",
        4: "4.fractional_knapsack.py",
        5: "5.prims.py",
        6: "6.kruskal.py",
        7: "7.multistage_graph.py",
        8: "8.multistage_graph.py",
        9: "9.huffman.py",
        10: "10.eight_queens.py",
    }
    fname = mapping.get(lab_num)
    if not fname:
        return None
    path = os.path.join(LABS_DIR, fname)
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            code = f.read()
        # Ensure ASCII-only for LaTeX engine compatibility, preserving newlines and indentation
        code_clean = sanitize_code_for_latex(code)
        return fname, code_clean
    except Exception:
        return None


def sanitize_code_for_latex(src: str) -> str:
    """Normalize code to ASCII while preserving newlines and reasonable spacing.

    - Map common unicode punctuation to ASCII first
    - Normalize to NFKD and drop non-ASCII
    - Normalize line endings to \n
    - Remove control chars except tab/newline
    - Optionally expand tabs to 4 spaces for consistent rendering
    """
    if not isinstance(src, str):
        src = str(src)
    replacements = {
        "→": "->",
        "←": "<-",
        "↔": "<->",
        "≤": "<=",
        "≥": ">=",
        "≠": "!=",
        "×": "x",
        "·": "-",
        "•": "-",
        "–": "-",
        "—": "-",
        "−": "-",
        "’": "'",
        "‘": "'",
        "“": '"',
        "”": '"',
        " ": " ",
    }
    for k, v in replacements.items():
        src = src.replace(k, v)
    # Keep original newlines; normalize CRLF/CR to LF
    src = src.replace("\r\n", "\n").replace("\r", "\n")
    # Normalize to ASCII; this drops remaining non-ASCII
    src = unicodedata.normalize("NFKD", src).encode("ascii", "ignore").decode("ascii")
    # Remove control characters except tab and newline
    src = "".join(ch for ch in src if ch in ("\n", "\t") or ord(ch) >= 32)
    # Expand tabs to 4 spaces for stable typesetting
    src = src.replace("\t", "    ")
    return src


def compile_tex(tex_path: str, out_dir: str) -> None:
    # Compile with pdflatex twice for TOC/refs stability, ignore if not installed
    cmd = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-output-directory={out_dir}",
        tex_path,
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except FileNotFoundError:
        print("pdflatex not found. Skipping PDF compilation.")
    except subprocess.CalledProcessError as e:
        print("LaTeX compilation failed. See output below:")
        try:
            sys.stdout.write(e.stdout.decode("utf-8", errors="ignore"))
        except Exception:
            pass


def main(argv: List[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Generate personalized lab writeups in LaTeX (and PDFs).")
    p.add_argument("--limit", type=int, default=None, help="Limit number of students processed (for preview).")
    p.add_argument("--only", nargs="*", default=None, help="Only process these PRNs (space-separated).")
    p.add_argument("--compile", action="store_true", help="Compile LaTeX to PDF using pdflatex.")
    args = p.parse_args(argv)

    students = read_students(STUDENTS_CSV)
    if args.only:
        only = set(s.upper() for s in args.only)
        students = [s for s in students if s.prn.upper() in only]
    if args.limit is not None:
        students = students[: args.limit]

    lab_titles = read_lab_titles(LABS_INDEX)

    ensure_dir(OUT_DIR)
    print(f"Generating writeups for {len(students)} student(s) → {OUT_DIR}")

    for i, stu in enumerate(students, 1):
        tex, pdf = build_writeup_for_student(stu, lab_titles, compile_pdf=args.compile)
        status = "PDF" if args.compile and os.path.exists(pdf) else "TEX"
        print(f"[{i:03d}] {stu.prn} {stu.name} → {status}: {os.path.basename(tex)}")

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
