# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

n = input("Enter a number: ")
if n.isdigit():
    print("You entered:", int(n))
else:
    print("Invalid input")