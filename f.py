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
students = [
    "Name:Alice,Age:20,Department:Computer Science",
    "Name:Bob,Age:22,Department:Mechanical Engineering",
    "Name:Charlie,Age:19,Department:Electrical Engineering"
]
with open("students.txt", "w") as f:
    for student in students:
        f.write(student + "\n")
with open("students.txt", "r") as f:
    print(f.read())


