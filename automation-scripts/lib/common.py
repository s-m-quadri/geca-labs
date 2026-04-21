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
from typing import Dict, List, Optional, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env_file(path: str) -> None:
    """Load ``KEY=value`` pairs from ``path`` into ``os.environ`` without extra deps.

    Does not override variables already set in the environment (same idea as dotenv).
    Supports optional single- or double-quoted values.
    """
    if not path or not os.path.isfile(path):
        return
    try:
        with open(path, encoding="utf-8") as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, _, rest = line.partition("=")
                key = key.strip()
                if not key or key in os.environ:
                    continue
                val = rest.strip()
                if len(val) >= 2 and ((val[0] == val[-1] == '"') or (val[0] == val[-1] == "'")):
                    val = val[1:-1]
                os.environ[key] = val
    except OSError:
        pass


# PRN prefixes treated as Direct Second Year (DSY) — listed last in rosters and reports.
DSY_PRN_PREFIXES: Tuple[str, ...] = ("BT25S05F",)


def is_dsy_prn(prn: str) -> bool:
    u = (prn or "").strip().upper()
    return any(u.startswith(pref) for pref in DSY_PRN_PREFIXES)


def student_sort_key(prn: str) -> Tuple[int, str]:
    """Sort key: non-DSY first (0), DSY last (1); then PRN alphabetically."""
    u = (prn or "").strip().upper()
    return (1 if is_dsy_prn(u) else 0, u)

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


# Lines like ``1 BT24F05F001 ABHYANKAR RAGHAV DHANANJAY`` in a plain-text roll export.
_ROLLS_LINE_RE = re.compile(r"^\s*\d+\s+(BT\d+[FS]\d+F\d{3})\s+(.+)$", re.MULTILINE)


def parse_students_from_rolls_raw_text(text: str) -> List[Student]:
    """Extract PRN/name pairs from pasted college roll text.

    Ordering is normalized by :func:`student_sort_key`: regular second-year (SY) cohort
    first, direct second-year (DSY) last (see :data:`DSY_PRN_PREFIXES`), then by PRN.
    """
    out: Dict[str, str] = {}
    for m in _ROLLS_LINE_RE.finditer(text or ""):
        prn = m.group(1).strip().upper()
        name = re.sub(r"\s+", " ", m.group(2).strip())
        if prn and name:
            out[prn] = name
    students = [Student(prn=k, name=v) for k, v in out.items()]
    students.sort(key=lambda s: student_sort_key(s.prn))
    return students


def parse_students_from_rolls_raw_path(path: str) -> List[Student]:
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    with open(path, encoding="utf-8") as f:
        return parse_students_from_rolls_raw_text(f.read())


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
    students.sort(key=lambda s: student_sort_key(s.prn))
    return students


# Removed after successful pdflatex so output dirs keep only .tex and .pdf.
_LATEX_ARTIFACT_SUFFIXES: Tuple[str, ...] = (
    ".aux",
    ".log",
    ".out",
    ".toc",
    ".nav",
    ".snm",
    ".vrb",
    ".fls",
    ".fdb_latexmk",
    ".synctex.gz",
    ".bbl",
    ".blg",
    ".bcf",
    ".run.xml",
    ".xdv",
)


def _cleanup_latex_artifacts(out_dir: str, stem: str) -> None:
    for suf in _LATEX_ARTIFACT_SUFFIXES:
        path = os.path.join(out_dir, stem + suf)
        try:
            os.remove(path)
        except OSError:
            pass


def cleanup_latex_auxiliary_files_in_directory(out_dir: str) -> None:
    """Drop pdflatex sidecars in ``out_dir`` so only ``.tex`` / ``.pdf`` (and similar sources) remain.

    Intended for folders like ``output/<course>/writeups`` after builds; skips non-regular files.
    """
    if not os.path.isdir(out_dir):
        return
    artifacts = set(_LATEX_ARTIFACT_SUFFIXES)
    for fname in os.listdir(out_dir):
        path = os.path.join(out_dir, fname)
        if not os.path.isfile(path):
            continue
        low = fname.lower()
        if low.endswith(".tex") or low.endswith(".pdf"):
            continue
        hit = False
        for suf in artifacts:
            if low.endswith(suf.lower()):
                hit = True
                break
        if hit:
            try:
                os.remove(path)
            except OSError:
                pass


def compile_tex(tex_path: str, out_dir: Optional[str] = None) -> None:
    out_dir = out_dir or os.path.dirname(tex_path)
    stem = os.path.splitext(os.path.basename(tex_path))[0]
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
    _cleanup_latex_artifacts(out_dir, stem)
