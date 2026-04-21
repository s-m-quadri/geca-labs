"""Pull-request workflow helpers for the interactive PR console (read-heavy; optional comment POST).

Aligned with ``geca-labs/.github/workflows``:

- ``status.yml`` — issue comment on PR must **contain** ``Hi @bot-s-m-quadri`` and must **not**
  contain ``merge``. Retargets base to ``sub-lab-{subject}-{NN}``, rewrites title to
  ``Submission of Lab NN by PRN``, blocks direct base ``stable`` (DAA).
- ``test-submission.yml`` — comment must contain ``@bot-s-m-quadri test``. Sets labels
  ``🧪 Tests Passed`` / ``⚠️ Tests Failed (Non-blocking)``. Those workflows do **not** publish
  GitHub Check Runs on the PR head SHA, so the REST check-runs API often shows ``none``; the
  console uses these labels as the source of truth for bot tests.
- ``merge-organize.yml`` — comment ``@bot-s-m-quadri merge``; base must match
  ``^sub-lab-[a-z]+-[0-9]{2}$``; only ``@s-m-quadri`` may trigger merge step.
"""

from __future__ import annotations

import random
import re
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Callable, Dict, List, Literal, Optional, Set, Tuple

import requests

from lib.common import student_sort_key

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


# Must match .github/workflows/test-submission.yml (Update labels step)
BOT_LABEL_TESTS_PASSED = "🧪 Tests Passed"
BOT_LABEL_TESTS_FAILED_NB = "⚠️ Tests Failed (Non-blocking)"

NextStep = Literal[
    "status",
    "test",
    "re_test",
    "incomplete",
    "merge",
    "fix_ci",
    "unknown",
]

NEXT_STEP_ORDER: Dict[str, int] = {
    "status": 0,
    "test": 1,
    "re_test": 2,
    "incomplete": 3,
    "fix_ci": 4,
    "merge": 5,
    "unknown": 6,
}

# test-submission.yml — acknowledge step + long posted report body
MARKER_BOT_TEST_ACK = "Running tests for"
MIN_BOT_TEST_REPORT_CHARS = 400


def effective_check_from_bot_labels(
    api_state: CheckState,
    api_detail: str,
    label_names: List[str],
) -> Tuple[CheckState, str]:
    """
    ``test-submission.yml`` runs on ``issue_comment`` and labels the PR; it does not attach
    check runs to ``head.sha`` in a way the Check Runs API reliably reports. Prefer labels
    when present so the digest matches “tests passed” on GitHub.
    """
    names = set(label_names)
    detail = api_detail or ""
    if BOT_LABEL_TESTS_PASSED in names:
        if api_state != "success":
            suffix = "bot test label (Check API empty — normal for issue_comment workflow)"
            detail = f"{detail}; {suffix}" if detail else suffix
        return "success", detail
    if BOT_LABEL_TESTS_FAILED_NB in names:
        suffix = "bot test label: failed (non-blocking)"
        detail = f"{detail}; {suffix}" if detail else suffix
        if api_state == "success":
            return "success", detail
        return "failure", detail
    return api_state, api_detail


def parse_github_datetime(iso: str) -> datetime:
    s = (iso or "").strip().replace("Z", "+00:00")
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def get_commit_committer_date(owner: str, repo: str, sha: str, token: Optional[str]) -> Optional[datetime]:
    if not sha:
        return None
    hdrs = github_headers(token)
    url = f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}"
    rate_limit_sleep()
    r = requests.get(url, headers=hdrs, timeout=60)
    if r.status_code != 200:
        return None
    commit = r.json().get("commit") or {}
    info = commit.get("committer") or commit.get("author") or {}
    date_s = info.get("date")
    if not date_s:
        return None
    return parse_github_datetime(date_s)


def list_issue_comments(
    owner: str, repo: str, issue_number: int, token: Optional[str]
) -> List[dict]:
    out: List[dict] = []
    page = 1
    hdrs = github_headers(token)
    max_pages = 15
    while page <= max_pages:
        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
        rate_limit_sleep()
        r = requests.get(
            url, headers=hdrs, params={"per_page": 100, "page": page}, timeout=60
        )
        r.raise_for_status()
        chunk = r.json()
        if not chunk:
            break
        out.extend(chunk)
        page += 1
    return out


def latest_bot_test_activity_time(
    owner: str, repo: str, issue_number: int, token: Optional[str]
) -> Optional[datetime]:
    """
    Newest timestamp that reflects a bot test run: the 'Running tests for…' ack and/or the
    long markdown report posted after tests (test-submission.yml).
    """
    try:
        comments = list_issue_comments(owner, repo, issue_number, token)
    except Exception:
        return None
    times: List[datetime] = []
    for c in comments:
        body = c.get("body") or ""
        ca = c.get("created_at")
        if not ca:
            continue
        if MARKER_BOT_TEST_ACK in body:
            times.append(parse_github_datetime(ca))
        elif len(body) >= MIN_BOT_TEST_REPORT_CHARS:
            times.append(parse_github_datetime(ca))
    return max(times) if times else None


def head_pushed_after_last_bot_test(
    owner: str, repo: str, issue_number: int, head_sha: str, token: Optional[str]
) -> Optional[bool]:
    """True if HEAD commit is strictly newer than the last bot test comment activity."""
    ref_t = latest_bot_test_activity_time(owner, repo, issue_number, token)
    head_t = get_commit_committer_date(owner, repo, head_sha, token)
    if ref_t is None or head_t is None:
        return None
    return head_t > ref_t


def classify_next_step(
    *,
    draft: bool,
    base_ok: bool,
    prn_ok: bool,
    api_state: CheckState,
    check_state: CheckState,
    has_bot_passed_label: bool,
    has_bot_failed_label: bool,
    head_after_failed_test: Optional[bool],
) -> NextStep:
    """
    ``fix_ci`` — GitHub Check Runs / Actions failed (no bot test outcome labels).

    ``incomplete`` — Bot tests failed (⚠️ label) and HEAD is not newer than last test activity
    (student has not updated since the run), or we could not compare timestamps.

    ``re_test`` — Bot tests failed label but HEAD is newer than last test activity → re-run
    ``@bot-s-m-quadri test``.

    ``test`` — No bot outcome yet; needs a first ``@bot-s-m-quadri test``.
    """
    if draft:
        return "unknown"
    if not base_ok or not prn_ok:
        return "status"
    if has_bot_passed_label:
        return "merge"
    if has_bot_failed_label:
        if head_after_failed_test is True:
            return "re_test"
        return "incomplete"
    if api_state == "failure":
        return "fix_ci"
    if check_state in ("none", "pending"):
        return "test"
    if check_state == "success":
        return "merge"
    return "unknown"


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
    n_timing = sum(
        1
        for p in open_prs
        if BOT_LABEL_TESTS_FAILED_NB in [x["name"] for x in (p.get("labels") or [])]
    )
    if progress and n_timing:
        progress(
            f"timing: HEAD vs bot test comments for {n_timing} PR(s) with failed-test label…"
        )

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
            api_state, api_detail = check_cache[sha]
        else:
            if sha:
                fetch_n += 1
                if progress:
                    progress(
                        f"check runs: fetching {fetch_n}/{n_shas} (PR #{num} {prn})…"
                    )
                api_state, api_detail = summarize_check_runs(owner, repo, sha, token)
                check_cache[sha] = (api_state, api_detail)
            else:
                api_state, api_detail = summarize_check_runs(owner, repo, "", token)

        check_state, check_detail = effective_check_from_bot_labels(
            api_state, api_detail, labels_list
        )

        names_set = set(labels_list)
        has_bot_passed = BOT_LABEL_TESTS_PASSED in names_set
        has_bot_failed = BOT_LABEL_TESTS_FAILED_NB in names_set

        head_after_failed: Optional[bool] = None
        if has_bot_failed and token and sha:
            head_after_failed = head_pushed_after_last_bot_test(
                owner, repo, num, sha, token
            )

        suggested = classify_next_step(
            draft=draft,
            base_ok=base_ok,
            prn_ok=prn_ok,
            api_state=api_state,
            check_state=check_state,
            has_bot_passed_label=has_bot_passed,
            has_bot_failed_label=has_bot_failed,
            head_after_failed_test=head_after_failed,
        )
        if suggested == "re_test" and head_after_failed is True:
            check_detail = (check_detail or "") + " → HEAD after last bot test; re-run @bot test"
        elif suggested == "incomplete" and has_bot_failed:
            check_detail = (check_detail or "") + " → fix submission before re-test (or timing unknown)"
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
    rows.sort(
        key=lambda r: (
            NEXT_STEP_ORDER.get(r.suggested, 99),
            student_sort_key(r.prn),
            r.number,
        )
    )
    return rows


def post_issue_comment(
    owner: str,
    repo: str,
    issue_number: int,
    body: str,
    token: str,
    *,
    max_attempts: int = 8,
) -> dict:
    """
    Post an issue comment with backoff for GitHub secondary rate limits on content creation.
    See https://docs.github.com/rest/overview/rate-limits-for-the-rest-api#about-secondary-rate-limits
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    hdrs = github_headers(token)
    backoff = 6.0
    last_error_text: Optional[str] = None
    for attempt in range(max_attempts):
        if attempt:
            jitter = random.uniform(0.85, 1.15)
            wait_s = min(120.0, backoff * jitter)
            time.sleep(wait_s)
            backoff = min(120.0, backoff * 1.8)
        rate_limit_sleep(0.25)
        r = requests.post(url, headers=hdrs, json={"body": body}, timeout=120)
        if r.status_code == 201:
            return r.json()
        msg = ""
        try:
            msg = (r.json().get("message") or "").lower()
        except Exception:
            pass
        retryable = r.status_code == 429 or (
            r.status_code == 403
            and (
                "secondary rate limit" in msg
                or "rate limit" in msg
                or "temporarily blocked" in msg
            )
        )
        if retryable:
            ra = r.headers.get("Retry-After")
            if ra and str(ra).isdigit():
                time.sleep(min(120, int(ra)))
            last_error_text = f"{r.status_code} {r.reason}: {msg or r.text[:400]}"
            continue
        r.raise_for_status()
    raise RuntimeError(last_error_text or "post_issue_comment: exhausted retries")


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
            label_names = [x.strip() for x in labels.split(",") if x.strip()]
            title_clean = title_nominal_for_workflow(title)
            base_ok = integration_base_ok(base_ref, course_id)
            prn_ok = prn_resolvable(title, "")
            prn_on_roster = prn in roster_prns if prn != "UNKNOWN" else False
            has_bot_passed = BOT_LABEL_TESTS_PASSED in label_names
            has_bot_failed = BOT_LABEL_TESTS_FAILED_NB in label_names
            suggested = classify_next_step(
                draft=False,
                base_ok=base_ok,
                prn_ok=prn_ok,
                api_state="none",
                check_state="none",
                has_bot_passed_label=has_bot_passed,
                has_bot_failed_label=has_bot_failed,
                head_after_failed_test=None,
            )
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
                    suggested=suggested,
                )
            )
    rows.sort(
        key=lambda r: (
            NEXT_STEP_ORDER.get(r.suggested, 99),
            student_sort_key(r.prn),
            r.number,
        )
    )
    return rows
