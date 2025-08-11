# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random

# Motivational quotes list
quotes = [
    "Believe you can and you're halfway there.",
    "The best time to start was yesterday. The next best time is now.",
    "Don’t watch the clock; do what it does. Keep going.",
    "It always seems impossible until it’s done.",
    "Push yourself, because no one else is going to do it for you."
]

try:
    # Ask for number
    num = int(input("Enter a number: "))

    # Check even or odd
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

    # Calculate square root
    print("Square root:", math.sqrt(num))

    # If number > 10, print a random quote
    if num > 10:
        print("Motivational Quote:", random.choice(quotes))

except ValueError:
    print("Invalid input! Please enter a valid integer.")
