# Task: Create a dictionary representing a student record (like a database row):
#  - id, name, age, department
#  - Print each field with its value
#  - Access and print only the student's name

# 💡 TIP:
student = {"id": 101, "name": "vedika", "age":20 , "department":"cse"}
for key, value in student.items():
    print(key,"->",value)

print("Student Name :", student["name"])
