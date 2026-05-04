"""Display helpers and action utilities for the interactive PR console."""

from __future__ import annotations

import os
from typing import Dict, List, Sequence

from lib.lab_course import LabCourse
from lib.pr_workflow import CMD_MERGE, CMD_TEST, PRDigestRow, NextStep


def hr(char: str = "─", n: int = 72) -> str:
    return char * n


def print_row_summary(r: PRDigestRow) -> None:
    flags: List[str] = []
    if not r.base_ok:
        flags.append("mis-base")
    if not r.title_clean:
        flags.append("title")
    if not r.prn_on_roster and r.prn != "UNKNOWN":
        flags.append("PRN∉roster")
    if r.draft:
        flags.append("draft")
    lab = f"L{r.lab}" if r.lab is not None else "—"
    fl = ",".join(flags) if flags else "ok"
    print(
        f"  #{r.number:5d}  {r.prn:12s}  {lab:4s}  {r.check_state:8s}  {r.suggested:8s}  {fl:16s}  {r.title[:40]}"
    )


def print_digest(
    course: LabCourse,
    rows: List[PRDigestRow],
    misbased: List[dict],
    *,
    live: bool,
    repo_owner: str,
    repo_name: str,
) -> None:
    print()
    print(hr("═"))
    print(f"Course: {course.label} ({course.id})")
    print(f"Workflow merge base: sub-lab-{course.id}-NN  |  legacy / pre-status base from JSON: {course.base_branch!r}")
    print(f"Repo: {repo_owner}/{repo_name}")
    print(hr("═"))
    print(f"Open PRs linked to this course (sub-lab / lab head / legacy base): {len(rows)}")
    print(f"Subset: lab-{course.id}-* head but base not sub-lab-{course.id}-NN: {len(misbased)}")
    if misbased:
        print("  (Typically needs a status-bot comment; see .github/workflows/status.yml.)")
        for pr in misbased[:20]:
            n = pr["number"]
            head = (pr.get("head") or {}).get("ref")
            base = (pr.get("base") or {}).get("ref")
            print(f"    #{n}  head={head!r}  base={base!r}")
        if len(misbased) > 20:
            print(f"    … and {len(misbased) - 20} more")
    print()
    buckets: Dict[NextStep, List[PRDigestRow]] = {
        k: []
        for k in ("status", "test", "re_test", "incomplete", "fix_ci", "merge", "unknown")
    }
    for r in rows:
        buckets[r.suggested].append(r)

    print(
        "Suggested buckets (labels + Check API + HEAD timing vs bot test comments; "
        "test-submission.yml only auto-parses lab-dbms-* heads today):"
    )
    print("  • Status: body must contain 'Hi @bot-s-m-quadri' and must not contain 'merge' (see status.yml).")
    print(f"  • First test: {CMD_TEST!r}")
    print("  • Re-test: same command after student updated HEAD since last bot test run.")
    print("  • Incomplete: failed-test label but no update since last bot comment (fix work first).")
    print("  • fix_ci: GitHub Actions / Check Runs failure (not bot label outcome).")
    print(f"  • Merge: {CMD_MERGE!r} (@s-m-quadri only)")
    print()
    for name, key in [
        ("(1) Status / title-base cleanup", "status"),
        ("(2) Trigger tests (first run)", "test"),
        ("(3) Re-test after student update", "re_test"),
        ("(4) Incomplete — fix before re-test", "incomplete"),
        ("(5) CI / Actions failed (fix_ci)", "fix_ci"),
        ("(6) Merge (checks green / bot passed)", "merge"),
        ("(7) Draft or unclear", "unknown"),
    ]:
        lst = buckets[key]  # type: ignore
        print(f"{name}: {len(lst)}")
    print()
    print(hr())
    print(f"{'#':>7}  {'PRN':12}  {'Lab':4}  {'checks':8}  {'next':8}  {'flags':16}  title")
    print(hr())
    if not rows:
        if live:
            print(
                "  (No open PRs matched this course — none with base sub-lab-%s-* / lab-%s-* / legacy %r.)"
                % (course.id, course.id, course.base_branch)
            )
        else:
            print(
                "  (No rows — offline CSV has no OPEN rows matching this course. "
                "Use --live or run fetch_pr.py first.)"
            )
    else:
        for r in rows:
            print_row_summary(r)
    print(hr())
    print()


def approval_manifest(
    action: str,
    rows: Sequence[PRDigestRow],
    comment_body: str,
    repo_owner: str,
    repo_name: str,
) -> str:
    lines = [
        hr("═"),
        "APPROVAL MANIFEST — read before posting",
        hr("═"),
        f"Repository: {repo_owner}/{repo_name}",
        f"Action: {action}",
        f"Comments to post (exact body): {comment_body!r}",
        f"Pull requests affected: {len(rows)}",
        hr("-"),
    ]
    for r in rows:
        lines.append(
            f"  #{r.number}  PRN={r.prn}  head={r.head_ref}  base={r.base_ref}  "
            f"checks={r.check_state} ({r.check_detail})  url={r.html_url}"
        )
    lines.append(hr("-"))
    lines.append("This tool will NOT post until you type the approval phrase printed below.")
    lines.append(hr("═"))
    return "\n".join(lines)


def prompt_approve_post(manifest_text: str, phrase: str) -> bool:
    print(manifest_text)
    print()
    print(f"Type this exact phrase to authorize posting ({len(phrase)} chars):")
    print(f"    {phrase}")
    print()
    typed = input("Approval phrase (empty = cancel): ").strip()
    return typed == phrase


def write_batch_file(course: LabCourse, text: str) -> str:
    path = course.path_in_output("pr_console_batch.txt")
    os.makedirs(course.output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def templates_for_rows(rows: Sequence[PRDigestRow], body: str) -> str:
    chunks = [
        f"# Bulk comments: {body!r}",
        "# One block per PR — paste into each conversation.",
        "",
    ]
    for r in rows:
        chunks.append(f"--- PR #{r.number} {r.html_url} ---")
        chunks.append(body)
        chunks.append("")
    return "\n".join(chunks)
