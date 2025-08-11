# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.

num1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = int(input("Enter second number: "))

    # Perform operation
if operator == "+":
        result = num1 + num2
elif operator == "-":
        result = num1 - num2
elif operator == "*":
        result = num1 * num2
elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error — Division by zero is not allowed.")
            result = None
else:
        print("Invalid operator.")
        result = None

print("Result:",result)