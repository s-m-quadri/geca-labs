# Task: Create a dictionary representing a student record (like a database row):
#  - id, name, age, department
#  - Print each field with its value
#  - Access and print only the student's name

# 💡 TIP:
# Dictionary: student = {"id": 101, "name": "Alice", ...}
# Access: student["name"]
# Loop: for key, value in student.items():

student = {'id' = 101, 'name' = "aditya", 'age' = 20, 'department' = "CSE"}

for k,v in student:
    print(f"{k} is {v}")

# for printing name of student
NAME = student['name']
print(f"the name of student is {NAME}")


