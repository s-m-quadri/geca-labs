"""Pluggable per-course writeup content (question banks, reference sources)."""

from __future__ import annotations

import importlib
from typing import Any

from lib.lab_course import LabCourse


def load_writeup_provider(course: LabCourse) -> Any:
    """Import ``course.writeup_provider_module`` and call ``create_provider(course)``."""
    mod = importlib.import_module(course.writeup_provider_module)
    return mod.create_provider(course)
