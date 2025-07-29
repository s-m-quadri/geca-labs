# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.
num = input("Enter a number: ")
if num.lstrip('-').isdigit():
    print(int(num))
else:
    print("Invalid input")
