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
    "Every day is a new opportunity.",
    "Stay positive and work hard.",
    "Success is just around the corner."
]

user_input = input("Enter a number: ")

try:
    num = int(user_input)
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
    if num >= 0:
        print(f"Square root of {num} is {math.sqrt(num):.2f}")
    else:
        print("Cannot compute square root of a negative number.")
    
    if num > 10:
        print("Motivational quote:", random.choice(quotes))
except ValueError:
    print("Invalid input")
