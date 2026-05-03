# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.

import random,math

num = int(input("Enter a number: "))
if num%2==0 :
    print("Its a even number")

print("Square root:", math.sqrt(num))

if num > 10:
    print(random.choice(["Hard work and smart work goes hands in hand","Trying to stop negative thought is itself a negative though"]))
