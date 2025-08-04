# Spoiler for the following labs.

These labs are designed to be solved by students.

## LAB `A`
```python
print("Hello, Python!")
print("This is Lab A")
```

## LAB `B`
```python
name = "Alice"
age = 21
is_student = True
print(name, age, is_student)
```

## LAB `C`
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")
```

## LAB `D`
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
print("Diff:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("Remainder:", a % b)
print("Power:", a ** b)
```

## LAB `E`
```python
sentence = input("Enter a sentence: ")
print("Uppercase:", sentence.upper())
print("Reversed:", sentence[::-1])
print("Length:", len(sentence))
```
## LAB `F`
```python
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

## LAB `G`
```python
print("Using for loop:")
for i in range(1, 11):
    print(i)

print("Using while loop:")
i = 1
while i <= 10:
    print(i)
    i += 1
```

## LAB `H`
```python
my_list = [10, 20, 30, 40, 50]
print("First:", my_list[0])
print("Middle:", my_list[len(my_list) // 2])
print("Last:", my_list[-1])

my_list[2] = 100
print("Modified List:", my_list)
```

## LAB `I`
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("---")

for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")
```

## LAB `J`
```python
words = []
words.append("zebra")
words.append("apple")
words.append("monkey")

words.sort()
print("Sorted:", words)

words.reverse()
print("Reversed:", words)
```
## LAB `K`
```python
my_tuple = ("red", "green", "blue")
# my_tuple[1] = "yellow"  # ❌ This will throw a TypeError

for color in my_tuple:
    print(color)
```

## LAB `L`
```python
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

print("Bob's marks:", students["Bob"])

for name, marks in students.items():
    print(f"{name}: {marks}")
```

## LAB `M`
```python
nums = {1, 2, 2, 3, 4, 4, 5}
print("Unique set:", nums)

nums.add(6)
print("After adding 6:", nums)
```

## LAB `N`
```python
def add(x, y):
    return x + y

result = add(10, 5)
print("Sum:", result)
```

## LAB `O`
```python
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")
```

## LAB `P`
```python
def void_function():
    print("Running")
def add(a, b):
    return a + b
```

## LAB `Q`
```python
for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()
```

## LAB `R`
```python
print(f"Student {name} scored {marks} marks.")
print("Student {} scored {} marks.".format(name, marks))
print("Student %s scored %d marks." % (name, marks))
```

## LAB `S`
```python
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter valid numbers.")
```

## LAB `T`
```python
with open("output.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")
with open("output.txt", "r") as f:
    print(f.read())
```

## LAB `U`
```python
squares = [x**2 for x in range(1, 11)]
evens = [x for x in range(1, 21) if x % 2 == 0]
```

## LAB `V`
```python
import math
print(math.sqrt(144))
print(math.pi)
print(math.sin(math.radians(90)))
```

## LAB `W`
```python
import random
print("Dice:", random.randint(1, 6))
print("Coin:", random.choice(["Heads", "Tails"]))
```

## LAB `X`
```python
import random
print("Dice:", random.randint(1, 6))
print("Coin:", random.choice(["Heads", "Tails"]))
```

## LAB `Y`
```python
num = input("Enter a number: ")
if num.isdigit():
    print("You entered:", int(num))
else:
    print("Invalid input")
```

## LAB `Z`
```python
import math, random
quotes = ["Keep going!", "You got this!", "Never stop learning."]
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
print("Square root:", math.sqrt(num))
if num > 10:
    print(random.choice(quotes))
```

## LAB `Z+`
```python
a = float(input("First number: "))
op = input("Operator (+ - * /): ")
b = float(input("Second number: "))
if op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/': print(a / b)
else: print("Invalid operator")
```

## LAB `Z++`
```python
name = input("Enter full name: ")
parts = name.split()
initials = '. '.join(p[0].upper() for p in parts) + '.'
print("Lower:", name.lower())
print("Upper:", name.upper())
print("Initials:", initials)
```

## LAB `Z+++`
```python
import time
while True:
    print("1. Greet\n2. Time\n3. Exit")
    choice = input("Choose: ")
    if choice == '1':
        print("Hello!")
    elif choice == '2':
        print(time.ctime())
    elif choice == '3':
        break
    else:
        print("Invalid")
```