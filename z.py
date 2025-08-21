# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else: 
    print("Odd number")
print("Square root:", math.sqrt(num))
if num > 10:
    print("First, solve the problem. Then, write the code.")