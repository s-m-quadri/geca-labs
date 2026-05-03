import time

while True:
    print("\nMenu:")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")
    choice = input("Enter choice (1-3): ")
    if choice == '1':
        print("Hello!")
    elif choice == '2':
        print("Current time:", time.strftime('%Y-%m-%d %H:%M:%S'))
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
