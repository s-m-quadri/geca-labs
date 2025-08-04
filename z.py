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
    
    sqrt_result = math.sqrt(number)
    print(f"Square root of {number}: {sqrt_result}")
    
    if number > 10:
        quotes = [
            "Keep going!",
            "You're doing great!",
            "Success is near!",
            "Believe in yourself!",
            "Never give up!"
        ]
        print(f"Motivational quote: {random.choice(quotes)}")
        
except ValueError:
    print("Please enter a valid number")
except ValueError as e:
    print(f"Error: Cannot calculate square root of negative number")