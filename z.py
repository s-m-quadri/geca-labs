import math
import random

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
print("Square root:", math.sqrt(num))
if num > 10:
    quotes = [
        "Keep going!",
        "You can do it!",
        "Never give up!",
        "Success is near!"
    ]
    print(random.choice(quotes))
