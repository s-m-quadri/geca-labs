# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.

import time

while True:
    print("\n===== MENU =====")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")

    choice = input("Apna choice daalo (1-3): ")

    if choice == '1':
        name = input("Apna naam batao: ")
        print(f"Namaste, {name}! 👋")
    elif choice == '2':
        current_time = time.strftime("%H:%M:%S")
        print("Current time:", current_time)
    elif choice == '3':
        print("Program se bahar nikal rahe hain... 👋")
        break
    else:
        print("Invalid choice! Sirf 1, 2, ya 3 daalo.")
