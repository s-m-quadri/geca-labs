# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

quotes = [
    "Keep going, you're doing great!",
    "Believe in yourself!",
    "Every day is a new beginning.",
    "Success is not final, failure is not fatal.",
    "You are capable of amazing things."
]

user_input = input("Enter a number: ")
try:
    num = int(user_input)
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
    print("Square root:", math.sqrt(num))
    if num > 10:
        print("Motivational quote:", random.choice(quotes))
except ValueError:
    print("Invalid input")