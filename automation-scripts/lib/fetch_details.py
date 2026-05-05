"""Fetch maximum PR details (open + merged) per course from GitHub REST API.

Collected per PR:
  - Full PR metadata (additions, deletions, changed_files, body, labels, …)
  - All commits with per-commit stats and files touched
  - All changed files (PR-level)
  - Reviews
  - Issue-thread comments

Output is a list of dicts suitable for ``json.dump``.
"""

from __future__ import annotations

import json
import os
import re
import time
from typing import Callable, Dict, List, Optional, Tuple

import requests

from lib.pr_workflow import (
    github_headers,
    extract_prn,
    integration_base_ok,
    lab_head_branch_pattern,
    rate_limit_sleep,
)


# ---------------------------------------------------------------------------
# Low-level paged fetchers
# ---------------------------------------------------------------------------

def _get_paged(url: str, hdrs: Dict, params: Dict | None = None) -> List[dict]:
    out: List[dict] = []
    page = 1
    while True:
        p = dict(params or {})
        p.update({"per_page": 100, "page": page})
        rate_limit_sleep()
        r = requests.get(url, headers=hdrs, params=p, timeout=60)
        r.raise_for_status()
        chunk = r.json()
        if not chunk:
            break
        if isinstance(chunk, list):
            out.extend(chunk)
        else:
            out.append(chunk)
            break
        page += 1
    return out


# ---------------------------------------------------------------------------
# PR list (all states)
# ---------------------------------------------------------------------------

def list_all_prs(
    owner: str,
    repo: str,
    token: Optional[str],
    progress: Optional[Callable[[str], None]] = None,
) -> List[dict]:
    """Return all PRs (open + closed/merged), paginated."""
    hdrs = github_headers(token)
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    out: List[dict] = []
    page = 1
    while True:
        rate_limit_sleep()
        r = requests.get(url, headers=hdrs, params={"state": "all", "per_page": 100, "page": page}, timeout=60)
        r.raise_for_status()
        chunk = r.json()
        if not chunk:
            break
        out.extend(chunk)
        if progress:
            progress(f"listing PRs: page {page} → {len(out)} so far")
        page += 1
    if progress:
        progress(f"listing PRs: done — {len(out)} total")
    return out


def filter_course_prs(
    course_id: str,
    base_branch: str,
    prs: List[dict],
) -> List[dict]:
    """Keep PRs that belong to this course (open or merged/closed)."""
    head_pat = lab_head_branch_pattern(course_id)
    legacy = {base_branch.strip()} if base_branch.strip() else set()
    out: List[dict] = []
    for pr in prs:
        b = (pr.get("base") or {}).get("ref") or ""
        h = (pr.get("head") or {}).get("ref") or ""
        if integration_base_ok(b, course_id) or head_pat.match(h) or b in legacy:
            out.append(pr)
    return out


# ---------------------------------------------------------------------------
# Per-PR detail fetchers
# ---------------------------------------------------------------------------

def fetch_pr_full(owner: str, repo: str, number: int, token: Optional[str]) -> dict:
    """Full PR object — includes additions/deletions/changed_files/body."""
    hdrs = github_headers(token)
    rate_limit_sleep()
    r = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}",
        headers=hdrs,
        timeout=60,
    )
    r.raise_for_status()
    return r.json()


def fetch_pr_commits_detailed(
    owner: str,
    repo: str,
    number: int,
    token: Optional[str],
) -> List[dict]:
    """Commits for a PR, each enriched with per-commit stats and files."""
    hdrs = github_headers(token)
    commits = _get_paged(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}/commits", hdrs
    )
    result: List[dict] = []
    for c in commits:
        sha = c.get("sha", "")
        commit_meta = c.get("commit") or {}
        author = commit_meta.get("author") or {}
        committer = commit_meta.get("committer") or {}

        entry: dict = {
            "sha": sha,
            "author_name": author.get("name", ""),
            "author_email": author.get("email", ""),
            "author_date": author.get("date", ""),
            "committer_name": committer.get("name", ""),
            "committer_date": committer.get("date", ""),
            "message": commit_meta.get("message", ""),
            "comment_count": commit_meta.get("comment_count", 0),
            "stats": {},
            "files": [],
        }

        # Fetch commit details for stats + files
        try:
            rate_limit_sleep()
            cr = requests.get(
                f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}",
                headers=hdrs,
                timeout=60,
            )
            cr.raise_for_status()
            cdata = cr.json()
            entry["stats"] = cdata.get("stats") or {}
            entry["files"] = [
                {
                    "filename": f.get("filename", ""),
                    "status": f.get("status", ""),
                    "additions": f.get("additions", 0),
                    "deletions": f.get("deletions", 0),
                    "changes": f.get("changes", 0),
                }
                for f in (cdata.get("files") or [])
            ]
        except Exception:
            pass

        result.append(entry)
    return result


def fetch_pr_files(owner: str, repo: str, number: int, token: Optional[str]) -> List[dict]:
    hdrs = github_headers(token)
    raw = _get_paged(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}/files", hdrs
    )
    return [
        {
            "filename": f.get("filename", ""),
            "status": f.get("status", ""),
            "additions": f.get("additions", 0),
            "deletions": f.get("deletions", 0),
            "changes": f.get("changes", 0),
            "previous_filename": f.get("previous_filename", ""),
        }
        for f in raw
    ]


def fetch_pr_reviews(owner: str, repo: str, number: int, token: Optional[str]) -> List[dict]:
    hdrs = github_headers(token)
    raw = _get_paged(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}/reviews", hdrs
    )
    return [
        {
            "id": rv.get("id"),
            "user": (rv.get("user") or {}).get("login", ""),
            "state": rv.get("state", ""),
            "submitted_at": rv.get("submitted_at", ""),
            "body": rv.get("body", ""),
        }
        for rv in raw
    ]


def fetch_pr_issue_comments(
    owner: str, repo: str, number: int, token: Optional[str]
) -> List[dict]:
    hdrs = github_headers(token)
    raw = _get_paged(
        f"https://api.github.com/repos/{owner}/{repo}/issues/{number}/comments", hdrs
    )
    return [
        {
            "id": c.get("id"),
            "user": (c.get("user") or {}).get("login", ""),
            "created_at": c.get("created_at", ""),
            "updated_at": c.get("updated_at", ""),
            "body": c.get("body", ""),
        }
        for c in raw
    ]


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def fetch_all_pr_details(
    owner: str,
    repo: str,
    prs: List[dict],
    token: Optional[str],
    progress: Optional[Callable[[str], None]] = None,
) -> List[dict]:
    """
    For each PR in *prs*, fetch full metadata, commits (with file stats), files,
    reviews, and issue comments.  Returns a list of enriched dicts.
    """
    result: List[dict] = []
    total = len(prs)
    for idx, pr in enumerate(prs, 1):
        number = pr["number"]
        title = pr.get("title", "")
        prn = extract_prn(title)
        head_ref = (pr.get("head") or {}).get("ref", "")
        base_ref = (pr.get("base") or {}).get("ref", "")
        state = pr.get("state", "")
        merged_at = pr.get("merged_at") or ""

        if progress:
            progress(f"[{idx}/{total}] PR #{number} ({prn}) — {state}")

        try:
            full = fetch_pr_full(owner, repo, number, token)
        except Exception as e:
            if progress:
                progress(f"  PR #{number}: full fetch failed — {e}")
            full = pr  # fall back to index data

        try:
            commits = fetch_pr_commits_detailed(owner, repo, number, token)
        except Exception as e:
            if progress:
                progress(f"  PR #{number}: commits failed — {e}")
            commits = []

        try:
            files = fetch_pr_files(owner, repo, number, token)
        except Exception as e:
            if progress:
                progress(f"  PR #{number}: files failed — {e}")
            files = []

        try:
            reviews = fetch_pr_reviews(owner, repo, number, token)
        except Exception as e:
            if progress:
                progress(f"  PR #{number}: reviews failed — {e}")
            reviews = []

        try:
            comments = fetch_pr_issue_comments(owner, repo, number, token)
        except Exception as e:
            if progress:
                progress(f"  PR #{number}: comments failed — {e}")
            comments = []

        result.append({
            "number": number,
            "prn": prn,
            "title": title,
            "state": state,
            "merged": bool(merged_at),
            "draft": full.get("draft", False),
            "head_ref": head_ref,
            "base_ref": base_ref,
            "url": full.get("html_url", pr.get("html_url", "")),
            "user": (full.get("user") or {}).get("login", ""),
            "created_at": full.get("created_at", pr.get("created_at", "")),
            "updated_at": full.get("updated_at", pr.get("updated_at", "")),
            "closed_at": full.get("closed_at") or "",
            "merged_at": full.get("merged_at") or "",
            "body": full.get("body") or "",
            "labels": [lb["name"] for lb in (full.get("labels") or [])],
            "additions": full.get("additions", 0),
            "deletions": full.get("deletions", 0),
            "changed_files": full.get("changed_files", 0),
            "commits_count": full.get("commits", 0),
            "comments_count": full.get("comments", 0),
            "review_comments_count": full.get("review_comments", 0),
            "commits": commits,
            "files": files,
            "reviews": reviews,
            "issue_comments": comments,
        })

    return result


# ---------------------------------------------------------------------------
# Incremental cache helpers (used by fetch_pr.py and pr_console)
# ---------------------------------------------------------------------------

def load_details_cache(path: str) -> Dict[int, dict]:
    """Load existing pr_details.json into a {number: record} dict."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return {int(d["number"]): d for d in data if "number" in d}
    except Exception as e:
        print(f"  Warning: could not load cache {path}: {e}")
        return {}


def save_details_cache(path: str, records: Dict[int, dict]) -> None:
    """Write cache back to pr_details.json sorted by PR number."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sorted(records.values(), key=lambda d: d["number"]), f, indent=2, ensure_ascii=False)


def needs_refetch(cached: dict, pr_index: dict) -> bool:
    """True if a cached record is stale relative to the PR index entry."""
    same_state = cached.get("state") == pr_index.get("state")
    same_updated = cached.get("updated_at", "") == (pr_index.get("updated_at") or "")
    same_merged = bool(cached.get("merged")) == bool(pr_index.get("merged_at"))
    return not (same_state and same_updated and same_merged)
