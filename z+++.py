import time

while True:
    # Display menu
    print("\nMenu:")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        name = input("Enter your name: ")
        print(f"Hello, {name}!")
        
    elif choice == "2":
        current_time = time.strftime("%H:%M:%S")
        print("Current time:", current_time)
        
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
