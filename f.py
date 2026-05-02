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

with open("students.txt", "w") as f:
    f.write("Aayush,21,CSE\n")
    f.write("Diya,20,Mechanical\n")
    f.write("Meera,22,IT\n")

with open("students.txt", "r") as f:
    print(f.read())

