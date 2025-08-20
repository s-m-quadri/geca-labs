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
    "Stay positive and strong!",
    "You can do it!"
]

user_input = input("Enter a number: ")

if user_input.isdigit():
    num = int(user_input)
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
    print("Square root:", math.sqrt(num))
    if num > 10:
        print(random.choice(quotes))
else:
    print("Invalid input")
