# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

x = input("Enter a number: ")
if x.isdigit():
    print("You entered:", int(x))
else:
    print("Invalid input")
