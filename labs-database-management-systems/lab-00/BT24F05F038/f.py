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
    f.write("Rahul,20,CSE\n")
    f.write("Sneha,19,IT\n")
    f.write("Amit,21,Mechanical\n")

with open("students.txt", "r") as f:
    content = f.read()
    print("Student Records:\n")
    print(content)
