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


# Write to file
with open("students.txt", "w") as f:
    f.write("Alice\n")
    f.write("Bob\n")
    f.write("Charlie\n")

# Read from file
with open("students.txt", "r") as f:
    content = f.read()
    print(content)