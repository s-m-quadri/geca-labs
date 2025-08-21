import random
import math

quotes = [
    "Keep going, you're doing great!",
    "Believe in yourself!",
    "Every step counts!",
    "Success is no accident.",
    "Dream big and dare to fail."
]

try:
    num = int(input("Enter a number: "))
    
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
    
    if num >= 0:
        sqrt_num = math.sqrt(num)
        print(f"Square root of {num} is {sqrt_num:.2f}")
    else:
        print("Cannot calculate square root of a negative number.")
    
    if num > 10:
        print("Motivational Quote:", random.choice(quotes))

except ValueError:
    print("Invalid input! Please enter a valid integer.")

