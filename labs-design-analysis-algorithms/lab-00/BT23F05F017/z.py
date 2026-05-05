# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random

number = int(input("Enter a number: "))

# Check if even
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Calculate square root
if number >= 0:
    sqrt_result = math.sqrt(number)
    print(f"Square root of {number} is {sqrt_result}")
else:
    print("Cannot calculate square root of negative number")

# Random motivational quote if > 10
if number > 10:
    quotes = [
        "Great things never come from comfort zones!",
        "The only impossible journey is the one you never begin!",
        "Success is not final, failure is not fatal!",
        "Dream big and dare to fail!"
    ]
    quote = random.choice(quotes)
    print("Motivational quote:", quote)