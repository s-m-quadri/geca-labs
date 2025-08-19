# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random

try:
    user_input = input("Enter a number: ")
    number = float(user_input)
    
    if number == int(number):
        if int(number) % 2 == 0:
            print(f"{int(number)} is even.")
        else:
            print(f"{int(number)} is odd.")
    else:
        print(f"{number} is a decimal number.")
    
    if number >= 0:
        sqrt_result = math.sqrt(number)
        print(f"Square root of {number}: {sqrt_result}")
    else:
        print("Cannot calculate square root of negative numbers.")
    
    if number > 10:
        motivational_quotes = [
            "Keep going, you're doing great!",
            "Success is the sum of small efforts repeated day in day out.",
            "The only way to do great work is to love what you do.",
            "Believe you can and you're halfway there.",
            "Don't watch the clock; do what it does. Keep going."
        ]
        quote = random.choice(motivational_quotes)
        print(f"Motivational quote: {quote}")

except ValueError:
    print("Invalid input. Please enter a valid number.")