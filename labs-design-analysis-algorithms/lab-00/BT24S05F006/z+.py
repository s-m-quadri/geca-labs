# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.

# Ask user for two numbers and an operator
try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if operator == '+':
        result = num1 + num2
        print("Result:", result)
    elif operator == '-':
        result = num1 - num2
        print("Result:", result)
    elif operator == '*':
        result = num1 * num2
        print("Result:", result)
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operator. Use +, -, *, or /.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
