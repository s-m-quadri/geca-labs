# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

try:
    number = int(input("Enter a number: "))
    
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    
    if number >= 0:
        sqrt_value = math.sqrt(number)
        print(f"Square root of {number}: {sqrt_value}")
    else:
        print("Cannot calculate square root of negative number")
    
    if number > 10:
        quotes = [
            "Keep going!",
            "You're doing great!",
            "Success is near!",
            "Never give up!",
            "Believe in yourself!"
        ]
        quote = random.choice(quotes)
        print(f"Motivational quote: {quote}")
        
except ValueError:
    print("Invalid input. Please enter a valid number.")
