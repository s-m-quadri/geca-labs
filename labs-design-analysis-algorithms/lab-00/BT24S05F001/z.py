# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random

num = input("Enter a number: ")

try:
    n = int(num)
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

    print("Square root:", math.sqrt(n))

    if n > 10:
        quotes = [
            "Keep going!",
            "You can do it!",
            "Never give up!",
            "Stay positive!"
        ]
        print("Motivational quote:", random.choice(quotes))

except ValueError:
    print("Invalid input")
