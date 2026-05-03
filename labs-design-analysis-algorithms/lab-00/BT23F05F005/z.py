# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

#solution
import math
import random

quotes = [
	"Keep going!",
	"You can do it!",
	"Never give up!",
	"Success is near!"
]

num = input("Enter a number: ")
if num.isdigit():
	n = int(num)
	if n % 2 == 0:
		print(f"{n} is even.")
	else:
		print(f"{n} is odd.")
	print("Square root:", math.sqrt(n))
	if n > 10:
		print(random.choice(quotes))
else:
	print("Invalid input")