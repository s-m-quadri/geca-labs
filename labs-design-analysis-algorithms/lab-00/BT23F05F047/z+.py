# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.


num1 = input("Enter first number: ")


operator = input("Enter operator (+, -, *, /): ")


num2 = input("Enter second number: ")

try:
    
    a = float(num1)
    b = float(num2)

    
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            result = "Error: Cannot divide by zero"
        else:
            result = a / b
    else:
        result = "Invalid operator"

    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter valid numbers.")
