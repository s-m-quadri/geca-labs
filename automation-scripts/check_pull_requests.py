#!/usr/bin/env python3
"""Validate PR data per course: identity clashes, duplicate PRs, filesystem cross-checks.

Reads from pr_details.json (preferred) or pull_requests.csv fallback.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import pandas as pd

from lib.lab_course import LabCourse

_SCRIPTS = Path(__file__).resolve().parent


def extract_lab(labels) -> int | None:
    """Accept a list of label strings or a comma-separated string."""
    if isinstance(labels, list):
        parts = labels
    else:
        parts = str(labels or "").split(",")
    for lbl in parts:
        m = re.search(r"Lab\s*0*([0-9]+)", str(lbl).strip(), re.IGNORECASE)
        if m:
            return int(m.group(1))
    return None


def count_files(dir_path: Path) -> int:
    skip_dirs = {"__pycache__", ".git", ".ipynb_checkpoints", ".venv", "venv", "node_modules"}
    total = 0
    for p in dir_path.rglob("*"):
        try:
            if any(part.startswith(".") for part in p.parts if part not in (".", "..")):
                continue
            if any(sd in p.parts for sd in skip_dirs):
                continue
            if p.is_file() and p.suffix.lower() != ".pyc":
                total += 1
        except Exception:
            continue
    return total


def load_data(course: LabCourse) -> tuple[list[dict], str]:
    """Load PR records. Returns (records, source_label)."""
    json_path = Path(course.path_in_output("pr_details.json"))
    if json_path.exists():
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)
        return data, str(json_path)

    csv_path = Path(course.pull_requests_csv)
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        records = []
        for _, row in df.iterrows():
            labels_raw = str(row.get("Labels", ""))
            records.append({
                "number": row.get("PR Number"),
                "prn": str(row.get("PRN", "")).strip().upper(),
                "title": str(row.get("Title", "")),
                "state": str(row.get("State", "")),
                "merged": bool(row.get("Merged At") and pd.notna(row.get("Merged At"))),
                "merged_at": row.get("Merged At") or "",
                "user": str(row.get("User", "")),
                "labels": [l.strip() for l in labels_raw.split(",") if l.strip()],
                "url": "",
            })
        return records, str(csv_path)

    return [], ""


def check_csv(records: list[dict]) -> None:
    print("\n==== CSV / PR Validity Checks ====\n")

    user_to_prns: dict[str, set] = {}
    prn_to_users: dict[str, set] = {}
    prn_lab_rows: dict[tuple, list] = {}

    for r in records:
        user = r.get("user", "")
        prn = str(r.get("prn", "")).strip().upper()
        if user and prn:
            user_to_prns.setdefault(user, set()).add(prn)
            prn_to_users.setdefault(prn, set()).add(user)
        lab = extract_lab(r.get("labels", []))
        if lab is not None and prn:
            prn_lab_rows.setdefault((prn, lab), []).append(r)

    # 1. One user -> multiple PRNs
    for user, prns in sorted(user_to_prns.items()):
        if len(prns) > 1:
            print(f"[ERROR] User '{user}' has multiple PRNs: {sorted(prns)}")

    # 2. One PRN -> multiple users
    for prn, users in sorted(prn_to_users.items()):
        if len(users) > 1:
            print(f"[ERROR] PRN '{prn}' used by multiple users: {sorted(users)}")

    # 3. Duplicate / inconsistent open+merged per (PRN, lab)
    for (prn, lab), rows in sorted(prn_lab_rows.items()):
        merged = [r for r in rows if r.get("merged") or r.get("merged_at")]
        open_ = [r for r in rows if r.get("state") == "open"]
        if merged and open_:
            nums = [r["number"] for r in rows]
            print(f"[ERROR] PRN '{prn}' Lab {lab}: open PR despite merged PR — PRs {nums}")
        if len(open_) > 1:
            nums = [r["number"] for r in open_]
            print(f"[ERROR] PRN '{prn}' Lab {lab}: multiple open PRs — #{nums}")


def check_filesystem(records: list[dict], course: LabCourse) -> None:
    labs_root = (_SCRIPTS.parent / course.labs_repo_subdir).resolve()
    if not labs_root.exists():
        print(f"\n[SKIP] Labs root not found (filesystem checks skipped): {labs_root}")
        return

    print(f"\n==== Filesystem Checks ({labs_root.name}) ====\n")

    merged_lookup: dict[tuple, set] = {}
    user_freq: dict[str, dict] = {}

    for r in records:
        prn = str(r.get("prn", "")).strip().upper()
        user = str(r.get("user", "")).strip()
        if not prn or not user:
            continue
        user_freq.setdefault(prn, {})
        user_freq[prn][user] = user_freq[prn].get(user, 0) + 1
        if not (r.get("merged") or r.get("merged_at")):
            continue
        lab = extract_lab(r.get("labels", []))
        if lab is not None:
            merged_lookup.setdefault((prn, int(lab)), set()).add(user)

    merged_set = set(merged_lookup.keys())

    def best_user(prn: str, lab: int) -> str:
        users = merged_lookup.get((prn, lab))
        if users:
            return sorted(users)[0]
        if prn in user_freq and user_freq[prn]:
            return sorted(user_freq[prn].items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
        return ""

    # Check 4: merged PR -> folder exists
    print("-> Check 4: each merged PR has a submission folder")
    seen: set[tuple] = set()
    for r in records:
        if not (r.get("merged") or r.get("merged_at")):
            continue
        prn = str(r.get("prn", "")).strip().upper()
        lab = extract_lab(r.get("labels", []))
        if not prn or lab is None:
            continue
        key = (prn, int(lab))
        if key in seen:
            continue
        seen.add(key)
        lab_dir = labs_root / f"lab-{int(lab):02d}"
        folder = lab_dir / prn
        if not lab_dir.exists():
            print(f"[ERROR] Lab dir missing for Lab {lab}: {lab_dir}")
        elif not folder.is_dir():
            print(f"[ERROR] Missing folder -> PRN '{prn}' Lab {lab}: {folder}")

    # Check 5: folder exists -> merged PR present
    print("\n-> Check 5: each submission folder has a merged PR")
    for lab_dir in sorted(labs_root.glob("lab-*")):
        if not lab_dir.is_dir():
            continue
        m = re.search(r"lab-0*([0-9]+)$", lab_dir.name, re.IGNORECASE)
        if not m:
            continue
        lab = int(m.group(1))
        for prn_dir in sorted(lab_dir.iterdir()):
            if not prn_dir.is_dir():
                continue
            prn = prn_dir.name.strip().upper()
            if (prn, lab) not in merged_set:
                print(f"[ERROR] Folder without merged PR -> PRN '{prn}' Lab {lab}: {prn_dir}")

    # Check 6: minimum file count
    print("\n-> Check 6: minimum file count per submission folder")
    lo, hi = course.lab_range
    min_files = {lab: 1 for lab in range(lo, hi + 1)}
    for lab_dir in sorted(labs_root.glob("lab-*")):
        if not lab_dir.is_dir():
            continue
        m = re.search(r"lab-0*([0-9]+)$", lab_dir.name, re.IGNORECASE)
        if not m:
            continue
        lab = int(m.group(1))
        required = min_files.get(lab, 1)
        for prn_dir in sorted(lab_dir.iterdir()):
            if not prn_dir.is_dir():
                continue
            prn = prn_dir.name.strip().upper()
            n = count_files(prn_dir)
            if n < required:
                user = best_user(prn, lab)
                gh = f"https://github.com/{user}" if user else "(unknown)"
                print(f"[ERROR] Too few files -> PRN '{prn}' Lab {lab}: {n}/{required} | {prn_dir} | {gh}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate PR data for a course.")
    ap.add_argument("--course", default="daa", help="Course id (daa, dbms, ...)")
    ap.add_argument("--no-fs", action="store_true", help="Skip filesystem checks")
    args = ap.parse_args()

    course = LabCourse.load(args.course.strip().lower(), root=str(_SCRIPTS))
    records, source = load_data(course)

    if not records:
        print(f"[ERROR] No data found for course '{course.id}'.")
        print(f"  Run: python3 fetch_pr.py --course {course.id}")
        print(f"   or: python3 fetch_pr.py --course {course.id}")
        return 1

    print(f"Course: {course.label} ({course.id})")
    print(f"Source: {source}")
    print(f"PRs:    {len(records)}")

    check_csv(records)
    if not args.no_fs:
        check_filesystem(records, course)

    print("\nDone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
