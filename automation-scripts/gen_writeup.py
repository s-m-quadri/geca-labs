#!/usr/bin/env python3
"""
Generate per-student LaTeX writeups with course-specific question banks.

Content lives in ``lib/writeup/providers/<course>.py`` (DAA, DBMS, ...).
See ``courses/<id>.json`` for ``writeup_provider_module`` and ``labs_index``.

Examples:
  python3 automation-scripts/gen_writeup.py --course daa --compile
  python3 automation-scripts/gen_writeup.py --course dbms --limit 2
"""

from __future__ import annotations

import argparse
import hashlib
import os
import random
import re
import sys
from typing import Any, Dict, List, Tuple

from lib.common import Student, cleanup_latex_auxiliary_files_in_directory, compile_tex, read_students
from lib.lab_course import LabCourse, repo_root_from_scripts
from lib.latex_duplex import latex_duplex_even_page_suffix
from lib.writeup import load_writeup_provider
from lib.writeup.context import WriteupContext
from lib.writeup.tex import latex_text, to_ascii

ROOT = os.path.dirname(os.path.abspath(__file__))


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "file"


def seeded_rng_for(prn: str) -> random.Random:
    h = hashlib.sha256(prn.encode("utf-8")).hexdigest()
    seed = int(h[:16], 16)
    return random.Random(seed)


def read_lab_titles(index_path: str) -> Dict[int, str]:
    mapping: Dict[int, str] = {}
    if not os.path.exists(index_path):
        return mapping
    with open(index_path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\s*Lab\s*0*([0-9]+)\s*:\s*(.+)$", line.strip())
            if m:
                mapping[int(m.group(1))] = to_ascii(m.group(2).strip())
    return mapping


def _default_lab_titles(course: LabCourse) -> Dict[int, str]:
    if course.id == "daa":
        return {
            0: "Python Warm-up and Submission Guidelines",
            1: "Recursive vs Non-Recursive Algorithms",
            2: "Merge Sort (Divide and Conquer)",
            3: "Binary Search (Iterative & Recursive)",
            4: "Greedy Knapsack Problem (Fractional)",
            5: "Prim's Algorithm for Minimum Spanning Tree",
            6: "Kruskal's Algorithm for Minimum Spanning Tree",
            7: "Single Source Shortest Path (Multistage Graph)",
            8: "All-Pairs Shortest Paths (Multistage Graph)",
            9: "Huffman Coding (Greedy Tree Construction)",
            10: "Combinatorial Problems (Knapsack / 8 Queens / Flow Shop)",
        }
    return {i: f"Lab {i:02d}" for i in course.lab_numbers()}


def resolve_lab_titles(course: LabCourse) -> Dict[int, str]:
    titles = read_lab_titles(course.labs_index)
    defaults = _default_lab_titles(course)
    for lab in course.lab_numbers():
        titles.setdefault(lab, defaults.get(lab, f"Lab {lab:02d}"))
    return titles


def latex_document_setup(student: Student, course: LabCourse, provider: Any) -> str:
    """Packages, listings, headers, and \\begin{document} plus either a custom cover or default front matter."""
    b = "\\"
    lines: List[str] = []
    lines.append("\\documentclass[11pt]{article}")
    lines.append("\\usepackage[T1]{fontenc}")
    lines.append("\\usepackage[a4paper,margin=0.8in]{geometry}")
    lines.append("\\usepackage[hidelinks]{hyperref}")
    lines.append("\\usepackage{enumitem}")
    lines.append("\\usepackage{titlesec}")
    lines.append("\\usepackage{titling}")
    lines.append("\\usepackage{parskip}")
    lines.append("\\usepackage{xcolor}")
    lines.append("\\usepackage{listings}")
    lines.append("\\usepackage{fancyhdr}")
    lines.append("\\usepackage{url}")
    lines.append("\\usepackage{amsmath}")
    lines.append("\\usepackage{setspace}")
    lines.append("\\usepackage{array}")
    extra_lines = getattr(provider, "latex_extra_usepackage_lines", None)
    if callable(extra_lines):
        for ln in extra_lines():
            lines.append(ln)
    lines.append("\\pagestyle{fancy}")
    lines.append("\\fancyhf{}")
    lines.append("\\definecolor{headercolor}{RGB}{26,26,0}")
    lines.append("\\titleformat{\\section}[hang]{\\color{headercolor}\\Large\\bfseries}{}{0pt}{}")
    lines.append("\\titleformat{\\subsection}[hang]{\\color{headercolor}\\large\\bfseries}{}{0pt}{}")
    prof_title = latex_text(course.writeup_header_subtitle)
    lines.append(f"{b}fancyhead[L]{{{b}color{{headercolor}} {b}small {prof_title}}}")
    lines.append(f"{b}fancyhead[R]{{{b}color{{headercolor}} {b}small {latex_text(student.name)}}}")
    lines.append(f"{b}fancyfoot[L]{{{b}color{{headercolor}} {b}small Manual: {b}url{{{course.writeup_footer_manual_url}}}}}")
    lines.append(f"{b}fancyfoot[C]{{{b}color{{headercolor}} {b}small {b}thepage}}")
    lines.append(f"{b}fancyfoot[R]{{{b}color{{headercolor}} {b}small PRN: {latex_text(student.prn)}}}")
    lang = "SQL" if getattr(provider, "listings_style", "py") == "sql" else "Python"
    lines.append("\\lstdefinestyle{labcode}{")
    lines.append(f"  language={lang},")
    listings_bs = getattr(provider, "listings_basicstyle_latex", None)
    if listings_bs:
        lines.append(f"  basicstyle={{{listings_bs}}},")
    else:
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
    if getattr(provider, "loose_enumerate_layout", False):
        lines.append("\\setlist[enumerate]{itemsep=0.55em, parsep=0.35em, topsep=0.45em}")
    else:
        lines.append("\\setlist[enumerate]{noitemsep, topsep=2pt}")
    lines.append(f"{b}pretitle{{{b}begin{{center}}{b}color{{headercolor}} {b}Huge {b}bfseries}}")
    lines.append(f"{b}posttitle{{{b}par{b}end{{center}}{b}vspace{{-0.3em}}{b}color{{headercolor}} {b}vspace{{0.6em}}}}")
    lines.append(f"{b}title{{{latex_text(course.writeup_document_title)}}}")
    lines.append(f"{b}author{{{latex_text(student.name)} (Enroll: {latex_text(student.prn)})}}")
    lines.append(f"{b}date{{{b}today}}")
    lines.append(f"{b}begin{{document}}")
    cover_fn = getattr(provider, "build_cover_page", None)
    if callable(cover_fn):
        chunk = cover_fn(student, course)
        if chunk:
            lines.append(chunk)
        else:
            lines.append(latex_default_front_matter(student, course, provider))
    else:
        lines.append(latex_default_front_matter(student, course, provider))
    return "\n".join(lines) + "\n"


def latex_default_front_matter(student: Student, course: LabCourse, provider: Any) -> str:
    b = "\\"
    default_instr = (
        "Keep answers clear and your own. Length is up to you unless a question needs detail. "
        "Numeric values are personalized; do not copy another student's numbers."
    )
    instr = getattr(provider, "instruction_blurb", None) or default_instr
    parts = [
        f"{b}maketitle",
        f"{b}small",
        f"{b}hrule",
        f"{b}vspace{{0.5em}}",
        f"{b}textbf{{Instructions}}: {latex_text(instr)}",
        "",
    ]
    return "\n".join(parts) + "\n"


def latex_lab_section(
    lab_num: int,
    title: str,
    subj: List[str],
    obj: List[str],
    code_qs: List[str],
    source_tuple: Tuple[str, str] | None,
    course: LabCourse,
    provider: Any,
    rng: random.Random | None = None,
) -> str:
    lab_title = f"Lab {lab_num:02d}: {title}"
    parts = ["\\clearpage", f"\\section*{{{latex_text(lab_title)}}}"]
    parts.append(f"\\noindent\\textit{{Lab Manual: \\url{{{course.manual_url(lab_num)}}}}}")
    parts.append(f"\\subsection*{{{lab_num}.1: Subjective}}")
    subj_intro_fn = getattr(provider, "subjective_section_intro_tex", None)
    parts.append(
        subj_intro_fn(lab_num)
        if callable(subj_intro_fn)
        else latex_text("Answer each part briefly and clearly.")
    )
    parts.append("\\begin{enumerate}")
    for q in subj:
        parts.append(f"  \\item {latex_text(q)}")
    parts.append("\\end{enumerate}")
    parts.append(f"\\subsection*{{{lab_num}.2: Objective}}")
    obj_intro_fn = getattr(provider, "objective_section_intro_tex", None)
    parts.append(
        obj_intro_fn(lab_num)
        if callable(obj_intro_fn)
        else latex_text("Concise answers are fine; add brief reasoning where it helps.")
    )
    parts.append("\\begin{enumerate}")
    for q in obj:
        if isinstance(q, str) and q.strip().startswith("\\[") and q.strip().endswith("\\]"):
            parts.append("  \\item ")
            parts.append(q)
        else:
            parts.append(f"  \\item {latex_text(q)}")
    parts.append("\\end{enumerate}")
    if source_tuple is not None:
        _fname, code = source_tuple
        subsec = getattr(provider, "source_subsection_title", "Source code")
        kind = getattr(provider, "source_kind_label", "code")
        parts.append(f"\\subsection*{{{latex_text(subsec)}}}")
        list_intro = getattr(provider, "reference_listing_intro_tex", None)
        if callable(list_intro):
            parts.append(list_intro(lab_num, title, _fname))
        else:
            parts.append(
                f"\\noindent\\textit{{{latex_text(title)} -- reference {latex_text(kind)} ({latex_text(_fname)})}}"
            )
        parts.append("\\begin{lstlisting}[style=labcode]")
        parts.append(code)
        parts.append("\\end{lstlisting}")
    digest_label = getattr(provider, "digest_subsection_title", "Code Digest")
    parts.append(f"\\subsection*{{{latex_text(f'{lab_num}.3: {digest_label}')}}}")
    digest_intro_fn = getattr(provider, "code_digest_section_intro_tex", None)
    parts.append(
        digest_intro_fn(lab_num)
        if callable(digest_intro_fn)
        else latex_text(getattr(provider, "digest_instruction", "Hand-run or trace as in the lab."))
    )
    parts.append("\\begin{enumerate}")
    for q in code_qs:
        if isinstance(q, str) and q.strip().startswith("\\[") and q.strip().endswith("\\]"):
            parts.append("  \\item ")
            parts.append(q)
        else:
            parts.append(f"  \\item {latex_text(q)}")
    parts.append("\\end{enumerate}")
    parts.append(f"\\subsection*{{{lab_num}.4: Conclusion}}")
    parts.append(latex_text("Summarize your main takeaways from this lab."))
    parts.append("\\vspace{0.35em}")
    parts.append("\\hrule\\vspace{0.35em}")
    return "\n".join(parts) + "\n"


def latex_footer() -> str:
    return latex_duplex_even_page_suffix() + "\n\\end{document}\n"


def build_writeup_for_student(
    student: Student,
    lab_titles: Dict[int, str],
    compile_pdf: bool,
    course: LabCourse,
    provider: Any,
) -> Tuple[str, str]:
    rng = seeded_rng_for(student.prn)
    ctx = WriteupContext(
        student_prn=student.prn,
        scripts_root=ROOT,
        repo_root=repo_root_from_scripts(),
        course=course,
    )
    content = [latex_document_setup(student, course, provider)]

    skip_labs = getattr(provider, "skip_lab_numbers", frozenset())
    for lab in course.lab_numbers():
        if lab in skip_labs:
            continue
        title = lab_titles.get(lab, f"Lab {lab:02d}")
        subj = provider.subjective_questions(lab, title, rng)
        obj = provider.objective_questions(lab, rng)
        code_qs = provider.code_digest_questions(lab, rng)
        source = provider.lab_source_tuple(lab, ctx)
        content.append(
            latex_lab_section(lab, title, subj, obj, code_qs, source, course, provider, rng)
        )

    appendix_fn = getattr(provider, "build_appendix_tex", None)
    if callable(appendix_fn):
        appendix_chunk = appendix_fn(student, course, rng)
        if appendix_chunk:
            content.append(appendix_chunk)

    content.append(latex_footer())
    tex_text = "\n".join(content)

    out_dir = course.writeups_dir
    ensure_dir(out_dir)
    base = f"{student.prn}-{slugify(student.name)}-writeup"
    tex_path = os.path.join(out_dir, base + ".tex")
    pdf_path = os.path.join(out_dir, base + ".pdf")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_text)

    if compile_pdf:
        compile_tex(tex_path, out_dir)

    return tex_path, pdf_path


def main(argv: List[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Generate personalized lab writeups (LaTeX/PDF).")
    p.add_argument("--course", default="daa", help="Course id (see courses/<id>.json)")
    p.add_argument("--limit", type=int, default=None, help="Limit number of students (preview).")
    p.add_argument("--only", nargs="*", default=None, help="Only these PRNs.")
    p.add_argument("--compile", action="store_true", help="Run pdflatex.")
    args = p.parse_args(argv)

    course = LabCourse.load(args.course, root=ROOT)
    if not course.features_writeup:
        print(
            f"Writeups disabled for {course.id!r}. Set features.writeup in courses/{course.id}.json.",
            file=sys.stderr,
        )
        return 2

    provider = load_writeup_provider(course)
    students = read_students(course.students_csv)
    if args.only:
        only = {s.upper() for s in args.only}
        students = [s for s in students if s.prn.upper() in only]
    if args.limit is not None:
        students = students[: args.limit]

    lab_titles = resolve_lab_titles(course)
    ensure_dir(course.writeups_dir)
    print(f"Generating writeups ({course.id}) for {len(students)} student(s) → {course.writeups_dir}")

    for i, stu in enumerate(students, 1):
        tex, pdf = build_writeup_for_student(stu, lab_titles, args.compile, course, provider)
        status = "PDF" if args.compile and os.path.exists(pdf) else "TEX"
        print(f"[{i:03d}] {stu.prn} {stu.name} → {status}: {os.path.basename(tex)}")

    if args.compile:
        cleanup_latex_auxiliary_files_in_directory(course.writeups_dir)

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
