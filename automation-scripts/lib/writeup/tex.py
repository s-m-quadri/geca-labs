"""LaTeX-safe text helpers for writeups (shared by all courses)."""

from __future__ import annotations

import re
import unicodedata


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
        text = text.replace(k, v)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def latex_text(text: str) -> str:
    return escape_latex(to_ascii(text))
