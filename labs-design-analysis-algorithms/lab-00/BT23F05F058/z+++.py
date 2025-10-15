import time

while True:
    print("1. Greet")
    print("2. Time")
    print("3. Exit")
    
    choice = input("Choose: ")
    
    if choice == '1':
        print("Hello!")
    elif choice == '2':
        print("Current time:", time.ctime())
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
