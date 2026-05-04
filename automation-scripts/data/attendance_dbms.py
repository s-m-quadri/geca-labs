"""DBMS lab attendance — Batches A(Mon), B(Tue), C(Fri), D/DSY(eve)."""

from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Tuple

# ----- Batch rules -----
# D is split: D24 = BT24F05F 61-70, D23 = BT23F05F repeaters, DDSY = BT25S05F lateral-entry
BATCH_RULES: List[dict] = [
    {"prefix": "BT24F05F", "ranges": [(1, 20, "A"), (21, 40, "B"), (41, 60, "C"), (61, 70, "D24")]},
    {"prefix": "BT23F05F", "ranges": [(1, 999, "D23")]},
    {"prefix": "BT25S05F", "ranges": [(1, 999, "DDSY")]},
]

SLOT_GROUPS = {
    "A": "afternoon", "B": "afternoon", "C": "morning",
    "D24": "evening", "D23": "evening", "DDSY": "evening",
}
SLOTS = {
    "morning": "10:30 AM to 12:30 PM",
    "afternoon": "1:15 PM to 3:15 PM",
    "evening": "3:30 PM to 5:30 PM",
}

# ----- Explicit in-person attendance -----
# Format: "Lab N" -> "DD/MM/YYYY" -> {batch_key: [last-3-digit roll numbers]}
ATTENDANCE: Dict[str, dict] = {
    "Lab 1": {
        "27/01/2026": {"B": [21, 24, 29, 33, 35, 36]},
        "29/01/2026": {
            "D24": [62, 63, 65, 66, 67, 70],
            "DDSY": [1, 2, 5, 6, 8],
        },
        "30/01/2026": {"C": [43, 44, 47, 49, 55, 60]},
        "02/02/2026": {"A": [1, 4, 5, 7, 10, 13, 14, 15, 16, 18, 19]},
    },
    "Lab 2": {
        "03/02/2026": {"B": [21, 23, 24, 25, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 40]},
        "05/02/2026": {
            "D24": [61, 66, 67],
            "D23": [40, 55],
            "DDSY": [1, 2, 3, 4, 6, 7, 8],
        },
        "06/02/2026": {"C": [41, 43, 44, 45, 48, 49, 53, 57, 59]},
        "09/02/2026": {"A": [1, 2, 4, 5, 6, 7, 8, 10, 14, 15, 16, 18, 19]},
    },
    "Lab 3": {
        "10/02/2026": {
            "B": [21, 22, 23, 24, 27, 32, 36, 40],
            "D24": [61, 64, 67, 70],
            "D23": [40, 55],
            "DDSY": [1, 2, 4, 5, 6],
        },
        "13/02/2026": {"C": [41, 42, 43, 44, 45, 47, 48, 53, 55, 56, 57, 58, 59, 60]},
        "02/03/2026": {"A": [1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]},
    },
    "Lab 4": {
        "24/02/2026": {
            "B": [21, 22, 23, 24, 25, 26, 27, 29, 31, 32, 35, 36, 37, 38, 40],
            "D24": [61, 62, 63, 64, 65, 66, 67, 70],
            "DDSY": [1, 2, 3, 4, 6, 7],
        },
        "27/02/2026": {"C": [42, 43, 44, 45, 47, 48, 49, 50, 53, 56, 57, 58, 59, 60]},
        "16/03/2026": {"A": [1, 2, 3, 4, 5, 7, 11, 12, 14, 18, 19]},
        "24/03/2026": {"D23": [40]},
    },
    "Lab 5": {
        "17/03/2026": {
            "B": [21, 22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 35, 36, 38, 40],
            "D24": [62, 63, 65, 66, 67, 70],
            "DDSY": [6],
        },
        "23/03/2026": {"A": [2, 5, 6, 7, 8, 10, 15, 19]},
        # Batch C: online session 27/03/2026 (see ONLINE_SESSIONS)
    },
    "Lab 6": {
        "24/03/2026": {
            "B": [23, 24, 25, 26, 29, 32, 34, 36, 37, 40],
            "D24": [63],
            "DDSY": [2, 3, 6, 7],
        },
        # Batch A: online 31/03/2026 (see ONLINE_SESSIONS)
        # Batch C: online 10/04/2026 (see ONLINE_SESSIONS)
    },
    "Lab 7": {
        "06/04/2026": {"A": [13, 14, 16, 18]},
        "28/04/2026": {"D24": [61, 62, 65, 67], "C": [48]},  # C-48: makeup in D session
        # Batch B: online 30/03 + 07/04 (see ONLINE_SESSIONS)
        # Batch C: online 10/04 (see ONLINE_SESSIONS)
    },
}

# ----- Online / instructor-absent sessions -----
# Students in the given batch are marked present if any PR was opened within window_days.
ONLINE_SESSIONS: List[Tuple[str, str, str, int]] = [
    ("Lab 5", "27/03/2026", "C",   3),
    ("Lab 6", "30/03/2026", "A",   3),  # Mon = Batch A
    ("Lab 7", "31/03/2026", "B",   3),  # Tue = Batch B
    ("Lab 7", "07/04/2026", "B",   3),  # second window: remaining B students
    ("Lab 6", "10/04/2026", "C",   3),
]

# ----- Build explicit lookup -----
LOOKUP: Dict[Tuple[str, str, int], str] = {}
for _lab, _dates in ATTENDANCE.items():
    for _date, _rec in _dates.items():
        for _bk, _nums in _rec.items():
            for _n in _nums:
                LOOKUP[(_lab, _bk, _n)] = _date

_ONLINE_SESSIONS_BY_LAB_BATCH: Dict[Tuple[str, str], List[str]] = {}
for _lab, _date, _bk, _ in ONLINE_SESSIONS:
    _ONLINE_SESSIONS_BY_LAB_BATCH.setdefault((_lab, _bk), []).append(_date)


def get_batch(prn: str):
    for rule in BATCH_RULES:
        if prn.startswith(rule["prefix"]):
            num = int(prn[-3:])
            for start, end, batch in rule["ranges"]:
                if start <= num <= end:
                    return batch, num, rule["prefix"]
    return None, None, None


def _load_online_presence() -> Dict[Tuple[str, str, str], str]:
    """Read pr_details.json and return {(lab, batch, prn): session_date} for online sessions."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pr_path = os.path.join(root, "output", "dbms", "pr_details.json")
    result: Dict[Tuple[str, str, str], str] = {}
    if not os.path.isfile(pr_path):
        return result
    with open(pr_path, encoding="utf-8") as f:
        prs = json.load(f)
    for lab_key, date_str, batch_key, window_days in ONLINE_SESSIONS:
        d0 = datetime.strptime(date_str, "%d/%m/%Y").replace(tzinfo=timezone.utc)
        d1 = d0 + timedelta(days=window_days)
        for pr in prs:
            prn = pr.get("prn", "")
            b, _, _ = get_batch(prn)
            if b != batch_key:
                continue
            created_str = pr.get("created_at", "")
            if not created_str:
                continue
            ca = datetime.fromisoformat(created_str.replace("Z", "+00:00")).astimezone(timezone.utc)
            if d0 <= ca <= d1:
                key = (lab_key, batch_key, prn)
                if key not in result:
                    result[key] = date_str
    return result


_ONLINE_PRESENCE: Optional[Dict[Tuple[str, str, str], str]] = None


def _online_presence() -> Dict[Tuple[str, str, str], str]:
    global _ONLINE_PRESENCE
    if _ONLINE_PRESENCE is None:
        _ONLINE_PRESENCE = _load_online_presence()
    return _ONLINE_PRESENCE


_LAB_ORDER: List[str] = list(ATTENDANCE.keys())


def _batch_has_any_session(batch: str, from_lab_idx: int) -> bool:
    """Return True if any lab at or after from_lab_idx has a session for this batch."""
    for lab in _LAB_ORDER[from_lab_idx:]:
        if any(bk == batch for (l, bk, _) in LOOKUP if l == lab):
            return True
        if (lab, batch) in _ONLINE_SESSIONS_BY_LAB_BATCH:
            return True
    return False


def was_present(prn: str, lab_key: str) -> str:
    batch, num, _ = get_batch(prn)
    if not batch:
        return "-"

    explicit_date = LOOKUP.get((lab_key, batch, num))
    if explicit_date:
        return explicit_date

    online_date = _online_presence().get((lab_key, batch, prn))
    if online_date:
        return f"{online_date}*"

    has_session = (
        any(bk == batch for (l, bk, _) in LOOKUP if l == lab_key)
        or (lab_key, batch) in _ONLINE_SESSIONS_BY_LAB_BATCH
    )
    if has_session:
        return "Absent"

    # No session for this lab+batch — but if a later lab was conducted, this one was too
    try:
        idx = _LAB_ORDER.index(lab_key)
    except ValueError:
        return "n/a"
    if _batch_has_any_session(batch, idx + 1):
        return "Absent"
    return "n/a"


def build_output_row(row: dict) -> dict:
    prn, name = row["PRN"], row["Name"]
    out = {"PRN": prn, "Name": name}
    for lab_key in ATTENDANCE.keys():
        out[lab_key] = was_present(prn, lab_key)
    return out


def attendance_fieldnames() -> List[str]:
    return ["PRN", "Name"] + list(ATTENDANCE.keys())
