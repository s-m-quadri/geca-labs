# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print("You entered:", number)
except ValueError:
    print("Invalid input")
