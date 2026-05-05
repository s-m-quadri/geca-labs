"""Shared numeric / matrix helpers for DAA-style writeup questions."""

from __future__ import annotations

import math
import random
from typing import List

from lib.writeup.tex import latex_text


def make_int_array(rng: random.Random, n: int, lo: int, hi: int, distinct: bool = False) -> List[int]:
    if distinct:
        pool = list(range(lo, hi + 1))
        rng.shuffle(pool)
        return pool[:n]
    return [rng.randint(lo, hi) for _ in range(n)]


def format_matrix_rows(rows: List[List[int | float | str]], inf_token: str = "\\infty") -> str:
    """LaTeX bmatrix from numeric/INF rows (for student work in writeups)."""

    def cell(v):
        if isinstance(v, (int, float)) and (v == math.inf or v == float("inf")):
            return inf_token
        s = str(v)
        if s.upper() == "INF":
            return inf_token
        return latex_text(s)

    lines = [" & ".join(cell(v) for v in row) for row in rows]
    row_sep = " \\\\\n"
    body = row_sep.join(lines)
    return f"\\[\\begin{{bmatrix}}\n{body}\n\\end{{bmatrix}}\\]"
