# Task: Create a dictionary representing a student record (like a database row):
#  - id, name, age, department
#  - Print each field with its value
#  - Access and print only the student's name

# 💡 TIP:
# Dictionary: student = {"id": 101, "name": "Alice", ...}
# Access: student["name"]
# Loop: for key, value in student.items():

student = {
    "id": 101,
    "name": "Alice",
    "age": 20,
    "department": "CSE",
    "cgpa": 8.5,
    "year": 2
}

print("\n" + "="*40)
print("STUDENT DATABASE RECORD")
print("="*40)
for key, value in student.items():
    print(f"  {key.upper()}: {value}")

print("\n" + "-"*40)
print(f"Student Name: {student['name']}")
print(f"CGPA: {student['cgpa']}/10.0")
print("="*40)


