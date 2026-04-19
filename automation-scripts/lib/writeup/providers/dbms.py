"""DBMS writeup question banks (aligned with https://s-m-quadri.me/geca/dbms manuals)."""

from __future__ import annotations

import os
import random
from typing import Dict, List, Sequence, Tuple

from lib.lab_course import LabCourse
from lib.writeup.context import WriteupContext
from lib.writeup.source import sanitize_code_for_latex
from lib.writeup.util import format_matrix_rows, make_int_array

# Preferred SQL files per lab (first match under the student's lab folder wins).
_SQL_PICK_ORDER: Dict[int, Sequence[str]] = {
    0: ("setup.sql", "tables.sql", "queries.sql", "01_create_database.sql", "02_create_table.sql"),
    1: ("02_create_table.sql", "01_create_database.sql", "03_insert_data.sql", "04_add_columns.sql"),
    2: ("01_setup.sql", "04_select_all.sql", "05_select_where.sql", "07_update_one.sql"),
    3: ("01_setup.sql", "02_count_sum.sql", "03_string_funcs.sql", "10_check_status.sql"),
    4: ("01_setup.sql", "03_inner_join.sql", "04_left_join.sql", "10_check_status.sql"),
    5: ("01_setup.sql", "02_user_vars_arithmetic.sql", "04_proc_apply_rate.sql", "10_check_status.sql"),
    6: ("01_setup.sql", "02_create_view.sql", "04_subquery_scalar.sql", "12_check_status.sql"),
    7: ("01_setup.sql", "schema.sql", "02_ddl.sql", "10_check_status.sql"),
    8: ("01_setup.sql", "02_transaction.sql", "10_check_status.sql"),
    9: ("01_setup.sql", "02_index.sql", "03_explain.sql", "10_check_status.sql"),
    10: ("01_setup.sql", "02_integration.sql", "10_check_status.sql", "review.sql"),
}


class DbmsWriteupProvider:
    listings_style = "sql"
    source_kind_label = "SQL"
    source_subsection_title = "Reference SQL (your repo)"
    digest_instruction = (
        "Execute mentally or on paper (or a scratch DB) as in the lab manual; show intermediate results."
    )

    def __init__(self, course: LabCourse) -> None:
        self._course = course

    def subjective_questions(self, lab_num: int, title: str) -> List[str]:
        bank = {
            0: [
                "Why is a virtual environment useful when mixing Python tooling with a DB client?",
                "What is the difference between a DBMS, a database, and a schema?",
                "Name two ways to connect an application to a relational database.",
                "What does SQL stand for, and is it declarative or imperative in spirit?",
            ],
            1: [
                "What is DDL and how does it differ from DML?",
                "Explain PRIMARY KEY vs UNIQUE with one short example each.",
                "What is a foreign key constraint trying to guarantee?",
                "When would you use ALTER TABLE instead of DROP + CREATE?",
            ],
            2: [
                "Contrast INSERT, UPDATE, and DELETE in one sentence each.",
                "What is the role of WHERE in DML statements?",
                "Explain why DELETE without WHERE is dangerous on production data.",
                "What does ORDER BY control, and does it change stored rows?",
            ],
            3: [
                "Give examples of aggregate functions and when GROUP BY is required.",
                "What is the difference between WHERE and HAVING?",
                "Why can SELECT list columns be restricted when aggregates appear?",
                "Name one string function and one numeric function you used in the lab.",
            ],
            4: [
                "Define INNER JOIN vs LEFT (OUTER) JOIN in terms of unmatched rows.",
                "What is an equi-join? Give a tiny example predicate.",
                "Why can joins explode row counts if keys are not unique?",
                "What is a self-join and when is it useful?",
            ],
            5: [
                "Contrast a stored function vs a stored procedure (PostgreSQL perspective).",
                "Why might PL/pgSQL use $$ ... $$ delimiters?",
                "What is a cursor loop used for in procedural SQL?",
                "How does CASE WHEN in SQL replace MySQL's IF(...) in SELECT lists?",
            ],
            6: [
                "What problem do views solve compared to repeating a complex SELECT?",
                "Contrast scalar, IN, and EXISTS subqueries (one line each).",
                "What makes a subquery correlated?",
                "What is a derived table (inline view) in the FROM clause?",
            ],
            7: [
                "State the goal of normalization up to 3NF in one paragraph.",
                "What is an ER diagram element you always label on relationships?",
                "How do you choose primary keys for associative (bridge) entities?",
                "Give one trade-off between more tables (normalized) vs fewer tables (denormalized).",
            ],
            8: [
                "State the four ACID properties in one line each.",
                "What is a transaction boundary and why COMMIT matters?",
                "What anomaly does isolation aim to prevent (name one)?",
                "Why might READ COMMITTED differ from REPEATABLE READ?",
            ],
            9: [
                "What is a B-tree index good for in a relational engine?",
                "Why can indexes speed SELECT but slow some INSERT/UPDATE paths?",
                "What does EXPLAIN (or EXPLAIN ANALYZE) help you inspect?",
                "When might a full table scan be acceptable?",
            ],
            10: [
                "Summarize how DDL, DML, views, and procedures fit into a layered application.",
                "What is one lesson from integrating multiple lab skills into one schema?",
                "How would you document assumptions for a mini-project schema?",
            ],
        }
        return bank.get(lab_num, [f"State two core ideas from: {title}."])

    def objective_questions(self, lab_num: int, rng: random.Random) -> List[str]:
        Q: List[str] = []
        if lab_num == 0:
            port = rng.choice([3306, 5432, 1433])
            Q += [
                f"A service listens on port {port}. Is it necessarily PostgreSQL? (Yes/No + reason)",
                f"You create {rng.randint(2, 5)} tables in schema `lab0`. How many catalogs are you using if everything is one database?",
            ]
        elif lab_num == 1:
            cols = rng.randint(3, 8)
            Q += [
                f"A CREATE TABLE lists {cols} columns with one PRIMARY KEY. Minimum PRIMARY KEY columns?",
                "Write one CHECK constraint idea for a positive price column (predicate only).",
            ]
        elif lab_num == 2:
            n = rng.randint(10, 99)
            Q += [
                f"DELETE removes {n} rows but WHERE clause matches {n + rng.randint(1, 5)} candidate rows - what happened?",
                f"UPDATE sets salary = salary * {rng.choice([1.05, 1.1, 1.2])}. Is this row-wise or set-wise?",
            ]
        elif lab_num == 3:
            k = rng.randint(5, 20)
            Q += [
                f"COUNT(*) on a table with {k} rows after a WHERE that filters half - expected count?",
                "GROUP BY dept_id with SUM(salary) - can SELECT include emp_name without aggregate? (Yes/No + rule)",
            ]
        elif lab_num == 4:
            a, b = rng.randint(8, 40), rng.randint(8, 40)
            Q += [
                f"Table A has {a} rows, B has {b} rows. Upper bound on INNER JOIN result size?",
                "LEFT JOIN A to B: which side's unmatched rows are preserved?",
            ]
        elif lab_num == 5:
            p = rng.randint(10, 30)
            Q += [
                f"Function apply_rate(base, {p}) returns base scaled by percent - does it return a scalar?",
                "CALL vs SELECT for a procedure that updates rows - pick one for a mutating routine.",
            ]
        elif lab_num == 6:
            v = rng.randint(2, 9)
            Q += [
                f"A view hides {v} underlying tables. Is the view materialized by default in PostgreSQL?",
                "EXISTS (SELECT 1 ...) stops early - true or false?",
            ]
        elif lab_num == 7:
            f = rng.randint(2, 5)
            Q += [
                f"You spot {f} repeating groups in one wide table - highest normal form violated first?",
                "Bridge table between students and courses: what are its typical PK columns?",
            ]
        elif lab_num == 8:
            Q += [
                f"Transaction T1 reads row X, T2 updates X, T1 reads X again - name the classical anomaly if values differ.",
                "After COMMIT, are changes visible to other sessions (typical default)?",
            ]
        elif lab_num == 9:
            idx = rng.randint(1, 4)
            Q += [
                f"You create {idx} secondary index(es) on the same table - how many clustered indexes are typical in PostgreSQL per table?",
                "Sequential scan vs index scan: which often wins on tiny tables?",
            ]
        elif lab_num == 10:
            Q += [
                f"List {rng.randint(2, 4)} artifacts you would ship besides `.sql` for a DB mini-project.",
                "Why keep migrations versioned instead of only the final schema?",
            ]
        else:
            Q += ["Give two crisp takeaways from this lab."]
        return Q

    def code_digest_questions(self, lab_num: int, rng: random.Random) -> List[str]:
        Q: List[str] = []
        if lab_num == 0:
            nums = make_int_array(rng, 4, 1, 12)
            Q += [
                f"Pretend `print(sum_rows({nums}))` prints row counts - compute the sum by hand.",
                "Write a one-line SQL comment explaining why UTF-8 matters for student names.",
            ]
        elif lab_num == 1:
            t = rng.choice(["books", "orders", "patients"])
            Q += [
                f"Draft CREATE TABLE {t} with columns id PK, name NOT NULL - list columns only (no full SQL).",
                f"ALTER TABLE {t} ADD COLUMN notes TEXT - does it affect existing rows' values?",
            ]
        elif lab_num == 2:
            bal = rng.randint(100, 900)
            delta = rng.randint(10, 80)
            Q += [
                f"UPDATE accounts SET balance = balance - {delta} WHERE id = 1; old balance {bal} - new balance?",
                f"INSERT {rng.randint(2, 5)} rows into a log table - how many times does INSERT fire?",
            ]
        elif lab_num == 3:
            wages = make_int_array(rng, 5, 20, 60)
            Q += [
                f"Given salaries {wages}, compute AVG by hand.",
                "HAVING AVG(salary) > 45 filters groups - does WHERE AVG(salary) > 45 work? Why?",
            ]
        elif lab_num == 4:
            # tiny snapshot: orders x customers
            cust = rng.randint(3, 6)
            ord_cnt = rng.randint(4, 9)
            Q += [
                f"{cust} customers and {ord_cnt} orders (many-to-one). Max INNER JOIN rows if every order has customer?",
                "Write the join predicate pattern `orders.cust_id = customers.cust_id` - what key type is this?",
            ]
        elif lab_num == 5:
            a, b = rng.randint(11, 40), rng.randint(2, 9)
            Q += [
                f"CASE WHEN balance >= {a} THEN 'high' ELSE 'low' END - classify balance={a + b}.",
                f"Cursor sums balances [{make_int_array(rng, 4, 100, 500)}] - hand total.",
            ]
        elif lab_num == 6:
            prices = sorted(make_int_array(rng, 5, 10, 90, distinct=True))
            Q += [
                f"Second-highest distinct price from {prices}?",
                "Correlated subquery references outer row - give a one-sentence English pattern.",
            ]
        elif lab_num == 7:
            ents = rng.randint(5, 12)
            rels = rng.randint(ents, ents + 6)
            Q += [
                f"ER sketch: {ents} entities, {rels} relationships - minimum bridge tables if M:N present?",
                "Convert `student enrolls course` M:N - name the bridge attributes besides FKs.",
            ]
        elif lab_num == 8:
            Q += [
                f"Schedule {rng.randint(2, 4)} statements in order BEGIN; UPDATE; ROLLBACK; - does UPDATE persist?",
                "Name one guarantee COMMIT provides versus autocommit off with no COMMIT.",
            ]
        elif lab_num == 9:
            rows = rng.randint(10_000, 500_000)
            sel = rng.randint(1, 5)
            Q += [
                f"Table cardinality ~{rows}, selective predicate returns ~{sel}% rows - index likely helpful?",
                "EXPLAIN shows Seq Scan - give one reason the planner might prefer it.",
            ]
        elif lab_num == 10:
            Q += [
                f"List dependencies between labs 1-{rng.randint(4, 7)} you would mention in a README.",
                "One SQL smell you would refactor before demo day?",
            ]
        else:
            Q += ["Trace one representative statement from your submitted SQL for this lab."]
        if lab_num == 4:
            # optional micro matrix: order lines
            m = rng.randint(2, 4)
            n = rng.randint(2, 4)
            mat = [[rng.randint(0, 3) for _ in range(n)] for _ in range(m)]
            Q.append("Interpret this toy qty matrix as line items (rows=orders, cols=products)  -  compute row sums:")
            Q.append(format_matrix_rows(mat))
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
                    raw = sanitize_code_for_latex(raw)
                    lines = raw.split("\n")
                    if len(lines) > 160:
                        raw = "\n".join(lines[:160]) + "\n-- ... truncated for writeup PDF; see full file in repo ..."
                    return name, raw
                except OSError:
                    return None
        return None


def create_provider(course: LabCourse) -> DbmsWriteupProvider:
    return DbmsWriteupProvider(course)
