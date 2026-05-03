#!/usr/bin/env python3
"""Build attendance CSV from students.csv using course-specific roster data."""

from __future__ import annotations

import argparse
import csv
import importlib
import os
import sys

from lib.lab_course import LabCourse

ROOT = os.path.dirname(os.path.abspath(__file__))


def load_attendance_module(course: LabCourse):
    """Import data.<attendance_module> (e.g. attendance_daa)."""
    name = course.attendance_module
    if "." in name or "/" in name:
        raise ValueError(f"Invalid attendance_module name: {name!r}")
    return importlib.import_module(f"data.{name}")


def run(course_id: str) -> int:
    course = LabCourse.load(course_id, root=ROOT)
    mod = load_attendance_module(course)
    students_path = course.students_csv
    out_path = course.attendance_csv

    if not os.path.isfile(students_path):
        print(f"Missing students CSV: {students_path}", file=sys.stderr)
        return 2

    os.makedirs(course.output_dir, exist_ok=True)
    fieldnames = mod.attendance_fieldnames()

    with open(students_path, newline="", encoding="utf-8") as infile, open(
        out_path, "w", newline="", encoding="utf-8"
    ) as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            writer.writerow(mod.build_output_row(row))

    print(f"Attendance CSV ({course.id}) → {out_path}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Generate attendance.csv for a lab course.")
    p.add_argument("--course", default="daa", help="Course id: daa | dbms (see courses/<id>.json)")
    args = p.parse_args()
    return run(args.course)


if __name__ == "__main__":
    raise SystemExit(main())
