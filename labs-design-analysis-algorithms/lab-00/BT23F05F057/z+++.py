# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.


import time
while True:
    print("1. Greet\n2. Time\n3. Exit")
    choice = input("Choose: ")
    if choice == '1':
        print("Hello!")
    elif choice == '2':
        print(time.ctime())
    elif choice == '3':
        break
    else:
        print("Invalid")