# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.

import time

while True:
    print("Menu:")
    print("1. Greet user")
    print("2. Print current time")
    print("3. Exit")

    num = int(input("Enter your choice(1,2,3): "))
    print()
    
    if num==1:
        print("Hello user\n")
    elif num==2:
        print(f"Current time : {time.strftime("%H:%M:%S")}\n")
    elif num==3:
        print("Exiting...\n")
        break
    else:
        print("Invalid choice\n")