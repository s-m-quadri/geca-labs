import argparse
import pandas as pd
import re
from pathlib import Path

from lib.lab_course import LabCourse

# ------------------------
# CONFIG
# ------------------------
_SCRIPTS = Path(__file__).resolve().parent
_ap = argparse.ArgumentParser(description="Validate pull_requests.csv for a course.")
_ap.add_argument("--course", default="daa")
_args = _ap.parse_args()
_course = LabCourse.load(_args.course, root=str(_SCRIPTS))
INPUT_FILE = _course.pull_requests_csv

# Legacy: repo root (geca-labs) for fallbacks
PROJ_ROOT = _SCRIPTS.parent

# ------------------------
# HELPER FUNCTIONS
# ------------------------
def extract_lab(labels):
    """Extract lab number from label like 'Lab 01', return as int."""
    for lbl in labels.split(","):
        match = re.search(r"Lab\s*0*([0-9]+)", lbl.strip(), re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None

def is_merged(row):
    return pd.notna(row["Merged At"]) and row["Merged At"] != ""

def is_open(row):
    return row["State"] == "open"

# ------------------------
# MAIN SCRIPT
# ------------------------
input_path = Path(INPUT_FILE).resolve()
if not input_path.exists():
    alt_path = PROJ_ROOT / "output" / "pull_requests.csv"
    if alt_path.exists():
        input_path = alt_path
    else:
        raise FileNotFoundError(
            f"Input CSV not found at '{input_path}'. Fetch with: "
            f"python3 automation-scripts/fetch_pull_requests.py --course {_course.id}"
        )

df = pd.read_csv(input_path)

print("\n==== Validity Checks ====\n")

# 1. Same GitHub username, different PRN
user_groups = df.groupby("User")
for user, group in user_groups:
    unique_prns = group["PRN"].unique()
    if len(unique_prns) > 1:
        print(f"[ERROR] GitHub user '{user}' has multiple PRNs: {list(unique_prns)}")
        print(group[["PR Number","PRN","Title","State"]], "\n")

# 2. Same PRN, different GitHub username
prn_groups = df.groupby("PRN")
for prn, group in prn_groups:
    unique_users = group["User"].unique()
    if len(unique_users) > 1:
        print(f"[ERROR] PRN '{prn}' is used by multiple GitHub users: {list(unique_users)}")
        print(group[["PR Number","User","Title","State"]], "\n")

# 3. Duplicate PRs / inconsistent states per lab per PRN
for prn, group in prn_groups:
    # Extract lab numbers present for this PRN
    all_labs = group["Labels"].apply(lambda x: extract_lab(str(x))).dropna().unique()
    
    for lab_num in all_labs:
        # Regex: match exact Lab number
        pattern = rf"\bLab 0*{lab_num}\b"
        lab_rows = group[group["Labels"].apply(lambda x: bool(re.search(pattern, str(x), re.IGNORECASE)))]

        if len(lab_rows) == 0:
            continue

        merged_rows = lab_rows[lab_rows["Merged At"].notna()]
        open_rows = lab_rows[lab_rows["State"] == "open"]

        # Only flag if open PR exists for this same lab that already has a merged PR
        if len(merged_rows) >= 1 and len(open_rows) >= 1:
            print(f"[ERROR] PRN '{prn}' Lab {lab_num}: Open PRs exist despite merged PR for this lab")
            print(lab_rows[["PR Number","State","Merged At","Title"]], "\n")

        if len(open_rows) > 1:
            print(f"[ERROR] PRN '{prn}' Lab {lab_num}: Multiple open PRs exist for this lab")
            print(open_rows[["PR Number","State","Title"]], "\n")

# ------------------------
# FILESYSTEM CROSS-CHECKS
# ------------------------
print("\n==== Filesystem Checks ====\n")

# Resolve labs root relative to this script to be robust no matter where it's run from
BASE_DIR = Path(__file__).resolve().parent
LABS_ROOT = (BASE_DIR.parent / "labs-design-analysis-algorithms").resolve()

if not LABS_ROOT.exists():
    print(f"[ERROR] Labs root not found at: {LABS_ROOT}")
else:
    # 4. For every merged PR with an identifiable Lab label, ensure folder exists: labs-design-analysis-algorithms/lab-XX/PRN
    print("-> Check 4: Each merged PR has a corresponding folder under labs-design-analysis-algorithms")

    merged_df = df[df["Merged At"].notna()].copy()
    # attach lab number parsed from labels
    merged_df["_lab_num"] = merged_df["Labels"].apply(lambda x: extract_lab(str(x)))
    merged_df = merged_df.dropna(subset=["_lab_num"])  # Keep only rows where we could parse lab

    seen_pairs = set()  # (PRN_upper, lab_num)
    for _, row in merged_df.iterrows():
        prn_val = str(row.get("PRN", "")).strip().upper()
        lab_num = int(row["_lab_num"]) if pd.notna(row["_lab_num"]) else None
        if not prn_val or lab_num is None:
            continue
        key = (prn_val, lab_num)
        if key in seen_pairs:
            continue
        seen_pairs.add(key)

        lab_dir = LABS_ROOT / f"lab-{lab_num:02d}"
        expected_folder = lab_dir / prn_val
        if not lab_dir.exists():
            print(f"[ERROR] Merged PR exists for Lab {lab_num} but lab folder missing: {lab_dir}")
        elif not expected_folder.exists() or not expected_folder.is_dir():
            print(
                f"[ERROR] Merged PR exists but submission folder missing -> PRN '{prn_val}', Lab {lab_num}, expected: {expected_folder}"
            )

    # 5. For every existing PRN folder under labs/lab-XX, ensure there is a merged PR for that PRN and Lab
    print("\n-> Check 5: Each existing submission folder has a corresponding merged PR entry")

    # Precompute a fast lookup for merged presence per (PRN_upper, lab_num)
    merged_lookup = set()
    label_cache = {}
    for _, row in df.iterrows():
        if pd.isna(row.get("Merged At")):
            continue
        prn_val = str(row.get("PRN", "")).strip().upper()
        labels_str = str(row.get("Labels", ""))
        if prn_val == "":
            continue
        if labels_str not in label_cache:
            label_cache[labels_str] = extract_lab(labels_str)
        lab_num = label_cache[labels_str]
        if lab_num is None:
            continue
        merged_lookup.add((prn_val, int(lab_num)))

    # Walk lab directories
    for lab_dir in sorted(LABS_ROOT.glob("lab-*")):
        if not lab_dir.is_dir():
            continue
        # parse lab number from folder name 'lab-XX'
        m = re.search(r"lab-0*([0-9]+)$", lab_dir.name, re.IGNORECASE)
        if not m:
            continue
        lab_num = int(m.group(1))

        # iterate PRN subfolders
        for prn_folder in sorted(lab_dir.iterdir()):
            if not prn_folder.is_dir():
                continue
            prn_name = prn_folder.name.strip().upper()
            if (prn_name, lab_num) not in merged_lookup:
                print(
                    f"[ERROR] Submission folder exists without a merged PR -> PRN '{prn_name}', Lab {lab_num}, path: {prn_folder}"
                )

    # 6. For every existing PRN folder, enforce minimum file count and report GitHub URL if below threshold
    print("\n-> Check 6: Minimum file count per submission folder (Lab 0 >= 26, Lab 1+ >= 6)")

    # Build helpers to map (PRN, lab_num) -> set(users) with merged PRs, and PRN -> most common user overall
    merged_users_lookup = {}
    prn_user_counts = {}
    for _, row in df.iterrows():
        prn_val = str(row.get("PRN", "")).strip().upper()
        user = str(row.get("User", "")).strip()
        if not prn_val or not user:
            continue
        # PRN -> user frequency
        if prn_val not in prn_user_counts:
            prn_user_counts[prn_val] = {}
        prn_user_counts[prn_val][user] = prn_user_counts[prn_val].get(user, 0) + 1

        # Only consider merged rows for (PRN, lab) mapping
        if pd.isna(row.get("Merged At")):
            continue
        labels_str = str(row.get("Labels", ""))
        lab_num = extract_lab(labels_str)
        if lab_num is None:
            continue
        key = (prn_val, int(lab_num))
        merged_users_lookup.setdefault(key, set()).add(user)

    def preferred_user_for(prn_upper: str, lab_number: int):
        """Return a best-effort GitHub username for a PRN and lab.
        Prefers users with a merged PR for that (PRN, lab). Falls back to most frequent user for PRN.
        Returns None if unknown.
        """
        users = merged_users_lookup.get((prn_upper, lab_number))
        if users:
            # If multiple due to data error, pick one deterministically (sorted)
            return sorted(users)[0]
        # Fallback to most frequent user for this PRN across all rows
        if prn_upper in prn_user_counts and prn_user_counts[prn_upper]:
            return sorted(prn_user_counts[prn_upper].items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
        return None

    def count_files_in(dir_path: Path) -> int:
        """Count files recursively in dir_path, skipping hidden files/dirs and common cache directories."""
        skip_dirs = {"__pycache__", ".git", ".ipynb_checkpoints", ".venv", "venv", "node_modules", ".mypy_cache"}
        total = 0
        for p in dir_path.rglob("*"):
            try:
                # Skip hidden files/dirs
                parts = {part for part in p.parts}
                if any(part.startswith(".") for part in p.parts if part != "."):
                    # If any path segment is hidden, skip
                    continue
                if any(sd in parts for sd in skip_dirs):
                    continue
                if p.is_file():
                    # Skip compiled Python bytecode files
                    if p.suffix.lower() == ".pyc":
                        continue
                    total += 1
            except Exception:
                # Best-effort; ignore inaccessible paths
                continue
        return total

    # Walk lab directories and validate counts
    for lab_dir in sorted(LABS_ROOT.glob("lab-*")):
        if not lab_dir.is_dir():
            continue
        m = re.search(r"lab-0*([0-9]+)$", lab_dir.name, re.IGNORECASE)
        if not m:
            continue
        lab_num = int(m.group(1))
        min_required = 26 if lab_num == 0 else 6

        for prn_folder in sorted(lab_dir.iterdir()):
            if not prn_folder.is_dir():
                continue
            prn_name = prn_folder.name.strip().upper()
            file_count = count_files_in(prn_folder)
            if file_count < min_required:
                user = preferred_user_for(prn_name, lab_num)
                profile_url = f"https://github.com/{user}" if user else "(unknown)"
                print(
                    f"[ERROR] Insufficient files -> PRN '{prn_name}', Lab {lab_num}: {file_count} files < {min_required} required | Path: {prn_folder} | GitHub: {profile_url}"
                )
