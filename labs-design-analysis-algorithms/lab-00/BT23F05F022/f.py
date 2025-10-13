# Ask the user to enter a number.
# Print:
#  - "Positive" if it's > 0
#  - "Negative" if it's < 0
#  - "Zero" if it's 0

# 💡 TIP:
# Use `if`, `elif`, and `else`.

num=int(input("Enter number: "))
print("Positive") if num>0 else print("Negative") if num<0 else print("Zero")