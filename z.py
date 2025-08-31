# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

quotes = [
    "Believe in yourself!",
    "Keep pushing forward!",
    "You can do it!",
    "Success is on the way!",
    "Never give up!"
]

num = input("Enter a number: ")

if num.isdigit():
    n = int(num)
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
    print("Square root:", math.sqrt(n))
    if n > 10:
        print("Motivation:", random.choice(quotes))
else:
    print("Invalid input")
