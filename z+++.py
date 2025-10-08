# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.

#solution
import time

while True:
	print("Menu:")
	print("1. Greet user")
	print("2. Print current time")
	print("3. Exit")
	choice = input("Enter choice (1-3): ")
	if choice == '1':
		print("Hello, user!")
	elif choice == '2':
		print("Current time:", time.strftime('%Y-%m-%d %H:%M:%S'))
	elif choice == '3':
		print("Goodbye!")
		break
	else:
		print("Invalid choice.")