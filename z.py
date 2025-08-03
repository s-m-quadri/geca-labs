# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math, random

quotes = ["Be the change.", "Serve others.", "Shake the world."]

n = input("Enter a number: ")
if n.isdigit():
    n = int(n)
    print("Even" if n % 2 == 0 else "Odd")
    print("√:", math.sqrt(n))
    if n > 10:
        print(random.choice(quotes))
else:
    print("Invalid input")
