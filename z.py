# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

# List of motivational quotes
quotes = [
    "Keep going, you're doing great!",
    "Every step counts, no matter how small.",
    "Believe in yourself and all that you are.",
    "Success is the sum of small efforts, repeated daily.",
    "You are stronger than you think."
]

# Get user input
user_input = input("Enter a number: ")

try:
    number = int(user_input)

    # Check if the number is even
    if number % 2 == 0:
        print("✅ The number is even.")
    else:
        print("⚠️ The number is odd.")

    # Calculate and display square root
    if number >= 0:
        sqrt = math.sqrt(number)
        print("📐 Square root:", sqrt)
    else:
        print("❌ Cannot calculate square root of a negative number.")

    # Show a motivational quote if number > 10
    if number > 10:
        quote = random.choice(quotes)
        print("💡 Motivational quote:", quote)

except ValueError:
    print("Invalid input")
