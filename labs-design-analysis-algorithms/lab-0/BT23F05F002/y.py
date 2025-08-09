# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

user_input = input("Enter a number: ")

try:
    number = int(user_input)
    print("Valid number:", number)
except ValueError:
    print("Invalid input")
