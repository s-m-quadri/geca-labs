# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.

import datetime

def greet_user():
    name = input("What's your name? ")
    print(f"Hello, {name}! Nice to meet you!")

def print_current_time():
    current_time = datetime.datetime.now()
    print(f"Current time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

while True:
    print("\n=== MENU ===")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        greet_user()
    elif choice == '2':
        print_current_time()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")