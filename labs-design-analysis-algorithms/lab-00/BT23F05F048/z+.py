# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
op = input("Enter an operator (+, -, *, /): ")

try:
    a = float(num1)
    b = float(num2)

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b != 0:
            result = a / b
        else:
            print("Error: Division by zero is not allowed.")
            exit()
    else:
        print("Invalid operator.")
        exit()

    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter valid numbers.")
