# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.
# Get inputs from the user
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
    print("Result:", result)

elif op == "-":
    result = num1 - num2
    print("Result:", result)

elif op == "*":
    result = num1 * num2
    print("Result:", result)

elif op == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero!")

else:
    print("Invalid operator!")
