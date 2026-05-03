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
# Write student data to file
with open("students.txt", "w") as f:
    f.write("Alice,20,Computer Science\n")
    f.write("Bob,21,Mechanical Engineering\n")
    f.write("Charlie,19,Electrical Engineering\n")

# Read and print file contents
print("Student Records from File:\n")
with open("students.txt", "r") as f:
    print(f.read())

