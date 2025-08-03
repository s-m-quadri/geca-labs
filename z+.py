# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    if y != 0:
        result = x / y
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid op"

print("Result:", result)
