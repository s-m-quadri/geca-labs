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
        print(n, "is even")
    else:
        print(n, "is odd")
    
    if n >= 0:
        print("Square root:", math.sqrt(n))
    else:
        print("Cannot compute square root of a negative number")
    
    if n > 10:
        quotes = [
            "Keep going, you're doing great!",
            "Believe in yourself!",
            "Every day is a new opportunity.",
            "Success is a journey, not a destination."
        ]
        print(random.choice(quotes))
except ValueError:
    print("Invalid input")
