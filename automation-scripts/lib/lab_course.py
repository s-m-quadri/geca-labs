"""Course configuration: separates lab metadata and paths from generator logic."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

SCRIPT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@dataclass(frozen=True)
class LabCourse:
    """One lab course (e.g. DAA, DBMS) with paths under automation-scripts/output/<id>/."""

    id: str
    label: str
    base_branch: str
    github_blob_branch: str
    labs_repo_subdir: str
    course_code: str
    course_name_short: str
    homepage_url: str
    manual_url_template: str
    lab_range: Tuple[int, int]
    attendance_module: str
    problem_set_branch_template: str
    problem_set_branch_overrides: Dict[int, str]
    writeup_document_title: str
    writeup_header_subtitle: str
    writeup_footer_manual_url: str
    features_writeup: bool
    students_csv: str
    labs_index: str
    writeup_provider_module: str

    @property
    def output_subdir(self) -> str:
        return os.path.join("output", self.id)

    @property
    def output_dir(self) -> str:
        return os.path.join(SCRIPT_ROOT, "output", self.id)

    def path_in_output(self, *parts: str) -> str:
        return os.path.join(self.output_dir, *parts)

    @property
    def pull_requests_csv(self) -> str:
        return self.path_in_output("pull_requests.csv")

    @property
    def commits_csv(self) -> str:
        return self.path_in_output("commits.csv")

    @property
    def attendance_csv(self) -> str:
        return self.path_in_output("attendance.csv")

    @property
    def summary_csv(self) -> str:
        return self.path_in_output("summary.csv")

    @property
    def covers_dir(self) -> str:
        return self.path_in_output("covers")

    @property
    def writeups_dir(self) -> str:
        return self.path_in_output("writeups")

    def manual_url(self, lab: int) -> str:
        return self.manual_url_template.format(lab=lab)

    def problem_set_branch(self, lab: int) -> str:
        """Branch name for the problem-set / Codespace target (e.g. ``lab-dbms-05`` vs ``lab-dbms-05-v2``)."""
        if lab in self.problem_set_branch_overrides:
            return self.problem_set_branch_overrides[lab]
        return self.problem_set_branch_template.format(lab=lab)

    def lab_numbers(self) -> List[int]:
        lo, hi = self.lab_range
        return list(range(lo, hi + 1))

    @classmethod
    def load(cls, course_id: str, root: str | None = None) -> LabCourse:
        root = root or SCRIPT_ROOT
        path = os.path.join(root, "courses", f"{course_id}.json")
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Unknown course '{course_id}': missing {path}")
        with open(path, encoding="utf-8") as f:
            raw: Dict[str, Any] = json.load(f)
        lr = raw.get("lab_range", [0, 10])
        if len(lr) != 2:
            raise ValueError(f"lab_range must be [min, max], got {lr!r}")
        feats = raw.get("features") or {}
        students_rel = raw.get("students_csv", "students.csv")
        students_path = (
            students_rel
            if os.path.isabs(students_rel)
            else os.path.join(SCRIPT_ROOT, "output", students_rel.replace("\\", "/").lstrip("/"))
        )
        labs_ix = raw.get("labs_index", "labs/index.md")
        labs_index_path = labs_ix if os.path.isabs(labs_ix) else os.path.join(SCRIPT_ROOT, labs_ix.replace("\\", "/"))
        branch_over: Dict[int, str] = {}
        for k, v in (raw.get("problem_set_branch_overrides") or {}).items():
            branch_over[int(k)] = str(v)
        return cls(
            id=str(raw["id"]),
            label=str(raw["label"]),
            base_branch=str(raw["base_branch"]),
            github_blob_branch=str(raw["github_blob_branch"]),
            labs_repo_subdir=str(raw["labs_repo_subdir"]),
            course_code=str(raw["course_code"]),
            course_name_short=str(raw["course_name_short"]),
            homepage_url=str(raw["homepage_url"]),
            manual_url_template=str(raw["manual_url_template"]),
            lab_range=(int(lr[0]), int(lr[1])),
            attendance_module=str(raw["attendance_module"]),
            problem_set_branch_template=str(raw["problem_set_branch_template"]),
            problem_set_branch_overrides=branch_over,
            writeup_document_title=str(raw["writeup_document_title"]),
            writeup_header_subtitle=str(raw["writeup_header_subtitle"]),
            writeup_footer_manual_url=str(raw["writeup_footer_manual_url"]),
            features_writeup=bool(feats.get("writeup", False)),
            students_csv=students_path,
            labs_index=labs_index_path,
            writeup_provider_module=str(raw.get("writeup_provider_module", "lib.writeup.providers.daa")),
        )


def repo_root_from_scripts() -> str:
    """Parent of automation-scripts (geca-labs root)."""
    return os.path.abspath(os.path.join(SCRIPT_ROOT, os.pardir))
