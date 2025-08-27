# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.

import time
while True:
    print("1. Greet\n2. Time\n3. Exit")
    ch = input("Choose any option: ")
    if ch == '1':
        print("Hello!")
    elif ch == '2':
       current_time = time.localtime()
       formatted_time = time.strftime("%H:%M:%S", current_time)
       print(formatted_time)
    elif ch == '3':
        break
    else:
        print("Invalid")