# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.

num1 = float(input("First number: "))
op = input("Operator (+ - * /): ")
num2 = float(input("Second number: "))

if op == '+':
     print(num1 + num2)
elif op == '-': 
    print(num1 - num2)
elif op == '*':
     print(num1 * num2)
elif op == '/':
     print(num1 / num2)
else: print("Invalid operator")
    
    
