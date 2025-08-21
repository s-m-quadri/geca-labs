# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

user_input = input("Enter a number: ")

if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
    num = int(user_input)
    print("You entered:", num)
else:
    print("Invalid input")
