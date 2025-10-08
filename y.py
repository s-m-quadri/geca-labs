# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.


#solution
num = input("Enter a number: ")
if num.isdigit():
    print("You entered:", int(num))
else:
    print("Invalid input")