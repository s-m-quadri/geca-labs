# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

num = input("Enter a number: ")

if num.isdigit():
    num = int(num)
    print(f"You entered: {num}")
else:
    print("Invalid input")


try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input")
