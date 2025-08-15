# Ask the user to enter a number.
# Print:
#  - "Positive" if it's > 0
#  - "Negative" if it's < 0
#  - "Zero" if it's 0

# 💡 TIP:
# Use `if`, `elif`, and `else`.
num=int(input("Enter a number: "))
if(num>0):
    print("Number is positive")
elif(num<0):
    print("Number is negative")
else:
    print("Number is zero")