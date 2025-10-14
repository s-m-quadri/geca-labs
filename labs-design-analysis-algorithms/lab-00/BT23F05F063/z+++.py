# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.

from datetime import datetime

while True:
    print("\nMenu:")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == '1':
        name = input("Enter your name: ")
        print(f"Hello, {name}!")
    elif choice == '2':
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
