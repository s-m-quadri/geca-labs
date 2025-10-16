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
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter your name: ")
        print(f"Hello, {name}!")
    elif choice == '2':
        print("Current time:", time.strftime("%H:%M:%S"))
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
        #todo
