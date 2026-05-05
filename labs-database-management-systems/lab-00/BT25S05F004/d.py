# Task: Create a dictionary representing a student record (like a database row):
#  - id, name, age, department
#  - Print each field with its value
#  - Access and print only the student's name

# 💡 TIP:
# Create a dictionary representing a student record
student = {
    "id": 101,
    "name": "Alice",
    "age": 20,
    "department": "Computer Science"
}

# Print each field with its value
for key, value in student.items():
    print(key, ":", value)

# Access and print only the student's name
print("Student Name:", student["name"])
