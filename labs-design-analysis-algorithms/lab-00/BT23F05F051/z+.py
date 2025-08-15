# Make a calculator that performs +, -, *, / between two numbers.

# 💡 TIP:
# Use `input()` for numbers and operator, then `if-elif` to select operation.
a=int(input())
b=int(input())
op=input("enter operation (+,-,*,/) :")

if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)    
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)    
else :
    print("invalid operation")
