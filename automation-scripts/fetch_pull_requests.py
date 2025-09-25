import requests
import csv
import re
from dotenv import load_dotenv
import os

# -----------------------------
# CONFIGURATION
# -----------------------------
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "s-m-quadri"
REPO_NAME = "geca-labs"
OUTPUT_FILE = "output/pull_requests.csv"

# -----------------------------
# HEADERS FOR AUTHENTICATION
# -----------------------------
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# -----------------------------
# FUNCTION TO GET ALL PRS (PAGINATED)
# -----------------------------
def get_all_prs():
    prs = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
        params = {"state": "all", "per_page": 100, "page": page}
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        prs.extend(data)
        page += 1
    return prs

# -----------------------------
# FUNCTION TO GET PR DETAILS
# -----------------------------
def extract_prn(title):
    match = re.search(r"(BT[0-9A-Z]+)", title, re.IGNORECASE)
    return match.group(1).upper() if match else "UNKNOWN"

def process_prs(prs):
    processed = []
    for pr in prs:
        pr_number = pr["number"]
        pr_title = pr["title"]
        pr_user = pr["user"]["login"]
        pr_state = pr["state"]
        pr_created = pr["created_at"]
        pr_closed = pr.get("closed_at")
        pr_merged = pr.get("merged_at")

        # Get labels
        labels = [lbl["name"] for lbl in pr.get("labels", [])]

        # Extract PRN
        prn = extract_prn(pr_title)

        processed.append({
            "PR Number": pr_number,
            "PRN": prn,
            "Title": pr_title,
            "User": pr_user,
            "Labels": ", ".join(labels),
            "State": pr_state,
            "Created At": pr_created,
            "Closed At": pr_closed if pr_closed else "",
            "Merged At": pr_merged if pr_merged else ""
        })
    return processed

# -----------------------------
# MAIN SCRIPT
# -----------------------------
if __name__ == "__main__":
    print("Fetching PRs from GitHub...")
    prs = get_all_prs()
    print(f"Total PRs retrieved: {len(prs)}")

    processed = process_prs(prs)

    # Sort by PRN
    processed.sort(key=lambda x: x["PRN"])

    # Save to CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=processed[0].keys())
        writer.writeheader()
        writer.writerows(processed)

    print(f"Data saved to {OUTPUT_FILE}")