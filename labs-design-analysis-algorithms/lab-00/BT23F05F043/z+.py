# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", x + y)
elif op == "-":
    print("Result:", x - y)
elif op == "*":
    print("Result:", x * y)
elif op == "/":
    if y != 0:
        print("Result:", x / y)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
