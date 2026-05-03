# Combine everything you've learned.
# Ask user for a number, check if it's even, calculate its square root,
# and print a random motivational quote if the number is > 10.

# 💡 TIP:
# Combine `if`, `math`, `random`, and type conversion.
import math
import random
quotes=["Believe in yourself","Keep going","You're doing right","Work hard"]

num=int(input("Enter a number: "))

if(num%2==0):
    print("Number is even")
else:
    print("Number is odd")
sqrt_num = math.sqrt(num)
print(f"Square root of {num} is {sqrt_num}")

if(num>10):
    print("Motivational quote:",random.choice(quotes))

