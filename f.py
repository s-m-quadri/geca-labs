# Ask the user to enter a number.
# Print:
#  - "Positive" if it's > 0
#  - "Negative" if it's < 0
#  - "Zero" if it's 0

# 💡 TIP:
# Use `if`, `elif`, and `else`.

number=int(input("enter a number"))
if(number>0):
    print("positive");
elif(number<0):
    print("negative")
else:
    print("zero")