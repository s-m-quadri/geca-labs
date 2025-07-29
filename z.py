# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random

num_str = input("Enter a number: ")
if num_str.lstrip('-').isdigit():
    num = int(num_str)
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
    if num >= 0:
        print("Square root:", math.sqrt(num))
    else:
        print("Cannot compute square root of negative number")
    if num > 10:
        quotes = ["Believe in yourself!",]
        print(random.choice(quotes))
else:
    print("Invalid input")
