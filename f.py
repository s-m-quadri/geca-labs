# Ask the user to enter a number.
# Print:
#  - "Positive" if it's > 0
#  - "Negative" if it's < 0
#  - "Zero" if it's 0

# 💡 TIP:
# Use `if`, `elif`, and `else`.
num=int(input("Enter the number:"))
if(num>0):
    print("Positive number.")
elif(num<0):
    print("Negative number.")
else:
    print("Zero")
