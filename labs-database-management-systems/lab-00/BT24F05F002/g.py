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

while (True):
    try:
        id = int(input("enter student id : "))
        print(f"ID : {id}")
        print("It is a VALID ID")
        break
    except ValueError:
        print("you enter invalid student id, input is not a number")
        print("Enter id again")



