# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.

num=input("Enter Number: ")
try:
    print(f"Number is valid digit") if num.isdigit() else print("Invalid input")
except:
    print("Something went wrong")