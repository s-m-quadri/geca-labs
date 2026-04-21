"""Normalize source listings for pdflatex."""

from __future__ import annotations

import re
import unicodedata


def sanitize_code_for_latex(src: str) -> str:
    if not isinstance(src, str):
        src = str(src)
    replacements = {
        "\u2192": "->",
        "\u2190": "<-",
        "\u2194": "<->",
        "\u2264": "<=",
        "\u2265": ">=",
        "\u2260": "!=",
        "\u00d7": "x",
        "\u00b7": "-",
        "\u2022": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u2019": "'",
        "\u2018": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u00a0": " ",
    }
    for k, v in replacements.items():
        src = src.replace(k, v)
    src = src.replace("\r\n", "\n").replace("\r", "\n")
    src = unicodedata.normalize("NFKD", src).encode("ascii", "ignore").decode("ascii")
    src = "".join(ch for ch in src if ch in ("\n", "\t") or ord(ch) >= 32)
    return src.replace("\t", "    ")


def _strip_inline_double_dash(line: str) -> str:
    """Truncate at ``--`` only when it begins a SQL comment (even number of prior single quotes)."""
    search = 0
    while True:
        i = line.find("--", search)
        if i < 0:
            return line
        prefix = line[:i]
        if prefix.count("'") % 2 == 0:
            return prefix.rstrip()
        search = i + 2


def strip_sql_comments(sql: str) -> str:
    """Remove SQL ``/* ... */`` blocks and ``--`` comments (best-effort for lab scripts)."""
    if not isinstance(sql, str):
        sql = str(sql)
    sql = re.sub(r"/\*[\s\S]*?\*/", "", sql)
    out_lines: list[str] = []
    for raw in sql.split("\n"):
        ln = raw.strip()
        if ln.startswith("--"):
            continue
        out_lines.append(_strip_inline_double_dash(raw))
    return "\n".join(out_lines)


def excerpt_sql_for_writeup(
    src: str,
    *,
    max_lines: int = 42,
    max_chars: int = 3800,
) -> str:
    """Sanitize, strip comments, trim blank runs, cap length for PDF listings."""
    text = sanitize_code_for_latex(src)
    text = strip_sql_comments(text)
    lines = [ln.rstrip() for ln in text.split("\n")]
    compact: list[str] = []
    blank_run = 0
    for ln in lines:
        if not ln.strip():
            blank_run += 1
            if blank_run <= 1:
                compact.append("")
            continue
        blank_run = 0
        compact.append(ln)
    text = "\n".join(compact[:max_lines]).strip()
    if len(text) > max_chars:
        text = text[:max_chars].rsplit("\n", 1)[0].rstrip()
        text += "\n-- ... truncated for write-up; see repository file ..."
    return text
