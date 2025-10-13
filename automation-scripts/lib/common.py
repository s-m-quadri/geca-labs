#!/usr/bin/env python3
"""Common utilities shared across automation scripts.

Includes:
- File I/O helpers
- Slugify
- Lab title/link helpers
- Students CSV reader
- LaTeX helpers and compile
"""
from __future__ import annotations

import os
import re
import subprocess
import unicodedata
import csv
from dataclasses import dataclass
from typing import Dict, List, Optional

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
STUDENTS_CSV = os.path.join(ROOT, "output", "students.csv")
LABS_INDEX = os.path.join(ROOT, "labs", "index.md")


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def slugify(text: str) -> str:
    text = str(text or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "file"


def to_ascii(text: str) -> str:
    if text is None:
        return ""
    if not isinstance(text, str):
        text = str(text)
    replacements = {
        "→": "->", "←": "<-", "↔": "<->",
        "≤": "<=", "≥": ">=", "≠": "!=",
        "×": "x", "·": "-", "•": "-",
        "–": "-", "—": "-", "−": "-",
        "’": "'", "‘": "'", "“": '"', "”": '"',
        "\u00a0": " ",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def escape_latex(text: str) -> str:
    if text is None:
        return ""
    if not isinstance(text, str):
        text = str(text)
    text = to_ascii(text)
    repl = {
        "\\": r"\\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\\textasciitilde{}",
        "^": r"\\textasciicircum{}",
    }
    for k, v in repl.items():
        text = text.replace(k, v)
    return text


def latex_manual_url(lab_num: int) -> str:
    return f"https://s-m-quadri.me/geca/daa/{lab_num:02d}"


def lab_titles_default() -> Dict[int, str]:
    return {
        0: "Python Warm-up and Submission Guidelines",
        1: "Recursive vs Non-Recursive Algorithms",
        2: "Merge Sort (Divide and Conquer)",
        3: "Binary Search (Iterative & Recursive)",
        4: "Greedy Knapsack Problem (Fractional)",
        5: "Prim’s Algorithm for Minimum Spanning Tree",
        6: "Kruskal’s Algorithm for Minimum Spanning Tree",
        7: "Single Source Shortest Path (Multistage Graph)",
        8: "All-Pairs Shortest Paths (Multistage Graph)",
        9: "Huffman Coding (Greedy Tree Construction)",
        10: "Combinatorial Problems (Knapsack / 8 Queens / Flow Shop)",
    }


@dataclass
class Student:
    prn: str
    name: str


def read_students(csv_path: Optional[str] = None) -> List[Student]:
    path = csv_path or STUDENTS_CSV
    students: List[Student] = []
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing students CSV at {path}")
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            prn = str(row.get("PRN", "")).strip()
            name = str(row.get("Name", "")).strip()
            if prn:
                students.append(Student(prn=prn, name=name))
    return students


def compile_tex(tex_path: str, out_dir: Optional[str] = None) -> None:
    out_dir = out_dir or os.path.dirname(tex_path)
    cmd = [
        "pdflatex", "-interaction=nonstopmode", "-halt-on-error",
        f"-output-directory={out_dir}", tex_path,
    ]
    # Run twice for stable references
    for _ in range(2):
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except FileNotFoundError:
            print("pdflatex not found. Skipping PDF compilation.")
            return
        except subprocess.CalledProcessError as e:
            # Surface TeX output for debugging
            try:
                print(e.stdout.decode("utf-8", errors="ignore"))
            except Exception:
                pass
            raise
