# Task: Create a dictionary representing a student record (like a database row):
#  - id, name, age, department
#  - Print each field with its value
#  - Access and print only the student's name

# 💡 TIP:
# Dictionary: student = {"id": 101, "name": "Alice", ...}
# Access: student["name"]
# Loop: for key, value in student.items():

studentinfo = {"id" : 101,
                "name" : "Meeran",
                "age" : 18,
                "department" : "CSE"}

for key, value in studentinfo.items():
    print(f"{key} : {value}")
    
print(studentinfo["name"])
