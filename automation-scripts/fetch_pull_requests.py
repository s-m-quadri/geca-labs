import requests
import csv
import re
from dotenv import load_dotenv
import os
from datetime import datetime
import time

# -----------------------------
# CONFIGURATION
# -----------------------------
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "s-m-quadri"
REPO_NAME = "geca-labs"
OUTPUT_DIR = "output"
PR_OUTPUT_FILE = f"{OUTPUT_DIR}/pull_requests.csv"
# FILES_OUTPUT_FILE removed: not generating file_changes.csv anymore
COMMITS_OUTPUT_FILE = f"{OUTPUT_DIR}/commits.csv"
INCREMENTAL_COMMITS = os.getenv("INCREMENTAL_COMMITS", "1") == "1"
SKIP_COMMIT_DETAILS = os.getenv("SKIP_COMMIT_DETAILS", "1") == "1"  # default to fast mode

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

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
# UTILITY FUNCTIONS
# -----------------------------
def extract_prn(title):
    match = re.search(r"(BT[0-9A-Z]+)", title, re.IGNORECASE)
    return match.group(1).upper() if match else "UNKNOWN"

def filter_merged_prs(prs):
    """Filter to only include merged PRs for processing"""
    merged_prs = [pr for pr in prs if pr.get("merged_at") is not None]
    print(f"Filtered to {len(merged_prs)} merged PRs out of {len(prs)} total PRs")
    return merged_prs

def rate_limit_sleep():
    """Add a small delay to avoid hitting GitHub API rate limits"""
    time.sleep(0.1)

# -----------------------------
# FUNCTION TO GET PR FILE CHANGES
# -----------------------------
def get_pr_files(pr_number):
    """Get all file changes for a specific PR"""
    files = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/files"
        params = {"per_page": 100, "page": page}
        rate_limit_sleep()
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        files.extend(data)
        page += 1
    return files

# -----------------------------
# FUNCTION TO GET PR COMMITS
# -----------------------------
def get_pr_commits(pr_number):
    """Get all commits for a specific PR"""
    commits = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pr_number}/commits"
        params = {"per_page": 100, "page": page}
        rate_limit_sleep()
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        commits.extend(data)
        page += 1
    return commits

# -----------------------------
# FUNCTION TO GET COMMIT DETAILS
# -----------------------------
def get_commit_details(commit_sha):
    """Get detailed information about a specific commit"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits/{commit_sha}"
    rate_limit_sleep()
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()

def process_prs(prs):
    """Process PR data for the main pull requests CSV"""
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

def process_file_changes(merged_prs):
    """Process file changes for merged PRs only"""
    all_file_changes = []
    
    for pr in merged_prs:
        pr_number = pr["number"]
        pr_title = pr["title"]
        pr_user = pr["user"]["login"]
        prn = extract_prn(pr_title)
        
        print(f"Processing file changes for PR #{pr_number} ({prn})...")
        
        try:
            files = get_pr_files(pr_number)
            
            for file_data in files:
                all_file_changes.append({
                    "PR Number": pr_number,
                    "PRN": prn,
                    "User": pr_user,
                    "File Path": file_data["filename"],
                    "Status": file_data["status"],  # added, modified, removed, renamed
                    "Additions": file_data["additions"],
                    "Deletions": file_data["deletions"],
                    "Changes": file_data["changes"],
                    "Patch": file_data.get("patch", "")[:500] + "..." if file_data.get("patch", "") and len(file_data.get("patch", "")) > 500 else file_data.get("patch", ""),  # Truncate patch for CSV
                    "Previous Filename": file_data.get("previous_filename", ""),
                })
        except Exception as e:
            print(f"Error processing files for PR #{pr_number}: {e}")
            continue
    
    return all_file_changes

def read_existing_commits(path):
    """Read existing commits.csv and return a set of commit SHAs already captured and a list of existing rows."""
    existing_rows = []
    existing_shas = set()
    existing_pr_numbers = set()
    if os.path.exists(path):
        try:
            with open(path, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    existing_rows.append(row)
                    sha = row.get("Commit SHA")
                    if sha:
                        existing_shas.add(sha)
                    prnum = row.get("PR Number")
                    if prnum:
                        try:
                            existing_pr_numbers.add(int(prnum))
                        except ValueError:
                            existing_pr_numbers.add(prnum)
        except Exception as e:
            print(f"Warning: Failed to read existing commits file '{path}': {e}")
    return existing_shas, existing_rows, existing_pr_numbers

def process_commits(merged_prs):
    """Process commit data for merged PRs only"""
    all_commits = []
    # Read existing commits and PR numbers when incremental mode is enabled
    if INCREMENTAL_COMMITS:
        existing_shas, existing_rows, existing_pr_numbers = read_existing_commits(COMMITS_OUTPUT_FILE)
    else:
        existing_shas, existing_rows, existing_pr_numbers = set(), [], set()
    appended = 0
    
    for pr in merged_prs:
        pr_number = pr["number"]
        pr_title = pr["title"]
        pr_user = pr["user"]["login"]
        prn = extract_prn(pr_title)
        
        print(f"Processing commits for PR #{pr_number} ({prn})...")
        
        # If incremental mode and this PR number already has commits recorded, skip fetching commits
        if INCREMENTAL_COMMITS and pr_number in existing_pr_numbers:
            print(f"Skipping PR #{pr_number} - already present in {COMMITS_OUTPUT_FILE}")
            continue

        try:
            commits = get_pr_commits(pr_number)
            
            for commit in commits:
                commit_sha = commit["sha"]
                if INCREMENTAL_COMMITS and commit_sha in existing_shas:
                    continue  # already captured

                commit_message = commit["commit"]["message"]
                commit_author = commit["commit"]["author"]["name"]
                commit_email = commit["commit"]["author"]["email"]
                commit_date = commit["commit"]["author"]["date"]

                files_changed = 0
                total_additions = 0
                total_deletions = 0
                affected_files = ""

                if not SKIP_COMMIT_DETAILS:
                    # Get detailed commit info for file statistics (slower)
                    try:
                        commit_details = get_commit_details(commit_sha)
                        files_changed = len(commit_details.get("files", []))
                        total_additions = sum(f.get("additions", 0) for f in commit_details.get("files", []))
                        total_deletions = sum(f.get("deletions", 0) for f in commit_details.get("files", []))
                        affected_files = ", ".join([f["filename"] for f in commit_details.get("files", [])])
                    except Exception as e:
                        print(f"Error getting details for commit {commit_sha}: {e}")

                all_commits.append({
                    "PR Number": pr_number,
                    "PRN": prn,
                    "PR User": pr_user,
                    "Commit SHA": commit_sha,
                    "Commit Author": commit_author,
                    "Commit Email": commit_email,
                    "Commit Message": commit_message.split('\n')[0][:200],
                    "Commit Date": commit_date,
                    "Files Changed": files_changed,
                    "Total Additions": total_additions,
                    "Total Deletions": total_deletions,
                    "Affected Files": affected_files[:500] + "..." if len(affected_files) > 500 else affected_files
                })
                appended += 1
        except Exception as e:
            print(f"Error processing commits for PR #{pr_number}: {e}")
            continue
    
    # If incremental, prepend existing rows so the output includes both old and new
    if INCREMENTAL_COMMITS and existing_rows:
        print(f"Incremental mode: found {len(existing_rows)} existing commits, appending {appended} new commits.")
        # Maintain chronological order by date after combining
        combined = existing_rows + all_commits
        # Ensure consistent fieldnames by returning combined
        return combined
    return all_commits

# -----------------------------
# MAIN SCRIPT
# -----------------------------
if __name__ == "__main__":
    print("Fetching PRs from GitHub...")
    prs = get_all_prs()
    print(f"Total PRs retrieved: {len(prs)}")
    
    # Filter to only merged PRs for file changes and commits processing
    merged_prs = filter_merged_prs(prs)
    
    print("\n" + "="*50)
    print("GENERATING PULL REQUESTS CSV")
    print("="*50)
    
    # Process basic PR data (all PRs for complete record)
    processed_prs = process_prs(prs)
    processed_prs.sort(key=lambda x: x["PRN"])
    
    # Save PR data to CSV
    if processed_prs:
        with open(PR_OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=processed_prs[0].keys())
            writer.writeheader()
            writer.writerows(processed_prs)
        print(f"✓ Pull requests data saved to {PR_OUTPUT_FILE}")
    
    # Skipping file changes generation to speed up and reduce IO
    
    print("\n" + "="*50)
    print("GENERATING COMMITS CSV (MERGED PRs ONLY)")
    print("="*50)
    
    # Process commits data (only merged PRs)
    commits = process_commits(merged_prs)
    # Guard against missing dates; sort with fallback
    commits.sort(key=lambda x: (x.get("PRN", ""), x.get("Commit Date", "")))
    
    # Save commits to CSV
    if commits:
        with open(COMMITS_OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=commits[0].keys())
            writer.writeheader()
            writer.writerows(commits)
        print(f"✓ Commits data saved to {COMMITS_OUTPUT_FILE}")
        print(f"  Total commits recorded: {len(commits)}")
    
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"📁 Pull Requests: {len(processed_prs)} records → {PR_OUTPUT_FILE}")
    print(f"💾 Commits: {len(commits)} records → {COMMITS_OUTPUT_FILE}")
    print("\nAll data has been successfully exported!")
    
    # Show some statistics
    if processed_prs:
        unique_students = len(set(pr["PRN"] for pr in processed_prs))
        print(f"\n📊 Statistics:")
        print(f"   • Unique students: {unique_students}")
        print(f"   • Total PRs: {len(processed_prs)}")
        if commits:
            if not SKIP_COMMIT_DETAILS:
                total_additions = sum(int(c.get("Total Additions", 0) or 0) for c in commits)
                total_deletions = sum(int(c.get("Total Deletions", 0) or 0) for c in commits)
                print(f"   • Total lines added: {total_additions}")
                print(f"   • Total lines deleted: {total_deletions}")
            else:
                print("   • Commit details skipped (fast mode). Set SKIP_COMMIT_DETAILS=0 to include stats.")