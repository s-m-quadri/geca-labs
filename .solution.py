# Solution file for Python basics (for self-verification)
# Don't copy-paste! Understand and write your own code.

# a.py solution
print("Hello, Python!")
print("Welcome to DBMS Lab")

# b.py solution
student_id = 101
student_name = "Alice"
marks = 85.5
department = "CSE"
print(f"ID: {student_id}, Name: {student_name}, Marks: {marks}, Dept: {department}")

# c.py solution
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
for student in students:
    print(student)
print(f"Total students: {len(students)}")

# d.py solution
student = {"id": 101, "name": "Alice", "age": 20, "department": "CSE"}
for key, value in student.items():
    print(f"{key}: {value}")
print(f"Student name: {student['name']}")

# e.py solution
def display_student(name, age, dept):
    print(f"Student: {name}, Age: {age}, Department: {dept}")

display_student("Alice", 20, "CSE")
display_student("Bob", 21, "ECE")
display_student("Charlie", 19, "MECH")

# f.py solution
with open("students.txt", "w") as f:
    f.write("Alice,20,CSE\n")
    f.write("Bob,21,ECE\n")
    f.write("Charlie,19,MECH\n")

with open("students.txt", "r") as f:
    print(f.read())

# g.py solution
try:
    student_id = int(input("Enter student ID: "))
    print(f"Valid ID: {student_id}")
except ValueError:
    print("Invalid input! Please enter a number.")


    
