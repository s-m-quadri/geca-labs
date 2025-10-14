# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.
# Take a number from user input
user_input = input("Enter a number: ")

try:
    num = int(user_input)
    print("You entered:", num)
except ValueError:
    print("Invalid input")
