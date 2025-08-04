# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.

a = int(input("First number: "))
b = int(input("Second number: "))
c= input("Enter operator from the following (+, -, *, /): ")

if c == "+":
    print("Sum:", a + b)
elif c == "-":
    print("Difffernce:", a - b)
elif c == "*":
    print("Multiply:", a * b)
elif c == "/":
    if b != 0:
        print("Divide:", a / b)
    else:
        print("Can't divide by zero")
