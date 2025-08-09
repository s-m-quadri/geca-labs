# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

num = input("Enter a number: ")

if not num.isdigit():
    print("Invalid Input")

# try:
#     num = int(input("Enter a number: "))
#     print("You entered:", num)
# except ValueError:
#     print("Invalid input")