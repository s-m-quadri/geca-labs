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
OUTPUT_DIR = "output"
PR_OUTPUT_FILE = f"{OUTPUT_DIR}/pull_requests.csv"
FILES_OUTPUT_FILE = f"{OUTPUT_DIR}/file_changes.csv"
COMMITS_OUTPUT_FILE = f"{OUTPUT_DIR}/commits.csv"

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

def process_commits(merged_prs):
    """Process commit data for merged PRs only"""
    all_commits = []
    
    for pr in merged_prs:
        pr_number = pr["number"]
        pr_title = pr["title"]
        pr_user = pr["user"]["login"]
        prn = extract_prn(pr_title)
        
        print(f"Processing commits for PR #{pr_number} ({prn})...")
        
        try:
            commits = get_pr_commits(pr_number)
            
            for commit in commits:
                commit_sha = commit["sha"]
                commit_message = commit["commit"]["message"]
                commit_author = commit["commit"]["author"]["name"]
                commit_email = commit["commit"]["author"]["email"]
                commit_date = commit["commit"]["author"]["date"]
                
                # Get detailed commit info for file statistics
                try:
                    commit_details = get_commit_details(commit_sha)
                    files_changed = len(commit_details.get("files", []))
                    total_additions = sum(f.get("additions", 0) for f in commit_details.get("files", []))
                    total_deletions = sum(f.get("deletions", 0) for f in commit_details.get("files", []))
                    affected_files = ", ".join([f["filename"] for f in commit_details.get("files", [])])
                except Exception as e:
                    print(f"Error getting details for commit {commit_sha}: {e}")
                    files_changed = 0
                    total_additions = 0
                    total_deletions = 0
                    affected_files = ""
                
                all_commits.append({
                    "PR Number": pr_number,
                    "PRN": prn,
                    "PR User": pr_user,
                    "Commit SHA": commit_sha,
                    "Commit Author": commit_author,
                    "Commit Email": commit_email,
                    "Commit Message": commit_message.split('\n')[0][:200],  # First line, truncated
                    "Commit Date": commit_date,
                    "Files Changed": files_changed,
                    "Total Additions": total_additions,
                    "Total Deletions": total_deletions,
                    "Affected Files": affected_files[:500] + "..." if len(affected_files) > 500 else affected_files
                })
        except Exception as e:
            print(f"Error processing commits for PR #{pr_number}: {e}")
            continue
    
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
    
    print("\n" + "="*50)
    print("GENERATING FILE CHANGES CSV (MERGED PRs ONLY)")
    print("="*50)
    
    # Process file changes data (only merged PRs)
    file_changes = process_file_changes(merged_prs)
    file_changes.sort(key=lambda x: (x["PRN"], x["File Path"]))
    
    # Save file changes to CSV
    if file_changes:
        with open(FILES_OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=file_changes[0].keys())
            writer.writeheader()
            writer.writerows(file_changes)
        print(f"✓ File changes data saved to {FILES_OUTPUT_FILE}")
        print(f"  Total file changes recorded: {len(file_changes)}")
    
    print("\n" + "="*50)
    print("GENERATING COMMITS CSV (MERGED PRs ONLY)")
    print("="*50)
    
    # Process commits data (only merged PRs)
    commits = process_commits(merged_prs)
    commits.sort(key=lambda x: (x["PRN"], x["Commit Date"]))
    
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
    print(f"📄 File Changes: {len(file_changes)} records → {FILES_OUTPUT_FILE}")
    print(f"💾 Commits: {len(commits)} records → {COMMITS_OUTPUT_FILE}")
    print("\nAll data has been successfully exported!")
    
    # Show some statistics
    if processed_prs:
        unique_students = len(set(pr["PRN"] for pr in processed_prs))
        print(f"\n📊 Statistics:")
        print(f"   • Unique students: {unique_students}")
        print(f"   • Total PRs: {len(processed_prs)}")
        if file_changes:
            unique_files = len(set(fc["File Path"] for fc in file_changes))
            print(f"   • Unique files modified: {unique_files}")
        if commits:
            total_additions = sum(c["Total Additions"] for c in commits)
            total_deletions = sum(c["Total Deletions"] for c in commits)
            print(f"   • Total lines added: {total_additions}")
            print(f"   • Total lines deleted: {total_deletions}")