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

with open("student.txt", "w") as f:
    f.write("")

def give_input(name, age, dept):
    with open("student.txt", "a") as f:
        f.write(f"Student detail,\n")
        f.write(f"1.Name\t:{name}\n")
        f.write(f"2.Age\t:{age}\n")
        f.write(f"Dept.\t:{dept}\n\n")

give_input("Mayur Wakchaure",20,"CSE")
give_input("Pawan Pawar",21,"CSE")
give_input("Rohan Pawar",19,"CSE")

with open("student.txt", "r") as f:
    print(f.read())