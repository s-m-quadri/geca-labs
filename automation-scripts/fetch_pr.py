#!/usr/bin/env python3
"""Fetch maximum PR details (open + merged) per course and save to JSON.

Fetches per PR: full metadata, commits with file stats, changed files,
reviews, issue comments.

Incremental: loads existing pr_details.json and skips PRs whose state and
updated_at are unchanged.  Open PRs that were updated (or became merged) are
re-fetched.  Saves after every PR so an interrupted run can be resumed.

Usage:
    python3 fetch_pr.py --course dbms
    python3 fetch_pr.py --course daa --only-merged
    python3 fetch_pr.py --course dbms --only-open
    python3 fetch_pr.py --course dbms --force   # ignore cache
"""

from __future__ import annotations

import argparse
import os
import sys

SCRIPT_ROOT = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_ROOT not in sys.path:
    sys.path.insert(0, SCRIPT_ROOT)

from lib.common import load_env_file

_ENV = os.path.join(SCRIPT_ROOT, ".env")
load_env_file(_ENV)
try:
    from dotenv import load_dotenv
    load_dotenv(_ENV, override=False)
except ImportError:
    pass

from lib.lab_course import LabCourse
from lib.fetch_details import (
    fetch_all_pr_details,
    filter_course_prs,
    list_all_prs,
    load_details_cache,
    save_details_cache,
    needs_refetch,
)

REPO_OWNER = os.getenv("GITHUB_REPO_OWNER", "s-m-quadri")
REPO_NAME = os.getenv("GITHUB_REPO_NAME", "geca-labs")


def _progress(msg: str) -> None:
    print(f"  -> {msg}", flush=True)


def run(course: LabCourse, token: str | None, only_merged: bool, only_open: bool, force: bool) -> int:
    os.makedirs(course.output_dir, exist_ok=True)
    out_path = course.path_in_output("pr_details.json")
    print(f"Output -> {out_path}")

    print(f"Fetching PR index from {REPO_OWNER}/{REPO_NAME}...")
    all_prs = list_all_prs(REPO_OWNER, REPO_NAME, token, progress=_progress)

    course_prs = filter_course_prs(course.id, course.base_branch, all_prs)
    print(f"Course {course.id!r}: {len(course_prs)} PRs (of {len(all_prs)} total)")

    if only_merged:
        course_prs = [p for p in course_prs if p.get("merged_at")]
        print(f"  -> filtered to {len(course_prs)} merged")
    elif only_open:
        course_prs = [p for p in course_prs if p.get("state") == "open"]
        print(f"  -> filtered to {len(course_prs)} open")
    else:
        merged_n = sum(1 for p in course_prs if p.get("merged_at"))
        open_n = sum(1 for p in course_prs if p.get("state") == "open")
        print(f"  -> {merged_n} merged, {open_n} open")

    if not course_prs:
        print("Nothing to fetch.")
        return 0

    cache = {} if force else load_details_cache(out_path)
    if cache:
        print(f"Loaded {len(cache)} existing entries from cache.")

    to_fetch = [pr for pr in course_prs
                if pr["number"] not in cache or force or needs_refetch(cache[pr["number"]], pr)]
    skipped = len(course_prs) - len(to_fetch)
    print(f"Skip (unchanged): {skipped}  |  To fetch: {len(to_fetch)}")

    if not to_fetch:
        print("All up to date.")
        save_details_cache(out_path, cache)
        return 0

    total = len(to_fetch)
    fetched = 0
    try:
        for idx, pr in enumerate(to_fetch, 1):
            _progress(f"[{idx}/{total}] PR #{pr['number']}")
            result = fetch_all_pr_details(REPO_OWNER, REPO_NAME, [pr], token)
            if result:
                cache[pr["number"]] = result[0]
            fetched += 1
            save_details_cache(out_path, cache)
    except KeyboardInterrupt:
        print(f"\nInterrupted after {fetched}/{total}. Progress saved to {out_path}")
        return 1

    merged_done = sum(1 for d in cache.values() if d.get("merged"))
    open_count = sum(1 for d in cache.values() if d.get("state") == "open")
    print(f"\nSaved {len(cache)} PRs -> {out_path}")
    print(f"  merged/accepted: {merged_done}  |  open: {open_count}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Fetch max PR details per course -> pr_details.json")
    ap.add_argument("--course", required=True, help="Course id (daa, dbms, ...)")
    ap.add_argument("--only-merged", action="store_true", help="Fetch only merged/accepted PRs")
    ap.add_argument("--only-open", action="store_true", help="Fetch only open PRs")
    ap.add_argument("--force", action="store_true", help="Ignore cache; re-fetch everything")
    args = ap.parse_args()

    token = os.getenv("GITHUB_TOKEN") or None
    if not token:
        print("Warning: GITHUB_TOKEN not set. GitHub allows ~60 unauthenticated API calls/hour.")

    course = LabCourse.load(args.course.strip().lower(), root=SCRIPT_ROOT)
    return run(course, token, args.only_merged, args.only_open, args.force)


if __name__ == "__main__":
    raise SystemExit(main())
