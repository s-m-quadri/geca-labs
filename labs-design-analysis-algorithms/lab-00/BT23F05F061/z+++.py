# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.

while True:
    print("Menu:")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        name = input("Enter your name: ")
        print(f"Hello, {name}!")
    elif choice == '2':
        from datetime import datetime
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current time: {current_time}")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")
        