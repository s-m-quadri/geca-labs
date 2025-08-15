# Ask the user to enter a number.
# Print:
#  - "Positive" if it's > 0
#  - "Negative" if it's < 0
#  - "Zero" if it's 0

# 💡 TIP:
# Use `if`, `elif`, and `else`.


a=input("Enter any number")
num=int(a)
if(num>0):
 print("Positive")
elif(num<0):
 print("Negative")
else:
 print("Zero")