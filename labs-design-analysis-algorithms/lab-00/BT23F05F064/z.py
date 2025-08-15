# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

quotes = [
    "Believe in yourself!",
    "You are stronger than you think.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Stay positive, work hard, make it happen."
]

try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

    sqrt_val = math.sqrt(num)
    print(f"Square root of {num} is {sqrt_val}")

    if num > 10:
        print("Motivational Quote:", random.choice(quotes))

except ValueError:
    print("Invalid input! Please enter a valid integer.")