"""LaTeX fragments for duplex (two-sided) printing.

Insert ``latex_duplex_even_page_suffix()`` immediately before ``\\end{document}``
so the PDF has an even total page count (blank final page when needed).
"""


def latex_duplex_even_page_suffix() -> str:
    """Emit TeX that pads the document to an even page count."""
    return (
        "% --- duplex: even total pages (blank sheet if needed) ---\n"
        "\\ifodd\\value{page}\n"
        "  \\clearpage\n"
        "  \\thispagestyle{empty}\n"
        "  \\null\n"
        "\\fi\n"
    )
