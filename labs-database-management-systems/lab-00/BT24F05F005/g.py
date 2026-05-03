# Task: Implement basic exception handling (important for database operations):
#  - Try to convert user input to integer (for student ID)
#  - Handle ValueError if input is not a number
#  - Print appropriate error message

# 💡 TIP:
# try:
#     value = int(input("Enter ID: "))
#     print(f"ID: {value}")
# except ValueError:
#     print("Invalid input! Please enter a number.")

try:
	student_id = int(input("Enter student ID: "))
	print(f"Valid ID: {student_id}")
except ValueError:
	print("Invalid input! Please enter a number.")


