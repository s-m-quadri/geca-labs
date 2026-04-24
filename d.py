# Task: Create a dictionary representing a student record (like a database row):
#  - id, name, age, department
#  - Print each field with its value
#  - Access and print only the student's name

# 💡 TIP:
# Dictionary: student = {"id": 101, "name": "Alice", ...}
# Access: student["name"]
# Loop: for key, value in student.items():


# Create a dictionary
student = {
    "id": 101,
    "name": "Alice",
    "age": 15,
    "grade": "10th"
}

# Access specific value
print("Student Name:", student["name"])

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)