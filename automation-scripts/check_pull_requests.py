import pandas as pd
import re
from pathlib import Path

# ------------------------
# CONFIG
# ------------------------
INPUT_FILE = "output/pull_requests.csv"

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
df = pd.read_csv(INPUT_FILE)

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
