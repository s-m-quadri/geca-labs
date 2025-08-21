# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random

def combine_all():
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        print("Invalid input")
        return
    
    num = int(user_input)
    
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    
    print("Square root:", math.sqrt(num))
    
    if num > 10:
        quotes = [
            "Keep going, you’re doing great!",
            "Believe in yourself and all that you are.",
            "Success is the sum of small efforts repeated daily.",
            "Your potential is endless!"
        ]
        print("Motivational Quote:", random.choice(quotes))

combine_all()
