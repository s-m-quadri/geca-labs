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

with open("student.txt","w") as f:
         f.write("Sheetal,20,CSE\n")
         f.write("Sanika,19,IT\n")
         f.write("Anjali,18,CSE\n")
with open("student.txt","r")as f:
        print(f.read())
                 

