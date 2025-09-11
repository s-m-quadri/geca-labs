import csv

# -----------------------------
# CONFIGURATION
# -----------------------------
INPUT_FILE = "output/students.csv"
OUTPUT_FILE = "output/attendance.csv"

# -------------------------------
# Batch mapping based on PRN rules
# -------------------------------
def get_batch(prn):
    if prn.startswith("BT23F05F"):
        num = int(prn[-3:])
        if 1 <= num <= 20:
            return 'A'
        elif 21 <= num <= 40:
            return 'B'
        elif 41 <= num <= 60:
            return 'C'
        elif 61 <= num <= 67:
            return 'D'
    elif prn.startswith("BT24S05F"):
        num = int(prn[-3:])
        if 1 <= num <= 10:
            return 'D'
    return None

# -------------------------------
# Batch time slots
# -------------------------------
SLOTS = {
    'A': "10:30 AM to 12:30 PM",
    'B': "10:30 AM to 12:30 PM",
    'C': "1:15 PM to 3:15 PM",
    'D': "3:30 PM to 5:30 PM"
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
# Helper to check presence
# -------------------------------
def was_present(prn, lab_key):
    batch = get_batch(prn)
    if not batch:
        return "-"

    # Distinguish between BT23F05F and BT24S05F
    if prn.startswith("BT23F05F"):
        num = int(prn[-3:])
        d_key = "D23" if batch == 'D' else batch
    elif prn.startswith("BT24S05F"):
        num = int(prn[-3:])
        d_key = "D24" if batch == 'D' else batch
    else:
        return "-"

    for date, rec in ATTENDANCE[lab_key].items():
        if d_key in rec and num in rec[d_key]:
            return f"{date} {SLOTS[batch]}"
    return "-"

# -------------------------------
# Main processing
# -------------------------------
with open(INPUT_FILE, newline='', encoding='utf-8') as infile, open(OUTPUT_FILE, "w", newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ["PRN", "Name", "Misc(intro)", "Lab 0", "Lab 1", "Lab 2"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        prn = row["PRN"]
        name = row["Name"]

        output_row = {
            "PRN": prn,
            "Name": name,
        }

        for lab_key in ["Misc(intro)", "Lab 0", "Lab 1", "Lab 2"]:
            output_row[lab_key] = was_present(prn, lab_key)

        writer.writerow(output_row)

print("attendance_output.csv generated.")