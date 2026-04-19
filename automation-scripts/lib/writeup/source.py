"""Normalize source listings for pdflatex."""

from __future__ import annotations

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
