# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

quotes = [
    "Keep going!",
    "You can do it!",
    "Believe in yourself!",
    "Never give up!"
]

num_input = input("Enter a number: ")

try:
    num = int(num_input)
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
    
    print("Square root:", math.sqrt(num))
    
    if num > 10:
        print("Motivational quote:", random.choice(quotes))
except ValueError:
    print("Invalid input")
