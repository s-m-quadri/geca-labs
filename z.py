# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.


import math
import random

quote = ["Comparison is a thief of joy"]

a = input("Enter number: ")

if a.isdigit():
    a = int(a)
    print("Even number:" if a % 2 == 0 else "Odd number")
    print("Square root:", math.sqrt(a))
    
    if a > 10:
        print("Motivational quote:", random.choice(quote))
else:
    print("Invalid input")