# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random

quotes = [
	"Keep going!",
	"You can do it!",
	"Success is near!",
	"Believe in yourself!"
]
try:
	num = int(input("Enter a number: "))
	if num % 2 == 0:
		print(f"{num} is even.")
	else:
		print(f"{num} is odd.")
	print(f"Square root: {math.sqrt(num):.2f}")
	if num > 10:
		print(random.choice(quotes))
except ValueError:
	print("Invalid input")
