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
students = open("students.txt", "w")
students.write("Alice,20,CSE\n")
students.write("Bob,22,ECE\n")
students.write("Charlie,21,ME\n")
students.close()    
with open("students.txt", "r") as f:
    print(f.read())