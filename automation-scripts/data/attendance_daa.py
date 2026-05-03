"""DAA lab attendance rosters and batch rules (data only)."""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

# -------------------------------
# Batch mapping based on PRN rules
# -------------------------------
BATCH_RULES: List[dict] = [
    {"prefix": "BT23F05F", "ranges": [(1, 20, "A"), (21, 40, "B"), (41, 60, "C"), (61, 67, "D")]},
    {"prefix": "BT24S05F", "ranges": [(1, 10, "D")]},
]

# -------------------------------
# Batch → Slot mapping
# -------------------------------
SLOT_GROUPS = {
    "A": "morning",
    "B": "morning",
    "C": "afternoon",
    "D": "evening",
}

SLOTS = {
    "morning": "10:30 AM to 12:30 PM",
    "afternoon": "1:15 PM to 3:15 PM",
    "evening": "3:30 PM to 5:30 PM",
}

# -------------------------------
# Attendance data
# -------------------------------
ATTENDANCE: Dict[str, dict] = {
    "Misc.": {
        "24/07/2025": {"A": [3, 4, 5, 6, 7, 10, 11, 12, 13, 15, 16, 17, 18, 19]},
        "28/07/2025": {"C": [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 56, 57, 59, 60]},
    },
    "Lab 0": {
        "04/08/2025": {"C": [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 57, 58, 59, 60]},
        "07/08/2025": {
            "A": [2, 3, 4, 6, 7, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20],
            "D23": [61, 62, 63, 64, 65, 67],
            "D24": [1, 2, 3, 4, 5, 6, 8, 9, 10],
        },
        "08/08/2025": {"B": [21, 22, 23, 24, 25, 26, 27, 28, 30, 33, 36, 37, 38, 39]},
    },
    "Lab 1": {
        "11/08/2025": {"C": [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 56, 57, 58]},
        "14/08/2025": {
            "A": [3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20],
            "D23": [61, 63],
            "D24": [5, 8, 10],
        },
        "22/08/2025": {"B": [21, 22, 26, 28, 30, 32, 33, 35, 37]},
    },
    "Lab 2": {
        "18/08/2025": {"C": [43, 44, 46, 47, 49, 50, 51, 60]},
        "21/08/2025": {
            "A": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19],
            "D23": [61, 62, 63, 64, 65, 67],
            "D24": [1, 2, 3, 4, 5, 6, 9],
        },
        "12/09/2025": {"B": [21, 22, 24, 25, 28, 30, 32, 33, 35]},
    },
    "Lab 3": {
        "25/08/2025": {"C": [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 57, 58, 59, 60]},
        "28/08/2025": {
            "A": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 20],
            "D23": [61, 63, 64, 65, 67],
            "D24": [1, 2, 3, 4, 6, 7, 8, 9, 10],
        },
        "19/09/2025": {"B": [22, 23, 24, 27, 28, 29, 30, 32, 33, 35, 36, 38, 39]},
    },
    "Lab 4": {
        "08/09/2025": {"C": [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 57, 60]},
        "11/09/2025": {
            "A": [3, 4, 10, 11, 15, 16],
            "D23": [61, 63, 64, 65, 67],
            "D24": [1, 2, 3, 4, 5, 6, 7, 9],
        },
        "26/09/2025": {"B": [21, 22, 24, 26, 28, 29, 30, 33, 35, 36, 37, 38]},
    },
    "Lab 5": {
        "15/09/2025": {"C": [44, 47, 49, 51, 56, 59]},
        "16/09/2025": {"D23": [63, 67], "D24": [1, 2, 3, 6, 7, 9]},
        "18/09/2025": {"A": [2, 3, 4, 7, 10, 11, 13, 15, 18, 19, 20]},
        "03/10/2025": {"B": [21, 22, 23, 24, 25, 26, 27, 28, 33, 35, 36, 37, 38, 39]},
    },
    "Lab 6": {
        "23/09/2025": {"D23": [61, 62, 63, 64, 67], "D24": [1, 2, 3, 4, 5, 6, 7, 9, 10]},
        "25/09/2025": {"A": [3, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]},
        "29/09/2025": {"C": [42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 57, 58, 60]},
    },
}

LOOKUP: Dict[Tuple[str, str, int], str] = {}
for lab, dates in ATTENDANCE.items():
    for date, rec in dates.items():
        for batch_key, nums in rec.items():
            for n in nums:
                LOOKUP[(lab, batch_key, n)] = date


def get_batch(prn: str):
    """Return (batch_letter, roll_num:int|None, prefix:str|None)."""
    for rule in BATCH_RULES:
        if prn.startswith(rule["prefix"]):
            num = int(prn[-3:])
            for start, end, batch in rule["ranges"]:
                if start <= num <= end:
                    return batch, num, rule["prefix"]
    return None, None, None


def was_present(prn: str, lab_key: str) -> str:
    batch, num, prefix = get_batch(prn)
    if not batch:
        return "-"

    if batch == "D":
        d_key = "D23" if prefix == "BT23F05F" else "D24"
    else:
        d_key = batch

    session_dates = [date for (lab, bkey, n), date in LOOKUP.items() if lab == lab_key and bkey == d_key]
    if not session_dates:
        return "n/a"

    date = LOOKUP.get((lab_key, d_key, num))
    if date:
        return f"{date}"
    return "Absent"


def build_output_row(row: dict) -> dict:
    prn, name = row["PRN"], row["Name"]
    out = {"PRN": prn, "Name": name}
    for lab_key in ATTENDANCE.keys():
        out[lab_key] = was_present(prn, lab_key)
    return out


def attendance_fieldnames() -> List[str]:
    return ["PRN", "Name"] + list(ATTENDANCE.keys())
