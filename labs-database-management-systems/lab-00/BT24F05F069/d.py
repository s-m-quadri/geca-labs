# Task: Create a dictionary representing a student record (like a database row):
#  - id, name, age, department
#  - Print each field with its value
#  - Access and print only the student's name

# 💡 TIP:
# Dictionary: student = {"id": 101, "name": "Alice", ...}
# Access: student["name"]
# Loop: for key, value in student.items():

student = {
    "id": 102,
    "name": "Aditya Sharma",
    "age": 20,
    "department": "IT"
}

for key, value in student.items():
    print(f"{key.capitalize()}: {value}")

print(f"Accessed Name: {student['name']}")
