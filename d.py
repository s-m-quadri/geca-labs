# Task: Create a dictionary representing a student record (like a database row):
#  - id, name, age, department
#  - Print each field with its value
#  - Access and print only the student's name

# 💡 TIP:
# Dictionary: student = {"id": 101, "name": "Alice", ...}
# Access: student["name"]
# Loop: for key, value in student.items():
dict_1={
    "id":40,
    "name":"prachi",
    "age":19
}
for key,value in dict_1.items():
    print(f"{key}:{value}")



