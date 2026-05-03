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

with open("studetn.txt", "w") as f:
    f.write("Rohan,20,CSE\n")
    f.write("Soham,37,ENTC\n")

    with open("students.txt", "r") as f:

        print("Student records from file")
        print(f.read())

