# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.
# Take inputs
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
op = input("Enter operator (+, -, *, /): ")

# Validate inputs
try:
    a = float(num1)
    b = float(num2)
    
    # Perform operation
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operator!")
        
except ValueError:
    print("Invalid input! Please enter numbers only.")
