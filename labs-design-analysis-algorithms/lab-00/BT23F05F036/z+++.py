# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.
import time

while True:
    print("\nMenu:")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        print("Hello! Hope you're having a great day.")
    elif choice == '2':
        print("Current time:", time.strftime("%Y-%m-%d %H:%M:%S"))
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
