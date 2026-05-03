from __future__ import annotations

from dataclasses import dataclass

from lib.lab_course import LabCourse


@dataclass
class WriteupContext:
    """Per-student paths for resolving reference source files."""

    student_prn: str
    scripts_root: str
    repo_root: str
    course: LabCourse
