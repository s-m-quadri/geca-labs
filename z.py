# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

quotes = [
    "Success is not final, failure is not fatal.",
    "Believe you can and you're halfway there.",
    "Every accomplishment starts with the decision to try."
]

try:
    number = float(input("Enter a number: "))
    
    # Check if even (for integers)
    if number.is_integer():
        if int(number) % 2 == 0:
            print(f"{int(number)} is even")
        else:
            print(f"{int(number)} is odd")
    
    # Calculate square root if non-negative
    if number >= 0:
        sqrt = math.sqrt(number)
        print(f"Square root: {sqrt:.2f}")
    else:
        print("Cannot calculate square root of negative number")
    
    # Print random quote if number > 10
    if number > 10:
        print("\nMotivational quote:")
        print(random.choice(quotes))

except ValueError:
    print("Invalid input. Please enter a number.")
