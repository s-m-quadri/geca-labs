# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.


x = input("Enter a number: ")

if x.isdigit():
    y = int(x)
    print(f"You entered: {y}")
else:
    print("Invalid input")
