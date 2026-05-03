# Take input from user
a = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))

# Perform operation
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
