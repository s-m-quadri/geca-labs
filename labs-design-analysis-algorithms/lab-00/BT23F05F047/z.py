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
    "Every step counts.",
    "You are capable of amazing things.",
    "Success is no accident!"
]

try:
    
    user_input = input("Enter a number: ")
    number = int(user_input)

   
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

    
    sqrt_val = math.sqrt(abs(number))  # use abs to avoid sqrt of negative
    print(f"Square root of {number} is: {sqrt_val}")

   
    if number > 10:
        quote = random.choice(quotes)
        print("✨ Motivational Quote:", quote)

except ValueError:
    print("Invalid input. Please enter a valid integer.")
