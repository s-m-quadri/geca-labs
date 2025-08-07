# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

# List of motivational quotes
quotes = [
    "Keep going, you're doing great!",
    "Believe in yourself!",
    "Every day is a fresh start.",
    "Stay positive and strong.",
    "You are capable of amazing things!"
]

try:
    # Ask user for a number
    num = int(input("Enter a number: "))

    # Check if even
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

    # Calculate and print square root
    sqrt_val = math.sqrt(num)
    print("Square root:", sqrt_val)

    # If number > 10, print a random motivational quote
    if num > 10:
        print("Motivational quote:", random.choice(quotes))

except ValueError:
    print("Invalid input. Please enter a valid number.")
