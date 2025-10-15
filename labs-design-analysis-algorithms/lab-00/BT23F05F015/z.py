# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

# List of motivational quotes
quotes = [
    "Keep going, you are doing great!",
    "Believe in yourself!",
    "Every day is a new opportunity!",
    "Success is the sum of small efforts repeated."
]

# Ask user for a number
try:
    num = float(input("Enter a number: "))

    # Check if number is even
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

    # Calculate square root (only for non-negative numbers)
    if num >= 0:
        print("Square root:", math.sqrt(num))
    else:
        print("Cannot calculate square root of negative number.")

    # Print a random quote if number > 10
    if num > 10:
        print("Motivational Quote:", random.choice(quotes))

except ValueError:
    print("Invalid input! Please enter a valid number.")

