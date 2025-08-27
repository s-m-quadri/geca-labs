# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random
n=int(input("enter a number:"))
if n%2==0:
    print(math.sqrt(n))
    if n>10:
        print(random.choice(["mistake is the first step of success","Action speaks louder than words"]))    
