# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.

import time

while True:
    
    print("\n=== MENU ===")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")


    choice = input("Choose an option (1-3): ")

    if choice == '1':
        name = input("Enter your name: ")
        print(f"👋 Hello, {name}!")
    elif choice == '2':
        current_time = time.strftime("%H:%M:%S")
        print("⏰ Current time:", current_time)
    elif choice == '3':
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid option. Please choose 1, 2, or 3.")
