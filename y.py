# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

# Method 1: Using isdigit()
user_input = input("Enter a number: ")
if user_input.isdigit():
    number = int(user_input)
    print(f"Valid number: {number}")
else:
    print("Invalid input")

# Method 2: Using try-except
try:
    number = int(input("Enter another number: "))
    print(f"Valid number: {number}")
except ValueError:
    print("Invalid input")
