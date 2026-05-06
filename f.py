<<<<<<< HEAD
# Task: Write student data to a file (simulating data persistence):
#  - Create a file named "students.txt"
#  - Write at least 3 student records (one per line)
#  - Format: Name,Age,Department
#  - Then read and print the file contents
with open("students.txt", "w") as f:
    f.write("kirti,20,CSE\n")
    f.write("poorva,21,ECE\n")
    f.write("renu,19,MECH\n")
with open("students.txt", "r") as f:
    print(f.read())  
# 💡 TIP:
# Write: with open("file.txt", "w") as f:
#           f.write("text\n")
# Read: with open("file.txt", "r") as f:
#          print(f.read())
=======
records = [
    "Alice,20,CSE",
    "Bob,21,ECE",
    "Cara,19,ME"
]

filename = "students.txt"
with open(filename, "w") as f:
    for record in records:
        f.write(record + "\n")

with open(filename, "r") as f:
    contents = f.read()

print(contents, end="")
>>>>>>> 5ca9861c (BT25S05F002)


