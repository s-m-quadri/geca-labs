# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math, random
quotes = ["Keep going!", "You got this!", "Never stop learning."]
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
print("Square root:", math.sqrt(num))
if num > 10:
    print(random.choice(quotes))