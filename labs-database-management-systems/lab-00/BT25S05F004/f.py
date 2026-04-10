# Task: Write student data to a file (simulating data persistence):
#  - Create a file named "students.txt"
#  - Write at least 3 student records (one per line)
#  - Format: Name,Age,Department
#  - Then read and print the file contents

# 💡 TIP:
# Write student data to a file

with open("students.txt", "w") as f:
    f.write("aaa,19,Information Technology\n")
    f.write("bbb,21,Electronics\n")
    f.write("ccc,20,Computer Science\n")

# Read and print the file contents

with open("students.txt", "r") as f:
    print("Student Records:\n")
    print(f.read())   
    print(f.read())


