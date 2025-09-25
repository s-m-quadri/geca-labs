# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.


num1_input = input("Enter the first number: ")

operator = input("Enter an operator (+, -, *, /): ")

num2_input = input("Enter the second number: ")

try:
    num1 = float(num1_input)
    num2 = float(num2_input)

    
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
            print("❌ Error: Cannot divide by zero.")
    else:
        print("❌ Invalid operator. Please use +, -, *, or /.")

except ValueError:
    print("❌ Invalid input. Please enter numeric values.")
