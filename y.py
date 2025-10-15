# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

num = input("Enter a number: ")
#todo

if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):
    print("Valid number:", int(num))
else:
    print("Invalid input")
