# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random

# Ask user for a number
user_input = input("Enter a number: ")

# Validate input
try:
    num = int(user_input)
    
    # Check if even or odd
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
    
    # Calculate square root
    print("Square root:", math.sqrt(num))
    
    # Print random motivational quote if number > 10
    if num > 10:
        quotes = [
            "Keep going, you're doing great!",
        ]
        print("Motivational Quote:", quotes)
        
except ValueError:
    print("Invalid input")
