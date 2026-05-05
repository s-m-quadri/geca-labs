# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.

try:
    # Get input from user
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    # Perform calculation based on operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2
    else:
        print("Invalid operator")
        exit()
    
    print(f"{num1} {operator} {num2} = {result}")

except ValueError:
    print("Invalid number input")
except ZeroDivisionError:
    print("Cannot divide by zero")
