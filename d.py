# Task: Create a dictionary representing a student record (like a database row):
#  - id, name, age, department
#  - Print each field with its value
#  - Access and print only the student's name

# 💡 TIP:
# Dictionary: student = {"id": 101, "name": "Alice", ...}
# Access: student["name"]
# Loop: for key, value in student.items():


# student = {"id": 101,
# "name": "Alice",
# "age": 20,
# "department": "CSE"}    

# print(f"ID: {student['id']}")
# print(f"Name: {student['name']}")
# print(f"Age: {student['age']}")
# print(f"Department: {student['department']}")

# print(f"Student's Name: {student['name']}")

# for key, value in student.items():
#     print(f"{key.capitalize()}: {value}")   

student = {
    "id": 101,
    "name": "Alice",
    "age": 20,
    "department": "CSE"
}  

# print(f"ID: {student['id']}")
# print(f"Name: {student['name']}")
# print(f"Age: {student['age']}")
# print(f"Department: {student['department']}")

for key, value in student.items():
    print(f"{key.capitalize()}: {value}")




