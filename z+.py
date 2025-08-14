# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.

 n1 = int(input("Enter num1 : "))

 n2 = int(input("Enter num2 : "))

 op = input("Enter operation")

 if op=="+":
    print(n1+n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
elif op=="%":
    print(n1%n2)

