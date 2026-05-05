#!/usr/bin/env python3
"""
Analyze pr_details.json:
  - Export flat CSVs (pr_flat, pr_commits, pr_files, pr_comments)
  - Extract .sql files per student per lab (depth 1 only) → sql_cleaned/
  - Normalize SQL: strip comments, unify casing, one statement per line
  - Plagiarism detection (pairwise similarity per lab)
  - Student behavior flags (late night, fast completion, bulk, etc.)
  - Output: output/{course}/analysis/pr_analysis.json

Usage:
  python3 analyze_pr.py --course dbms
  python3 analyze_pr.py --course dbms --no-csv --threshold 0.75
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from difflib import SequenceMatcher
from typing import Dict, List, Optional, Set, Tuple

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from lib.lab_course import LabCourse, repo_root_from_scripts
from lib.common import ensure_dir

IST = timezone(timedelta(hours=5, minutes=30))


# ------------------------------------------------------------------
# Load
# ------------------------------------------------------------------

def load_prs(course: LabCourse) -> List[dict]:
    path = course.path_in_output("pr_details.json")
    if not os.path.exists(path):
        sys.exit(f"Not found: {path}\nRun: python3 fetch_pr.py --course {course.id}")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return list(data.values()) if isinstance(data, dict) else data


def infer_lab(head_ref: str, course: LabCourse) -> Optional[int]:
    subject = re.escape(course.id)
    m = re.search(rf"lab[-_]{subject}[-_](\d+)", head_ref, re.I)
    if m:
        return int(m.group(1))
    return None


def _parse_dt(s: str) -> Optional[datetime]:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def _to_ist(dt: datetime) -> datetime:
    return dt.astimezone(IST)


_EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\u2600-\u27BF"
    "\u26A0\uFE0F"
    "]+",
    flags=re.UNICODE,
)


def _strip_emoji(s: str) -> str:
    return _EMOJI_RE.sub("", s).strip()


# ------------------------------------------------------------------
# Export CSVs
# ------------------------------------------------------------------

def export_csvs(prs: List[dict], course: LabCourse) -> None:
    out = course.output_dir
    ensure_dir(out)

    flat_fields = [
        "number", "prn", "user", "state", "merged", "draft", "head_ref", "base_ref",
        "created_at", "updated_at", "closed_at", "merged_at", "title",
        "additions", "deletions", "changed_files", "commits_count", "comments_count",
    ]
    with open(os.path.join(out, "pr_flat.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=flat_fields, extrasaction="ignore")
        w.writeheader()
        for pr in prs:
            row = {k: pr.get(k, "") for k in flat_fields}
            row["merged"] = "1" if pr.get("merged") else "0"
            w.writerow(row)

    commit_fields = ["pr_number", "prn", "sha", "author_name", "author_email", "author_date", "message", "additions", "deletions"]
    with open(os.path.join(out, "pr_commits.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=commit_fields)
        w.writeheader()
        for pr in prs:
            for c in pr.get("commits", []):
                stats = c.get("stats") or {}
                w.writerow({
                    "pr_number": pr["number"], "prn": pr.get("prn", ""),
                    "sha": c.get("sha", ""), "author_name": c.get("author_name", ""),
                    "author_email": c.get("author_email", ""),
                    "author_date": c.get("author_date", ""),
                    "message": (c.get("message") or "")[:200],
                    "additions": stats.get("additions", 0),
                    "deletions": stats.get("deletions", 0),
                })

    file_fields = ["pr_number", "prn", "filename", "status", "additions", "deletions", "changes"]
    with open(os.path.join(out, "pr_files.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=file_fields)
        w.writeheader()
        for pr in prs:
            for fi in pr.get("files", []):
                w.writerow({
                    "pr_number": pr["number"], "prn": pr.get("prn", ""),
                    "filename": fi.get("filename", ""), "status": fi.get("status", ""),
                    "additions": fi.get("additions", 0),
                    "deletions": fi.get("deletions", 0),
                    "changes": fi.get("changes", 0),
                })

    comment_fields = ["pr_number", "prn", "id", "user", "created_at", "body"]
    with open(os.path.join(out, "pr_comments.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=comment_fields)
        w.writeheader()
        for pr in prs:
            for cm in pr.get("issue_comments", []):
                w.writerow({
                    "pr_number": pr["number"], "prn": pr.get("prn", ""),
                    "id": cm.get("id", ""), "user": cm.get("user", ""),
                    "created_at": cm.get("created_at", ""),
                    "body": (cm.get("body") or "")[:300],
                })

    print(f"CSVs: {out}/pr_flat.csv, pr_commits.csv, pr_files.csv, pr_comments.csv")


# ------------------------------------------------------------------
# Problem-set seed extraction from git orphan branches
# ------------------------------------------------------------------

# Map lab number → problem set branch name
PROBLEM_SET_BRANCHES = {
    0: "lab-dbms-00",
    1: "lab-dbms-01",
    2: "lab-dbms-02",
    3: "lab-dbms-03",
    4: "lab-dbms-04",
    5: "lab-dbms-05-v2",
    6: "lab-dbms-06-v2",
}


def _git_show(branch: str, filename: str, repo_root: str) -> Optional[str]:
    try:
        result = subprocess.run(
            ["git", "show", f"{branch}:{filename}"],
            cwd=repo_root,
            capture_output=True, text=True, timeout=10,
        )
        return result.stdout if result.returncode == 0 else None
    except Exception:
        return None


def _git_ls_sql(branch: str, repo_root: str) -> List[str]:
    try:
        result = subprocess.run(
            ["git", "ls-tree", "--name-only", branch],
            cwd=repo_root,
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode != 0:
            return []
        return [f for f in result.stdout.splitlines() if f.lower().endswith(".sql")]
    except Exception:
        return []


def load_problem_set_stmts(course: LabCourse) -> Dict[int, Set[str]]:
    """
    Returns {lab: set_of_normalized_statements} from the problem-set git branches.
    Only for DBMS currently; other courses return empty.
    """
    if course.id != "dbms":
        return {}

    repo_root = repo_root_from_scripts()
    result: Dict[int, Set[str]] = {}

    for lab, branch in PROBLEM_SET_BRANCHES.items():
        sql_files = _git_ls_sql(branch, repo_root)
        stmts: Set[str] = set()
        for fname in sql_files:
            raw = _git_show(branch, fname, repo_root)
            if not raw:
                continue
            for stmt in clean_sql(raw).splitlines():
                s = stmt.strip()
                if s:
                    stmts.add(s)
        if stmts:
            result[lab] = stmts
            print(f"  Problem set lab {lab:02d} ({branch}): {len(stmts)} seed statements")

    return result


# ------------------------------------------------------------------
# SQL extraction and cleaning
# ------------------------------------------------------------------

def clean_sql(content: str) -> str:
    """Remove comments, normalize casing, one statement per line."""
    content = re.sub(r"/\*.*?\*/", " ", content, flags=re.DOTALL)
    content = re.sub(r"--[^\n]*", "", content)
    stmts = content.split(";")
    cleaned = []
    for s in stmts:
        s = re.sub(r"\s+", " ", s).strip().upper()
        if s:
            cleaned.append(s + ";")
    return "\n".join(cleaned)


def _subtract_seed(cleaned: str, seed_stmts: Set[str]) -> str:
    """Remove statements from student SQL that appear verbatim in the problem set."""
    significant = []
    for line in cleaned.splitlines():
        s = line.strip()
        if s and s not in seed_stmts:
            significant.append(s)
    return "\n".join(significant)


def extract_and_clean_sql(
    prs: List[dict], course: LabCourse, labs: Optional[List[int]] = None
) -> Dict[int, Dict[str, List[str]]]:
    """
    For each merged PR:
     - Extract .sql files (depth 1)
     - Save normalized to sql_cleaned/{lab:02d}/{prn}/
     - Subtract problem-set seed → save to sql_significant/{lab:02d}/{prn}/
    Returns {lab: {prn: [significant_content, ...]}} for plagiarism.
    """
    repo_root = repo_root_from_scripts()
    allowed_labs = set(labs) if labs else set(course.lab_numbers())

    print("Loading problem-set seed statements...")
    seed: Dict[int, Set[str]] = load_problem_set_stmts(course)

    # Latest merged PR per (prn, lab)
    best: Dict[Tuple[str, int], dict] = {}
    for pr in prs:
        if not pr.get("merged"):
            continue
        prn = (pr.get("prn") or "").strip().upper()
        if not prn:
            continue
        lab = infer_lab(pr.get("head_ref", ""), course)
        if lab is None or lab not in allowed_labs:
            continue
        key = (prn, lab)
        if key not in best or (pr.get("merged_at") or "") > (best[key].get("merged_at") or ""):
            best[key] = pr

    result: Dict[int, Dict[str, List[str]]] = {}

    for (prn, lab), pr in best.items():
        lab_dir = os.path.join(repo_root, course.labs_repo_subdir, f"lab-{lab:02d}", prn)
        if not os.path.isdir(lab_dir):
            continue

        sql_files = [
            os.path.join(lab_dir, name)
            for name in os.listdir(lab_dir)
            if name.lower().endswith(".sql") and os.path.isfile(os.path.join(lab_dir, name))
        ]
        if not sql_files:
            continue

        cleaned_dir = course.path_in_output(f"sql_cleaned/{lab:02d}/{prn}")
        sig_dir = course.path_in_output(f"sql_significant/{lab:02d}/{prn}")
        ensure_dir(cleaned_dir)
        ensure_dir(sig_dir)

        lab_seed = seed.get(lab, set())
        significant_contents = []

        for abs_path in sorted(sql_files):
            try:
                with open(abs_path, encoding="utf-8", errors="replace") as f:
                    raw = f.read()
            except Exception:
                continue
            cleaned = clean_sql(raw)
            if not cleaned.strip():
                continue
            fname = os.path.basename(abs_path)
            with open(os.path.join(cleaned_dir, fname), "w", encoding="utf-8") as f:
                f.write(cleaned)

            sig = _subtract_seed(cleaned, lab_seed)
            if sig.strip():
                with open(os.path.join(sig_dir, fname), "w", encoding="utf-8") as f:
                    f.write(sig)
                significant_contents.append(sig)

        if significant_contents:
            result.setdefault(lab, {})[prn] = significant_contents

    total = sum(len(v) for v in result.values())
    print(f"SQL extracted: {total} students across {len(result)} labs")
    print(f"  → sql_cleaned/  (normalized)")
    print(f"  → sql_significant/  (student-added only, used for plagiarism)")
    return result


# ------------------------------------------------------------------
# Plagiarism
# ------------------------------------------------------------------

_LITERAL_RE = re.compile(r"'([^']*)'|\"([^\"]*)\"|([-]?\b\d+(?:\.\d+)?\b)")


def _extract_literals(sql: str) -> str:
    """Extract only string/numeric literals from SQL — what the student actually chose."""
    return " ".join(
        m.group(1) or m.group(2) or m.group(3)
        for m in _LITERAL_RE.finditer(sql)
    ).upper()

def run_plagiarism(
    sql_data: Dict[int, Dict[str, List[str]]],
    course: LabCourse,
    threshold: float = 0.85,
    min_chars: int = 30,
) -> Tuple[Dict[int, List[dict]], Dict[int, Dict[str, float]]]:
    """
    Pairwise comparison on sql_significant content using LITERAL VALUES only.
    Returns (matches_above_threshold, per_student_max_similarity).
    max_similarity per student: lower = more unique.
    """
    out = course.path_in_output("analysis")
    ensure_dir(out)
    all_matches: Dict[int, List[dict]] = {}
    uniqueness_scores: Dict[int, Dict[str, float]] = {}  # lab → prn → max_sim

    for lab, prn_map in sorted(sql_data.items()):
        prns = sorted(prn_map.keys())
        matches = []
        lab_max_sim: Dict[str, float] = {prn: 0.0 for prn in prns}
        for i, prn_a in enumerate(prns):
            for prn_b in prns[i + 1:]:
                best_sim = 0.0
                for ca in prn_map[prn_a]:
                    for cb in prn_map[prn_b]:
                        la_vals = _extract_literals(ca)
                        lb_vals = _extract_literals(cb)
                        if len(la_vals) < min_chars or len(lb_vals) < min_chars:
                            continue
                        sim = SequenceMatcher(None, la_vals, lb_vals).ratio()
                        best_sim = max(best_sim, sim)
                if best_sim > 0:
                    lab_max_sim[prn_a] = max(lab_max_sim[prn_a], best_sim)
                    lab_max_sim[prn_b] = max(lab_max_sim[prn_b], best_sim)
                if best_sim >= threshold:
                    matches.append({"lab": lab, "prn_a": prn_a, "prn_b": prn_b, "similarity": round(best_sim, 3)})

        matches.sort(key=lambda m: -m["similarity"])
        all_matches[lab] = matches
        uniqueness_scores[lab] = lab_max_sim

        csv_path = os.path.join(out, f"plagiarism_{lab:02d}.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["lab", "prn_a", "prn_b", "similarity"])
            w.writeheader()
            w.writerows(matches)
        if matches:
            print(f"  Lab {lab:02d}: {len(matches)} similar pairs (>={threshold*100:.0f}%) → {csv_path}")

    return all_matches, uniqueness_scores


# ------------------------------------------------------------------
# Label / review helpers
# ------------------------------------------------------------------

_ISSUE_LABELS: Set[str] = {
    "Duplicate", "Incomplete", "Tests Failed (Non-blocking)",
    "Error! Must Provide PRN", "Error! Please Resubmit",
    "Conflict! Please Give Access to Resolve",
}
_MINOR_MERGED_LABELS: Set[str] = {"Incomplete", "Tests Failed (Non-blocking)"}
_ACCEPTED_LABELS: Set[str] = {"Accepted"}
_BOT_USERS: Set[str] = {"bot-s-m-quadri"}
_BOT_MENTION_RE = re.compile(r"@bot-", re.I)


def _label_names(pr: dict) -> List[str]:
    return [_strip_emoji(l if isinstance(l, str) else l.get("name", "")) for l in pr.get("labels", []) if l]


_LEFTOVER_FILE_RE = re.compile(r"(\.DS_Store|Thumbs\.db|\.solution\.|\.pyc$|__pycache__|backup[_\-\.]|temp[_\-\.]|tmp[_\-\.])")


def _is_leftover_file(filename: str) -> bool:
    base = os.path.basename(filename)
    return bool(_LEFTOVER_FILE_RE.search(base))


def _pr_outcome(pr: dict) -> str:
    """merged | rejected | open | changes_requested"""
    if pr.get("merged"):
        return "merged"
    if pr.get("state") == "closed":
        return "rejected"
    review_states = {r["state"] for r in pr.get("reviews", [])}
    if "CHANGES_REQUESTED" in review_states:
        return "changes_requested"
    return "open"


def _meaningful_comments(pr: dict) -> Tuple[List[dict], List[dict]]:
    """Returns (student_comments, instructor_comments) filtering bots and trigger pings."""
    owner = pr.get("user", "")
    student, instructor = [], []
    for c in pr.get("issue_comments", []):
        user = c.get("user", "")
        body = c.get("body", "")
        if user in _BOT_USERS or _BOT_MENTION_RE.search(body):
            continue
        if user == owner:
            student.append(c)
        else:
            instructor.append(c)
    return student, instructor


_GENERIC_MSG_RE = re.compile(
    r"^\s*(completed?|done|added|updated?|uploaded?|lab\s*\d*|finished?|"
    r"commit\d*|initial\s+commit|files?|work|merge|first|final)\s*[.!]?\s*$",
    re.I,
)


# ------------------------------------------------------------------
# Behavior analysis
# ------------------------------------------------------------------

def run_behavior(prs: List[dict], course: LabCourse) -> Dict[str, Dict[int, List[dict]]]:
    """
    Returns {prn: {lab_or_-1: [flag_dict, ...]}}
    lab=-1 means cross-lab flag.
    Each flag_dict has at minimum {"type": str, ...}.
    """
    by_prn: Dict[str, List[dict]] = {}
    for pr in prs:
        prn = (pr.get("prn") or "").strip().upper()
        if not prn:
            continue
        by_prn.setdefault(prn, []).append(pr)

    result: Dict[str, Dict[int, List[dict]]] = {}

    for prn, prn_prs in by_prn.items():
        flags: Dict[int, List[dict]] = {}

        def flag(lab_key: Optional[int], f: dict) -> None:
            flags.setdefault(lab_key if lab_key is not None else -1, []).append(f)

        pr_with_labs = [(pr, infer_lab(pr.get("head_ref", ""), course)) for pr in prn_prs]

        # Per lab
        seen_labs: Dict[int, List[dict]] = {}
        for pr, lab in pr_with_labs:
            if lab is not None:
                seen_labs.setdefault(lab, []).append(pr)

        for lab, lab_prs in seen_labs.items():
            # --- Attempt history (single or multiple PRs) ---
            sorted_attempts = sorted(lab_prs, key=lambda p: p.get("created_at", ""))
            if len(sorted_attempts) > 1:
                attempts_summary = []
                for att in sorted_attempts:
                    outcome = _pr_outcome(att)
                    issue_lbls = [l for l in _label_names(att) if l in _ISSUE_LABELS]
                    accepted = any(l in _ACCEPTED_LABELS for l in _label_names(att))
                    review_states = list({r["state"] for r in att.get("reviews", [])})
                    attempts_summary.append({
                        "pr_number": att["number"],
                        "outcome": outcome,
                        "accepted": accepted,
                        "issue_labels": issue_lbls,
                        "review_states": review_states,
                    })
                flag(lab, {"type": "attempt_history", "attempts": attempts_summary})

            for pr in lab_prs:
                outcome = _pr_outcome(pr)
                labels = _label_names(pr)
                issue_lbls = [l for l in labels if l in _ISSUE_LABELS]
                accepted = any(l in _ACCEPTED_LABELS for l in labels)
                review_states_set = {r["state"] for r in pr.get("reviews", [])}

                # --- Acceptance / rejection ---
                if outcome == "rejected" or (outcome == "open" and issue_lbls):
                    flag(lab, {"type": "rejected_pr", "pr_number": pr["number"],
                               "issue_labels": issue_lbls, "accepted": False})
                elif outcome == "changes_requested":
                    flag(lab, {"type": "review_changes_requested", "pr_number": pr["number"],
                               "issue_labels": issue_lbls})

                # --- Issue labels on merged PRs (skip minor ones) ---
                serious_lbls = [l for l in issue_lbls if l not in _MINOR_MERGED_LABELS]
                if serious_lbls and outcome == "merged":
                    flag(lab, {"type": "label_issue", "pr_number": pr["number"], "labels": serious_lbls})

                # --- Student conversation on PR (effort signal) ---
                student_comments, instructor_comments = _meaningful_comments(pr)
                if student_comments or instructor_comments:
                    flag(lab, {"type": "conversation", "pr_number": pr["number"],
                               "student_comments": len(student_comments),
                               "instructor_comments": len(instructor_comments)})

                commits = pr.get("commits", [])

                # --- Generic commit messages ---
                generic = [c["message"].split("\n")[0].strip() for c in commits
                           if _GENERIC_MSG_RE.match((c.get("message") or "").split("\n")[0])]
                if len(generic) >= 3 or (commits and len(generic) / max(len(commits), 1) >= 0.8):
                    flag(lab, {"type": "generic_commits", "pr_number": pr["number"],
                               "generic_count": len(generic), "total_commits": len(commits),
                               "samples": generic[:3]})

                # --- No SQL files submitted (for SQL-based courses) ---
                sql_files = [f["filename"] for f in pr.get("files", []) if f["filename"].endswith(".sql")]
                if pr.get("merged") and not sql_files and pr.get("changed_files", 0) > 0:
                    flag(lab, {"type": "no_sql_submitted", "pr_number": pr["number"],
                               "changed_files": pr.get("changed_files", 0)})

                # --- Solution file submitted (answer key committed) ---
                sol_files = [f["filename"] for f in pr.get("files", [])
                             if re.search(r'\.solution\.', os.path.basename(f["filename"]), re.I)]
                if sol_files:
                    flag(lab, {"type": "solution_file_submitted", "pr_number": pr["number"],
                               "files": sol_files})

                # --- Late night: use commit author_date (student's action, not instructor's merge) ---
                late_night: Optional[Tuple[datetime, dict]] = None
                for c in commits:
                    cdt = _parse_dt(c.get("author_date", ""))
                    if not cdt:
                        continue
                    ist = _to_ist(cdt)
                    if ist.hour >= 22 or ist.hour < 5:
                        if late_night is None:
                            late_night = (ist, c)
                        else:
                            prev_h = late_night[0].hour
                            cur_h = ist.hour
                            if (cur_h if cur_h >= 5 else cur_h + 24) > (prev_h if prev_h >= 5 else prev_h + 24):
                                late_night = (ist, c)
                if late_night:
                    ist, c = late_night
                    flag(lab, {"type": "late_night", "pr_number": pr["number"],
                               "commit_sha": c.get("sha", ""), "datetime_ist": ist.isoformat()})

                # --- Fast completion (first → last commit span) ---
                dates = sorted(d for d in (_parse_dt(c.get("author_date", "")) for c in commits) if d)
                if len(dates) >= 2:
                    span = (dates[-1] - dates[0]).total_seconds()
                    if span < 600:
                        flag(lab, {"type": "fast_completion", "pr_number": pr["number"],
                                   "commits": len(commits), "span_seconds": int(span)})

                # --- High commit count ---
                if len(commits) > 15:
                    flag(lab, {"type": "high_commit_count", "pr_number": pr["number"], "commits": len(commits)})

                # --- Empty merged PR ---
                if pr.get("changed_files", 0) == 0 and pr.get("merged"):
                    flag(lab, {"type": "empty_merged_pr", "pr_number": pr["number"]})

        # Cross-lab: multiple PRs on same day (use created_at — student opened PR)
        pr_dates: List[Tuple[datetime, int, int]] = []
        for pr, lab in pr_with_labs:
            if lab is None:
                continue
            dt = _parse_dt(pr.get("created_at", ""))
            if dt:
                pr_dates.append((_to_ist(dt), lab, pr["number"]))

        by_day: Dict[str, List[Tuple[datetime, int, int]]] = {}
        for dt, lab, num in pr_dates:
            by_day.setdefault(dt.strftime("%Y-%m-%d"), []).append((dt, lab, num))

        for day, entries in by_day.items():
            if len(entries) >= 2:
                flag(None, {"type": "bulk_same_day", "date": day,
                            "labs": [l for _, l, _ in entries],
                            "pr_numbers": [n for _, _, n in entries]})

        # Short gap between different labs (< 30 min)
        sorted_pr_dates = sorted(pr_dates, key=lambda x: x[0])
        for i in range(len(sorted_pr_dates) - 1):
            dt1, lab1, num1 = sorted_pr_dates[i]
            dt2, lab2, num2 = sorted_pr_dates[i + 1]
            gap = (dt2 - dt1).total_seconds()
            if 0 < gap < 1800 and lab1 != lab2:
                flag(None, {"type": "rapid_succession", "lab_a": lab1, "lab_b": lab2,
                            "gap_minutes": int(gap // 60), "pr_a": num1, "pr_b": num2})

        if flags:
            result[prn] = flags

    return result


# ------------------------------------------------------------------
# Positive analysis
# ------------------------------------------------------------------

def _percentile_tier(rank_1_best: int, total: int) -> Optional[int]:
    """Returns top-X% tier (10/20/30/40/50) if in top 50%, else None."""
    pct = rank_1_best / total * 100
    for tier in [10, 20, 30, 40, 50]:
        if pct <= tier:
            return tier
    return None


def run_positive(
    prs: List[dict],
    sql_data: Dict[int, Dict[str, List[str]]],
    uniqueness_scores: Dict[int, Dict[str, float]],
    course: LabCourse,
) -> Dict[str, Dict[int, List[dict]]]:
    result: Dict[str, Dict[int, List[dict]]] = {}

    def pflag(prn: str, lab_key: Optional[int], f: dict) -> None:
        result.setdefault(prn, {}).setdefault(lab_key if lab_key is not None else -1, []).append(f)

    # --- Uniqueness percentile (per lab) ---
    for lab, prn_scores in uniqueness_scores.items():
        ranked = sorted(prn_scores.items(), key=lambda x: x[1])  # ascending: low sim = unique = best
        for rank_0, (prn, max_sim) in enumerate(ranked):
            tier = _percentile_tier(rank_0 + 1, len(ranked))
            if tier is not None:
                pflag(prn, lab, {"type": "unique_submission", "lab": lab,
                                 "uniqueness_score": round(1 - max_sim, 3),
                                 "top_percentile": tier})

    # --- Commit quality percentile (per lab, merged PRs only) ---
    cq_scores: Dict[int, Dict[str, float]] = {}
    for pr in prs:
        prn = (pr.get("prn") or "").strip().upper()
        if not prn or not pr.get("merged"):
            continue
        lab = infer_lab(pr.get("head_ref", ""), course)
        if lab is None:
            continue
        commits = pr.get("commits", [])
        if not commits:
            continue
        generic = sum(1 for c in commits if _GENERIC_MSG_RE.match((c.get("message") or "").split("\n")[0]))
        score = 1 - generic / len(commits)
        cq_scores.setdefault(lab, {})[prn] = max(cq_scores.get(lab, {}).get(prn, 0.0), score)

    for lab, prn_scores in cq_scores.items():
        ranked = sorted(prn_scores.items(), key=lambda x: -x[1])
        for rank_0, (prn, score) in enumerate(ranked):
            if score < 0.5:
                continue
            tier = _percentile_tier(rank_0 + 1, len(ranked))
            if tier is not None:
                pflag(prn, lab, {"type": "commit_quality", "lab": lab,
                                 "quality_score": round(score, 3),
                                 "top_percentile": tier})

    # --- Per-student per-lab ---
    by_prn: Dict[str, List[dict]] = {}
    for pr in prs:
        prn = (pr.get("prn") or "").strip().upper()
        if prn:
            by_prn.setdefault(prn, []).append(pr)

    for prn, prn_prs in by_prn.items():
        pr_with_labs = [(pr, infer_lab(pr.get("head_ref", ""), course)) for pr in prn_prs]
        seen_labs: Dict[int, List[dict]] = {}
        for pr, lab in pr_with_labs:
            if lab is not None:
                seen_labs.setdefault(lab, []).append(pr)

        for lab, lab_prs in seen_labs.items():
            merged_prs = [p for p in lab_prs if p.get("merged")]
            if not merged_prs:
                continue

            best_pr = sorted(merged_prs, key=lambda p: p.get("created_at", ""))[0]
            issue_lbls = [l for l in _label_names(best_pr) if l in _ISSUE_LABELS]
            review_states = {r["state"] for r in best_pr.get("reviews", [])}

            # --- First attempt clean ---
            if len(lab_prs) == 1 and not issue_lbls and "CHANGES_REQUESTED" not in review_states:
                pflag(prn, lab, {"type": "first_attempt_clean", "pr_number": best_pr["number"]})

            # --- Clean submission (no leftover/temp/solution files) ---
            all_files = [f["filename"] for f in best_pr.get("files", [])]
            leftover = [fn for fn in all_files if _is_leftover_file(fn)]
            if all_files and not leftover:
                pflag(prn, lab, {"type": "clean_submission", "pr_number": best_pr["number"],
                                 "files": len(all_files)})

            # --- Iterative development (commits across >= 2 distinct days) ---
            commits = best_pr.get("commits", [])
            days = {_to_ist(d).strftime("%Y-%m-%d")
                    for c in commits
                    for d in [_parse_dt(c.get("author_date", ""))]
                    if d}
            if len(days) >= 2:
                pflag(prn, lab, {"type": "iterative_development", "pr_number": best_pr["number"],
                                 "commit_days": len(days), "total_commits": len(commits)})

    return result


# ------------------------------------------------------------------
# Save combined analysis
# ------------------------------------------------------------------

def save_analysis(
    plagiarism: Dict[int, List[dict]],
    behavior: Dict[str, Dict[int, List[dict]]],
    positive: Dict[str, Dict[int, List[dict]]],
    course: LabCourse,
) -> None:
    out = course.path_in_output("analysis")
    ensure_dir(out)

    # Flatten plagiarism → per-prn per-lab flag dicts
    plag_flags: Dict[str, Dict[int, List[dict]]] = {}
    for lab, matches in plagiarism.items():
        for m in matches:
            for prn in (m["prn_a"], m["prn_b"]):
                other = m["prn_b"] if prn == m["prn_a"] else m["prn_a"]
                plag_flags.setdefault(prn, {}).setdefault(lab, []).append(
                    {"type": "plagiarism", "matched_prn": other, "similarity": round(m["similarity"], 4)}
                )

    # Merge behavior + plagiarism + positive into {prn: {lab_str: [flag_dict]}}
    all_prns = set(behavior) | set(plag_flags) | set(positive)
    merged: Dict[str, Dict[str, List[dict]]] = {}
    for prn in all_prns:
        b = behavior.get(prn, {})
        p = plag_flags.get(prn, {})
        pos = positive.get(prn, {})
        combined: Dict[str, List[dict]] = {}
        for lab in set(b) | set(p) | set(pos):
            combined[str(lab)] = b.get(lab, []) + p.get(lab, []) + pos.get(lab, [])
        if combined:
            merged[prn] = combined

    path = os.path.join(out, "pr_analysis.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)

    flagged = len(merged)
    total_flags = sum(len(v) for d in merged.values() for v in d.values())
    pos_count = sum(1 for d in merged.values() for flags in d.values()
                    for fl in flags if fl.get("type") in {
                        "unique_submission", "commit_quality", "clean_submission",
                        "first_attempt_clean", "iterative_development"})
    print(f"Analysis → {path}")
    print(f"  {flagged} students with entries, {total_flags} total flags ({pos_count} positive)")


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Analyze pr_details.json for a course")
    p.add_argument("--course", default="dbms")
    p.add_argument("--labs", nargs="*", type=int, help="Limit to specific lab numbers")
    p.add_argument("--only", nargs="*", help="Limit to specific PRNs")
    p.add_argument("--no-csv", action="store_true", help="Skip CSV export")
    p.add_argument("--no-plagiarism", action="store_true", help="Skip plagiarism check")
    p.add_argument("--threshold", type=float, default=0.85, help="Literal-value similarity threshold (default 0.85)")
    args = p.parse_args(argv)

    course = LabCourse.load(args.course, root=ROOT)
    prs = load_prs(course)

    if args.only:
        only_upper = {x.upper() for x in args.only}
        prs = [pr for pr in prs if (pr.get("prn") or "").upper() in only_upper]

    print(f"Loaded {len(prs)} PRs for {course.id}")

    if not args.no_csv:
        export_csvs(prs, course)

    sql_data = extract_and_clean_sql(prs, course, args.labs)

    plagiarism: Dict[int, List[dict]] = {}
    uniqueness_scores: Dict[int, Dict[str, float]] = {}
    if not args.no_plagiarism and sql_data:
        print("Plagiarism check...")
        plagiarism, uniqueness_scores = run_plagiarism(sql_data, course, args.threshold, min_chars=50)

    print("Behavior analysis...")
    behavior = run_behavior(prs, course)

    print("Positive analysis...")
    positive = run_positive(prs, sql_data, uniqueness_scores, course)

    save_analysis(plagiarism, behavior, positive, course)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
