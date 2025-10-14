import math
import random

# List of motivational quotes
quotes = [
    "Believe in yourself!",
    "Keep pushing forward.",
    "You can do it!",
    "Every day is a new opportunity."
]

# Taking user input and handling invalid input
try:
    num = int(input("Enter a number: "))
    
    # Check if number is even or odd
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
    
    # Calculate and print square root
    if num >= 0:
        sqrt_val = math.sqrt(num)
        print(f"Square root of {num} is {sqrt_val}")
    else:
        print("Cannot calculate square root of negative number.")
    
    # Print a random motivational quote if number > 10
    if num > 10:
        print("Motivational Quote:", random.choice(quotes))

except ValueError:
    print("Invalid input! Please enter an integer.")
