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

print("\n" + "="*40)
print("STUDENT ID VALIDATOR")
print("="*40)

for attempt in range(3):
    try:
        student_id = int(input(f"Attempt {attempt+1}/3 - Enter Student ID: "))
        if 100 <= student_id <= 999:
            print(f"✓ Valid Student ID: {student_id}")
            print("SUCCESS!")
            break
        else:
            print("  ID must be between 100-999")
    except ValueError:
        print("  ✗ Invalid input! Please enter a number.")
else:
    print("\nFailed: Max attempts reached.")
print("="*40)


