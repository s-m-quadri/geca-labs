# Solution file for Python basics (for self-verification)
# Don't copy-paste! Understand and write your own code.

# a.py solution
print("Hello, Python!")
print("Welcome to DBMS Lab")

# b.py solution
student_id = BT24F05F038
student_name = "Akshada"
marks = 85.5
department = "CSE"
print(f"ID: {student_id}, Name: {student_name}, Marks: {marks}, Dept: {department}")

# c.py solution
students = ["Shreya", "Tejas", "Pradnya", "Diana", "Eve"]
for student in students:
    print(student)
print(f"Total students: {len(students)}")

# d.py solution
student = {"id": 101, "name": "Shreya", "age": 20, "department": "CSE"}
for key, value in student.items():
    print(f"{key}: {value}")
print(f"Student name: {student['name']}")

# e.py solution
def display_student(name, age, dept):
    print(f"Student: {name}, Age: {age}, Department: {dept}")

display_student("Shreya", 20, "CSE")
display_student("Tejas", 21, "ECE")
display_student("Pradnya", 19, "MECH")

# f.py solution
with open("students.txt", "w") as f:
    f.write("Shreya,20,CSE\n")
    f.write("Tejas,21,ECE\n")
    f.write("Pradnya,19,MECH\n")

with open("students.txt", "r") as f:
    print(f.read())

# g.py solution
try:
    student_id = int(input("Enter student ID: "))
    print(f"Valid ID: {student_id}")
except ValueError:
    print("Invalid input! Please enter a number.")
