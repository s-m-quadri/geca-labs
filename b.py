# Task: Create variables for a student record:
#  - student_id (integer, e.g., 101)
#  - student_name (string, e.g., "Alice")
#  - marks (float, e.g., 85.5)
#  - department (string, e.g., "CSE")
# Print all variables in a formatted way.

# 💡 TIP:
# Use f-strings for formatting: f"ID: {student_id}"

student_id = 101
student_name = "Alice"
marks = 85.5
department = "CSE"
passtatus = "Pass" if marks >= 40 else "Fail"

print("\n" + "="*40)
print("STUDENT RECORD")
print("="*40)
print(f"Student ID: {student_id}")
print(f"Name: {student_name}")
print(f"Marks: {marks}")
print(f"Department: {department}")
print(f"Status: {passtatus}")
print("="*40)


