# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random   
user_input = input("Enter a number: ")
if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
    number = int(user_input)
    print(f"You entered the number: {number}")
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
    if number >= 0:
        sqrt_value = math.sqrt(number)
        print(f"The square root of {number} is {sqrt_value}.")
    else:
        print("Cannot compute square root of a negative number.")
    if number > 10:
        quotes = [
            "Believe you can and you're halfway there.",
            "Your limitation—it's only your imagination.",
            "Push yourself, because no one else is going to do it for you."
        ]
        print("Motivational Quote:", random.choice(quotes))
else:
    print("Invalid input")      
            