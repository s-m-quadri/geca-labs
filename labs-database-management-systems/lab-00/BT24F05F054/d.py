# Task: Create a dictionary representing a student record (like a database row):
#  - id, name, age, department
#  - Print each field with its value
#  - Access and print only the student's name

# 💡 TIP:
# Dictionary: student = {"id": 101, "name": "Alice", ...}
# Access: student["name"]
# Loop: for key, value in student.items():


student = {"Id": 67, "Name": "Mayur", "Age": 20, "Dept": "CSE"}

for key,value in student.items():
    print(f"{key}: {value}")
print(f"student Name: {student['Name']}")