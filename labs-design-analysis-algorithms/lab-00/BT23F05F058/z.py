import math
import random

# Motivational quotes
quotes = ["Keep going!", "You got this!", "Never stop learning."]

# Take user input
num = int(input("Enter a number: "))

# Check if even
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Calculate square root
print("Square root:", math.sqrt(num))

# Print random quote if number > 10
if num > 10:
    print(random.choice(quotes))
