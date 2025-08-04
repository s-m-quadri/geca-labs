# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random

quotes = [
    "Keep pushing forward!",
    "Believe in yourself!",
    "Every day is a new opportunity!",
    "Stay positive and work hard!",
    "You are capable of amazing things!"
]

user_input = input("Enter a number: ")

try:
    number = int(user_input)
    
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    
    if number >= 0:
        print(f"Square root of {number} is {math.sqrt(number)}")
    else:
        print("Cannot calculate square root of a negative number.")
    
    if number > 10:
        print(random.choice(quotes))
except ValueError:
    print("Invalid input")