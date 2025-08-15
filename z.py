# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

quotes = [
    "Keep going, you're doing great!",
    "Believe in yourself!",
    "Every step counts!",
    "Stay positive and work hard!",
    "You are capable of amazing things!"
]


    num = int(input("Enter a number: "))
    
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
    
    
    if num >= 0:
        sqrt_val = math.sqrt(num)
        print(f"Square root of {num} is {sqrt_val:.2f}")
    else:
        print("Cannot calculate square root of a negative number.")
    
    if num > 10:
        print("Motivational quote:")
        print(random.choice(quotes))

except ValueError:
    print("Invalid input! Please enter an integer.")
