import csv

# -----------------------------
# CONFIGURATION
# -----------------------------
INPUT_FILE = "output/students.csv"
OUTPUT_FILE = "output/attendance.csv"

# -------------------------------
# Batch mapping based on PRN rules
# -------------------------------
BATCH_RULES = [
    {"prefix": "BT23F05F", "ranges": [(1,20,"A"), (21,40,"B"), (41,60,"C"), (61,67,"D")]},
    {"prefix": "BT24S05F", "ranges": [(1,10,"D")]}
]

def get_batch(prn):
    """Return batch letter (A/B/C/D) based on PRN and rules."""
    for rule in BATCH_RULES:
        if prn.startswith(rule["prefix"]):
            num = int(prn[-3:])
            for start, end, batch in rule["ranges"]:
                if start <= num <= end:
                    return batch, num, rule["prefix"]
    return None, None, None

# -------------------------------
# Batch → Slot mapping
# -------------------------------
SLOT_GROUPS = {
    "A": "morning",
    "B": "morning",
    "C": "afternoon",
    "D": "evening"
}

SLOTS = {
    "morning": "10:30 AM to 12:30 PM",
    "afternoon": "1:15 PM to 3:15 PM",
    "evening": "3:30 PM to 5:30 PM"
}

# -------------------------------
# Attendance data
# -------------------------------
ATTENDANCE = {
    "Misc(intro)": {
        "24/07/2025": {"A": [3,4,5,6,7,10,11,12,13,15,16,17,18,19]},
        "28/07/2025": {"C": [42,43,44,45,46,47,48,49,50,51,52,56,57,59,60]}
    },
    "Lab 0": {
        "04/08/2025": {"C": [42,43,44,45,46,47,48,49,50,51,52,57,58,59,60]},
        "07/08/2025": {"A": [2,3,4,6,7,10,11,13,14,15,16,17,18,19,20],
                 "D23": [61,62,63,64,65,67],
                 "D24": [1,2,3,4,5,6,8,9,10]},
        "08/08/2025": {"B": [21,22,23,24,25,26,27,28,30,33,36,37,38,39]}
    },
    "Lab 1": {
        "11/08/2025": {"C": [42,43,44,45,46,47,48,49,50,51,52,53,56,57,58]},
        "14/08/2025": {"A": [3,4,6,7,8,9,10,11,12,13,16,17,18,19,20],
                 "D23": [61,63],
                 "D24": [5,8,10]},
        "22/08/2025": {"B": [21,22,26,28,30,32,33,35,37]}
    },
    "Lab 2": {
        "18/08/2025": {"C": [43,44,46,47,49,50,51,60]},
        "21/08/2025": {"A": [2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19],
                 "D23": [61,62,63,64,65,67],
                 "D24": [1,2,3,4,5,6,9]}
    },
    "Lab 3": {
        "25/08/2025": {"C": [42,43,44,45,46,47,48,49,50,51,52,57,58,59,60]},
        "28/08/2025": {"A": [2,3,4,5,6,7,8,9,10,11,12,15,16,20],
                 "D23": [61,63,64,65,67],
                 "D24": [1,2,3,4,6,7,8,9,10]},
    },
    "Lab 4": {
        "08/09/2025": {"C": [42,43,44,45,46,47,48,49,50,51,52,57,60]},
        "11/09/2025": {"A": [3,4,10,11,15,16]},
    }
}

# -------------------------------
# Precompute attendance lookup
# -------------------------------
LOOKUP = {}
for lab, dates in ATTENDANCE.items():
    for date, rec in dates.items():
        for batch_key, nums in rec.items():
            for n in nums:
                LOOKUP[(lab, batch_key, n)] = date

# -------------------------------
# Helper to check presence
# -------------------------------
def was_present(prn, lab_key):
    batch, num, prefix = get_batch(prn)
    if not batch:
        print(f"Warning: PRN {prn} did not match any batch rule")
        return "-"

    # Resolve D-subgroup keys
    if batch == "D":
        d_key = "D23" if prefix == "BT23F05F" else "D24"
    else:
        d_key = batch

    date = LOOKUP.get((lab_key, d_key, num))
    if date:
        return f"{date} {SLOTS[SLOT_GROUPS[batch]]}"
    return "-"

# -------------------------------
# Build one student's row
# -------------------------------
def build_output_row(row):
    prn, name = row["PRN"], row["Name"]
    output_row = {"PRN": prn, "Name": name}
    for lab_key in ATTENDANCE.keys():
        output_row[lab_key] = was_present(prn, lab_key)
    return output_row

# -------------------------------
# Main processing
# -------------------------------
def process_file():
    with open(INPUT_FILE, newline='', encoding='utf-8') as infile, \
         open(OUTPUT_FILE, "w", newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["PRN", "Name"] + list(ATTENDANCE.keys()))
        writer.writeheader()
        for row in reader:
            writer.writerow(build_output_row(row))

process_file()
print("attendance_output.csv generated.")
