# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

quotes = [
    "Believe in yourself and all that you are.",
    "You are stronger than you think.",
    "Every day is a second chance.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones."
]

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
print("Square root:", math.sqrt(num))
if num > 10:
    print(random.choice(quotes))
