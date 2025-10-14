# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("Square root:", math.sqrt(num))

if num > 10:
    quotes = [
        "Keep going, you’re doing great!",
        "Believe in yourself!",
        "Success is the sum of small efforts repeated daily.",
        "You can do hard things!",
        "Dream big and work hard!"
    ]
    print(random.choice(quotes))
