# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
