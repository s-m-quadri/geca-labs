import pandas as pd
import re

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
