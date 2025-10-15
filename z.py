import math, random
quotes = ["Keep going!", "You got this!", "Never stop learning."]
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
print("Square root:", math.sqrt(num))
if num > 10:
    print(random.choice(quotes))
