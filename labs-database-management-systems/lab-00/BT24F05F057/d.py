# Task: Create a dictionary representing a student record (like a database row):
#  - id, name, age, department
#  - Print each field with its value
#  - Access and print only the student's name

# 💡 TIP:
# Dictionary: student = {"id": 101, "name": "Alice", ...}
# Access: student["name"]
# Loop: for key, value in student.items():

# Task -1 
student = {
    "id":106,
    "name":"Adarsh",
    "sex":"Male",
    "age":69
}

# Task - 2
print(f"Accessing student['name'] -> {student['name']}\n")


# Task - 3
for key , value in student.items():
    print(f"{key} -> {value}")