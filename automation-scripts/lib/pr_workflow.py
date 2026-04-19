"""Pull-request workflow helpers for the interactive PR console (read-heavy; optional comment POST).

Aligned with ``geca-labs/.github/workflows``:

- ``status.yml`` — issue comment on PR must **contain** ``Hi @bot-s-m-quadri`` and must **not**
  contain ``merge``. Retargets base to ``sub-lab-{subject}-{NN}``, rewrites title to
  ``Submission of Lab NN by PRN``, blocks direct base ``stable`` (DAA).
- ``test-submission.yml`` — comment must contain ``@bot-s-m-quadri test``. **YAML currently
  only derives the baseline from ``lab-dbms-*`` head branches** (DAA ``lab-daa-*`` is not handled).
- ``merge-organize.yml`` — comment ``@bot-s-m-quadri merge``; base must match
  ``^sub-lab-[a-z]+-[0-9]{2}$``; only ``@s-m-quadri`` may trigger merge step.
"""

from __future__ import annotations

import re
import time
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Literal, Optional, Set, Tuple

import requests

# Bot commands (issue comments on the PR thread)
BOT_HANDLE = "bot-s-m-quadri"
# status.yml matches substring "Hi @bot-s-m-quadri" and rejects comments that contain "merge"
CMD_STATUS = "Hi @bot-s-m-quadri give us the status"
CMD_TEST = "@bot-s-m-quadri test"
CMD_MERGE = "@bot-s-m-quadri merge"

PRN_TITLE_RE = re.compile(
    r"^BT\d{2}[A-Z]\d{2}[A-Z]\d{2}[A-Z]\d{3}\s*$",
    re.IGNORECASE,
)
# After status.yml runs, title becomes this form (see "Update PR title" step)
POST_STATUS_TITLE_RE = re.compile(
    r"^Submission\s+of\s+Lab\s+(\d+)\s+by\s+(BT[0-9A-Z]+)\s*$",
    re.IGNORECASE,
)


def extract_prn(title: str) -> str:
    m = re.search(r"(BT[0-9A-Z]+)", title or "", re.IGNORECASE)
    return m.group(1).upper() if m else "UNKNOWN"


def extract_prn_from_branch(head_ref: str) -> Optional[str]:
    m = re.search(r"(BT[0-9A-Z]+)", head_ref or "", re.IGNORECASE)
    return m.group(1).upper() if m else None


def resolve_prn(title: str, head_ref: str) -> str:
    """PRN from title, else embedded in head branch (status.yml reads both)."""
    pt = extract_prn(title)
    if pt != "UNKNOWN":
        return pt
    ph = extract_prn_from_branch(head_ref)
    return ph if ph else "UNKNOWN"


def integration_base_ok(base_ref: str, course_id: str) -> bool:
    """merge-organize / post-status: base must be ``sub-lab-{subject}-{NN}``."""
    return bool(
        re.match(rf"^sub-lab-{re.escape(course_id)}-\d{{2}}$", base_ref or "", re.IGNORECASE)
    )


def title_nominal_for_workflow(title: str) -> bool:
    """PRN-only student title, or bot-standard title after status.yml."""
    t = (title or "").strip()
    return bool(PRN_TITLE_RE.match(t) or POST_STATUS_TITLE_RE.match(t))


def prn_resolvable(title: str, head_ref: str) -> bool:
    return resolve_prn(title, head_ref) != "UNKNOWN"


def extract_lab_from_labels(labels: str) -> Optional[int]:
    for lbl in (labels or "").split(","):
        m = re.search(r"Lab\s*0*([0-9]+)", lbl.strip(), re.IGNORECASE)
        if m:
            return int(m.group(1))
    return None


def lab_head_branch_pattern(course_id: str) -> re.Pattern[str]:
    return re.compile(rf"^lab-{re.escape(course_id)}-\d+", re.IGNORECASE)


def rate_limit_sleep(seconds: float = 0.12) -> None:
    time.sleep(seconds)


def github_headers(token: Optional[str]) -> Dict[str, str]:
    h: Dict[str, str] = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def list_open_pulls_for_base(
    owner: str, repo: str, base_branch: str, token: Optional[str]
) -> List[dict]:
    """Open PRs targeting ``base_branch`` (paginated)."""
    out: List[dict] = []
    page = 1
    hdrs = github_headers(token)
    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        params = {"state": "open", "base": base_branch, "per_page": 100, "page": page}
        rate_limit_sleep()
        r = requests.get(url, headers=hdrs, params=params, timeout=60)
        r.raise_for_status()
        chunk = r.json()
        if not chunk:
            break
        out.extend(chunk)
        page += 1
    return out


def list_all_open_pulls(
    owner: str,
    repo: str,
    token: Optional[str],
    progress: Optional[Callable[[str], None]] = None,
) -> List[dict]:
    out: List[dict] = []
    page = 1
    hdrs = github_headers(token)
    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        params = {"state": "open", "per_page": 100, "page": page}
        rate_limit_sleep()
        r = requests.get(url, headers=hdrs, params=params, timeout=60)
        r.raise_for_status()
        chunk = r.json()
        if not chunk:
            break
        out.extend(chunk)
        if progress:
            progress(f"listing open PRs: page {page} → {len(out)} so far")
        page += 1
    if progress and out:
        progress(f"listing open PRs: done — {len(out)} open in repo")
    return out


def misbased_lab_prs(course_id: str, open_prs: List[dict]) -> List[dict]:
    """Lab head for this course but base is not ``sub-lab-{course}-{NN}`` (needs status / retarget)."""
    pat = lab_head_branch_pattern(course_id)
    found: List[dict] = []
    for pr in open_prs:
        base_ref = (pr.get("base") or {}).get("ref") or ""
        head_ref = (pr.get("head") or {}).get("ref") or ""
        if pat.match(head_ref) and not integration_base_ok(base_ref, course_id):
            found.append(pr)
    return found


def open_prs_for_course(
    owner: str,
    repo: str,
    course_id: str,
    legacy_integration_bases: Tuple[str, ...],
    token: Optional[str],
    all_open: Optional[List[dict]] = None,
    progress: Optional[Callable[[str], None]] = None,
) -> List[dict]:
    """
    Open PRs belonging to this course: ``sub-lab-{id}-*`` base, ``lab-{id}-*`` head,
    or legacy base from ``courses/*.json`` (e.g. ``stable``, ``dbms``) before status bot runs.

    Pass ``all_open`` from a prior ``list_all_open_pulls`` call to avoid fetching twice.
    """
    if all_open is None:
        all_open = list_all_open_pulls(owner, repo, token, progress=progress)
    head_pat = lab_head_branch_pattern(course_id)
    legacy = {b.strip() for b in legacy_integration_bases if b.strip()}
    out: List[dict] = []
    for pr in all_open:
        b = (pr.get("base") or {}).get("ref") or ""
        h = (pr.get("head") or {}).get("ref") or ""
        if integration_base_ok(b, course_id) or head_pat.match(h) or b in legacy:
            out.append(pr)
    if progress:
        progress(
            f"course filter: {len(out)} PR(s) for {course_id!r} (of {len(all_open)} open in repo)"
        )
    return out


CheckState = Literal["none", "pending", "success", "failure"]


def summarize_check_runs(owner: str, repo: str, sha: str, token: Optional[str]) -> Tuple[CheckState, str]:
    """
    Aggregate GitHub Check Runs for a commit SHA.
    Returns (state, detail line for humans).
    """
    if not sha:
        return "none", "no head SHA"
    hdrs = github_headers(token)
    url = f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}/check-runs"
    rate_limit_sleep()
    r = requests.get(url, headers=hdrs, params={"per_page": 100}, timeout=60)
    if r.status_code == 403:
        err = ""
        try:
            err = r.json().get("message", "")
        except Exception:
            pass
        if "rate limit" in (err + r.reason).lower():
            hint = (
                "rate limited (anonymous = 60/hr); set GITHUB_TOKEN and ensure automation-scripts/.env loads "
                "(needs no python-dotenv)."
            )
            if not token:
                hint += " Currently no token is set on requests."
            return "none", f"checks skipped — {hint}"
        r.raise_for_status()
    if r.status_code == 404:
        return "none", "no check-runs (404)"
    r.raise_for_status()
    runs = r.json().get("check_runs") or []
    if not runs:
        return "none", "no check runs on head commit"

    failures: List[str] = []
    pending: List[str] = []
    success_n = 0
    for run in runs:
        name = run.get("name") or "check"
        status = (run.get("status") or "").lower()
        conclusion = (run.get("conclusion") or "").lower()
        if status in ("queued", "in_progress", "waiting", "requested", "pending"):
            pending.append(name)
        elif conclusion in ("failure", "timed_out", "cancelled", "action_required"):
            failures.append(f"{name}({conclusion})")
        elif conclusion == "success":
            success_n += 1
        elif conclusion in ("skipped", "neutral"):
            continue
        else:
            pending.append(f"{name}?{conclusion or status}")

    if failures:
        return "failure", "failed: " + ", ".join(failures[:6]) + ("…" if len(failures) > 6 else "")
    if pending:
        return "pending", "pending: " + ", ".join(pending[:6]) + ("…" if len(pending) > 6 else "")
    if success_n:
        return "success", f"{success_n} check(s) success"
    return "none", "no decisive check conclusions"


NextStep = Literal["status", "test", "merge", "fix_ci", "unknown"]


@dataclass
class PRDigestRow:
    number: int
    prn: str
    title: str
    user: str
    head_ref: str
    base_ref: str
    labels: str
    lab: Optional[int]
    draft: bool
    html_url: str
    check_state: CheckState
    check_detail: str
    title_clean: bool
    base_ok: bool
    prn_on_roster: bool
    suggested: NextStep
    comment_status: str = field(default=CMD_STATUS)
    comment_test: str = field(default=CMD_TEST)
    comment_merge: str = field(default=CMD_MERGE)


def suggest_next(
    *,
    draft: bool,
    base_ok: bool,
    prn_ok: bool,
    check_state: CheckState,
) -> NextStep:
    if draft:
        return "unknown"
    if not base_ok or not prn_ok:
        return "status"
    if check_state == "failure":
        return "fix_ci"
    if check_state in ("none", "pending"):
        return "test"
    if check_state == "success":
        return "merge"
    return "unknown"


def build_digest_rows(
    *,
    owner: str,
    repo: str,
    token: Optional[str],
    course_id: str,
    open_prs: List[dict],
    roster_prns: Set[str],
    progress: Optional[Callable[[str], None]] = None,
) -> List[PRDigestRow]:
    rows: List[PRDigestRow] = []
    check_cache: Dict[str, Tuple[CheckState, str]] = {}
    unique_shas: List[str] = []
    _seen: Set[str] = set()
    for pr in open_prs:
        s = (pr.get("head") or {}).get("sha") or ""
        if s and s not in _seen:
            _seen.add(s)
            unique_shas.append(s)
    n_shas = len(unique_shas)
    if progress and n_shas:
        progress(f"check runs: {n_shas} unique head commit(s) to query (reused across PRs)")

    fetch_n = 0
    for pr in open_prs:
        num = int(pr["number"])
        title = pr.get("title") or ""
        user = (pr.get("user") or {}).get("login") or ""
        head_ref = (pr.get("head") or {}).get("ref") or ""
        base_ref = (pr.get("base") or {}).get("ref") or ""
        labels_list = [x["name"] for x in pr.get("labels") or []]
        labels = ", ".join(labels_list)
        lab = extract_lab_from_labels(labels)
        draft = bool(pr.get("draft"))
        html_url = pr.get("html_url") or ""
        sha = (pr.get("head") or {}).get("sha") or ""
        prn = resolve_prn(title, head_ref)
        base_ok = integration_base_ok(base_ref, course_id)
        title_clean = title_nominal_for_workflow(title)
        prn_ok = prn_resolvable(title, head_ref)
        prn_on_roster = prn in roster_prns if prn != "UNKNOWN" else False

        if sha and sha in check_cache:
            check_state, check_detail = check_cache[sha]
        else:
            if sha:
                fetch_n += 1
                if progress:
                    progress(
                        f"check runs: fetching {fetch_n}/{n_shas} (PR #{num} {prn})…"
                    )
            check_state, check_detail = summarize_check_runs(owner, repo, sha, token)
            if sha:
                check_cache[sha] = (check_state, check_detail)

        suggested = suggest_next(
            draft=draft,
            base_ok=base_ok,
            prn_ok=prn_ok,
            check_state=check_state,
        )
        rows.append(
            PRDigestRow(
                number=num,
                prn=prn,
                title=title,
                user=user,
                head_ref=head_ref,
                base_ref=base_ref,
                labels=labels,
                lab=lab,
                draft=draft,
                html_url=html_url,
                check_state=check_state,
                check_detail=check_detail,
                title_clean=title_clean,
                base_ok=base_ok,
                prn_on_roster=prn_on_roster,
                suggested=suggested,
            )
        )
    rows.sort(key=lambda r: (r.suggested, r.prn, r.number))
    return rows


def post_issue_comment(owner: str, repo: str, issue_number: int, body: str, token: str) -> dict:
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    rate_limit_sleep()
    r = requests.post(
        url,
        headers=github_headers(token),
        json={"body": body},
        timeout=60,
    )
    r.raise_for_status()
    return r.json()


def load_open_rows_from_csv(
    path: str,
    course_id: str,
    legacy_base: str,
    owner: str,
    repo: str,
    roster_prns: Set[str],
) -> List[PRDigestRow]:
    """Offline fallback: rows from pull_requests.csv (no check runs, limited fields)."""
    import csv
    import os

    rows: List[PRDigestRow] = []
    if not os.path.isfile(path):
        return rows
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for rec in reader:
            if (rec.get("State") or "").lower() != "open":
                continue
            base_ref = rec.get("Base Branch") or ""
            if base_ref != legacy_base and not integration_base_ok(base_ref, course_id):
                continue
            title = rec.get("Title") or ""
            prn = extract_prn(title)
            num = int(rec["PR Number"])
            labels = rec.get("Labels") or ""
            title_clean = title_nominal_for_workflow(title)
            base_ok = integration_base_ok(base_ref, course_id)
            prn_ok = prn_resolvable(title, "")
            prn_on_roster = prn in roster_prns if prn != "UNKNOWN" else False
            rows.append(
                PRDigestRow(
                    number=num,
                    prn=prn,
                    title=title,
                    user=rec.get("User") or "",
                    head_ref="?",
                    base_ref=base_ref,
                    labels=labels,
                    lab=extract_lab_from_labels(labels),
                    draft=False,
                    html_url=f"https://github.com/{owner}/{repo}/pull/{num}",
                    check_state="none",
                    check_detail="offline CSV — run with --live for checks",
                    title_clean=title_clean,
                    base_ok=base_ok,
                    prn_on_roster=prn_on_roster,
                    suggested=suggest_next(
                        draft=False,
                        base_ok=base_ok,
                        prn_ok=prn_ok,
                        check_state="none",
                    ),
                )
            )
    rows.sort(key=lambda r: (r.suggested, r.prn, r.number))
    return rows
