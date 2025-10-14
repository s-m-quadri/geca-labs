import time

while True:
    print("Menu:")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        print("Hello, user!")
    elif choice == "2":
        print("Current time:", time.strftime("%H:%M:%S"))
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
