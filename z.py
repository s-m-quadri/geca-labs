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
    "You are stronger than you think!",
    "Success is the sum of small efforts repeated daily.",
    "Dream it. Wish it. Do it."
]

try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

    print("Square root:", math.sqrt(num))

    if num > 10:
        print("Motivational Quote:", random.choice(quotes))

except ValueError:
    print("Invalid input! Please enter a valid integer.")
