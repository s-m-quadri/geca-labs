# Ask the user to enter a number.
# Print:
#  - "Positive" if it's > 0
#  - "Negative" if it's < 0
#  - "Zero" if it's 0

# 💡 TIP:
# Use `if`, `elif`, and `else`.
number = int(input("Enter a number: "))
if(number>0):
    print("Positive")
elif (number<0):
    print("Negative")
else:
    print("Zero")