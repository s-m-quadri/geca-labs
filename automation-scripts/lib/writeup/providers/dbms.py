"""DBMS writeup question banks (aligned with https://s-m-quadri.me/geca/dbms manuals)."""

from __future__ import annotations

import hashlib
import os
import random
from typing import Dict, List, Sequence, Tuple

from lib.common import Student
from lib.lab_course import LabCourse
from lib.writeup.context import WriteupContext
from lib.writeup.source import excerpt_sql_for_writeup
from lib.writeup.tex import latex_text

# Preferred SQL files per lab (first match under the student's lab folder wins).
_SQL_PICK_ORDER: Dict[int, Sequence[str]] = {
    0: ("setup.sql", "tables.sql", "queries.sql", "01_create_database.sql", "02_create_table.sql"),
    1: ("02_create_table.sql", "01_create_database.sql", "03_insert_data.sql", "04_add_columns.sql"),
    2: ("01_setup.sql", "04_select_all.sql", "05_select_where.sql", "07_update_one.sql"),
    3: ("01_setup.sql", "02_count_sum.sql", "03_string_funcs.sql", "10_check_status.sql"),
    4: ("01_setup.sql", "03_inner_join.sql", "04_left_join.sql", "10_check_status.sql"),
    5: ("01_setup.sql", "02_user_vars_arithmetic.sql", "04_proc_apply_rate.sql", "10_check_status.sql"),
    6: ("01_setup.sql", "02_create_view.sql", "04_subquery_scalar.sql", "12_check_status.sql"),
    7: (
        "02_integration.sql",
        "review.sql",
        "01_setup.sql",
        "schema.sql",
        "02_ddl.sql",
        "02_transaction.sql",
        "02_index.sql",
        "03_explain.sql",
        "10_check_status.sql",
    ),
}

# Fictional campus library schema shared across appendix and cross-references (ASCII names).
_APPENDIX_DEPARTMENTS: Tuple[Tuple[str, str], ...] = (
    ("CS", "Computer Science"),
    ("EE", "Electrical Engineering"),
    ("ME", "Mechanical Engineering"),
    ("CE", "Civil Engineering"),
    ("ASH", "Applied Sciences and Humanities"),
    ("MBA", "Business Administration"),
)

# member_id, dept_id, joined_year — full_name is filled per student (PRN-seeded Western-style names).
_APPENDIX_MEMBER_ROWS_BASE: Tuple[Tuple[str, str, int], ...] = (
    ("M001", "CS", 2024),
    ("M002", "CS", 2024),
    ("M003", "EE", 2024),
    ("M004", "CS", 2024),
    ("M005", "ME", 2023),
    ("M006", "CE", 2024),
    ("M007", "CS", 2024),
    ("M008", "EE", 2023),
    ("M009", "ME", 2024),
    ("M010", "MBA", 2024),
    ("M011", "CS", 2023),
    ("M012", "ASH", 2024),
    ("M013", "CS", 2024),
)

# Distinct synthetic names (ASCII); each student receives a PRN-specific assignment into M001..M013.
_WESTERN_FULL_NAMES: Tuple[str, ...] = (
    "James Miller",
    "Emily Chen",
    "Michael O'Brien",
    "Sarah Johnson",
    "David Walsh",
    "Emma Thompson",
    "Daniel Foster",
    "Olivia Harper",
    "Matthew Reed",
    "Sophia Bennett",
    "Andrew Hayes",
    "Grace Sullivan",
    "Ryan Cooper",
    "Chloe Anderson",
    "Nathan Brooks",
    "Hannah Mitchell",
    "Ethan Parker",
    "Madison Kelly",
    "Jacob Turner",
    "Abigail Ross",
    "William Hughes",
    "Elizabeth Ward",
    "Benjamin Price",
    "Victoria Long",
    "Samuel Butler",
    "Lillian Simmons",
    "Christopher Perry",
    "Natalie Powell",
    "Jonathan Russell",
    "Avery Patterson",
    "Alexander Jenkins",
    "Ella Henderson",
    "Tyler Coleman",
    "Scarlett Bryant",
    "Brandon Griffin",
    "Aria Hayes",
    "Justin West",
    "Penelope Stone",
    "Kevin Brooks",
    "Layla Ford",
    "Timothy Murray",
    "Zoey Gordon",
    "Eric Wallace",
    "Stella Shaw",
    "Adam Crawford",
    "Violet Spencer",
    "Stephen Gardner",
    "Claire Elliott",
    "Patrick Daniels",
    "Skylar Porter",
    "Sean Reynolds",
    "Lucy Gibson",
    "Kenneth Hunt",
    "Paisley Daniels",
    "Raymond Boyd",
    "Anna Morrison",
    "Gregory Mills",
    "Caroline Warren",
    "Peter Lawson",
    "Kennedy Barrett",
    "Dennis Pierce",
    "Savannah Cole",
    "Gerald Wheeler",
    "Brooklyn Silva",
    "Keith Arnold",
    "Allison Ramsey",
    "Ralph Fowler",
    "Maya Chandler",
    "Lawrence Day",
    "Autumn Powers",
    "Wayne Schultz",
    "Katherine Guzman",
    "Russell Bowen",
    "Alexis Figueroa",
    "Bruce Zimmerman",
    "Jasmine Ingram",
    "Joel Christensen",
    "Melanie Larson",
    "Leonard Moss",
    "Gabriella Sharp",
)


def _personalized_appendix_members(prn: str) -> Tuple[Tuple[str, str, str, int], ...]:
    """Stable pseudo-random Western-style names per PRN; keeps ids, departments, and years fixed for graded prompts."""
    seed = int(hashlib.sha256(prn.strip().upper().encode("utf-8")).hexdigest()[:16], 16)
    rng = random.Random(seed)
    pool = list(_WESTERN_FULL_NAMES)
    rng.shuffle(pool)
    n = len(_APPENDIX_MEMBER_ROWS_BASE)
    if len(pool) < n:
        raise RuntimeError("Western name pool smaller than appendix member rows")
    chosen = pool[:n]
    return tuple(
        (mid, name, dept, year)
        for (mid, dept, year), name in zip(_APPENDIX_MEMBER_ROWS_BASE, chosen)
    )

_APPENDIX_BOOKS: Tuple[Tuple[str, str, int], ...] = (
    ("B101", "Database Systems Concepts", 4),
    ("B102", "Operating Systems Internals", 3),
    ("B103", "Circuits and Networks", 5),
    ("B104", "Structural Analysis", 2),
    ("B105", "Linear Algebra", 6),
    ("B106", "Professional Communication", 8),
    ("B107", "Data Structures in Practice", 4),
    ("B108", "Thermodynamics", 3),
    ("B109", "Project Management Basics", 5),
    ("B110", "Discrete Mathematics", 7),
)

_APPENDIX_LOANS: Tuple[Tuple[str, str, str, str, str], ...] = (
    ("L5001", "M001", "B101", "2025-01-10", "2025-02-10"),
    ("L5002", "M002", "B107", "2025-01-11", "2025-02-11"),
    ("L5003", "M003", "B103", "2025-01-12", "2025-02-12"),
    ("L5004", "M004", "B101", "2025-01-13", "2025-02-13"),
    ("L5005", "M005", "B108", "2025-01-14", "2025-02-14"),
    ("L5006", "M006", "B104", "2025-01-15", "2025-02-15"),
    ("L5007", "M007", "B105", "2025-01-16", "2025-02-16"),
    ("L5008", "M008", "B103", "2025-01-17", "2025-02-17"),
    ("L5009", "M009", "B108", "2025-01-18", "2025-02-18"),
    ("L5010", "M010", "B109", "2025-01-19", "2025-02-19"),
    ("L5011", "M011", "B101", "2025-01-20", "2025-02-20"),
    ("L5012", "M012", "B106", "2025-01-21", "2025-02-21"),
    ("L5013", "M001", "B107", "2025-02-01", "2025-03-03"),
    ("L5014", "M004", "B110", "2025-02-02", "2025-03-04"),
    ("L5015", "M007", "B101", "2025-02-03", "2025-03-05"),
)


def _lt_row_two(a: str, b: str) -> str:
    return f"{latex_text(a)} & {latex_text(b)} \\\\"


def _lt_row_four(a: str, b: str, c: str, d: str) -> str:
    return f"{latex_text(a)} & {latex_text(b)} & {latex_text(c)} & {latex_text(d)} \\\\"


def _lt_row_five(a: str, b: str, c: str, d: str, e: str) -> str:
    return f"{latex_text(a)} & {latex_text(b)} & {latex_text(c)} & {latex_text(d)} & {latex_text(e)} \\\\"


class DbmsWriteupProvider:
    listings_style = "sql"
    listings_basicstyle_latex = r"\footnotesize\ttfamily"
    source_kind_label = "SQL"
    source_subsection_title = "Reference SQL (your repo)"
    digest_subsection_title = "Query Digest"
    skip_lab_numbers = frozenset({0})

    digest_instruction = (
        "Answer using plain reasoning or short calculations. When a question names columns or values that appear in "
        "Appendix A, use those relations as the single source of truth."
    )

    instruction_blurb = (
        "Prompts and numeric details are personalized. Answer in your own words; aim for clarity rather than a fixed length."
    )

    def __init__(self, course: LabCourse) -> None:
        self._course = course

    def latex_extra_usepackage_lines(self) -> List[str]:
        return ["\\usepackage{booktabs}", "\\usepackage{longtable}"]

    def build_appendix_tex(self, student: Student, course: LabCourse, rng: random.Random) -> str:
        """Appendix relations (fictional): member full names vary by PRN; ids and facts stay aligned with prompts."""
        del course, rng
        intro = latex_text(
            "This appendix lists fictional relations used in several query-digest questions. "
            "Primary keys match the column lists below. Dates use ISO format (YYYY-MM-DD). "
            "Member full names in your copy are synthetic and unique to your enrollment number; member ids and departments stay as printed. "
            "These relations are for written practice only and are separate from your graded submission files."
        )
        dept_rows = "\n".join(_lt_row_two(a, b) for a, b in _APPENDIX_DEPARTMENTS)
        members = _personalized_appendix_members(student.prn)
        mem_rows = "\n".join(_lt_row_four(m, n, d, str(y)) for m, n, d, y in members)
        book_rows_fixed = "\n".join(
            f"{latex_text(b)} & {latex_text(t)} & {latex_text(str(c))} \\\\" for b, t, c in _APPENDIX_BOOKS
        )
        loan_rows = "\n".join(_lt_row_five(*row) for row in _APPENDIX_LOANS)

        parts = [
            r"\clearpage",
            r"\appendix",
            r"\section*{Appendix A: Reference database for practice questions}",
            r"\noindent ",
            intro,
            r"\par\vspace{0.65em}",
            r"\subsection*{A.1 Department and member}",
            r"\noindent\textit{department: dept\_id, dept\_name. member: member\_id, full\_name, dept\_id, joined\_year.}",
            r"\par\vspace{0.45em}",
            r"{\footnotesize\setlength{\tabcolsep}{6pt}",
            r"\begin{longtable}{@{}ll@{}}",
            r"\toprule",
            r"\textbf{dept\_id} & \textbf{dept\_name} \\",
            r"\midrule",
            dept_rows,
            r"\bottomrule",
            r"\end{longtable}",
            r"}",
            r"\vspace{0.85em}",
            r"{\footnotesize\setlength{\tabcolsep}{5pt}",
            r"\begin{longtable}{@{}lllr@{}}",
            r"\toprule",
            r"\textbf{member\_id} & \textbf{full\_name} & \textbf{dept\_id} & \textbf{joined\_year} \\",
            r"\midrule",
            mem_rows,
            r"\bottomrule",
            r"\end{longtable}",
            r"}",
            r"\clearpage",
            r"\subsection*{A.2 Book and loan}",
            r"\noindent\textit{book: book\_id, title, copies\_owned. loan: loan\_id, member\_id, book\_id, loan\_date, due\_date.}",
            r"\par\vspace{0.45em}",
            r"{\footnotesize\setlength{\tabcolsep}{6pt}",
            r"\begin{longtable}{@{}llr@{}}",
            r"\toprule",
            r"\textbf{book\_id} & \textbf{title} & \textbf{copies\_owned} \\",
            r"\midrule",
            book_rows_fixed,
            r"\bottomrule",
            r"\end{longtable}",
            r"}",
            r"\vspace{0.85em}",
            r"{\footnotesize\setlength{\tabcolsep}{4pt}",
            r"\begin{longtable}{@{}lllll@{}}",
            r"\toprule",
            r"\textbf{loan\_id} & \textbf{member\_id} & \textbf{book\_id} & \textbf{loan\_date} & \textbf{due\_date} \\",
            r"\midrule",
            loan_rows,
            r"\bottomrule",
            r"\end{longtable}",
            r"}",
            "",
        ]
        return "\n".join(parts)

    def reference_listing_intro_tex(self, lab_num: int, title: str, fname: str) -> str:
        del lab_num, title
        return (
            r"\noindent\textit{"
            + latex_text(
                f"A minimal excerpt from problem set file {fname}."
            )
            + "}"
        )

    def build_cover_page(self, student: Student, course: LabCourse) -> str:
        manual = course.homepage_url.rstrip("/")
        name = latex_text(student.name)
        prn = latex_text(student.prn)
        lines = [
            r"\setstretch{1.05}",
            r"\thispagestyle{empty}",
            r"\null\vfill",
            r"\begin{center}",
            r"{\LARGE\bfseries " + latex_text("Database Management Systems") + r"}\\[0.45em]",
            r"{\Large " + latex_text("Laboratory Write-up") + r"}\\[1em]",
            r"\rule{0.75\textwidth}{0.45pt}\\[1.2em]",
            rf"{{\normalsize \textbf{{Student:}} {name} \\[0.35em]",
            rf"\textbf{{Enrollment (PRN):}} {prn} }}\\[1.8em]",
            r"\begin{minipage}{0.86\textwidth}",
            r"\raggedright\setstretch{1.18}",
            r"\textbf{" + latex_text("How to use this PDF") + r"}\\[0.5em]",
            latex_text(
                "This document is for written answers only. Objectives, rubrics, problem sets, and submission workflow "
                "are on the course manual site, not reproduced here. "
                "Numbered write-up sections begin at Laboratory 1; Laboratory 0 is manual-only. "
                "Appendix A lists practice relations some questions refer to."
            )
            + r"\\[0.85em]",
            r"\textbf{" + latex_text("Course manual (web)") + r"}\\[0.45em]",
            latex_text("The index and navigation hub is")
            + " "
            + r"\url{" + manual + "}"
            + ". "
            + latex_text("From there you open")
            + " "
            + r"\url{" + manual + "/00}"
            + " "
            + latex_text("(basics and environment),")
            + " "
            + r"\url{" + manual + "/01}"
            + " "
            + latex_text("through")
            + " "
            + r"\url{" + manual + "/06}"
            + " "
            + latex_text("for weekly labs,")
            + " "
            + r"\url{" + manual + "/07}"
            + " "
            + latex_text("for the homework mini project, plus")
            + " "
            + r"\url{" + manual + "/cheatsheet}"
            + " "
            + latex_text("and")
            + " "
            + r"\url{" + manual + "/quiz}"
            + latex_text(".")
            + r"\\[0.85em]",
            r"\textbf{" + latex_text("Repository and Codespaces") + r"}\\[0.45em]",
            latex_text("Hands-on work uses")
            + " "
            + r"\url{https://github.com/s-m-quadri/geca-labs}"
            + latex_text(", with one orphan branch per lab (")
            + r"\texttt{lab-dbms-00} "
            + latex_text("through")
            + r" \texttt{lab-dbms-07}"
            + latex_text("). Students normally start from the manual in")
            + r" \textbf{GitHub Codespaces}"
            + latex_text(", which builds the environment defined in the repo (for example the")
            + r" \texttt{.devcontainer} "
            + latex_text(
                "configuration and related setup). What is installed on which branch is documented there and on the "
                "manual, not in this write-up."
            )
            + r"\\[1em]",
            r"\fbox{\begin{minipage}{0.88\textwidth}\small\raggedright ",
            r"\textbf{" + latex_text("Laboratory 0.") + r"} ",
            latex_text(
                "Laboratory 0 covers tools and connectivity only. It does not appear again in the numbered sections. "
                "Formal answers begin at Laboratory 1."
            ),
            r"\\[0.45em]",
            r"\textit{",
            latex_text(
                "If you print the write-up for submission, start from Laboratory 1. "
                "You may omit this cover sheet from the printout."
            ),
            r"}\end{minipage}}",
            r"\end{minipage}",
            r"\end{center}",
            r"\vfill\null",
            r"\clearpage",
            r"\setstretch{1.12}",
            r"\pagestyle{fancy}",
            "",
        ]
        return "\n".join(lines)

    def subjective_section_intro_tex(self, lab_num: int) -> str:
        if lab_num == 7:
            return latex_text(
                "This laboratory has more prompts than earlier weeks. Work through each one; organize your answer "
                "however makes sense to you."
            )
        return latex_text("Answer each part briefly and clearly.")

    def objective_section_intro_tex(self, lab_num: int) -> str:
        if lab_num == 7:
            return latex_text(
                "Where a number or short label is enough, keep it concise; add reasoning when the question calls for it."
            )
        return latex_text("Concise answers are fine; add brief reasoning where it helps.")

    def code_digest_section_intro_tex(self, lab_num: int) -> str:
        if lab_num == 7:
            return latex_text(
                "These items revisit the appendix and ideas from across the course. Reason on paper; use more space if a "
                "question needs it."
            )
        return latex_text(self.digest_instruction)

    def subjective_questions(self, lab_num: int, title: str, rng: random.Random | None = None) -> List[str]:
        bank = {
            1: [
                "Explain what DDL does and what DML does, and briefly contrast them.",
                "Explain how a primary key differs from a unique constraint. Give one situation where they behave differently.",
                "Explain what a foreign key is meant to enforce between two tables.",
                "Explain when altering a table is preferable to dropping it and creating it again.",
            ],
            2: [
                "Briefly explain INSERT, UPDATE, and DELETE in terms of what each does to stored rows.",
                "Explain why WHERE matters on UPDATE and DELETE statements.",
                "Explain what goes wrong if someone runs DELETE without a WHERE clause on production data.",
                "Explain whether ORDER BY changes how rows are stored on disk.",
            ],
            3: [
                "Name two aggregate functions and explain when GROUP BY becomes required.",
                "Explain how WHERE differs from HAVING when aggregates are involved.",
                "Explain why mixing plain columns with SUM(...) in SELECT can produce errors or misleading results.",
                "Name one string function and one numeric function you used in the laboratory session.",
            ],
            4: [
                "Explain how an inner join differs from a left outer join when some rows do not match.",
                "Give one join condition that compares two columns with an equality test.",
                "Explain why a join can return more rows than either input table.",
                "Give one example where joining a table to itself is useful.",
            ],
            5: [
                "Explain how a stored function differs from a stored procedure for your chosen database system.",
                "Explain why dollar quoting is used around some procedural SQL bodies in PostgreSQL.",
                "Explain one task that procedural SQL handles well compared with a single SELECT.",
                "Explain why CASE expressions are portable across vendors compared with vendor-specific IF helpers.",
            ],
            6: [
                "Explain what problem a view solves for someone reading your queries later.",
                "Explain when you would prefer EXISTS instead of IN for a subquery.",
                "Explain what makes a subquery correlated with an outer query.",
                "Explain why placing a derived table in FROM can reduce repeated code.",
            ],
            7: [
                "Explain third normal form in language a classmate could follow.",
                "Explain what must appear on every relationship line in an entity-relationship diagram.",
                "Explain how you would choose the primary key for an enrollment bridge between students and courses.",
                "Explain one trade-off between normalized tables and fewer, wider tables.",
                "List the four ACID properties and outline what each one is about.",
                "Explain what BEGIN and COMMIT group together for the database.",
                "Name a concurrency concern that transaction isolation is meant to address.",
                "Explain why READ COMMITTED can give different results from REPEATABLE READ within one transaction.",
                "Explain what a B-tree style index helps you do faster on large tables.",
                "Explain why adding indexes can slow down some INSERT or UPDATE operations.",
                "Explain what EXPLAIN shows that running SELECT alone does not.",
                "Explain why the planner might still choose a sequential scan on a small table.",
                "Explain how DDL, queries, views, and routines fit together in one application.",
                "Describe a lesson you take away from combining several weeks of database work.",
                "What would you include in a README so another student can run your scripts and understand the schema?",
            ],
        }
        items = list(bank.get(lab_num, [f"Summarize two main ideas from {title}."]))
        if rng is not None and items:
            if lab_num == 7:
                k = min(9, len(items))
                items = rng.sample(items, k)
            elif len(items) >= 4:
                items = rng.sample(items, 3)
            else:
                rng.shuffle(items)
        return items

    def objective_questions(self, lab_num: int, rng: random.Random) -> List[str]:
        Q: List[str] = []
        if lab_num == 1:
            cols = rng.randint(3, 8)
            Q += [
                (
                    f"A CREATE TABLE statement lists {cols} columns and declares one PRIMARY KEY. "
                    "What is the smallest number of columns the primary key can use?"
                ),
                (
                    "Write one CHECK constraint that rejects negative prices (you may show just the predicate)."
                ),
            ]
        elif lab_num == 2:
            n = rng.randint(10, 99)
            Q += [
                (
                    f"A DELETE reports {n} rows removed, but the WHERE clause could have matched more rows. "
                    "What usually explains that outcome?"
                ),
                (
                    f"An UPDATE multiplies salary by {rng.choice([1.05, 1.1, 1.2])} for every row that matches. "
                    "Does the database update rows one at a time or as a set?"
                ),
            ]
        elif lab_num == 3:
            k = rng.randint(5, 20)
            Q += [
                (
                    f"A table holds {k} rows. A WHERE clause removes half of them. "
                    "What COUNT(*) should you expect before any GROUP BY?"
                ),
                (
                    "You group by dept_id and select SUM(salary). "
                    "May you also select emp_name without wrapping it in an aggregate? Explain briefly, including the SQL rule you use."
                ),
            ]
        elif lab_num == 4:
            a, b = rng.randint(8, 40), rng.randint(8, 40)
            Q += [
                (
                    f"Table R has {a} rows and table S has {b} rows. "
                    "What is the largest possible number of rows from an inner join if every combination is allowed?"
                ),
                ("In a left join from R to S, which input relation keeps unmatched rows in the result?"),
            ]
        elif lab_num == 5:
            p = rng.randint(10, 30)
            Q += [
                (
                    f"A function apply_rate(base, {p}) scales the base value by a percent parameter. "
                    "Does it normally return a single scalar value?"
                ),
                (
                    "You call a routine that updates rows in place. "
                    "Should you normally use CALL or SELECT for that routine in PostgreSQL-style SQL?"
                ),
            ]
        elif lab_num == 6:
            v = rng.randint(2, 9)
            Q += [
                (
                    f"A view definition mentions {v} underlying relations. "
                    "Is that view materialized by default in PostgreSQL?"
                ),
                ("Does EXISTS (SELECT 1 ...) stop searching after the first match? Explain briefly."),
            ]
        elif lab_num == 7:
            f = rng.randint(2, 5)
            idx = rng.randint(1, 4)
            candidates = [
                (
                    f"You see {f} repeating groups inside one wide row. "
                    "Which normal form is violated first?"
                ),
                (
                    "You model students and courses as many-to-many. "
                    "Which columns typically belong in the composite primary key of the bridge table?"
                ),
                (
                    "Transaction T1 reads a row, transaction T2 updates that row, and T1 reads it again with a different "
                    "value. What is the usual name for that behaviour?"
                ),
                ("After COMMIT, are the changes normally visible to other sessions under typical default isolation?"),
                (
                    f"You define {idx} secondary indexes on one PostgreSQL table. "
                    "How many clustered indexes does PostgreSQL normally keep per table?"
                ),
                ("For a table with very few rows, why might the planner prefer a sequential scan?"),
                (f"List {rng.randint(2, 4)} kinds of artefacts you would ship besides raw .sql files for a database project."),
                ("Why do teams keep numbered migration scripts instead of relying on a single final CREATE script?"),
            ]
            Q += rng.sample(candidates, 7)
        else:
            Q += ["Give two clear conclusions from this laboratory session."]
        return Q

    def code_digest_questions(self, lab_num: int, rng: random.Random) -> List[str]:
        Q: List[str] = []
        ap = "Appendix A"
        if lab_num == 1:
            t = rng.choice(["book", "loan", "member"])
            Q += [
                (
                    f"Design a CREATE TABLE statement for relation {t} that includes a primary key and at least one "
                    "NOT NULL column. List column names and types in words; you do not need full vendor syntax."
                ),
                (
                    "You add a nullable TEXT column to an existing table that already holds rows. "
                    "What value appears in that column for old rows?"
                ),
            ]
        elif lab_num == 2:
            bal = rng.randint(100, 900)
            delta = rng.randint(10, 80)
            Q += [
                (
                    f"In {ap}, suppose book B101 had copies_owned equal to {bal}. "
                    f"You subtract {delta} copies for a lost item update. "
                    "What new copies_owned value appears before any other transaction runs?"
                ),
                (
                    "You run INSERT ... SELECT ... and the SELECT returns six rows. "
                    "How many rows does the INSERT statement add?"
                ),
            ]
        elif lab_num == 3:
            Q += [
                (
                    f"In {ap}, count how many members list dept_id CS in relation member. "
                    "Show how you counted without running SQL."
                ),
                (
                    "You group loans by member_id and filter groups where COUNT(*) > 1. "
                    "Should that filter sit in WHERE or in HAVING? Explain briefly."
                ),
            ]
        elif lab_num == 4:
            Q += [
                (
                    f"In {ap}, join loan to member on member_id using only matching rows. "
                    "How many result rows appear?"
                ),
                (
                    f"In {ap}, start from member and left join loan on member_id. "
                    "Which members would show NULL columns from loan for a member who never borrowed? "
                    "Name at least one member_id from the appendix that fits that case."
                ),
            ]
        elif lab_num == 5:
            Q += [
                (
                    f"In {ap}, compare copies_owned for book B106 with copies_owned for book B104. "
                    "Which title reports more copies, and by how many?"
                ),
                (
                    "You sum four balances stored as integers. Describe the order of operations if you implement that sum "
                    "inside a cursor loop instead of one aggregate query."
                ),
            ]
        elif lab_num == 6:
            Q += [
                (
                    f"In {ap}, list distinct book_id values that appear in loan. "
                    "How many distinct titles are borrowed at least once?"
                ),
                ("Explain briefly how a correlated subquery references a row from an outer query."),
            ]
        elif lab_num == 7:
            rows = rng.randint(10_000, 500_000)
            sel = rng.randint(1, 5)
            bal = rng.randint(100, 900)
            delta = rng.randint(10, 80)
            pool = [
                (
                    f"In {ap}, sketch how you would split a wide inventory sheet into department, member, book, and loan "
                    "so that each fact appears once. Words or a rough diagram are fine."
                ),
                (
                    "If student and course are many-to-many, which non-key columns might you store on the enrollment "
                    "bridge besides the foreign keys?"
                ),
                (
                    "You run BEGIN, UPDATE loan SET due_date = due_date + 7 days for one loan_id, then ROLLBACK. "
                    "What happens to that UPDATE after ROLLBACK, and why?"
                ),
                (
                    "Name a durability guarantee that COMMIT normally provides compared with leaving work uncommitted."
                ),
                (
                    f"A table holds about {rows} rows and a predicate returns about {sel} percent of them. "
                    "When might a secondary index help? Discuss briefly."
                ),
                ("EXPLAIN shows Seq Scan. Give a plausible reason the planner might accept that plan."),
                (
                    f"List {rng.randint(2, 4)} topic dependencies you would document for someone joining your mini project."
                ),
                ("Name a design or SQL habit you would tidy up before a final demonstration."),
                (
                    f"In {ap}, compare copies_owned for book B106 with copies_owned for book B104. "
                    "Which title reports more copies, and by how many?"
                ),
                (
                    f"In {ap}, list distinct book_id values that appear in loan. "
                    "How many distinct books are borrowed at least once?"
                ),
                (
                    "How does a correlated subquery refer to rows from an outer query? Explain briefly."
                ),
                (
                    f"In {ap}, count how many members list dept_id CS in relation member. "
                    "Explain your reasoning without running SQL."
                ),
                (
                    "You group loans by member_id and filter groups where COUNT(*) > 1. "
                    "Should that filter appear in WHERE or in HAVING? Explain briefly."
                ),
                (
                    f"In {ap}, join loan to member on member_id using only matching rows. "
                    "How many result rows appear?"
                ),
                (
                    f"In {ap}, start from member and left join loan on member_id. "
                    "Which members would show NULL columns from loan for someone who never borrowed? "
                    "Name at least one member_id from the appendix that fits that pattern."
                ),
                (
                    f"In {ap}, suppose book B101 had copies_owned equal to {bal}. "
                    f"You subtract {delta} copies for a lost-item update. "
                    "What new copies_owned appears before any other transaction runs?"
                ),
                (
                    "You run INSERT ... SELECT ... and the SELECT returns six rows. "
                    "How many rows does the INSERT add?"
                ),
            ]
            Q += rng.sample(pool, min(8, len(pool)))
        else:
            Q += ["Trace one representative statement from your submitted SQL for this laboratory."]
        return Q

    def lab_source_tuple(self, lab_num: int, ctx: WriteupContext) -> Tuple[str, str] | None:
        prn = ctx.student_prn.strip()
        subdir = self._course.labs_repo_subdir
        lab_dir = os.path.join(ctx.repo_root, subdir, f"lab-{lab_num:02d}", prn)
        if not os.path.isdir(lab_dir):
            return None
        for name in _SQL_PICK_ORDER.get(lab_num, ("01_setup.sql",)):
            path = os.path.join(lab_dir, name)
            if os.path.isfile(path):
                try:
                    with open(path, encoding="utf-8") as f:
                        raw = f.read()
                    raw = excerpt_sql_for_writeup(raw, max_lines=45, max_chars=4000)
                    return name, raw
                except OSError:
                    return None
        return None


def create_provider(course: LabCourse) -> DbmsWriteupProvider:
    return DbmsWriteupProvider(course)
