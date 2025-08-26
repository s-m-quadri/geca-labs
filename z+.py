# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.

num1 = float(input("Pehla number daalo: "))
operator = input("Operator choose karo (+, -, *, /): ")
num2 = float(input("Doosra number daalo: "))

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
        print("Error: Zero se divide nahi kar sakte!")
else:
    print("Invalid operator. Sirf +, -, *, / use karo.")
