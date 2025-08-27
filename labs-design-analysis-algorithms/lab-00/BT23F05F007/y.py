# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.
def take_number():
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        print("You entered:", int(user_input))
    else:
        print("Invalid input")

take_number()
