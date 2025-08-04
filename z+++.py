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

    a = input("Enter your number (1-3): ")

    if a == "1":
        name = input("Enter your name: ")
        print(f"Namaskar, {name}")
    elif a == "2":
        print("Current time:", time.strftime("%H:%M:%S"))
    elif a == "3":
        print("Exit")
        break