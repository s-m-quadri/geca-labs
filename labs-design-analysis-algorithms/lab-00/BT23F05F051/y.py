# Take a number from user input. 
# If the input is not a valid integer, print "Invalid input".

# 💡 TIP:
# Use `.isdigit()` or handle exceptions using try-except.
try :
    n=int(input("enter a number:"))
except:
    print("Invalid input")