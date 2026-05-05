# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.
import datetime

while True:
    print("\nMenu:")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello, User!")
    elif choice == "2":
        print("Current time:", datetime.datetime.now())
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
