# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

# Ask user for a number
user_input = input("Enter a number: ")

# Option 1: Using str.isdigit()
if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
    number = int(user_input)
    print("You entered:", number)
else:
    print("Invalid input")

# --- OR ---

# Option 2: Using try-except (safer, recommended)
try:
    number = int(user_input)
    print("You entered:", number)
except ValueError:
    print("Invalid input")
