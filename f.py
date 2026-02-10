# Task: Write student data to a file (simulating data persistence):
#  - Create a file named "students.txt"
#  - Write at least 3 student records (one per line)
#  - Format: Name,Age,Department
#  - Then read and print the file contents

# 💡 TIP:
with open("students.txt", "w") as f:
        f.write("Hello, My name is vedika, I am 20 years old and I am from cse department\n")
        f.write("Hello, My name is vanshita, I am 23 years old and I am from it department\n")
        f.write("Hello, My name is akshay, I am 20 years old and I am from aiml department")
with open("students.txt", "r") as f:
         print(f.read())


