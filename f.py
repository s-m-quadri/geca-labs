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
# Your code here
students_data = [       
    "Alice,20,CSE",
    "Bob,22,ECE",
    "Charlie,21,ME"
]       

with open("students.txt", "w") as f:
    for record in students_data:
        f.write(record + "\n")          

with open("students.txt", "r") as f:
    contents = f.read()
    print(contents) 




                    


