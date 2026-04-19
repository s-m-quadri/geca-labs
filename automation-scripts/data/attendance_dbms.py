"""DBMS lab attendance — edit BATCH_RULES and ATTENDANCE like data/attendance_daa.py."""

from __future__ import annotations

from typing import Dict, List, Tuple

# Extend prefixes to match your DBMS cohorts; placeholders for BT24F/BT25 CSE used in rolls.
BATCH_RULES: List[dict] = [
    {"prefix": "BT24F05F", "ranges": [(1, 999, "A")]},
    {"prefix": "BT25S05F", "ranges": [(1, 999, "A")]},
]

SLOT_GROUPS = {"A": "morning", "B": "morning", "C": "afternoon", "D": "evening"}
SLOTS = {
    "morning": "10:30 AM to 12:30 PM",
    "afternoon": "1:15 PM to 3:15 PM",
    "evening": "3:30 PM to 5:30 PM",
}

# Sample attendance (paste into ATTENDANCE when you have real sessions):
#   ATTENDANCE = {
#       "Lab 1": {
#           "15/01/2026": {"A": [1, 2, 3, 5, 7, 10, 12]},
#           "22/01/2026": {"A": [1, 4, 6, 8, 11, 15]},
#       },
#       "Lab 2": {"29/01/2026": {"A": [2, 3, 4, 9, 14]}},
#   }
# Lab keys become CSV columns. Date format DD/MM/YYYY. Batch keys ("A", …) must match
# BATCH_RULES; values are the last three digits of each present student’s PRN in that batch.

ATTENDANCE: Dict[str, dict] = {}

LOOKUP: Dict[Tuple[str, str, int], str] = {}
for lab, dates in ATTENDANCE.items():
    for date, rec in dates.items():
        for batch_key, nums in rec.items():
            for n in nums:
                LOOKUP[(lab, batch_key, n)] = date


def get_batch(prn: str):
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
    d_key = batch
    if batch == "D":
        d_key = "D23" if prefix and "23" in prefix else "D24"
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
