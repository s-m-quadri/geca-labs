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
#     # Handle the error (e.g., log it, re-prompt the user, etc.)   


def main() -> None: 
    try:
        student_id = int(input("Enter student ID: "))
        print(f"Student ID: {student_id}")
    except ValueError:
        print("Invalid input! Please enter a number.")
        # Optionally, you can re-prompt the user or log the error here.
    finally:
        print("Exiting program.")
        # Optionally, you can perform cleanup actions here.
if __name__ == "__main__":
    main()              