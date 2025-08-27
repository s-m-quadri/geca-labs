# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(f"Valid integer: {number}")
except ValueError:
    print("Invalid input")

print("\nAlternative method using .isdigit():")
user_input = input("Enter a positive number: ")
if user_input.isdigit():
    number = int(user_input)
    print(f"Valid positive integer: {number}")
else:
    print("Invalid input")