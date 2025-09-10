# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

# Some motivational quotes
quotes = [
    "Keep going, you’re doing great!",
    "Believe in yourself and all that you are.",
    "Every step counts, no matter how small.",
    "Dream big and dare to fail.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts."
]

# Ask user for a number
user_input = input("Enter a number: ")

try:
    number = int(user_input)   # convert to integer

    # Check if it's even or odd
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

    # Calculate square root
    sqrt_val = math.sqrt(abs(number))   # use abs in case it's negative
    print(f"The square root of |{number}| is {sqrt_val}")

    # Print a random motivational quote if number > 10
    if number > 10:
        print("Motivational quote:", random.ch
