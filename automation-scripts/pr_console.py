#!/usr/bin/env python3
"""
Interactive pull-request console for lab integration workflows.

Logic is aligned with ``geca-labs/.github/workflows`` (``status.yml``,
``test-submission.yml``, ``merge-organize.yml``): merge expects
``sub-lab-{daa|dbms}-{NN}`` base; status bot is triggered by a comment containing
``Hi @bot-s-m-quadri`` (without the word ``merge``).

Summarizes open PRs per course, buckets suggested bot steps, and supports bulk
copy or — only after you type an explicit approval code — posting issue comments.

Nothing is posted or merged unless you approve with the displayed phrase.

On a TTY, startup asks whether to allow the (p) API post action; use
``--allow-github-post`` to skip the question (e.g. non-interactive use).
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import secrets
import sys
import time
import webbrowser
from typing import Dict, List, Sequence

SCRIPT_ROOT = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_ROOT not in sys.path:
    sys.path.insert(0, SCRIPT_ROOT)

from lib.common import load_env_file, read_students

_ENV_PATH = os.path.join(SCRIPT_ROOT, ".env")
load_env_file(_ENV_PATH)

try:
    from dotenv import load_dotenv

    load_dotenv(_ENV_PATH, override=False)
except ImportError:
    pass

from lib.lab_course import LabCourse
from lib.pr_workflow import (
    CMD_MERGE,
    CMD_STATUS,
    CMD_TEST,
    PRDigestRow,
    NextStep,
    build_digest_rows,
    list_all_open_pulls,
    load_open_rows_from_csv,
    misbased_lab_prs,
    open_prs_for_course,
    post_issue_comment,
)
from lib.console_display import (
    hr,
    print_row_summary,
    print_digest,
    approval_manifest,
    prompt_approve_post,
    write_batch_file,
    templates_for_rows,
)
from lib.fetch_details import fetch_all_pr_details, filter_course_prs, list_all_prs

REPO_OWNER = os.getenv("GITHUB_REPO_OWNER", "s-m-quadri")
REPO_NAME = os.getenv("GITHUB_REPO_NAME", "geca-labs")


def discover_courses() -> Dict[str, LabCourse]:
    out: Dict[str, LabCourse] = {}
    for path in sorted(glob.glob(os.path.join(SCRIPT_ROOT, "courses", "*.json"))):
        with open(path, encoding="utf-8") as f:
            raw = json.load(f)
        cid = str(raw["id"])
        out[cid] = LabCourse.load(cid, root=SCRIPT_ROOT)
    return out


def roster_prn_set(course: LabCourse) -> set:
    try:
        students = read_students(course.students_csv)
    except FileNotFoundError:
        return set()
    return {s.prn.strip().upper() for s in students}







def interactive_menu(
    course: LabCourse,
    rows: List[PRDigestRow],
    misbased: List[dict],
    token: str | None,
    allow_network_post: bool,
    live: bool,
) -> str:
    """Returns ``quit`` or ``refresh``."""
    while True:
        print_digest(course, rows, misbased, live=live, repo_owner=REPO_OWNER, repo_name=REPO_NAME)
        print("Actions (human-in-the-loop; default is copy/preview only):")
        print("  r — refresh digest (re-fetch from GitHub)")
        print("  d — fetch maximum PR details (open + merged) → pr_details.json")
        print("  c — print bulk COMMENT templates for a bucket (copy from terminal)")
        print("  w — write bulk templates to output/<course>/pr_console_batch.txt")
        print("  o — open all PR URLs in bucket in browser (many tabs)")
        if allow_network_post and token:
            print("  p — POST comments via API (requires typed approval; uses token)")
        print("  q — quit")
        choice = input("Choice: ").strip().lower()
        if choice == "q":
            return "quit"
        if choice == "r":
            return "refresh"
        if choice == "d":
            if not token:
                print("GITHUB_TOKEN not set; rate-limited to 60 req/hr without auth.")
            from lib.fetch_details import load_details_cache, save_details_cache, needs_refetch

            def _dp(msg: str) -> None:
                print(f"  -> {msg}", flush=True)

            out_path = course.path_in_output("pr_details.json")
            print(f"Output -> {out_path}")
            try:
                all_prs = list_all_prs(REPO_OWNER, REPO_NAME, token, progress=_dp)
                course_prs = filter_course_prs(course.id, course.base_branch, all_prs)
                merged_n = sum(1 for p in course_prs if p.get("merged_at"))
                open_n = sum(1 for p in course_prs if p.get("state") == "open")
                print(f"Course {course.id!r}: {len(course_prs)} PRs ({merged_n} merged, {open_n} open)")
                cache = load_details_cache(out_path)
                if cache:
                    print(f"Loaded {len(cache)} existing entries from cache.")
                to_fetch = [pr for pr in course_prs
                            if pr["number"] not in cache or needs_refetch(cache[pr["number"]], pr)]
                print(f"Skip (unchanged): {len(course_prs) - len(to_fetch)}  |  To fetch: {len(to_fetch)}")
                os.makedirs(course.output_dir, exist_ok=True)
                for idx, pr in enumerate(to_fetch, 1):
                    _dp(f"[{idx}/{len(to_fetch)}] PR #{pr['number']}")
                    result = fetch_all_pr_details(REPO_OWNER, REPO_NAME, [pr], token)
                    if result:
                        cache[pr["number"]] = result[0]
                    save_details_cache(out_path, cache)
                print(f"Saved {len(cache)} PRs -> {out_path}")
            except KeyboardInterrupt:
                print("Interrupted. Progress saved.")
            except Exception as e:
                print(f"Detail fetch failed: {e}")
            continue
        if choice == "c" or choice == "w" or choice == "o" or choice == "p":
            print(
                "Buckets: 1=status  2=test  3=re_test  4=incomplete  "
                "5=fix_ci  6=merge  7=unknown"
            )
            b = input("Bucket number: ").strip()
            key_map = {
                "1": "status",
                "2": "test",
                "3": "re_test",
                "4": "incomplete",
                "5": "fix_ci",
                "6": "merge",
                "7": "unknown",
            }
            step = key_map.get(b)
            if not step:
                print("Invalid bucket.")
                continue
            sub = [r for r in rows if r.suggested == step]
            if not sub:
                print("No PRs in that bucket.")
                continue
            if step == "status":
                body = CMD_STATUS
                label = "status bot"
            elif step == "test":
                body = CMD_TEST
                label = "first test bot"
            elif step == "re_test":
                body = CMD_TEST
                label = "re-test bot"
            elif step == "merge":
                body = CMD_MERGE
                label = "merge bot"
            elif step == "incomplete":
                print(
                    "Incomplete: students should fix incorrect/incomplete work before re-running tests; "
                    "no standard bot line."
                )
                if choice == "c":
                    print("\n--- PRs (open in browser or message manually) ---")
                    for r in sub:
                        print(f"  #{r.number}  {r.html_url}")
                elif choice == "w":
                    p = write_batch_file(
                        course,
                        "\n".join(f"# PR #{r.number}\n{r.html_url}\n" for r in sub),
                    )
                    print(f"Wrote URL list to {p}")
                elif choice == "o":
                    for r in sub:
                        if r.html_url:
                            webbrowser.open(r.html_url)
                    print(f"Opened {len(sub)} tabs.")
                elif choice == "p":
                    print("Posting disabled for incomplete bucket — use manual outreach.")
                continue
            elif step == "fix_ci":
                print("fix_ci: GitHub Actions / Check Runs failed — review workflow logs on GitHub.")
                print("No automatic comment template.")
                continue
            elif step == "unknown":
                print("Unknown bucket needs manual review.")
                continue

            text = templates_for_rows(sub, body)
            if choice == "c":
                print()
                print(text)
            elif choice == "w":
                p = write_batch_file(course, text)
                print(f"Wrote {p}")
            elif choice == "o":
                for r in sub:
                    if r.html_url:
                        webbrowser.open(r.html_url)
                print(f"Opened {len(sub)} tabs (browser).")
            elif choice == "p":
                if not token:
                    print("GITHUB_TOKEN not set; cannot post.")
                    continue
                phrase = f"POST {secrets.token_hex(4).upper()} TO {len(sub)} PRS AS {label}"
                manifest = approval_manifest(label, sub, body, REPO_OWNER, REPO_NAME)
                if not prompt_approve_post(manifest, phrase):
                    print("Cancelled (phrase mismatch or empty).")
                    continue
                delay_sec = float(os.getenv("GITHUB_COMMENT_DELAY_SECONDS", "5"))
                print(
                    f"Posting with {delay_sec}s pause between PRs (set GITHUB_COMMENT_DELAY_SECONDS "
                    "to reduce secondary rate limits). Retries use backoff inside post_issue_comment."
                )
                ok = 0
                for i, r in enumerate(sub):
                    try:
                        post_issue_comment(REPO_OWNER, REPO_NAME, r.number, body, token)
                        ok += 1
                        print(f"  posted #{r.number}")
                    except Exception as e:
                        print(f"  ERROR #{r.number}: {e}")
                    if i + 1 < len(sub):
                        time.sleep(delay_sec)
                print(f"Done: {ok}/{len(sub)} comments posted.")
        else:
            print("Unknown choice.")


def run_interactive(course_id: str, live: bool, allow_post: bool) -> int:
    courses = discover_courses()
    if course_id not in courses:
        print(f"Unknown course {course_id!r}. Known: {', '.join(sorted(courses))}")
        return 2
    course = courses[course_id]
    token = os.getenv("GITHUB_TOKEN") or None
    roster = roster_prn_set(course)

    while True:
        misbased: List[dict] = []
        if live:
            if not token:
                print(
                    f"Warning: GITHUB_TOKEN not set after loading {_ENV_PATH!r}. "
                    "Without it, GitHub allows ~60 API calls/hour (rate limit on check-runs)."
                )
            try:

                def _live_progress(msg: str) -> None:
                    print(f"  → {msg}", flush=True)

                print("Loading from GitHub…", flush=True)
                all_open = list_all_open_pulls(
                    REPO_OWNER, REPO_NAME, token, progress=_live_progress
                )
                misbased = misbased_lab_prs(course.id, all_open)
                course_prs = open_prs_for_course(
                    REPO_OWNER,
                    REPO_NAME,
                    course.id,
                    (course.base_branch,),
                    token,
                    all_open=all_open,
                    progress=_live_progress,
                )
                rows = build_digest_rows(
                    owner=REPO_OWNER,
                    repo=REPO_NAME,
                    token=token,
                    course_id=course.id,
                    open_prs=course_prs,
                    roster_prns=roster,
                    progress=_live_progress,
                )
                print("Done.", flush=True)
            except Exception as e:
                print(f"GitHub fetch failed: {e}")
                return 1
        else:
            rows = load_open_rows_from_csv(
                course.pull_requests_csv,
                course.id,
                course.base_branch,
                REPO_OWNER,
                REPO_NAME,
                roster,
            )
            print("(offline mode: no mis-based scan; checks unknown — use --live)")

        action = interactive_menu(
            course, rows, misbased, token, allow_post and bool(token), live=live
        )
        if action == "refresh":
            continue
        if action == "quit":
            break
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Interactive PR workflow console (human-in-the-loop).")
    ap.add_argument(
        "--course",
        default="",
        help="Course id (daa, dbms, …). If omitted, you will be prompted.",
    )
    ap.add_argument(
        "--live",
        action="store_true",
        help="Fetch open PRs and check runs from GitHub (recommended).",
    )
    ap.add_argument(
        "--allow-github-post",
        action="store_true",
        help="Enable API posting without asking (for scripts/CI). "
        "Default: you are asked at startup (y/N).",
    )
    args = ap.parse_args()

    if args.allow_github_post:
        allow_post = True
    elif sys.stdin.isatty():
        print(
            "Enable GitHub API for the (p)ost action? "
            "You still type a unique approval phrase for each batch; nothing is sent without that. [y/N] ",
            end="",
            flush=True,
        )
        try:
            allow_post = input().strip().lower() in ("y", "yes")
        except EOFError:
            allow_post = False
        print()
    else:
        allow_post = False

    course_id = args.course.strip().lower()
    if not course_id:
        courses = discover_courses()
        print("Courses:")
        for cid, c in sorted(courses.items()):
            print(
                f"  [{cid}] {c.label} — merge base sub-lab-{cid}-NN; "
                f"CSV/legacy base {c.base_branch!r}"
            )
        course_id = input("Course id: ").strip().lower()
    if not args.live:
        print("Tip: use --live for accurate check status and mis-targeted lab PRs.")
    return run_interactive(course_id, live=args.live, allow_post=allow_post)


if __name__ == "__main__":
    raise SystemExit(main())
