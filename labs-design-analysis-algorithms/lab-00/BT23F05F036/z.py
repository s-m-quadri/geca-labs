# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random

quotes = [
    "Keep going, you're doing great!",
    "Believe in yourself and all that you are.",
    "Every day is a fresh start.",
    "You are capable of amazing things.",
    "Success is no accident. Keep pushing."
]

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print("Square root:", math.sqrt(num))

if num > 10:
    print("Motivational quote:", random.choice(quotes))
