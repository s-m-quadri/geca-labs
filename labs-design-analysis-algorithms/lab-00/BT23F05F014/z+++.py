# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.

import datetime

while True:
    print("\n--- MENU ---")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        name = input("Enter your name: ")
        print(f"Hello, {name}! Hope you're having a great day 😊")

    elif choice == '2':
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Current time:", current_time)

    elif choice == '3':
        print("Exiting program...Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
