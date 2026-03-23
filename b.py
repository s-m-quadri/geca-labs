# Task: Create variables for a student record:
#  - student_id (integer, e.g., 101)
#  - student_name (string, e.g., "Alice")
#  - marks (float, e.g., 85.5)
#  - department (string, e.g., "CSE")
# Print all variables in a formatted way.

# 💡 TIP:
# Use f-strings for formatting: f"ID: {student_id}"

student_id = int(input("enter student_id : "))
student_name = input("enter student_name : ")
marks = float(input("enter marks : "))
department = input("enter department name : ")

print(f"student_id is {student_id}\nstudent_name is {student_name}\nmarks is {marks}\ndepartment is {department}")