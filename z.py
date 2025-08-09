# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
    sqrt_number = math.sqrt(number)
    print(f"The square root of {number} is {sqrt_number}.")
    if number > 10:
        quotes = [
            "Keep going, you're doing great!",
            "Believe in yourself!",
            "Every day is a new opportunity.",
            "Stay positive, work hard, make it happen."
        ]
        print("Motivational Quote:", random.choice(quotes))
else:
    print(f"{number} is odd. No further calculations.")