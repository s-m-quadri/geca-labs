# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.

# Ask user for two numbers and an operator
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    op = input("Enter an operator (+, -, *, /): ")

    # Perform the calculation
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        # Handle divide by zero
        if b == 0:
            result = "Error: Cannot divide by zero!"
        else:
            result = a / b
    else:
        result = "Invalid operator!"

    print("Result:", result)

except ValueError:
