# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

user_input = input("Enter a number: ")

# Method 1: Using isdigit()
if user_input.isdigit():
    number = int(user_input)
    print("Valid number:", number)
else:
    print("Invalid input")

# Method 2: Using try-except (commented)
# try:
#     number = int(user_input)
#     print("Valid number:", number)
# except ValueError:
#     print("Invalid input")
