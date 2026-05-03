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
    # Take input from user
    student_id = input("Enter Student ID: ")
    
    # Convert to integer
    student_id = int(student_id)
    
    # If successful
    print(f"Student ID: {student_id}")

except ValueError:
    # Handle invalid input
    print("Invalid input! Please enter a valid number.")
