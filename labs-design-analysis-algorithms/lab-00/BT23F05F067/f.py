# Ask the user to enter a number.
# Print:
#  - "Positive" if it's > 0
#  - "Negative" if it's < 0
#  - "Zero" if it's 0

# 💡 TIP:
# Use `if`, `elif`, and `else`.

a = int(input("Enter a no:"))
if(a<0):
    print("Negative")
elif(a>0):
    print("Positive")
else:
    print("Zero")
