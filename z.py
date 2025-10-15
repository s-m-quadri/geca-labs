# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math
import random

num_input = input("Enter a number: ")

try:
    num = int(num_input)
    
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
    
    if num >= 0:
        print("Square root:", math.sqrt(num))
    else:
        print("Cannot calculate square root of a negative number")
    
    if num > 10:
        quotes = [
            "Keep going, you're doing great!",
            "Success is the sum of small efforts.",
            "Believe in yourself!"
        ]
        print("Motivational Quote:", random.choice(quotes))
#todo
except ValueError:
    print("Invalid input")
