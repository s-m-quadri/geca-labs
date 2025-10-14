# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.

# Take two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Take operator input
op = input("Enter operator (+, -, *, /): ")

# Perform calculation based on operator
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"

# Print the result
print("Result:", result)
