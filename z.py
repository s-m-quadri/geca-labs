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
    "Believe in yourself!",
    "Success is the sum of small efforts repeated daily.",
    "Stay positive and work hard!"
]

# Asking user for a number
try:
    num = int(input("Enter a number: "))

    # Check if the number is even or odd
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

    # Calculate and print square root
    sqrt_num = math.sqrt(num)
    print(f"Square root of {num} is {sqrt_num}")

    # Print a motivational quote if number > 10
    if num > 10:
        quote = random.choice(quotes)
        print("Motivational quote:", quote)

except ValueError:
    print("Invalid input! Please enter a valid integer.")
