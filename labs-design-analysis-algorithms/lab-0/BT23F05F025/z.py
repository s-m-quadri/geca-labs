# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random
quotes = [
    "Believe in yourself!",
    "Keep going, you’re doing great!",
    "Every day is a second chance.",
    "You are stronger than you think.",
    "Success is no accident."
]
try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

    print("Square root:", math.sqrt(num))
    if num > 10:
        print("Motivational quote:", random.choice(quotes))
except ValueError:
    print("Invalid input")
