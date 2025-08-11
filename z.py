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
    "Every step counts!",
    "Success starts with the first step.",
    "You have got this!"
]

num = int(input("Enter a number: "))

if num % 2 == 0:
        print(f"{num} is even.")
print("Square root:", math.sqrt(num))

if num > 10:
        print("Motivation:", random.choice(quotes))
