# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import math

number = int(input("Enter a number: "))

if number%2==0:
    print("The number is even")
else:
    print("The number is not odd")

sqrt = math.sqrt(number)
print(sqrt)

if number>10 :
    print("Honesty is the best Policy")