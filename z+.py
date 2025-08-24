# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.

a = float(input("First number: "))
op = input("Operator (+ - * /): ")
b = float(input("Second number: "))
if op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/': print(a / b)
else: print("Invalid operator")