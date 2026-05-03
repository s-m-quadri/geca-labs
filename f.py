# Task: Write student data to a file (simulating data persistence):
#  - Create a file named "students.txt"
#  - Write at least 3 student records (one per line)
#  - Format: Name,Age,Department
#  - Then read and print the file contents

# 💡 TIP:
# Write: with open("file.txt", "w") as f:
#           f.write("text\n")
# Read: with open("file.txt", "r") as f:
#          print(f.read())

# Write student records to file
student_data = [
    "Alice,20,CSE,8.5",
    "Bob,21,ECE,7.8",
    "Charlie,19,ME,8.2",
    "Diana,20,CSE,8.9"
]

with open("students.txt", "w") as f:
    f.write("Name,Age,Department,CGPA\n")
    for record in student_data:
        f.write(record + "\n")

print("\n" + "="*50)
print("FILE CONTENTS - students.txt")
print("="*50)
with open("students.txt", "r") as f:
    for line_num, line in enumerate(f, 1):
        print(f"Line {line_num}: {line.rstrip()}")
print("="*50)


